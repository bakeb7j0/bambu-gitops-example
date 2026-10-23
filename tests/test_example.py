"""Independent public-consumer tests; no printer connections or external services."""
from __future__ import annotations
import json
from pathlib import Path
import shutil
import tempfile
import unittest

from bambu_gitops.conformance import report

SOURCE = Path(__file__).resolve().parents[1]

class ReferenceTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        shutil.copy2(SOURCE / "bambu-gitops.json", self.root)
        shutil.copytree(SOURCE / "profiles", self.root / "profiles")

    def patch(self, path, fn):
        p = self.root / path
        x = json.loads(p.read_text())
        fn(x)
        p.write_text(json.dumps(x))

    def findings(self):
        return report(self.root)["findings"]

    def test_reference_passes_schema(self):
        self.assertEqual(self.findings(), [])

    def test_missing_profile_is_rejected(self):
        self.patch("bambu-gitops.json", lambda x: x["profiles"]["process"].append("missing-process"))
        self.assertIn("PROFILE_NOT_FOUND", [f["code"] for f in self.findings()])

    def test_inheritance_cycle_is_rejected(self):
        self.patch("profiles/filament/pla-basic.json", lambda x: x.update(inherits="pla-basic"))
        self.assertIn("INHERITANCE_CYCLE", [f["code"] for f in self.findings()])

    def test_wrong_nozzle_is_rejected(self):
        self.patch("profiles/printer/example-printer.json", lambda x: x.update(nozzle_diameter_mm=0.8))
        self.assertIn("NOZZLE_INCOMPATIBLE", [f["code"] for f in self.findings()])

    def test_machine_gcode_flags_safety_review(self):
        self.patch("profiles/printer/example-printer.json", lambda x: x["settings"].update(machine_start_gcode="SYNTHETIC-ONLY"))
        self.assertIn("SAFETY_REVIEW_REQUIRED", [f["code"] for f in self.findings()])

if __name__ == "__main__":
    unittest.main()
