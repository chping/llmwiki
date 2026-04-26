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
- File names must be lowercase with hyphens
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

= Use [[wikilink]] between pages
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

- Add in frontmatter:
    `status: needs-review`

For data or conclusions:

- Mark with [!needs-verification]


## Markdown Quality Enforcement

After ANY modification in wiki/:

1. Run lint:
    npx markdownlint wiki/
2. Fix automatically:
    npx markdownlint wiki/ –fix
3. Manually fix remaining issues

Rules:

- Lint errors are BLOCKING
- Do not finalize changes if lint fails

## Ingest Workflow (Critical)

When processing inbox files:

1. Create target directory:
    raw/YYYY/MMDD/
2. Move or copy files from inbox/ → raw/YYYY/MMDD/
3. This movement:
    - DOES NOT require deletion approval
    - IS considered part of ingestion
4. After ingestion:
    - Files in raw/ become immutable

## Allowed Actions

- Create / modify files in wiki/
- Create subdirectories in wiki/
- Create dated directories in raw/
- Move/copy files from inbox/ → raw/

## Restricted Actions

Require explicit user approval:
- Deleting ANY file or directory (except ingest move from inbox)

## Strictly Prohibited Actions

- Modify ANY file inside raw/
- Rename files inside raw/
- Delete files inside raw_
- Overwrite existing raw files
- Modify .obsidian/

## Completion Criteria

A task is considered complete ONLY IF:

- Markdown content is created/updated
- Links are valid
- index.md updated (if needed)
- log.md updated
- markdownlint passes with zero errors

## Agent States

- RAW (in inbox/)
- INGESTED (in raw/)
- PROCESSED (in wiki/)
- VERIFIED (reviewed)

Agent must ensure correct transitions.

## Failure Handling

If a step fails:

- Do not continue blindly
- Report failure clearly
- Suggest next action