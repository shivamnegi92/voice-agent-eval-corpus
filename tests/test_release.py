"""Release integrity regression checks; temporary mutations never touch sources."""
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("verify_release", ROOT / "scripts/verify_release.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class ReleaseTests(unittest.TestCase):
    def test_release_manifest_matches(self):
        module.verify(ROOT)

    def test_isca_identifier_requires_matching_canonical_url(self):
        row = {"identifier": "isca:interspeech_2021/chen21n_interspeech",
               "url": "https://www.isca-archive.org/interspeech_2021/chen21n_interspeech.html"}
        module.validate_identifiers([row])
        with self.assertRaisesRegex(ValueError, "canonical URL"):
            module.validate_identifiers([{**row, "url": "https://example.com/paper"}])
        with self.assertRaisesRegex(ValueError, "Malformed ISCA"):
            module.validate_identifiers([{**row, "identifier": "isca:../../secret"}])
        with self.assertRaisesRegex(ValueError, "Unknown source"):
            module.validate_identifiers([{**row, "identifier": "unknown:paper"}])

    def test_changed_metadata_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copy2(ROOT / "release_manifest.json", root / "release_manifest.json")
            manifest = json.loads((root / "release_manifest.json").read_text())
            for name in manifest["sha256"]:
                target = root / name
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(ROOT / name, target)
            first = root / next(iter(manifest["sha256"]))
            first.write_bytes(first.read_bytes() + b"\nchanged\n")
            with self.assertRaisesRegex(ValueError, "checksum mismatch"):
                module.verify(root)


if __name__ == "__main__":
    unittest.main()
