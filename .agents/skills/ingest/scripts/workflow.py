from __future__ import annotations

from pathlib import Path

from archive import archive_and_relink
from codex_integration import load_codex_run_template, render_prompt, run_codex_command
from manifest import archive_manifest_history, load_manifest, validate_manifest_structure
from paths import build_paths, ensure_layout


def run_workflow(
    *,
    repo: Path,
    skill_dir: Path,
    codex_cmd: str,
    codex_run_template: str | None = None,
    today: str | None = None,
    dry_run: bool = False,
    skip_codex: bool = False,
    archive_only: bool = False,
    timeout: int | None = None,
) -> list[dict[str, object]]:
    if skip_codex and not archive_only:
        archive_only = True

    paths = build_paths(repo=repo, skill_dir=skill_dir, today=today)
    ensure_layout(paths)

    prompt_file: Path | None = None
    try:
        if not archive_only:
            run_template = codex_run_template or load_codex_run_template(paths.codex_run_template_file)
            prompt_file = render_prompt(paths.prompt_template, repo, paths.inbox_rel)
            run_codex_command(
                run_template=run_template,
                codex_cmd=codex_cmd,
                repo=repo,
                prompt_file=prompt_file,
                timeout=timeout,
            )

        validate_manifest_structure(paths)
        archive_manifest_history(paths, dry_run=dry_run)
        entries = load_manifest(paths)
        results = archive_and_relink(paths, entries, dry_run=dry_run)
        return results
    finally:
        if prompt_file is not None and prompt_file.exists():
            prompt_file.unlink()
