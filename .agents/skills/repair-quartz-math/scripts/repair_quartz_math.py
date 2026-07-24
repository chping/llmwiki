#!/usr/bin/env python3

import argparse
import re
import sys
from pathlib import Path


PROTECTED_START = "<!-- user-notes:start -->"
PROTECTED_END = "<!-- user-notes:end -->"
FENCE_RE = re.compile(r"^\s*(`{3,}|~{3,})")
INLINE_CODE_RE = re.compile(r"(`+)(.*?)\1")
DISPLAY_OPEN_RE = re.compile(r"^(\s*)\\\[\s*$")
DISPLAY_CLOSE_RE = re.compile(r"^(\s*)\\\]\s*$")
INLINE_MATH_RE = re.compile(r"(?<!\\)\\\((.+?)(?<!\\)\\\)")


def mask_inline_code(line):
    spans = []

    def replace(match):
        spans.append(match.group(0))
        return f"\0{len(spans) - 1}\0"

    return INLINE_CODE_RE.sub(replace, line), spans


def restore_inline_code(line, spans):
    for index, value in enumerate(spans):
        line = line.replace(f"\0{index}\0", value)
    return line


def process_file(path, fix):
    original = path.read_text(encoding="utf-8")
    lines = original.splitlines(keepends=True)
    output = []
    findings = []
    in_frontmatter = bool(lines and lines[0].rstrip("\r\n") == "---")
    in_fence = False
    fence_char = ""
    fence_length = 0
    in_protected = False

    for number, line in enumerate(lines, 1):
        plain = line.rstrip("\r\n")

        if number > 1 and in_frontmatter:
            output.append(line)
            if plain == "---":
                in_frontmatter = False
            continue

        if PROTECTED_START in line:
            in_protected = True
        if in_protected:
            output.append(line)
            if PROTECTED_END in line:
                in_protected = False
            continue

        fence = FENCE_RE.match(line)
        if fence:
            marker = fence.group(1)
            if not in_fence:
                in_fence = True
                fence_char = marker[0]
                fence_length = len(marker)
            elif marker[0] == fence_char and len(marker) >= fence_length:
                in_fence = False
            output.append(line)
            continue

        if in_fence:
            output.append(line)
            continue

        display_open = DISPLAY_OPEN_RE.match(plain)
        display_close = DISPLAY_CLOSE_RE.match(plain)
        if display_open or display_close:
            findings.append((number, plain))
            if fix:
                indent = (display_open or display_close).group(1)
                ending = line[len(plain):]
                line = f"{indent}$${ending}"

        masked, spans = mask_inline_code(line)
        matches = list(INLINE_MATH_RE.finditer(masked))
        if matches:
            findings.extend((number, restore_inline_code(match.group(0), spans)) for match in matches)
            if fix:
                masked = INLINE_MATH_RE.sub(lambda match: f"${match.group(1)}$", masked)
                line = restore_inline_code(masked, spans)

        output.append(line)

    updated = "".join(output)
    if fix and updated != original:
        path.write_text(updated, encoding="utf-8")
    return findings, updated != original


def main():
    parser = argparse.ArgumentParser(description="Scan or repair Quartz-incompatible math delimiters.")
    parser.add_argument("root", nargs="?", default="wiki", help="Markdown file or directory to scan")
    parser.add_argument("--fix", action="store_true", help="convert safe delimiters in place")
    args = parser.parse_args()

    root = Path(args.root)
    if not root.exists():
        parser.error(f"path does not exist: {root}")
    paths = [root] if root.is_file() else sorted(root.rglob("*.md"))
    total = 0
    changed = 0

    for path in paths:
        findings, was_changed = process_file(path, args.fix)
        if findings:
            for line, text in findings:
                print(f"{path}:{line}: {text}")
            total += len(findings)
        changed += int(was_changed)

    action = "fixed" if args.fix else "found"
    print(f"{action} {total} unsupported delimiter(s) in {changed if args.fix else len(paths)} {'changed file(s)' if args.fix else 'scanned file(s)'}")
    return 0 if args.fix or total == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
