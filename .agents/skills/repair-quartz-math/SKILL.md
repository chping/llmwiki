---
name: repair-quartz-math
description: Scan and repair Markdown math that Quartz cannot render. Use when Codex needs to check all wiki pages for unsupported LaTeX delimiters, convert Obsidian-style \(...\) and \[...\] formulas to Quartz-compatible $...$ and $$...$$, verify that protected notes and code remain unchanged, or validate rendered KaTeX output.
---

# Repair Quartz Math

Use this skill only in the `llmwiki` repository. Quartz v5 uses `remark-math` with KaTeX: inline formulas use `$...$` and display formulas use `$$...$$`.

## Workflow

1. Inspect the worktree:

```bash
git status --short
```

2. Scan every Markdown page without changing files:

```bash
python3 .agents/skills/repair-quartz-math/scripts/repair_quartz_math.py wiki
```

The script reports unsupported `\(...\)` and `\[...\]` delimiters outside YAML frontmatter, fenced code, inline code, and protected `<!-- user-notes:start -->...<!-- user-notes:end -->` blocks. Treat unmatched delimiters as manual-review errors.

3. Apply only safe delimiter conversions:

```bash
python3 .agents/skills/repair-quartz-math/scripts/repair_quartz_math.py wiki --fix
```

Do not rewrite formula bodies. Review every changed file and preserve protected user notes byte-for-byte.

4. Rescan until the command exits successfully with zero findings:

```bash
python3 .agents/skills/repair-quartz-math/scripts/repair_quartz_math.py wiki
```

5. Run repository checks:

```bash
node scripts/update-wiki-index.mjs
npx --yes markdownlint-cli wiki/
cd site
npm run quartz -- build -d ../wiki
```

6. If formulas changed, confirm generated HTML contains KaTeX markup and no unsupported delimiters:

```bash
rg 'katex|math-display' site/public/
rg -F '\(' site/public/ || true
rg -F '\[' site/public/ || true
```

7. Inspect `git diff --check` and the relevant file diffs. Report changed pages, conversion count, lint result, Quartz build result, and any formulas requiring manual review.

## Constraints

- Never modify `.obsidian/` or `.git/`.
- Never modify, remove, reorder, or relocate protected user-note blocks.
- Never alter fenced code, inline code, YAML frontmatter, escaped literals, or formula content.
- Do not convert ambiguous unmatched delimiters automatically.
- If more than 10 wiki files would change, stop after the scan and ask for confirmation.
- After changing files under `wiki/`, append the required monthly operation log.
