from __future__ import annotations

import argparse

from tools.kb_common import append_log


def main() -> None:
    parser = argparse.ArgumentParser(description="Append one operation log entry to wiki/log.md.")
    parser.add_argument("message")
    parser.add_argument("--date")
    args = parser.parse_args()

    append_log(args.message, date=args.date)
    print("log updated")


if __name__ == "__main__":
    main()
