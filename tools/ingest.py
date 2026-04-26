from __future__ import annotations

import argparse
import shutil
from pathlib import Path

from tools.common import INBOX_DIR, RAW_DIR, append_log, ensure_inside, raw_date_dir


def ingest(paths: list[str], *, date: str | None, copy: bool) -> list[Path]:
    target_dir = raw_date_dir(date)
    target_dir.mkdir(parents=True, exist_ok=True)

    archived: list[Path] = []

    for raw in paths:
        src = Path(raw)
        if not src.is_absolute():
            src = Path.cwd() / src

        if not src.exists():
            raise FileNotFoundError(src)

        ensure_inside(src, INBOX_DIR)

        dst = target_dir / src.name
        ensure_inside(dst, RAW_DIR)

        if dst.exists():
            raise FileExistsError(f"Refusing to overwrite existing raw file: {dst}")

        if copy:
            if src.is_dir():
                shutil.copytree(src, dst)
            else:
                shutil.copy2(src, dst)
            action = "Copied"
        else:
            shutil.move(str(src), str(dst))
            action = "Moved"

        archived.append(dst)
        append_log(f"{action} `{src.relative_to(Path.cwd())}` to `{dst.relative_to(Path.cwd())}`.")

    return archived


def main() -> None:
    parser = argparse.ArgumentParser(description="Archive inbox files into raw/YYYY/MMDD/.")
    parser.add_argument("paths", nargs="+")
    parser.add_argument("--date")
    parser.add_argument("--copy", action="store_true")
    args = parser.parse_args()

    archived = ingest(args.paths, date=args.date, copy=args.copy)
    for path in archived:
        print(path)


if __name__ == "__main__":
    main()
