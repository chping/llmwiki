from __future__ import annotations

import hashlib
import json
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import quote, unquote

from models import ManifestEntry, WorkflowPaths
from utils import safe_relpath


MD_LINK_RE = re.compile(r"\[([^\]]+)\]\((<[^>]+>|(?:\\.|[^)])+)\)")


def normalize_link_target(raw_target: str) -> str:
    target = raw_target.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    target = target.replace(r"\(", "(").replace(r"\)", ")")
    return unquote(target)


def encode_link_target(raw_target: str) -> str:
    return quote(raw_target, safe="/-._~")


def sha256_file(path: Path, chunk_size: int = 1024 * 1024) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


def sha256_dir(path: Path) -> str:
    """
    Build a deterministic hash for a directory tree based on:
    - relative path
    - entry type
    - file content hash (for files)
    """
    h = hashlib.sha256()

    if not path.exists():
        raise FileNotFoundError(f"Directory does not exist: {path}")
    if not path.is_dir():
        raise NotADirectoryError(f"Expected directory path: {path}")

    for subpath in sorted(path.rglob("*"), key=lambda p: str(p.relative_to(path)).replace("\\", "/")):
        rel = str(subpath.relative_to(path)).replace("\\", "/")
        if subpath.is_dir():
            h.update(f"D:{rel}\n".encode("utf-8"))
        elif subpath.is_file():
            h.update(f"F:{rel}\n".encode("utf-8"))
            h.update(sha256_file(subpath).encode("utf-8"))
            h.update(b"\n")
        else:
            h.update(f"O:{rel}\n".encode("utf-8"))

    return h.hexdigest()


def sha256_path(path: Path) -> str:
    if path.is_dir():
        return sha256_dir(path)
    return sha256_file(path)


def remove_path(path: Path) -> None:
    if not path.exists() and not path.is_symlink():
        return
    if path.is_dir() and not path.is_symlink():
        shutil.rmtree(path)
    else:
        path.unlink()


def make_backup_path(target: Path) -> Path:
    parent = target.parent
    name = target.name
    index = 1
    while True:
        candidate = parent / f".{name}.archive_backup_{index}"
        if not candidate.exists():
            return candidate
        index += 1


def backup_existing_target(target: Path, backups: list[tuple[Path, Path]]) -> None:
    if not target.exists() and not target.is_symlink():
        return

    backup_path = make_backup_path(target)
    shutil.move(str(target), str(backup_path))
    backups.append((backup_path, target))


def cleanup_empty_dirs_upward(path: Path, stop_at: Path) -> None:
    current = path
    stop_at_resolved = stop_at.resolve()

    while True:
        try:
            if current.resolve() == stop_at_resolved:
                break
        except FileNotFoundError:
            break

        if not current.exists() or not current.is_dir():
            break

        try:
            current.rmdir()
        except OSError:
            break

        parent = current.parent
        if parent == current:
            break
        current = parent


def move_with_overwrite(
    src: Path,
    dst: Path,
    moved_pairs: list[tuple[Path, Path]],
    overwritten_targets: list[tuple[Path, Path]],
) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)

    if dst.exists() or dst.is_symlink():
        backup_existing_target(dst, overwritten_targets)

    shutil.move(str(src), str(dst))
    moved_pairs.append((dst, src))


def merge_directory(
    src_dir: Path,
    dst_dir: Path,
    moved_pairs: list[tuple[Path, Path]],
    overwritten_targets: list[tuple[Path, Path]],
    root_src_dir: Path,
) -> None:
    """
    Merge src_dir into dst_dir recursively.

    Rules:
    - file conflict: overwrite target
    - dir conflict: recursive merge
    - file vs dir conflict: overwrite target completely
    """
    if not src_dir.is_dir():
        raise NotADirectoryError(f"Expected source directory: {src_dir}")

    if not dst_dir.exists():
        move_with_overwrite(src_dir, dst_dir, moved_pairs, overwritten_targets)
        return

    if not dst_dir.is_dir():
        move_with_overwrite(src_dir, dst_dir, moved_pairs, overwritten_targets)
        return

    for child in list(src_dir.iterdir()):
        target_child = dst_dir / child.name

        if child.is_dir():
            if target_child.exists() and target_child.is_dir():
                merge_directory(child, target_child, moved_pairs, overwritten_targets, root_src_dir)
            else:
                move_with_overwrite(child, target_child, moved_pairs, overwritten_targets)
        else:
            move_with_overwrite(child, target_child, moved_pairs, overwritten_targets)

    cleanup_empty_dirs_upward(src_dir, root_src_dir.parent)


def validate_entries(paths: WorkflowPaths, entries: list[ManifestEntry]) -> None:
    repo_resolved = paths.repo.resolve()
    for entry in entries:
        try:
            entry.inbox_path.relative_to(repo_resolved)
        except ValueError as exc:
            raise ValueError(f"Manifest inbox_path escapes repo: {entry.inbox_path}") from exc

        if entry.inbox_path != paths.inbox_dir and paths.inbox_dir not in entry.inbox_path.parents:
            raise ValueError(f"Manifest inbox_path is not under inbox/: {entry.inbox_path}")

        if entry.source_size < 0 or entry.source_mtime_ns < 0:
            raise ValueError(f"Invalid file fingerprint for: {entry.inbox_path}")

        if not entry.wiki_pages:
            raise ValueError(f"Manifest entry missing wiki_pages for: {entry.inbox_path}")

        for page in entry.wiki_pages:
            try:
                page.relative_to(repo_resolved)
            except ValueError as exc:
                raise ValueError(f"Manifest wiki page escapes repo: {page}") from exc
            if paths.wiki_dir not in page.parents:
                raise ValueError(f"Manifest wiki page is not under wiki/: {page}")
            if not page.exists():
                raise FileNotFoundError(f"Manifest wiki page does not exist: {page}")


def page_contains_reference(page: Path, target_abs: Path) -> bool:
    text = page.read_text(encoding="utf-8", errors="replace")
    target_resolved = target_abs.resolve()

    for _label, link in MD_LINK_RE.findall(text):
        resolved = (page.parent / normalize_link_target(link)).resolve()
        if resolved == target_resolved:
            return True
    return False


def validate_backlinks(entries: list[ManifestEntry]) -> None:
    for entry in entries:
        missing = [str(page) for page in entry.wiki_pages if not page_contains_reference(page, entry.inbox_path)]
        if missing:
            raise ValueError(
                f"Manifest entry references inbox file not linked from wiki pages: {entry.inbox_path} | pages: {missing}"
            )


def validate_fingerprint(paths: WorkflowPaths, entry: ManifestEntry) -> tuple[str, str]:
    archive_candidate = paths.archive_dir / entry.inbox_path.name

    if entry.inbox_path.exists():
        if entry.inbox_path.is_file():
            stat = entry.inbox_path.stat()
            if stat.st_size != entry.source_size or stat.st_mtime_ns != entry.source_mtime_ns:
                raise ValueError(
                    f"Inbox file changed after Codex processing: {entry.inbox_path} "
                    f"(expected size={entry.source_size}, mtime_ns={entry.source_mtime_ns}; "
                    f"actual size={stat.st_size}, mtime_ns={stat.st_mtime_ns})"
                )
        return "inbox", sha256_path(entry.inbox_path)

    if archive_candidate.exists():
        if archive_candidate.is_file():
            stat = archive_candidate.stat()
            if stat.st_size != entry.source_size:
                raise ValueError(
                    f"Archived file fingerprint mismatch for: {archive_candidate} "
                    f"(expected size={entry.source_size}, actual size={stat.st_size})"
                )
        return "archive", sha256_path(archive_candidate)

    raise FileNotFoundError(f"Neither inbox nor archive file exists: {entry.inbox_path}")


def rewrite_page_links(page: Path, old_abs: Path, new_abs: Path) -> bool:
    text = page.read_text(encoding="utf-8", errors="replace")
    new_rel = safe_relpath(page, new_abs)
    new_rel_encoded = encode_link_target(new_rel)
    changed = False
    old_abs_resolved = old_abs.resolve()

    def replace_link(match: re.Match[str]) -> str:
        nonlocal changed
        label, target = match.group(1), match.group(2)
        resolved = (page.parent / normalize_link_target(target)).resolve()
        if resolved == old_abs_resolved:
            changed = True
            return f"[{label}]({new_rel_encoded})"
        return match.group(0)

    new_text = MD_LINK_RE.sub(replace_link, text)
    if changed:
        page.write_text(new_text, encoding="utf-8")
    return changed


def ensure_log_entry(log_text: str, date_str: str, line: str) -> str:
    heading = f"## {date_str}"
    if heading not in log_text:
        if not log_text.endswith("\n"):
            log_text += "\n"
        log_text += f"\n{heading}\n\n"

    section_re = re.compile(rf"(?ms)^## {re.escape(date_str)}\s*(.*?)(?=^## |\Z)")
    match = section_re.search(log_text)
    if not match:
        return log_text.rstrip() + f"\n\n{heading}\n\n{line}\n"

    block = match.group(1).strip("\n")
    existing = set(x.strip() for x in block.splitlines() if x.strip())
    if line in existing:
        return log_text

    merged = block.splitlines() if block else []
    merged.append(line)
    replacement = f"{heading}\n\n" + "\n".join(merged).rstrip() + "\n\n"
    start, end = match.span()
    return log_text[:start] + replacement + log_text[end:]


def write_report(paths: WorkflowPaths, *, entries: list[ManifestEntry], results: list[dict[str, Any]], dry_run: bool) -> None:
    report = {
        "version": 5,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "dry_run": dry_run,
        "archive_dir": str(paths.archive_dir.relative_to(paths.repo)),
        "manifest": str(paths.manifest_path.relative_to(paths.repo)),
        "entries_count": len(entries),
        "results": results,
    }
    paths.report_path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def append_archive_logs(paths: WorkflowPaths, results: list[dict[str, Any]], date_str: str, dry_run: bool) -> None:
    if dry_run:
        return

    log_text = paths.log_md.read_text(encoding="utf-8", errors="replace")
    for item in results:
        archive_rel = safe_relpath(paths.log_md, paths.repo / item["archive_path"])
        archive_rel_encoded = encode_link_target(archive_rel)
        pages = ", ".join(item["wiki_pages"])
        line = f"- Archived `{Path(item['inbox_path']).name}` to `{archive_rel_encoded}` ; updated backlinks in: {pages}"
        log_text = ensure_log_entry(log_text, date_str, line)

    paths.log_md.write_text(log_text, encoding="utf-8")


def archive_and_relink(paths: WorkflowPaths, entries: list[ManifestEntry], dry_run: bool = False) -> list[dict[str, Any]]:
    moved_pairs: list[tuple[Path, Path]] = []
    overwritten_targets: list[tuple[Path, Path]] = []
    rewritten_pages: list[tuple[Path, str]] = []
    results: list[dict[str, Any]] = []

    validate_entries(paths, entries)
    validate_backlinks(entries)

    try:
        for entry in entries:
            origin, file_sha256 = validate_fingerprint(paths, entry)
            old_path = entry.inbox_path
            new_path = paths.archive_dir / old_path.name

            status = {
                "inbox_path": str(old_path.relative_to(paths.repo)),
                "archive_path": str(new_path.relative_to(paths.repo)),
                "wiki_pages": [str(page.relative_to(paths.repo)) for page in entry.wiki_pages],
                "fingerprint_origin": origin,
                "sha256": file_sha256,
                "moved": False,
                "rewritten_pages": [],
                "already_archived": origin == "archive",
            }

            if dry_run:
                results.append(status)
                continue

            if origin == "inbox":
                new_path.parent.mkdir(parents=True, exist_ok=True)

                if old_path.is_dir():
                    merge_directory(
                        src_dir=old_path,
                        dst_dir=new_path,
                        moved_pairs=moved_pairs,
                        overwritten_targets=overwritten_targets,
                        root_src_dir=old_path,
                    )
                else:
                    move_with_overwrite(
                        src=old_path,
                        dst=new_path,
                        moved_pairs=moved_pairs,
                        overwritten_targets=overwritten_targets,
                    )

                status["moved"] = True

            for page in entry.wiki_pages:
                before = page.read_text(encoding="utf-8", errors="replace")
                changed = rewrite_page_links(page, old_path, new_path)
                if changed:
                    rewritten_pages.append((page, before))
                    status["rewritten_pages"].append(str(page.relative_to(paths.repo)))

            results.append(status)

        date_str = paths.archive_dir.parent.name + "-" + paths.archive_dir.name[:2] + "-" + paths.archive_dir.name[2:]
        append_archive_logs(paths, results, date_str, dry_run)
        write_report(paths, entries=entries, results=results, dry_run=dry_run)
        return results

    except Exception:
        for page, original_text in reversed(rewritten_pages):
            page.write_text(original_text, encoding="utf-8")

        for moved_new, rollback_old in reversed(moved_pairs):
            if moved_new.exists() and not rollback_old.exists():
                rollback_old.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(moved_new), str(rollback_old))

        for backup_path, target_path in reversed(overwritten_targets):
            if backup_path.exists():
                if target_path.exists() or target_path.is_symlink():
                    remove_path(target_path)
                target_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(backup_path), str(target_path))

        raise