"""Reject accidental replacement of synthetic test data with production recipes."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def assert_synthetic(root=ROOT):
    m = json.loads((root / "bambu-gitops.json").read_text())
    assert "SYNTHETIC" in m["instance"]["display_name"], "Missing synthetic warning"
    assert "FICTIONAL" in m["hardware"]["hotend"], "Hardware must be fictional"
    for kind in ("printer", "process", "filament"):
        for path in (root / "profiles" / kind).glob("*.json"):
            p = json.loads(path.read_text())
            assert "DO NOT PRINT" in p["display_name"], f"Missing warning in {path}"
            assert p["reviewed"] is False, f"Example may never be marked reviewed: {path}"
            assert "schema_demo_only" in p["settings"], f"Do not publish a real preset: {path}"
            assert not any("gcode" in key.lower() for key in p["settings"]), "No real G-code here"
    for item in m.get("calibrations", []):
        assert "FICTIONAL" in item.get("notes", ""), "Calibration must be marked fictitious"

if __name__ == "__main__":
    assert_synthetic()
    print("Confirmed: synthetic-only. Never print these values.")
