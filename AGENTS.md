# Repository Guidelines

## Project Overview
This repository is a personal research knowledge base organized as a Markdown wiki.
Primary working directories:

- `wiki/`
- `.agents/skills/`

All generated wiki content must be written in Chinese unless explicitly required otherwise.

## Skills

Use repository skills under:
```
.agents/skills/
```
whenever relevant.

## Critical Rules

### Protected User Notes
The following block is strictly protected and must never be modified, removed, reordered, or relocated:
```markdown
<!-- user-notes:start -->
...
<!-- user-notes:end -->
```
When updating a file:

1. Never modify this block.
2. Preserve the entire block exactly
3. Apply changes only outside the block
4. Restore the block unchanged

### Forbidden Paths

Never modify anything under:

```
.obsidian/
.git/
```


### Minimal Changes

* Prefer minimal, localized edits.
* Do not rewrite large sections unless necessary.
* Preserve existing structure and writing style whenever possible.

### Idempotency

Avoid duplicate pages, duplicate log entries, and redundant rewrites.


## Writing Rules

### Language

* All wiki content must be written in Chinese
* English is allowed for:
    * code
    * commands
    * file paths
    * filenames
    * technical terms
    * proper nouns

### Markdown Rules

* Do not insert artificial line wrapping
* Keep paragraphs as single continuous lines
* Use proper Markdown headings
* Use fenced code blocks for commands and examples
* Do not create empty pages

### Linking Rules
Use:

* [[wikilink]] for internal references
* Markdown links for external or raw file references

When an important concept appears repeatedly and has no dedicated page, create one.


## Templates and Metadata

### Frontmatter

All Markdown files under wiki/ must contain YAML frontmatter.

Default format:
```yaml
---
category: paper | topic | chat
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: []
summary: 
zotero: 
  item_key:
  citation_key:
source_uri:
---
```

If a directory contains template.md, that template overrides the default recursively.


## Update Workflow

### Update Rules

When updating wiki content:

* Prefer updating existing pages instead of creating duplicates
* Update wiki/index.md if discoverability changes
* Append a concise entry to wiki/log.md

If modifying more than 10 files, ask for confirmation first.

### Markdown Quality

After modifying Markdown files under wiki/:
```bash
npx markdownlint wiki/
```
If needed:
```bash
npx markdownlint wiki/ --fix
```
Manually resolve remaining important issues.

## Wiki Structure

### Main Directories

  * wiki/index.md — wiki pages index for navigation 
  * wiki/papers/ — paper reading notes
  * wiki/topics/ — research topics
  * wiki/chats/ — chat records
  * wiki/logs/YYYY_MM_log.md — operation logs, split by month

## Permissions

### Allowed Actions

* Create or update files under wiki/
* Create subdirectories under wiki/

### Actions Requiring Confirmation

* Deleting files or directories


## Completion Criteria

A task is complete when:

* Required wiki pages are updated
* Protected blocks are preserved
* Important metadata and links remain valid

