"""Helpers that parse the CLI live log for quick insights."""

from dataclasses import dataclass
from pathlib import Path

LOG_FILE = Path(__file__).resolve().parents[1] / "notes" / "live-log.md"

@dataclass
class LogSummary:
    entry_count: int
    last_entry: str
    total_lines: int


def inspect_log() -> LogSummary:
    text = LOG_FILE.read_text()
    lines = text.strip().splitlines()
    headings = [line for line in lines if line.startswith("##")]
    entry_count = len(headings)
    last_entry = headings[-1] if headings else "(none)"
    return LogSummary(entry_count, last_entry, len(lines))


def format_summary(summary: LogSummary) -> str:
    return (
        f"Entries: {summary.entry_count}\n"
        f"Last heading: {summary.last_entry}\n"
        f"Total lines: {summary.total_lines}\n"
    )


if __name__ == "__main__":
    summary = inspect_log()
    print(format_summary(summary))
