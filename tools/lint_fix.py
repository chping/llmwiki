from __future__ import annotations

import shutil
import subprocess
import sys


def run(cmd: list[str]) -> int:
    print("+ " + " ".join(cmd))
    proc = subprocess.run(cmd)
    return proc.returncode


def main() -> None:
    if shutil.which("npx") is None:
        print("npx is not available. Install Node.js/npm before running markdownlint.", file=sys.stderr)
        raise SystemExit(127)

    fix_rc = run(["npx", "markdownlint", "wiki/", "--fix"])
    check_rc = run(["npx", "markdownlint", "wiki/"])

    if fix_rc != 0 or check_rc != 0:
        raise SystemExit(check_rc or fix_rc)

    print("markdownlint passed.")


if __name__ == "__main__":
    main()
