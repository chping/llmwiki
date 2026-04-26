---
name: kb-ingest
description: Use when processing files from inbox into raw/YYYY/MMDD and recording the ingestion in the wiki log.
---

# Knowledge Base Ingest Skill

Use this skill when the user asks to ingest, archive, import, process, or move materials from `inbox/`.

Follow this workflow:

1. Inspect the file names in `inbox/`.
2. Move or copy selected files into `raw/YYYY/MMDD/` using:

```bash
python3 tools/ingest.py inbox/<file-or-dir>
```

Use `--copy` only when the source must remain in `inbox/`.

3. Treat files under `raw/` as immutable after ingestion.
4. Do not overwrite existing files in `raw/`.
5. Continue by creating or updating `wiki/` pages if requested.
6. Run completion checks before finalizing:

```bash
python3 tools/done_check.py
```
