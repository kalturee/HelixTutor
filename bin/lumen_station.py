"""CLI helper that records a station prompt into LumenTide notes."""

from argparse import ArgumentParser
from datetime import datetime
from pathlib import Path
import sys

root = Path(__file__).resolve().parents[1]
if str(root / "tools") not in sys.path:
    sys.path.insert(0, str(root))

from tools import mixchain

LOG_FILE = root / "notes" / "live-log.md"


def build_entry(note: str) -> str:
    prompt = mixchain.sample_station()
    timestamp = datetime.utcnow().replace(microsecond=0)
    parts = [
        f"## {timestamp.isoformat()}Z",
        f"- Prompt: {prompt}",
    ]
    if note:
        parts.append(f"- Note: {note}")
    parts.append("- Status: queued for recap")
    return "\n".join(parts) + "\n\n"


def ensure_log_exists() -> None:
    if not LOG_FILE.exists():
        LOG_FILE.write_text("# Live Log\n\n")


def main() -> None:
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("-n", "--note", help="Add a quick thought about the current prompt", default="")
    args = parser.parse_args()

    current = LOG_FILE.read_text() if LOG_FILE.exists() else ""
    ensure_log_exists()
    entry = build_entry(args.note)
    LOG_FILE.write_text(current + entry)
    print("Recorded:")
    print(entry.strip())


if __name__ == "__main__":
    main()
