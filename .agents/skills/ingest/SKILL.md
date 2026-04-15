---
name: ingest
description: Process files in raw/inbox for this repository. Use this when the task is to analyze inbox notes, update wiki pages, add source backlinks, generate a processed manifest, and archive processed files into raw/YYYY/MMDD/.
---

# Wiki Inbox Ingest

Use this skill only for this repository's inbox-to-wiki workflow.

## What this skill does
- Analyze files in `raw/inbox/`
- Create or update curated wiki pages in `wiki/`
- Add `## Sources` backlinks to original files
- Update `wiki/index.md` and `wiki/log.md`
- Generate `.wiki-inbox/processed-manifest.json`
- Archive processed files into `raw/YYYY/MMDD/`
- Rewrite wiki backlinks to the archived paths

## Required workflow
1. Review `AGENTS.md`.
2. Read `references/codex_prompt_template.md` for the content-generation contract.
3. Use the Python scripts in `scripts/` for deterministic execution.
4. Do not manually move files from `raw/inbox/` unless the workflow requires it.
5. Prefer running:

```bash
python3 .agents/skills/ingest/scripts/cli.py --repo .