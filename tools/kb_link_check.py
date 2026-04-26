from __future__ import annotations

import argparse
import re
from pathlib import Path

from tools.kb_common import WIKI_DIR, slugify


WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
SKIP_FILES = {"template.md"}


def collect_pages() -> dict[str, Path]:
    pages: dict[str, Path] = {}

    for path in WIKI_DIR.rglob("*.md"):
        if path.name in SKIP_FILES:
            continue

        rel_no_suffix = path.relative_to(WIKI_DIR).with_suffix("").as_posix()

        pages[path.stem] = path
        pages[path.stem.lower()] = path
        pages[rel_no_suffix] = path
        pages[rel_no_suffix.lower()] = path

    return pages


def check_links() -> int:
    pages = collect_pages()
    missing: list[tuple[Path, str]] = []

    for markdown_path in WIKI_DIR.rglob("*.md"):
        if markdown_path.name in SKIP_FILES:
            continue

        text = markdown_path.read_text(encoding="utf-8")

        for match in WIKILINK_RE.finditer(text):
            target = match.group(1).strip()
            key = slugify(target)

            if target not in pages and target.lower() not in pages and key not in pages:
                missing.append((markdown_path, target))

    if not missing:
        print("All wikilinks resolve.")
        return 0

    print("Missing wikilinks found. Create the target markdown files manually.")
    print("Expected action: analyze each missing target and create or update the corresponding page.")

    for src, target in missing:
        print(f"- [[{target}]] referenced by {src}")

    return 1


def main() -> None:
    parser = argparse.ArgumentParser(description="Check wiki-style [[links]].")
    parser.parse_args()

    raise SystemExit(check_links())


if __name__ == "__main__":
    main()