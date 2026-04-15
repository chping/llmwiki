from __future__ import annotations

from datetime import datetime
from pathlib import Path

from models import WorkflowPaths
from utils import ensure_text_file


def build_paths(repo: Path, skill_dir: Path, today: str | None = None) -> WorkflowPaths:
    dt = datetime.strptime(today, "%Y-%m-%d") if today else datetime.now()
    raw_dir = repo / "raw"
    wiki_dir = repo / "wiki"
    meta_dir = repo / ".wiki-inbox"
    return WorkflowPaths(
        repo=repo,
        skill_dir=skill_dir,
        prompt_template=skill_dir / "codex_prompt_template.md",
        codex_run_template_file=skill_dir / "codex_run_template.txt",
        raw_dir=raw_dir,
        inbox_dir=raw_dir / "inbox",
        wiki_dir=wiki_dir,
        index_md=wiki_dir / "index.md",
        log_md=wiki_dir / "log.md",
        meta_dir=meta_dir,
        manifest_path=meta_dir / "processed-manifest.json",
        report_path=meta_dir / "last-archive-report.json",
        history_dir=meta_dir / "history",
        archive_dir=raw_dir / f"{dt:%Y}" / f"{dt:%m%d}",
    )


def ensure_layout(paths: WorkflowPaths) -> None:
    paths.inbox_dir.mkdir(parents=True, exist_ok=True)
    paths.wiki_dir.mkdir(parents=True, exist_ok=True)
    paths.meta_dir.mkdir(parents=True, exist_ok=True)
    paths.history_dir.mkdir(parents=True, exist_ok=True)
    paths.archive_dir.mkdir(parents=True, exist_ok=True)
    ensure_text_file(paths.index_md, "# Wiki Index\n")
    ensure_text_file(paths.log_md, "# Project Log\n")
