from __future__ import annotations

import argparse
from pathlib import Path

from tools.common import WIKI_DIR, append_log, ensure_inside, read_template, slugify, today_str


VALID_TYPES = {"source", "concept", "entity", "comparison", "synthesis"}


def default_subdir(page_type: str) -> Path:
    if page_type == "concept":
        return WIKI_DIR / "concepts"
    if page_type == "entity":
        return WIKI_DIR / "entities"
    if page_type == "source":
        return WIKI_DIR / "sources"
    return WIKI_DIR / "topics"


def build_frontmatter(title: str, page_type: str, sources: list[str], status: str | None) -> str:
    date = today_str()
    status_line = f"status: {status}\n" if status else ""
    source_items = ", ".join(repr(s) for s in sources)
    return (
        "---\n"
        f"title: {title}\n"
        f"type: {page_type}\n"
        f"created: {date}\n"
        f"updated: {date}\n"
        "tags: []\n"
        f"sources: [{source_items}]\n"
        f"{status_line}"
        "---\n"
    )


def create_page(
    title: str,
    *,
    page_type: str,
    directory: str | None,
    sources: list[str],
    status: str | None,
    overwrite: bool,
) -> Path:
    if page_type not in VALID_TYPES:
        raise ValueError(f"Invalid page type: {page_type}")

    target_dir = Path(directory) if directory else default_subdir(page_type)
    if not target_dir.is_absolute():
        target_dir = Path.cwd() / target_dir

    ensure_inside(target_dir, WIKI_DIR)
    target_dir.mkdir(parents=True, exist_ok=True)

    path = target_dir / f"{slugify(title)}.md"
    if path.exists() and not overwrite:
        raise FileExistsError(f"Page already exists: {path}")

    template = read_template(target_dir)
    frontmatter = build_frontmatter(title, page_type, sources, status)

    if template:
        body = template
        if body.startswith("---"):
            second = body.find("---", 3)
            if second != -1:
                body = body[second + 3 :].lstrip()
        content = frontmatter + "\n" + body
    else:
        content = frontmatter + f"\n# {title}\n\n[!needs-verification]\n"

    path.write_text(content, encoding="utf-8")
    append_log(f"Created page `{path.relative_to(Path.cwd())}`.")
    return path


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a wiki Markdown page with frontmatter.")
    parser.add_argument("title")
    parser.add_argument("--type", required=True, choices=sorted(VALID_TYPES))
    parser.add_argument("--dir", dest="directory")
    parser.add_argument("--source", action="append", default=[])
    parser.add_argument("--status", choices=["needs-review"])
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()

    path = create_page(
        args.title,
        page_type=args.type,
        directory=args.directory,
        sources=args.source,
        status=args.status,
        overwrite=args.overwrite,
    )
    print(path)


if __name__ == "__main__":
    main()
