# Repository Guidelines

Use repository skills under `.agents/skills/` and command-line tools under `tools/` whenever they match the task.

## Project Overview

This repository is a personal research knowledge base organized as a Markdown wiki.

The agent must:
- Ingest raw materials
- Structure knowledge into Markdown pages
- Maintain consistency, traceability, and quality

## Directory Structure

### inbox/
Contains all unprocessed files and materials.

### raw/
Stores original source materials after ingestion.

- Files must be organized by date:  
  raw/YYYY/MMDD/

- Rules:
  - Files in raw/ are immutable reference sources
  - Once placed in raw/, files must NOT be:
    - modified
    - renamed
    - deleted
    - overwritten

### wiki/
Primary working directory for structured knowledge.

Contains:
- processed, summarized, and synthesized content
- Markdown files only

Key files:
- wiki/index.md → entry point and knowledge index
- wiki/log.md → operation log
- wiki/template.md → global template

### Template Override

- If a subdirectory contains template.md (e.g. wiki/topics/template.md)
- That template overrides the global template
- Applies recursively to all subdirectories

### tools/
Command-line tools available for use

### .obsidian/
Private Obsidian metadata directory  
→ MUST NOT be modified or deleted

### .trash/
Temporary storage for deleted files

## File Organization Rules

### Topics / Concepts / Entities

- wiki/topics/ → research topics
- wiki/concepts/ → definitions, theorems, laws, terminology
- wiki/entities/ → people, tools, products, companies

Rules:
- One Markdown file per item
- Markdown file names must be lowercase with hyphens.
  - example: model-comparison.md

## YAML Frontmatter (Mandatory)

Every Markdown file must include:

```yaml
---
title: Title of this page
type: source | concept | entity | comparison | synthesis
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [tag1, tag2]
sources: ['raw/YYYY/MMDD/file.ext']
---
```
- If a local template exists → follow that template instead
- Missing or incorrect frontmatter is NOT allowed

## Writing Rules

- All content MUST be written in Chinese
- Technical terms:
  - Use standard Chinese translations when available
  - Otherwise keep English terms

Style:

- Clear heading hierarchy
- Short paragraphs
- Use Markdown formatting properly
- Use code blocks for commands and examples


## Cross-linking Rules

- Use [[wikilink]] between pages
- When referencing:
  - existing concepts/entities → MUST link
  - frequently used concepts without pages → MUST create page

## Knowledge Write-back Rules

After each user interaction:

- Evaluate whether new knowledge should be persisted
- If YES:
  - Create a new page (type: synthesis)
  - Update wiki/index.md
  - Append entry to wiki/log.md

## Update Strategy

- If modifying >10 pages:
  - list changes and request user confirmation
- Uncertain content:
  - mark with [!needs-verification]
- Conflicting content:
  - mark with [!contradiction] and explain sources

## Human Review Rules

If confidence is low:
- Add in frontmatter:`status: needs-review`

For data or conclusions:
- Mark with [!needs-verification]


## Markdown Quality Enforcement

After ANY modification in wiki/:

1. Run lint: `npx markdownlint wiki/`
2. Fix automatically: `npx markdownlint wiki/ --fix`
3. Manually fix remaining issues

Rules:
- Lint errors are BLOCKING
- Do not finalize changes if lint fails

## Allowed Actions

- Create / modify files in wiki/
- Create subdirectories in wiki/
- Create dated directories in raw/
- Move/copy files from inbox/ to raw/

## Restricted Actions

Require explicit user approval:
- Deleting ANY file or directory (except ingest move from inbox)

## Strictly Prohibited Actions

- Modify ANY file inside raw/
- Rename files inside raw/
- Delete files inside raw/
- Overwrite existing raw files
- Modify .obsidian/

## Completion Criteria

A task is considered complete ONLY IF:

- wiki/index.md is updated when new pages are created or renamed
- Links are valid
- log.md updated
- markdownlint passes with zero errors

## Agent States

- RAW (in inbox/)
- INGESTED (in raw/)
- PROCESSED (in wiki/)
- VERIFIED (reviewed)

Agent must ensure correct transitions.

## State Transitions

- inbox → raw → wiki must follow: RAW → INGESTED → PROCESSED
- Pages with status: needs-review are NOT VERIFIED

## Failure Handling

If any step fails:

- Stop execution immediately
- Report the exact failing command
- Do NOT proceed to subsequent steps

## Full Ingest Workflow

When the user asks to ingest, archive, import, or process files from `inbox/`, the full ingest workflow MUST be used whenever possible. The agent MUST NOT manually reproduce these steps if `tools/kb.py` is available.

Run:

```bash
python tools/kb.py ingest inbox/<file-or-dir>
```

This single command must complete the whole workflow:

1. Move or copy files from `inbox/` to `raw/YYYY/MMDD/`.
2. Create the corresponding Markdown page under `wiki/`.
3. Add required YAML frontmatter.
4. Update `wiki/index.md`.
5. Validate wikilinks.
6. Run markdownlint auto-fix and final lint check.
7. Append operation records to `wiki/log.md`.

Do not use the lower-level tools separately unless the user explicitly asks for a partial operation.

The lower-level tools remain available for debugging or targeted maintenance:

```bash
python tools/kb_ingest.py ...
python tools/kb_write_page.py ...
python tools/kb_sync_index.py
python tools/kb_link_check.py
python tools/kb_lint_fix.py
python tools/kb_log_update.py ...
python tools/kb_done_check.py
```
Moving files from inbox/ to raw/ as part of ingest is NOT considered deletion.

Ignore .DS_Store files

## Tool Usage Priority

- Prefer `tools/kb.py` over all other tools
- Use lower-level tools ONLY when explicitly required

## Idempotency

- Do not recreate pages if they already exist
- Do not duplicate log entries
- Avoid redundant writes