#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
from datetime import datetime
from pathlib import Path


def normalize_name(name: str) -> str:
    return name.replace(" ", "_")


def remove_existing(path: Path) -> None:
    if path.is_dir() and not path.is_symlink():
        shutil.rmtree(path)
    elif path.exists() or path.is_symlink():
        path.unlink()


def normalize_tree_names(root: Path) -> None:
    paths = sorted(root.rglob("*"), key=lambda p: len(p.parts), reverse=True)

    for path in paths:
        new_name = normalize_name(path.name)
        if new_name == path.name:
            continue

        new_path = path.with_name(new_name)

        if new_path.exists():
            raise FileExistsError(f"Cannot rename because target already exists: {new_path}")

        path.rename(new_path)


def iter_top_level_items(source_dir: Path) -> list[Path]:
    return sorted(source_dir.iterdir(), key=lambda p: p.name)


def make_page_path(raw_item: Path, raw_dir: Path, pages_dir: Path) -> Path:
    rel_path = raw_item.relative_to(raw_dir)

    if raw_item.is_dir():
        return pages_dir / rel_path / "index.md"

    return pages_dir / rel_path.with_suffix(".md")


def create_markdown_page(page_path: Path, title: str) -> None:
    page_path.parent.mkdir(parents=True, exist_ok=True)

    content = f"""# {title}"""

    page_path.write_text(content, encoding="utf-8")


def restore_item(raw_path: Path, original_path: Path) -> None:
    remove_existing(original_path)
    original_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(raw_path), str(original_path))


def archive(target_dir: Path) -> list[dict[str, str]]:
    if not target_dir.exists():
        raise FileNotFoundError(f"Target directory does not exist: {target_dir}")

    if not target_dir.is_dir():
        raise NotADirectoryError(f"Target path is not a directory: {target_dir}")

    project_root = Path.cwd()

    now = datetime.now()
    year_dir = now.strftime("%Y")
    day_dir = now.strftime("%m_%d")

    raw_dir = project_root / "raw" / year_dir / day_dir
    pages_dir = project_root / "wiki" / "pages" / year_dir / day_dir

    raw_dir.mkdir(parents=True, exist_ok=True)
    pages_dir.mkdir(parents=True, exist_ok=True)

    normalize_tree_names(target_dir)

    moved_records: list[dict[str, str]] = []
    completed_items: list[tuple[Path, Path, Path]] = []

    try:
        for source_item in iter_top_level_items(target_dir):
            raw_path = raw_dir / source_item.name

            remove_existing(raw_path)
            shutil.move(str(source_item), str(raw_path))

            page_path = make_page_path(raw_path, raw_dir, pages_dir)
            remove_existing(page_path)
            create_markdown_page(page_path, raw_path.stem)

            completed_items.append((raw_path, source_item, page_path))

            moved_records.append(
                {
                    "source": str(source_item),
                    "target": str(raw_path),
                    "page": str(page_path),
                    "type": "directory" if raw_path.is_dir() else "file",
                }
            )

    except Exception:
        for raw_path, original_path, page_path in reversed(completed_items):
            remove_existing(page_path)

            parent = page_path.parent
            while parent != pages_dir and parent.exists():
                try:
                    parent.rmdir()
                except OSError:
                    break
                parent = parent.parent

            if raw_path.exists():
                restore_item(raw_path, original_path)

        raise

    return moved_records


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Archive all files and directories under a target directory into raw/YYYY/MM_DD/."
    )
    parser.add_argument(
        "target_dir",
        help="Directory whose contents will be moved into raw/YYYY/MM_DD/.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    moved_records = archive(Path(args.target_dir).expanduser().resolve())

    print(
        json.dumps(
            {
                "count": len(moved_records),
                "items": moved_records,
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()