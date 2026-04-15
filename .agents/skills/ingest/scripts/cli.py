#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

CURRENT_DIR = Path(__file__).resolve().parent
if str(CURRENT_DIR) not in sys.path:
    sys.path.insert(0, str(CURRENT_DIR))

from workflow import run_workflow  # noqa: E402


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Pure Python Codex + archive workflow for processing raw/inbox into wiki pages."
    )
    parser.add_argument("--repo", required=True, help="Repository root path")
    parser.add_argument("--today", default=None, help="Override date in YYYY-MM-DD format")
    parser.add_argument("--dry-run", action="store_true", help="Validate and plan changes without writing files")
    parser.add_argument("--skip-codex", action="store_true", help="Skip Codex and only archive using the existing manifest")
    parser.add_argument("--archive-only", action="store_true", help="Alias for --skip-codex")
    parser.add_argument("--codex-cmd", default="codex", help="Codex executable")
    parser.add_argument(
        "--codex-run-template",
        default=None,
        help="Optional command template override. If omitted, codex_run_template.txt is used.",
    )
    parser.add_argument("--timeout", type=int, default=None, help="Optional Codex subprocess timeout in seconds")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    skill_dir = Path(__file__).resolve().parent.parent

    results = run_workflow(
        repo=repo,
        skill_dir=skill_dir,
        codex_cmd=args.codex_cmd,
        codex_run_template=args.codex_run_template,
        today=args.today,
        dry_run=args.dry_run,
        skip_codex=args.skip_codex,
        archive_only=args.archive_only,
        timeout=args.timeout,
    )

    print(f"Processed entries: {len(results)}")
    for item in results:
        print(
            f"- {item['inbox_path']} -> {item['archive_path']} | "
            f"origin={item['fingerprint_origin']} | rewritten={len(item['rewritten_pages'])}"
        )


if __name__ == "__main__":
    main()
