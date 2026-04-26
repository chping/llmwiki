---
name: kb-full-ingest
description: Use when the user asks to ingest, archive, import, or process materials from inbox and complete the whole knowledge-base workflow automatically.
---

# Full Knowledge Base Ingest Skill

Use this skill whenever the user asks to ingest or archive materials.

Run the full workflow with:

```bash
python3 tools/kb.py ingest inbox/<file-or-dir>
```

This command performs all required steps:

1. Move or copy files from `inbox/` to `raw/YYYY/MMDD/`.
2. Create a corresponding Markdown page in `wiki/`.
3. Use the required YAML frontmatter.
4. Update `wiki/index.md`.
5. Check wikilinks.
6. Run markdownlint auto-fix.
7. Record operation logs in `wiki/log.md`.

Useful options:

```bash
python3 tools/kb.py ingest inbox/paper.pdf --title "Paper Title" --type source
python3 tools/kb.py ingest inbox/note.md --type synthesis --needs-review
python3 tools/kb.py ingest inbox/file.pdf --copy
python3 tools/kb.py ingest inbox/file.pdf --create-missing-links
```

Do not run partial tools unless the user explicitly asks for a partial workflow.
