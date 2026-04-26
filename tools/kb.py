from __future__ import annotations

import argparse
import subprocess
from pathlib import Path

from tools.common import append_log
from tools.ingest import ingest
from tools.sync_index import sync_index
from tools.write_page import create_page


def rel(path: Path) -> str:
    return path.relative_to(Path.cwd()).as_posix()


def run_step(cmd: list[str], *, required: bool = True) -> int:
    print("+ " + " ".join(cmd))
    proc = subprocess.run(cmd)
    if required and proc.returncode != 0:
        raise SystemExit(proc.returncode)
    return proc.returncode


def infer_title_from_path(path: Path) -> str:
    return path.stem.replace("-", " ").replace("_", " ").strip().title()


def ingest_full(args: argparse.Namespace) -> None:
    archived = ingest(args.paths, date=args.date, copy=args.copy)

    created_pages: list[Path] = []
    if not args.no_page:
        if args.title and len(archived) > 1:
            raise ValueError("--title can only be used when ingesting one file.")

        for raw_path in archived:
            title = args.title or infer_title_from_path(raw_path)
            page = create_page(
                title,
                page_type=args.type,
                directory=args.directory,
                sources=[rel(raw_path)],
                status="needs-review" if args.needs_review else None,
                overwrite=args.overwrite_page,
            )
            created_pages.append(page)

    if not args.no_index:
        sync_index()

    if not args.no_link_check:
        link_cmd = ["python", "tools/link_check.py"]
        if args.create_missing_links:
            link_cmd.append("--create-missing")
        run_step(link_cmd, required=not args.allow_link_errors)

    if not args.no_lint:
        run_step(["python", "tools/lint_fix.py"], required=True)

    append_log(
        "Completed full ingest workflow for "
        + ", ".join(f"`{rel(path)}`" for path in archived)
        + "."
    )

    print("Full ingest workflow completed.")
    if archived:
        print("Archived files:")
        for path in archived:
            print(f"  - {rel(path)}")
    if created_pages:
        print("Created pages:")
        for path in created_pages:
            print(f"  - {rel(path)}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Unified knowledge-base CLI.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    ingest_parser = subparsers.add_parser(
        "ingest",
        description="Run the full ingest workflow: inbox -> raw -> wiki page -> index -> link check -> lint.",
    )
    ingest_parser.add_argument("paths", nargs="+")
    ingest_parser.add_argument("--date")
    ingest_parser.add_argument("--copy", action="store_true")
    ingest_parser.add_argument("--title")
    ingest_parser.add_argument(
        "--type",
        default="source",
        choices=["source", "concept", "entity", "comparison", "synthesis"],
    )
    ingest_parser.add_argument("--dir", dest="directory")
    ingest_parser.add_argument("--needs-review", action="store_true")
    ingest_parser.add_argument("--overwrite-page", action="store_true")
    ingest_parser.add_argument("--create-missing-links", action="store_true")
    ingest_parser.add_argument("--allow-link-errors", action="store_true")
    ingest_parser.add_argument("--no-page", action="store_true")
    ingest_parser.add_argument("--no-index", action="store_true")
    ingest_parser.add_argument("--no-link-check", action="store_true")
    ingest_parser.add_argument("--no-lint", action="store_true")

    args = parser.parse_args()

    if args.command == "ingest":
        ingest_full(args)
    else:
        raise SystemExit(f"Unknown command: {args.command}")


if __name__ == "__main__":
    main()
