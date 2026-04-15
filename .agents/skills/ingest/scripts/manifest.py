from __future__ import annotations

import json
import shutil
from pathlib import Path

from models import ManifestEntry, WorkflowPaths
from utils import utc_timestamp


def load_manifest(paths: WorkflowPaths) -> list[ManifestEntry]:
    if not paths.manifest_path.exists():
        raise FileNotFoundError(f"Manifest not found: {paths.manifest_path}")

    data = json.loads(paths.manifest_path.read_text(encoding="utf-8"))
    if data.get("version") != 2:
        raise ValueError(f"Unsupported manifest version: {data.get('version')!r}")

    raw_entries = data.get("files")
    if not isinstance(raw_entries, list):
        raise ValueError("Manifest field 'files' must be a list")

    dedup: dict[str, dict[str, object]] = {}
    for item in raw_entries:
        if not isinstance(item, dict):
            raise ValueError("Manifest file entries must be objects")

        inbox_path = item.get("inbox_path")
        wiki_pages = item.get("wiki_pages")
        source_size = item.get("source_size")
        source_mtime_ns = item.get("source_mtime_ns")

        if not isinstance(inbox_path, str):
            raise ValueError("Each manifest entry must have a string inbox_path")
        if not isinstance(wiki_pages, list) or not all(isinstance(x, str) for x in wiki_pages):
            raise ValueError("Each manifest entry must have a list[str] wiki_pages")
        if not isinstance(source_size, int):
            raise ValueError("Each manifest entry must have an integer source_size")
        if not isinstance(source_mtime_ns, int):
            raise ValueError("Each manifest entry must have an integer source_mtime_ns")

        current = dedup.setdefault(
            inbox_path,
            {
                "wiki_pages": set(),
                "source_size": source_size,
                "source_mtime_ns": source_mtime_ns,
            },
        )
        if current["source_size"] != source_size or current["source_mtime_ns"] != source_mtime_ns:
            raise ValueError(f"Duplicate manifest entries disagree on fingerprint: {inbox_path}")
        current["wiki_pages"].update(wiki_pages)

    entries: list[ManifestEntry] = []
    for inbox_path_str in sorted(dedup.keys()):
        payload = dedup[inbox_path_str]
        pages = tuple(sorted((paths.repo / p).resolve() for p in payload["wiki_pages"]))
        entries.append(
            ManifestEntry(
                inbox_path=(paths.repo / inbox_path_str).resolve(),
                wiki_pages=pages,
                source_size=int(payload["source_size"]),
                source_mtime_ns=int(payload["source_mtime_ns"]),
            )
        )
    return entries


def validate_manifest_structure(paths: WorkflowPaths) -> int:
    entries = load_manifest(paths)
    return len(entries)


def archive_manifest_history(paths: WorkflowPaths, *, dry_run: bool = False) -> Path:
    if not paths.manifest_path.exists():
        raise FileNotFoundError(f"Manifest not found: {paths.manifest_path}")
    stamp = utc_timestamp().replace(":", "").replace("-", "")
    history_path = paths.history_dir / f"processed-manifest.{stamp}.json"
    if not dry_run:
        shutil.copy2(paths.manifest_path, history_path)
    return history_path
