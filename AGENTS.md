# Repository Guidelines

Use repository skills under `.agents/skills/` and command-line tools under `tools/` whenever they match the task.

## Project Overview

This repository is a personal research knowledge base organized as a Markdown wiki.

The agent must:

- Analyze source materials before archiving them.
- Structure knowledge into Markdown pages.
- Maintain consistency, traceability, and quality.
- Keep all generated wiki Markdown content in Chinese.

## Directory Structure

### inbox/

Contains all unprocessed files and materials.

### raw/

Stores original source materials after ingestion.

Files must be organized by date:

```text
raw/YYYY/MMDD/
```

Rules:

- Files in `raw/` are immutable reference sources.
- Once placed in `raw/`, files must not be modified, renamed, deleted, or overwritten.
- The agent must not predict final `raw/` paths before the archive step is completed.

### wiki/

Primary working directory for structured knowledge.

Contains processed, summarized, and synthesized Markdown content.

Key files:

- `wiki/index.md`: entry point and knowledge index
- `wiki/log.md`: operation log

### Template Override

If a subdirectory contains `template.md`, such as `wiki/topics/template.md`, that template overrides the global template and applies recursively to that subdirectory and its descendants.

### tools/

Command-line tools available for use.

### .agents/skills/

Repository-local agent skills.

### .obsidian/

Private Obsidian metadata directory. The agent must not modify or delete anything under `.obsidian/`.

### .trash/

Temporary storage for deleted files.

## File Organization Rules

### Pages / Topics / Concepts / Entities

- `wiki/pages/`:     Archived source pages. Each Markdown file corresponds to a source file with the same name that has been archived in the raw/ directory, and is used to record the summary, key points, and essential content extraction of that source file.
- `wiki/topics/`: research topics
- `wiki/concepts/`: definitions, theorems, laws, terminology
- `wiki/entities/`: people, tools, products, companies

Rules:

- Create one Markdown file per item.
- Markdown file names must be lowercase with hyphens.
- Example: `wiki/topics/model-comparison.md`

## YAML Frontmatter

Every Markdown file under `wiki/` must include YAML frontmatter.

Default frontmatter:

```yaml
---
title: Title of this page
type: source | concept | entity 
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [tag1, tag2]
---
```

Rules:

- If a local `template.md` exists, follow that template instead.
- Missing or incorrect frontmatter is not allowed.

## Writing Language Enforcement

All Markdown content generated under `wiki/` must be written in Chinese.

This applies to:

- Page content
- Section titles
- Explanations and summaries
- Generated placeholder text

English is allowed only for:

- File paths
- Commands
- Code
- Technical terms without standard Chinese translations
- Proper nouns and product names

## Writing Style

- Use clear heading hierarchy.
- Use Markdown formatting properly.
- Use fenced code blocks for commands and examples.
- Do not create empty pages.
- If the analysis is incomplete, mark the relevant content with tag `#needs-verification`.

## Cross-linking Rules

- Use `[[wikilink]]` between markdown pages.
- Use `[title](soruce_link)` when refer to files in `raw/`
- When referencing existing concepts or entities, link them.
- When a frequently used concept has no independent page, create a new page.

## Knowledge Write-back Rules

After each user interaction:

- Evaluate whether new knowledge should be persisted.
- If yes:
  - Create or update a Markdown page.
  - Update `wiki/index.md` if discoverability changes.
  - Append an entry to `wiki/log.md`.

## Update Strategy

- If modifying more than 10 pages, list the planned changes and request user confirmation first.
- Mark uncertain content with tag `#needs-verification!`.
- Mark conflicting content with  tag `#contradiction!` and explain the conflicting sources.

## Human Review Rules

If confidence is low, add this to the page frontmatter:

```yaml
status: needs-review
```

For data, conclusions, or judgments, mark uncertain statements with tag `#needs-verification!`.

## Markdown Quality Enforcement

After any modification under `wiki/`:

1. Run lint:

   ```bash
   npx markdownlint wiki/
   ```

2. Fix automatically:

   ```bash
   npx markdownlint wiki/ --fix
   ```

3. Manually fix remaining issues.

Rules:

- Lint errors are blocking.
- Do not finalize changes if lint fails.


## Allowed Actions

- Create or modify files in `wiki/`.
- Create subdirectories in `wiki/`.
- Create dated directories in `raw/`.
- Move or copy files from `inbox/` to `raw/` as part of the ingest workflow.

## Restricted Actions

Require explicit user approval:

- Deleting any file or directory, except moving files from `inbox/` to `raw/` during ingest.

## Strictly Prohibited Actions

- Modify any file inside `raw/`.
- Rename files inside `raw/`.
- Delete files inside `raw/`.
- Overwrite existing raw files.
- Modify or delete anything under `.obsidian/`.

## Completion Criteria

A task is considered complete only if:

- Markdown content is created or updated when required.
- `wiki/index.md` is updated when new pages are created or renamed.
- Wikilinks are valid.
- `wiki/log.md` is updated.
- markdownlint passes with zero errors.

## Failure Handling

If any step fails:

- Stop execution immediately.
- Report the exact failing command.
- Do not proceed to subsequent steps.
- Do not silently ignore partial updates.

## Idempotency

- Do not recreate pages if they already exist.
- Do not duplicate log entries intentionally.
- Avoid redundant writes.
- Do not overwrite existing `raw/` files.
