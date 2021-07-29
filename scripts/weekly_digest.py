#!/usr/bin/env python3
"""Produce a small weekly digest from the curated signal corpus."""

import json
from datetime import datetime
from pathlib import Path

SAMPLE_FILE = Path(__file__).resolve().parents[1] / "samples" / "signal-corpus.json"
OUTPUT = Path(__file__).resolve().parents[1] / "notes" / "weekly-digest.md"


def summarize(signals):
    total = sum(item["value"] for item in signals)
    avg = total / len(signals) if signals else 0
    latest = max(signals, key=lambda item: item["recorded_at"], default=None)
    lines = ["# Weekly Digest\n", f"* Source: {SAMPLE_FILE.name}\n"]
    if latest:
        lines.append(f"* Latest signal: {latest['signal_type']} at {latest['recorded_at']}\n")
    lines.append(f"* Average magnitude: {avg:.2f}\n")
    for signal in signals:
        lines.append(f"  - {signal['recorded_at']}: {signal['signal_type']} ({signal['moment']})\n")
    lines.append("\n")
    return "".join(lines)


def main():
    if not SAMPLE_FILE.exists():
        raise SystemExit("Missing sample corpus")
    signals = json.loads(SAMPLE_FILE.read_text())
    digest = summarize(signals)
    OUTPUT.write_text(digest)
    print("Digest saved to", OUTPUT)


if __name__ == "__main__":
    main()
