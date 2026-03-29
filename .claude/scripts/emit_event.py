#!/usr/bin/env python3
"""Append a single JSONL event to .claude/logs/YYYY-MM-DD.jsonl.

Usage:
    echo '{"event":"hook.block","detail":"uv add requests"}' | python3 .claude/scripts/emit_event.py

Reads a JSON object from stdin, adds a UTC timestamp, and appends one line
to the daily log file. Zero external dependencies (stdlib only).
"""

import json
import sys
from datetime import UTC, datetime
from pathlib import Path

LOGS_DIR = Path(__file__).resolve().parent.parent / "logs"


def main() -> None:
    try:
        raw = sys.stdin.read().strip()
        if not raw:
            return
        record = json.loads(raw)
    except (json.JSONDecodeError, OSError):
        return

    record["ts"] = datetime.now(UTC).isoformat()

    log_file = LOGS_DIR / f"{datetime.now(UTC).strftime('%Y-%m-%d')}.jsonl"
    log_file.parent.mkdir(parents=True, exist_ok=True)

    with open(log_file, "a") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
