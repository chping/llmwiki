from __future__ import annotations

import argparse
import shutil
from pathlib import Path

from tools.kb_common import INBOX_DIR, RAW_DIR, append_log, ensure_inside, raw_date_dir, rel


def ingest(paths: list[str], *, date: str | None = None, copy: bool = False) -> dict[str, str]:
    target_dir = raw_date_dir(date)
    target_dir.mkdir(parents=True, exist_ok=True)

    path_map: dict[str, str] = {}

    for raw_path in paths:
        src = Path(raw_path)
        if not src.is_absolute():
            src = Path.cwd() / src

        if not src.exists():
            raise FileNotFoundError(src)

        ensure_inside(src, INBOX_DIR)

        dst = target_dir / src.name
        ensure_inside(dst, RAW_DIR)

        if dst.exists():
            raise FileExistsError(f"Refusing to overwrite existing raw file: {dst}")

        src_rel = rel(src)

        if copy:
            if src.is_dir():
                shutil.copytree(src, dst)
            else:
                shutil.copy2(src, dst)
            action = "Copied"
        else:
            shutil.move(str(src), str(dst))
            action = "Moved"

        dst_rel = rel(dst)
        path_map[src_rel] = dst_rel
        append_log(f"{action} `{src_rel}` to `{dst_rel}`.")

    return path_map


def main() -> None:
    parser = argparse.ArgumentParser(description="Archive inbox files into raw/YYYY/MMDD/.")
    parser.add_argument("paths", nargs="+")
    parser.add_argument("--date")
    parser.add_argument("--copy", action="store_true")
    args = parser.parse_args()

    path_map = ingest(args.paths, date=args.date, copy=args.copy)
    for src, dst in path_map.items():
        print(f"{src} -> {dst}")


if __name__ == "__main__":
    main()
