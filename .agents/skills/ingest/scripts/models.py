from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class ManifestEntry:
    inbox_path: Path
    wiki_pages: tuple[Path, ...]
    source_size: int
    source_mtime_ns: int


@dataclass(frozen=True)
class WorkflowPaths:
    repo: Path
    skill_dir: Path
    prompt_template: Path
    codex_run_template_file: Path
    raw_dir: Path
    inbox_dir: Path
    wiki_dir: Path
    index_md: Path
    log_md: Path
    meta_dir: Path
    manifest_path: Path
    report_path: Path
    history_dir: Path
    archive_dir: Path
