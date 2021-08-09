#!/usr/bin/env python3
"""Capture a reflection note from the live log summary."""

from datetime import datetime
from pathlib import Path
import os
import sys

root = Path(__file__).resolve().parents[1]
if str(root) not in sys.path:
    sys.path.insert(0, str(root))

from tools.log_inspector import format_summary, inspect_log

REFLECTION_PATH = Path(__file__).resolve().parents[1] / "notes" / "reflection.md"


def build_entry(summary_text: str) -> str:
    custom_time = os.environ.get("LUMEN_REFLECT_TIME")
    if custom_time:
        now = custom_time
    else:
        now = datetime.utcnow().replace(microsecond=0).isoformat() + "Z"
    lines = [f"## Reflection {now}", "", summary_text.strip(), "", "- Next: listen for the next signal bubble", ""]
    return "\n".join(lines)


def main() -> None:
    summary = inspect_log()
    content = format_summary(summary)
    entry = build_entry(content)
    existing = REFLECTION_PATH.read_text() if REFLECTION_PATH.exists() else "# Reflections\n\n"
    REFLECTION_PATH.write_text(existing + entry)
    print("Reflection appended")


if __name__ == "__main__":
    main()
