Pure Python refactor of the Codex + archive workflow, corrected for direct script execution.

Files:
- `cli.py`
- `workflow.py`
- `paths.py`
- `models.py`
- `utils.py`
- `codex_integration.py`
- `manifest.py`
- `archive.py`
- `codex_prompt_template.md`
- `codex_run_template.txt`
- `SKILL.md`

Default use:

```bash
python3 skills/ingest/cli.py --repo .
```

Optional runtime override:

```bash
python3 skills/ingest/cli.py \
  --repo . \
  --codex-run-template '{codex_cmd} exec --cwd "{repo}" --instruction-file "{prompt_file}"'
```
