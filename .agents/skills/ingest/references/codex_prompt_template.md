You are operating inside a Markdown wiki repository.

Your job is to process files in `raw/inbox/` and update the wiki.

You must do all content analysis and wiki writing. You must not move or delete raw files.

Repository rules:
- Analyze all files under `raw/inbox/`.
- Summarize important ideas, facts, decisions, and references.
- Create new topic pages under `wiki/` or merge into existing pages when appropriate.
- Update `wiki/index.md` so new pages are discoverable.
- Update `wiki/log.md` with a concise note for today.
- Every wiki page derived from an inbox file must contain a `## Sources` section.
- In `## Sources`, add Markdown links pointing to the source file in `raw/inbox/`.
- Use relative links from the wiki page location.
- Avoid duplicate source links.
- Avoid duplicate log entries.

Critical output requirement:
After all wiki writing is complete, write this manifest file:

- `.wiki-inbox/processed-manifest.json`

Manifest schema:

```json
{
  "version": 2,
  "generated_by": "codex",
  "processed_at": "<UTC ISO8601 timestamp>",
  "files": [
    {
      "inbox_path": "raw/inbox/example-note.md",
      "wiki_pages": [
        "wiki/example-note.md"
      ],
      "source_size": 12345,
      "source_mtime_ns": 1713184496000000000
    }
  ]
}
```

Manifest rules:
- `inbox_path` and `wiki_pages` must be repository-relative paths.
- `source_size` must match the inbox file size in bytes at the time you processed it.
- `source_mtime_ns` must match the inbox file modification time in nanoseconds at the time you processed it.
- Only include files that you actually processed in this run.
- Only include files that are now referenced by wiki pages.
- Deduplicate file entries.
- Deduplicate page paths within each entry.
- Do not archive anything yourself.
- Do not rewrite backlinks to archive paths.

Backlink example:

```md
## Sources

- [Original source](../raw/inbox/example-note.md)
```

Repository root:
{repo}
