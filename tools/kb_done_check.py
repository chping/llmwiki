from __future__ import annotations

import subprocess


CHECKS = [
    ["python3", "-m", "tools.kb_link_check"],
    ["python3", "tools/kb_lint_fix.py"],
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
