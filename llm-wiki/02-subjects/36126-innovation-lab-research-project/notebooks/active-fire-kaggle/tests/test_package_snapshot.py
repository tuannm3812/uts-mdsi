from pathlib import Path
import sys
import pytest
import json
import hashlib
import shutil

KAG_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(KAG_DIR))

from package_snapshot import validate_manifest, package_snapshot


def test_unconfirmed_source_cannot_be_packaged():
    manifest = {
        "sources": [{
            "source_id": "nsw-rfs-fire-history",
            "licence_status": "unconfirmed",
            "allowed_files": ["nsw_fire_history.geojson"],
        }]
    }
    with pytest.raises(ValueError, match="unconfirmed"):
        validate_manifest(manifest)


def test_confirmed_source_requires_attribution():
    manifest = {
        "sources": [{
            "source_id": "npws-fire-history",
            "licence_status": "confirmed",
            "licence_name": "Creative Commons Attribution",
            "kaggle_license_name": "CC-BY-4.0",
            "reviewed_sha256": {"npws_fire_history.geojson": "dummy"},
            "attribution": "",
            "allowed_files": ["npws_fire_history.geojson"],
        }]
    }
    with pytest.raises(ValueError, match="attribution"):
        validate_manifest(manifest)


def test_packager_writes_checksums_for_every_file(tmp_path):
    source_dir = tmp_path / "sources"
    source_dir.mkdir()
    
    file1 = source_dir / "dea_hotspots.geojson"
    file1.write_text("content1", encoding="utf-8")
    hash1 = hashlib.sha256(b"content1").hexdigest()
    
    file2 = source_dir / "fire_history.geojson"
    file2.write_text("content2", encoding="utf-8")
    hash2 = hashlib.sha256(b"content2").hexdigest()
    
    file3 = source_dir / "source-config.json"
    file3.write_text("content3", encoding="utf-8")
    hash3 = hashlib.sha256(b"content3").hexdigest()
    
    manifest = {
        "sources": [
            {
                "source_id": "dea-hotspots",
                "licence_status": "confirmed",
                "licence_name": "CC BY 4.0",
                "kaggle_license_name": "CC-BY-4.0",
                "attribution": "Geoscience Australia",
                "reviewed_sha256": {
                    "dea_hotspots.geojson": hash1,
                    "source-config.json": hash3,
                },
                "allowed_files": ["dea_hotspots.geojson", "source-config.json"]
            },
            {
                "source_id": "npws-fire-history",
                "licence_status": "confirmed",
                "licence_name": "Creative Commons Attribution",
                "kaggle_license_name": "CC-BY-4.0",
                "attribution": "NPWS NSW",
                "reviewed_sha256": {
                    "fire_history.geojson": hash2
                },
                "allowed_files": ["fire_history.geojson"]
            }
        ]
    }
    
    manifest_path = tmp_path / "licence-manifest.json"
    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
    
    output_dir = tmp_path / "package"
    packaged = package_snapshot(manifest_path, source_dir, output_dir)
    
    assert len(packaged) == 3
    snapshot_manifest = json.loads((output_dir / "snapshot-manifest.json").read_text(encoding="utf-8"))
    assert set(snapshot_manifest["sha256"].keys()) == {
        "dea_hotspots.geojson",
        "fire_history.geojson",
        "source-config.json",
    }
    assert snapshot_manifest["sha256"]["dea_hotspots.geojson"] == hash1
    assert snapshot_manifest["sha256"]["fire_history.geojson"] == hash2
    assert snapshot_manifest["sha256"]["source-config.json"] == hash3


def test_packager_rejects_file_that_differs_from_reviewed_provenance(tmp_path):
    source_dir = tmp_path / "sources"
    source_dir.mkdir()
    
    file1 = source_dir / "dea_hotspots.geojson"
    file1.write_text("content1", encoding="utf-8")
    hash1 = hashlib.sha256(b"content1").hexdigest()
    
    manifest = {
        "sources": [
            {
                "source_id": "dea-hotspots",
                "licence_status": "confirmed",
                "licence_name": "CC BY 4.0",
                "kaggle_license_name": "CC-BY-4.0",
                "attribution": "Geoscience Australia",
                "reviewed_sha256": {
                    "dea_hotspots.geojson": hash1
                },
                "allowed_files": ["dea_hotspots.geojson"]
            }
        ]
    }
    
    manifest_path = tmp_path / "licence-manifest.json"
    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
    
    # Modify the file contents to differ from the expected hash
    file1.write_text("content1-modified", encoding="utf-8")
    
    output_dir = tmp_path / "package"
    with pytest.raises(ValueError, match="differs from reviewed provenance"):
        package_snapshot(manifest_path, source_dir, output_dir)
