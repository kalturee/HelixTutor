"""Assistive sampler for LumenTide station prompts."""

import random
from datetime import datetime

SIGNAL_BANK = [
    "midnight trade whisper",
    "quiet sensor drift",
    "bot rumor pulse",
    "experimental mint log",
    "lunar commute beacon",
]

MOMENTS = [
    "Clouded, but steady",
    "Sunrise fuzz",
    "Still air with static",
    "Hyperfocus bubble",
    "Slow burn, no panic",
]

def sample_station() -> str:
    """Return a short prompt describing the current station mood."""
    signal = random.choice(SIGNAL_BANK)
    moment = random.choice(MOMENTS)
    timestamp = datetime.utcnow().replace(microsecond=0).isoformat() + "Z"
    return f"[{timestamp}] {moment} — {signal}"

if __name__ == "__main__":
    print("    ," * 10)
    print("LumenTide mixchain prompt")
    for _ in range(3):
        print("-", sample_station())
