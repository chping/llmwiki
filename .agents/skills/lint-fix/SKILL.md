---
name: kb-lint-fix
description: Use after modifying any Markdown file under wiki to run markdownlint --fix and confirm zero lint errors.
---

# Knowledge Base Markdown Lint Skill

Use this skill after any change under `wiki/`.

Run:

```bash
python3 tools/lint_fix.py
```

This wraps:

```bash
npx markdownlint wiki/ --fix
npx markdownlint wiki/
```

Lint errors are blocking. Do not finalize the task until they are fixed.
