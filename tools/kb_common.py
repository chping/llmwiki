from __future__ import annotations

import datetime as _dt
from pathlib import Path


REPO_ROOT = Path.cwd()
INBOX_DIR = REPO_ROOT / "inbox"
RAW_DIR = REPO_ROOT / "raw"
WIKI_DIR = REPO_ROOT / "wiki"


def today_str() -> str:
    return _dt.date.today().isoformat()


def raw_date_dir(date: str | None = None) -> Path:
    if date is None:
        date = today_str()
    year, month, day = date.split("-")
    return RAW_DIR / year / f"{month}{day}"


def ensure_inside(path: Path, parent: Path) -> None:
    resolved_path = path.resolve()
    resolved_parent = parent.resolve()
    if resolved_path != resolved_parent and resolved_parent not in resolved_path.parents:
        raise ValueError(f"Path is outside allowed directory: {path}")


def rel(path: Path) -> str:
    return path.resolve().relative_to(REPO_ROOT.resolve()).as_posix()


def slugify(text: str) -> str:
    value = text.strip().lower()
    chars: list[str] = []
    last_dash = False

    for ch in value:
        if ch.isalnum():
            chars.append(ch)
            last_dash = False
        elif ch in {" ", "_", "-", "/", "\\", ".", ":", "，", "。", "、", "："}:
            if not last_dash:
                chars.append("-")
                last_dash = True

    return "".join(chars).strip("-") or "untitled"


def read_template(target_dir: Path) -> str | None:
    current = target_dir.resolve()
    wiki_root = WIKI_DIR.resolve()

    while current == wiki_root or wiki_root in current.parents:
        candidate = current / "template.md"
        if candidate.exists():
            return candidate.read_text(encoding="utf-8")
        if current == wiki_root:
            break
        current = current.parent

    global_template = WIKI_DIR / "template.md"
    if global_template.exists():
        return global_template.read_text(encoding="utf-8")

    return None


def append_log(message: str, *, date: str | None = None) -> None:
    if date is None:
        date = today_str()

    log_path = WIKI_DIR / "log.md"
    log_path.parent.mkdir(parents=True, exist_ok=True)

    entry = f"- {message}\n"
    if not log_path.exists():
        log_path.write_text(f"# Operation Log\n\n## {date}\n\n{entry}", encoding="utf-8")
        return

    content = log_path.read_text(encoding="utf-8")
    heading = f"## {date}"

    if heading not in content:
        content = content.rstrip() + f"\n\n{heading}\n\n{entry}"
    else:
        before, after = content.split(heading, 1)
        after = after.lstrip("\n")
        content = before + heading + "\n\n" + entry + after

    log_path.write_text(content, encoding="utf-8")
