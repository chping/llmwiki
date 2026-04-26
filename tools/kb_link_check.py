from __future__ import annotations

import argparse
import re
from pathlib import Path

from tools.kb_common import WIKI_DIR, ensure_inside, slugify, today_str


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


def check_links(*, create_missing: bool = False) -> int:
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

    for src, target in missing:
        print(f"Missing wikilink target: [[{target}]] referenced by {src}")

    if create_missing:
        concepts_dir = WIKI_DIR / "concepts"
        concepts_dir.mkdir(parents=True, exist_ok=True)

        for _, target in missing:
            path = concepts_dir / f"{slugify(target)}.md"
            ensure_inside(path, WIKI_DIR)

            if not path.exists():
                date = today_str()
                path.write_text(
                    "---\n"
                    f"title: {target}\n"
                    "type: concept\n"
                    f"created: {date}\n"
                    f"updated: {date}\n"
                    "tags: []\n"
                    "sources: []\n"
                    "status: needs-review\n"
                    "---\n\n"
                    f"# {target}\n\n[!needs-verification]\n",
                    encoding="utf-8",
                )
                print(f"Created placeholder: {path}")

    return 1


def main() -> None:
    parser = argparse.ArgumentParser(description="Check wiki-style [[links]].")
    parser.add_argument("--create-missing", action="store_true")
    args = parser.parse_args()

    raise SystemExit(check_links(create_missing=args.create_missing))


if __name__ == "__main__":
    main()
