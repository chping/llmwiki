from __future__ import annotations

import subprocess


CHECKS = [
    ["python", "tools/link_check.py"],
    ["python", "tools/lint_fix.py"],
]


def main() -> None:
    for cmd in CHECKS:
        print("+ " + " ".join(cmd))
        proc = subprocess.run(cmd)
        if proc.returncode != 0:
            raise SystemExit(proc.returncode)
    print("All completion checks passed.")


if __name__ == "__main__":
    main()
