"""wadv-1125: worst-advice one-liner shipper with comprehension-based gate."""

import json
import os

CEILING = 140
ADVICE = "entry.txt"


def read_advice(folder):
    pieces = [ln for ln in open(os.path.join(folder, ADVICE), encoding="utf-8").read().splitlines() if ln.strip()]
    return " ".join(pieces).strip()


def passes_gate(text):
    checks = [len(text) >= 1, len(text) <= CEILING, any(ch.isalpha() for ch in text)]
    return all(checks)


def emit_advice(folder, text):
    zone = os.environ.get("MAKEFUN_OUTPUT_DIR") or folder
    os.makedirs(zone, exist_ok=True)
    spot = os.path.join(zone, ADVICE)
    with open(spot, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text + "\n")
    return spot


folder = os.path.dirname(os.path.abspath(__file__))
advice = read_advice(folder)
if not passes_gate(advice):
    raise SystemExit("gate says no: %d chars" % len(advice))
print(json.dumps({"advice_ok": True, "n": len(advice), "quality": "confidently wrong", "placed": emit_advice(folder, advice)}))
