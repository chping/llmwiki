#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
from datetime import datetime
from pathlib import Path


def remove_existing(path: Path) -> None:
    if path.is_dir() and not path.is_symlink():
        shutil.rmtree(path)
    elif path.exists() or path.is_symlink():
        path.unlink()


def collect_file_list(source_dir: Path, raw_dir: Path) -> list[dict[str, str]]:
    records: list[dict[str, str]] = []

    for path in sorted(source_dir.rglob("*")):
        rel_path = path.relative_to(source_dir)
        target_path = raw_dir / rel_path

        records.append(
            {
                "source": str(path),
                "target": str(target_path),
                "type": "directory" if path.is_dir() else "file",
            }
        )

    return records


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
    raw_dir.mkdir(parents=True, exist_ok=True)

    moved_records = collect_file_list(target_dir, raw_dir)

    for item in sorted(target_dir.iterdir()):
        dest = raw_dir / item.name
        remove_existing(dest)
        shutil.move(str(item), str(dest))

    return moved_records


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Archive all files and directories under a target directory into raw/YYYY_MM_DD/."
    )
    parser.add_argument(
        "target_dir",
        help="Directory whose contents will be moved into raw/YYYY_MM_DD/.",
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