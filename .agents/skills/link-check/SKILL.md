---
name: kb-link-check
description: Use when validating Obsidian-style wikilinks in wiki Markdown pages.
---

# Knowledge Base Link Check Skill

Use this skill after creating or modifying Markdown files under `wiki/`.

Run:

```bash
python3 tools/link_check.py
```

If missing concept pages should be created as placeholders, run:

```bash
python3 tools/link_check.py --create-missing
```

Do not create placeholder pages for entities unless the target is clearly a concept. For entities, create a proper entity page with `write_page.py`.
