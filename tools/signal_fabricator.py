"""Lightweight signal generator for LumenTide prototypes."""

from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from random import choice, uniform
from typing import Iterable, List, Optional

SIGNAL_TYPES = [
    "price-jump",
    "bot-nudge",
    "sensor-drift",
    "mint-gambit",
    "commute-chime",
]

MOMENT_TAGS = [
    "calm",
    "static",
    "electric",
    "luminous",
    "flicker",
]

@dataclass
class SignalPatch:
    signal_type: str
    value: float
    note: str
    moment: str
    recorded_at: str


def fabricate_signal(signal_type: Optional[str] = None, shift: float = 0.0) -> SignalPatch:
    """Return a synthetic signal patch for experimentation."""
    kind = signal_type or choice(SIGNAL_TYPES)
    magnitude = round(uniform(0.5, 3.3) + shift, 3)
    moment = choice(MOMENT_TAGS)
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    note = f"{kind} w/ {moment} drift"
    return SignalPatch(kind, magnitude, note, moment, now)


def batch_pack(count: int = 5) -> List[SignalPatch]:
    """Create a list of signal patches for quick visualization."""
    return [fabricate_signal(shift=i * 0.1) for i in range(count)]


def dump_examples() -> List[dict]:
    return [asdict(patch) for patch in batch_pack(4)]

if __name__ == "__main__":
    import json
    samples = dump_examples()
    print(json.dumps(samples, indent=2))
