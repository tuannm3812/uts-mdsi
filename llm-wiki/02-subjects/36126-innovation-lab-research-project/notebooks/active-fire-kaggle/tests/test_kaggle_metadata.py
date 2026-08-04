import json
from pathlib import Path
import pytest

import sys
KAG_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(KAG_DIR))
KERNEL_METADATA = KAG_DIR / "kaggle" / "kernel-metadata.json"
DATASET_METADATA = KAG_DIR / "kaggle" / "dataset-metadata.json"
LICENCE_MANIFEST = KAG_DIR / "licence-manifest.json"


def test_kernel_is_private_cpu_and_snapshot_first():
    assert KERNEL_METADATA.is_file(), "kernel-metadata.json is missing"
    metadata = json.loads(KERNEL_METADATA.read_text())
    assert metadata["enable_gpu"] is False
    assert metadata["enable_internet"] is False
    assert metadata["is_private"] is True


def test_dataset_is_private_and_has_no_collaborators():
    assert DATASET_METADATA.is_file(), "dataset-metadata.json is missing"
    metadata = json.loads(DATASET_METADATA.read_text())
    assert metadata["isPrivate"] is True
    assert metadata.get("collaborators", []) == []


def test_dataset_licence_matches_confirmed_manifest():
    assert DATASET_METADATA.is_file(), "dataset-metadata.json is missing"
    assert LICENCE_MANIFEST.is_file(), "licence-manifest.json is missing"
    dataset = json.loads(DATASET_METADATA.read_text())
    manifest = json.loads(LICENCE_MANIFEST.read_text())
    confirmed = {source["kaggle_license_name"] for source in manifest["sources"]}
    
    # In Kaggle dataset metadata, the field is 'licenses' which is a list of dicts, e.g. [{"name": "cc-by-4.0"}]
    # Let's check that the metadata has a valid license matching the confirmed sources.
    assert "licenses" in dataset, "licenses field is missing from dataset metadata"
    assert len(dataset["licenses"]) > 0, "licenses list is empty"
    # Convert Kaggle licence name to lowercase for comparison if needed
    assert dataset["licenses"][0]["name"] in confirmed


from unittest.mock import patch, MagicMock

def test_upload_private_mocked(tmp_path):
    creds_file = tmp_path / "fake_kaggle.json"
    fake_key = "super_secret_kaggle_api_key_12345"
    creds_file.write_text(json.dumps({"username": "testuser", "key": fake_key}))
    
    staging_dir = tmp_path / "staging"
    staging_dir.mkdir()
    
    # We mock validate_private_metadata, shutil.copy2, and subprocess.run to run purely in isolation
    with patch("upload_private.validate_private_metadata") as mock_validate, \
         patch("shutil.copy2") as mock_copy, \
         patch("subprocess.run") as mock_run:
         
        mock_run.return_value = MagicMock(returncode=0, stdout="success status", stderr="")
        
        from upload_private import upload_private
        
        results = upload_private(creds_file, staging_dir)
        
        # Verify credentials validation and username extraction
        assert results["username"] == "testuser"
        assert results["dataset_status"] == "success"
        
        # Verify key was not stored in results
        assert fake_key not in str(results)
        
        # Verify that subprocess was called with temporary kaggle.json path in env
        called_args = [call[0][0] for call in mock_run.call_args_list]
        called_kwargs = [call[1] for call in mock_run.call_args_list]
        
        # Check that child commands were called
        assert any("kaggle" in arg for arg in called_args[0])
        
        # Check that env KAGGLE_CONFIG_DIR was set to a temporary path
        env_dirs = [kw.get("env", {}).get("KAGGLE_CONFIG_DIR") for kw in called_kwargs]
        assert all(d is not None for d in env_dirs)
        
        # Check that the temporary path no longer exists (clean up verified)
        for d in env_dirs:
            assert not Path(d).exists(), "Temporary credentials directory was not cleaned up!"

