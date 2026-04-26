---
name: kb-sync-index
description: Use when new wiki pages are created or discoverability needs to be refreshed in wiki/index.md.
---

# Knowledge Base Index Sync Skill

Use this skill after creating, renaming, or moving pages under `wiki/`.

Run:

```bash
python3 tools/sync_index.py
```

Then run:

```bash
python3 tools/done_check.py
```
