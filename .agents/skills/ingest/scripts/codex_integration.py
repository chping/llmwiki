from __future__ import annotations

import subprocess
from pathlib import Path


def render_prompt(prompt_template: Path, repo: Path) -> Path:
    import tempfile

    text = prompt_template.read_text(encoding="utf-8")
    text = text.replace("{repo}", str(repo.resolve()))

    with tempfile.NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        prefix="codex-wiki-prompt.",
        suffix=".md",
        delete=False,
    ) as f:
        f.write(text)
        return Path(f.name)


def load_codex_run_template(template_file: Path) -> str:
    if not template_file.exists():
        raise FileNotFoundError(f"Codex run template file not found: {template_file}")
    template = template_file.read_text(encoding="utf-8").strip()
    if not template:
        raise ValueError(f"Codex run template file is empty: {template_file}")
    return template


def run_codex_command(
    *,
    run_template: str,
    codex_cmd: str,
    repo: Path,
    prompt_file: Path,
    timeout: int | None = None,
) -> None:
    cmd = run_template.format(
        codex_cmd=codex_cmd,
        repo=str(repo.resolve()),
        prompt_file=str(prompt_file.resolve()),
    )

    prompt_text = prompt_file.read_text(encoding="utf-8")

    print(f"Running Codex command: {cmd}")
    subprocess.run(
        cmd,
        input=prompt_text,
        text=True,
        shell=True,
        check=True,
        timeout=timeout,
    )