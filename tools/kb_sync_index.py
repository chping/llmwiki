from __future__ import annotations

from collections import defaultdict
from pathlib import Path

from tools.kb_common import WIKI_DIR, append_log


SKIP = {"index.md", "log.md", "template.md"}


def sync_index() -> Path:
    index_path = WIKI_DIR / "index.md"
    pages: dict[str, list[Path]] = defaultdict(list)

    for path in sorted(WIKI_DIR.rglob("*.md")):
        rel_path = path.relative_to(WIKI_DIR)

        if rel_path.name in SKIP:
            continue
        if "template.md" in rel_path.parts:
            continue

        group = rel_path.parts[0] if len(rel_path.parts) > 1 else "pages"
        pages[group].append(rel_path)

    block_lines = ["<!-- AUTO-GENERATED:START -->", ""]

    for group in sorted(pages):
        block_lines.append(f"## {group}")
        block_lines.append("")

        for rel_path in pages[group]:
            link_target = rel_path.with_suffix("").as_posix()
            title = rel_path.stem.replace("-", " ")
            block_lines.append(f"- [[{link_target}|{title}]]")

        block_lines.append("")

    block_lines.append("<!-- AUTO-GENERATED:END -->")
    new_block = "\n".join(block_lines)

    if index_path.exists():
        old = index_path.read_text(encoding="utf-8")
        start = "<!-- AUTO-GENERATED:START -->"
        end = "<!-- AUTO-GENERATED:END -->"

        if start in old and end in old:
            prefix = old.split(start, 1)[0].rstrip()
            suffix = old.split(end, 1)[1].lstrip()
            content = prefix + "\n\n" + new_block + "\n\n" + suffix
        else:
            content = old.rstrip() + "\n\n" + new_block + "\n"
    else:
        content = "# Knowledge Base Index\n\n" + new_block + "\n"

    index_path.write_text(content, encoding="utf-8")
    append_log("Synchronized `wiki/index.md`.")
    return index_path


def main() -> None:
    print(sync_index())


if __name__ == "__main__":
    main()
