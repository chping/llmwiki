# Repository Guidelines

## Project Structure & Module Organization
This repository is a lightweight Markdown wiki. Keep source material in `raw/`, using `raw/inbox/` for unprocessed notes and dated folders in the format `raw/YYYY/MMDD/` for archived processed inputs. Publish curated content in `wiki/`. The current entry points are `wiki/index.md` for navigation and `wiki/log.md` for the running project log. Add new topic pages under `wiki/` and link them from `wiki/index.md`.

## Build, Test, and Development Commands
There is no build system or test runner configured yet. Day-to-day work is file-based:

- `ls wiki raw` to inspect the current content layout.
- `sed -n '1,120p' wiki/index.md` to review an existing page from the terminal.
- `rg "keyword" wiki raw` %% to %% find topics, notes, or source references quickly.

If tooling is added later, document the exact commands here and keep them runnable from the repository root.

## Inbox Processing Workflow
Use the standard inbox-processing workflow to process `raw/inbox/`.

This repository provides a repo-local Codex skill for inbox processing:

- `.agents/skills/ingest/`

For deterministic local execution, run:

```bash
python3 .agents/skills/ingest/scripts/cli.py --repo .
```
For Codex-driven execution, prefer the repo-local skill workflow by asking Codex to use the ingest skill when processing inbox files.

This workflow:
- uses Codex to analyze inbox files and update wiki pages,
- requires wiki pages to include ## Sources backlinks to raw/inbox/...,
- requires Codex to write .wiki-inbox/processed-manifest.json,
- archives processed files into raw/YYYY/MMDD/,
- rewrites wiki backlinks to the archive paths,
- records archive actions in wiki/log.md,
- stores manifest history under .wiki-inbox/history/.

The default Codex command template is stored in:
- .agents/skills/ingest/references/codex_run_template.txt

Do not manually move files out of raw/inbox/ before the archive step succeeds.

## Coding Style & Naming Conventions
Write content in Markdown with clear heading hierarchy and short paragraphs. Prefer fenced code blocks for commands and examples. Use descriptive, lowercase file names with hyphens for multiword pages, for example `wiki/model-comparison.md`. Keep log entries chronological under dated headings such as `## 2026-04-15`. Use relative links between wiki pages where possible.

## Testing Guidelines
Quality checks are manual at this stage. Before submitting changes, verify that:

- Markdown headings are ordered correctly.
- Internal links point to existing files.
- New pages are linked from `wiki/index.md` when they should be discoverable.
- Significant updates are recorded in `wiki/log.md`.

When automated linting or link checking is introduced, add the command here and run it before review.

## Commit & Pull Request Guidelines
This workspace does not currently include Git history, so no established commit convention can be inferred. Use short, imperative commit subjects such as `Add retrieval notes page` or `Update project log`. Keep each commit focused on one content change. Pull requests should include a brief summary, the files changed, and any follow-up pages or links contributors should add.

## Contributor Workflow
Start with raw notes in `raw/inbox/`, distill them into topic pages in `wiki/`, update `wiki/index.md` and `wiki/log.md`, then archive processed source files into `raw/YYYY/MMDD/` using the standard inbox-processing workflow.

When using Codex inside this repository, prefer the repo-local skill under `.agents/skills/ingest/` instead of ad hoc manual inbox processing.
