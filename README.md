# Knowledge Base Agent Tools v3 Complete

This package provides a complete repository-local workflow for a personal research knowledge base.

## Core workflow

```text
analyze inbox -> write Chinese Markdown with inbox refs -> archive -> rewrite refs to raw -> index -> links -> lint -> log
```

## Install

Copy all files from this package into the repository root.

Expected layout:

```text
repo/
├── AGENTS.md
├── inbox/
├── raw/
├── wiki/
├── tools/
│   ├── __init__.py
│   ├── kb.py
│   ├── kb_common.py
│   └── ...
└── .agents/
    └── skills/
        └── ...
```

## Main command

```bash
python3 tools/kb.py ingest inbox/<file-or-dir>
```

## Examples

```bash
python3 tools/kb.py ingest inbox/paper.pdf --title "SRAM 读电流分析" --type source
python3 tools/kb.py ingest inbox/note.md --type synthesis --needs-review
python3 tools/kb.py ingest inbox/file.pdf --copy
python3 tools/kb.py ingest inbox/file.pdf --create-missing-links
```

## Requirements

Python 3.10+ is recommended.

For Markdown linting:

```bash
npm install -g markdownlint-cli
```

The workflow will call:

```bash
npx markdownlint wiki/ --fix
npx markdownlint wiki/
```

## Notes

- The workflow never predicts raw paths before archive.
- Generated Markdown content is Chinese.
- Markdown initially uses exact inbox paths.
- After archive, references are replaced with actual raw paths.
