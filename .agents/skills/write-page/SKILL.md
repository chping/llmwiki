---
name: kb-write-page
description: Use when creating a new Markdown knowledge page under wiki with required frontmatter and template handling.
---

# Knowledge Base Write Page Skill

Use this skill when creating a new `wiki/` Markdown page.

Create pages with:

```bash
python3 tools/write_page.py "Page Title" --type concept
python3 tools/write_page.py "Page Title" --type entity
python3 tools/write_page.py "Page Title" --type synthesis --source raw/YYYY/MMDD/file.pdf
```

Rules:

- Write page content in Chinese.
- Use the applicable `template.md`.
- Use required YAML frontmatter.
- Use `[[wikilink]]` for existing concepts and entities.
- Mark uncertain statements with `[!needs-verification]`.
- Add `--status needs-review` when confidence is low.

Run checks before finalizing:

```bash
python3 tools/done_check.py
```
