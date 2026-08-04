from pathlib import Path
import sys
import pytest
import json

KAG_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(KAG_DIR))

from audit_public_artifact import run_hash_audit, scan_language, scan_absolute_paths


def test_audit_identifies_unreviewed_hashes():
    # Mock a manifest with an unreviewed hash
    manifest = {
        "sources": [
            {
                "source_id": "dea-hotspots",
                "reviewed_sha256": {
                    "dea_hotspots.geojson": "invalid_hash_value"
                }
            }
        ]
    }
    # Path to dummy files or passing actual dir
    # It should fail because the expected hash doesn't match the actual file or is not in the reviewed manifest
    # We pass KAG_DIR which contains no such file with that hash
    results = run_hash_audit(manifest, Path("/nonexistent"))
    assert not results["passed"]
    assert "missing" in results["errors"][0] or "mismatch" in results["errors"][0]


def test_audit_flags_non_public_language():
    text = "The results show that MODIS had several false alarms and false positives."
    issues = scan_language(text)
    assert any("false alarm" in issue.lower() for issue in issues)
    assert any("false positive" in issue.lower() for issue in issues)


def test_audit_detects_absolute_paths():
    code_text = "df = pd.read_csv('/Users/tuannm3812/Documents/GitHub/1. Study/uts-mdsi/data.csv')"
    paths = scan_absolute_paths(code_text)
    assert len(paths) == 1
    assert "Users" in paths[0]
