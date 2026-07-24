---
name: publish-quartz-site
description: Commit, push, and publish the llmwiki Quartz website. Use when the user asks to 提交并发布, commit and push, push and publish, 发布站点, 发布 wiki, deploy Quartz, update the GitHub Pages site, rerun or check the publish workflow, or otherwise wants Codex to validate the wiki, create a git commit, push to GitHub, and confirm the GitHub Pages deployment for this repository.
---

# Publish Quartz Site

## Scope

Use this skill only in `/Users/chengping/code/github/llmwiki`.

Publish source content from `wiki/` through the Quartz project in `site/`. Do not move Markdown content into `site/` and do not recreate a root `content` symlink.

## Workflow

1. Inspect status before changing anything:

```bash
git status --short
```

2. Identify the requested commit scope. Include only changes that belong to the user's publish request. Never stage `.obsidian/` changes unless the user explicitly asks.

3. If Markdown under `wiki/` changed, run Markdown lint:

```bash
npx --yes markdownlint-cli wiki/
```

If lint fails, fix only necessary Markdown issues outside protected `<!-- user-notes:start -->...<!-- user-notes:end -->` blocks, then rerun lint.

4. Check Quartz math syntax before building. Quartz v5 LaTeX uses `remark-math`, so display math must use `$$...$$` and inline math must use `$...$`. It does not render Obsidian/LaTeX delimiters `\[...\]` or `\(...\)` reliably.

```bash
rg '^\\\[|^\\\]$|\\\(|\\\)' wiki/
```

If matches are found, convert only formula delimiters:

- Convert block display math from:

```latex
\[
...
\]
```

to:

```latex
$$
...
$$
```

- Convert inline math from `\(x\)` to `$x$` only when it is clearly math syntax, not prose or an escaped literal.

After conversion, rerun the check until no unsupported formula delimiters remain.

5. Validate Quartz build from `site/`:

```bash
cd site
npm run quartz -- build -d ../wiki
```

If the local default Node is too old, use the Codex bundled Node path already available in the thread, or tell the user to use Node 22+.

If formula rendering was changed, inspect the generated HTML for KaTeX markers before committing:

```bash
rg 'katex|math-display' site/public/
```

If formulas still appear as raw `\[` or `\(` in `site/public/`, fix the Markdown delimiters and rebuild.

6. Stage only relevant files:

```bash
git add <files>
```

7. Commit with a concise Chinese message unless the user provided one:

```bash
git commit -m "发布 Quartz wiki 站点"
```

8. Push the current branch:

```bash
git push origin <branch>
```

9. Confirm publishing. Prefer `gh` if available:

```bash
gh run list --workflow deploy.yml --limit 3
gh run view <run-id> --log-failed
```

If `gh` is unavailable, give the user the Actions URL and exact expected site URL:

```text
https://github.com/chping/llmwiki/actions
https://chping.github.io/llmwiki/
```

## GitHub Pages Checks

If deployment fails with `Failed to create deployment (status: 404)` or `Ensure GitHub Pages has been enabled`, tell the user to set:

```text
Repository Settings -> Pages -> Build and deployment -> Source -> GitHub Actions
```

Then rerun the failed workflow or push again.

## Completion

Finish only after reporting:

- commit hash, if a commit was created
- pushed branch
- build result
- deployment result, or the exact GitHub Actions URL to check
- site URL: `https://chping.github.io/llmwiki/`
