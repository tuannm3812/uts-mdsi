import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
import argparse

KAG_DIR = Path(__file__).resolve().parent

# `kaggle datasets version` (used below for an existing dataset) does not
# reliably push isPrivate, expectedUpdateFrequency, or userSpecifiedSources
# from dataset-metadata.json -- confirmed via Kaggle/kaggle-api#339 and, for
# the latter two fields, by the fact the installed kaggle package's own
# `dataset_metadata_update()` silently drops them (reads title/subtitle/
# description/isPrivate/licenses/keywords/collaborators/data, nothing else).
# This uses the underlying SDK's update_dataset_metadata call directly to
# push the fields that path drops. Confirmed live against the real dataset,
# 2026-08-06 (T-040) -- prior to this, Version 16/17/18 pushes all silently
# failed to apply these despite dataset-metadata.json having correct values
# since Version 16.
#
# Kaggle's newer metadata-update endpoint validates against its own stored
# canonical strings, not the short slugs dataset-metadata.json uses for the
# older create/version endpoints -- e.g. it wants the full license display
# name ("Attribution 4.0 International (CC BY 4.0)"), not "CC-BY-4.0", and
# only accepts keywords that match its fixed tag taxonomy (of this dataset's
# 5 local keywords, only "earth science" and "australia" are valid tags).
# Hardcoded here rather than in dataset-metadata.json since the slug form
# is what the primary create/version path actually needs.
_LICENSE_DISPLAY_NAME = "Attribution 4.0 International (CC BY 4.0)"
_VALID_KEYWORDS = ["earth science", "australia"]


def push_dataset_metadata_extras(dataset_meta_path: Path, config_dir: str = "") -> dict:
    """Push expectedUpdateFrequency, userSpecifiedSources, and per-file
    descriptions to an existing Kaggle dataset via the SDK update endpoint,
    since `kaggle datasets version` doesn't reliably apply them. Best-effort:
    failures here shouldn't fail the whole upload, since the primary
    data/notebook content already succeeded by the time this runs."""
    import kaggle
    from kagglesdk.datasets.types.dataset_types import (
        DatasetSettings, DatasetSettingsFile, SettingsLicense,
    )
    from kagglesdk.datasets.types.dataset_api_service import (
        ApiUpdateDatasetMetadataRequest,
    )

    # kaggle.api is a process-wide singleton that reads credentials from the
    # real environment, not from the `env` dict passed to subprocess.run
    # elsewhere in this module -- mirror the temp-credentials setup here so
    # this honours the same --credentials override, then restore afterward.
    previous_config_dir = os.environ.get("KAGGLE_CONFIG_DIR")
    if config_dir:
        os.environ["KAGGLE_CONFIG_DIR"] = config_dir
    try:
        kaggle.api.authenticate()

        metadata = json.loads(dataset_meta_path.read_text())

        settings = DatasetSettings()
        settings.title = metadata["title"]
        settings.subtitle = metadata["subtitle"]
        settings.description = metadata["description"]
        settings.is_private = metadata.get("isPrivate", False)
        settings.keywords = _VALID_KEYWORDS

        license_obj = SettingsLicense()
        license_obj.name = _LICENSE_DISPLAY_NAME
        settings.licenses = [license_obj]

        settings.expected_update_frequency = metadata["expectedUpdateFrequency"]
        sources = metadata.get("userSpecifiedSources", [])
        settings.user_specified_sources = "; ".join(
            f"{s['name']} ({s['url']}): {s['description']}" for s in sources
        )

        data_files = []
        for resource in metadata.get("resources", []):
            f = DatasetSettingsFile()
            f.name = resource["path"]
            f.description = resource.get("description", "")
            data_files.append(f)
        settings.data = data_files

        owner_slug, dataset_slug = metadata["id"].split("/")
        request = ApiUpdateDatasetMetadataRequest()
        request.owner_slug = owner_slug
        request.dataset_slug = dataset_slug
        request.settings = settings

        with kaggle.api.build_kaggle_client() as client:
            response = client.datasets.dataset_api_client.update_dataset_metadata(
                request
            )
            if len(response.errors) > 0:
                return {"status": "failed", "errors": [str(e) for e in response.errors]}
            return {"status": "success"}
    finally:
        if previous_config_dir is None:
            os.environ.pop("KAGGLE_CONFIG_DIR", None)
        else:
            os.environ["KAGGLE_CONFIG_DIR"] = previous_config_dir


def validate_private_metadata(dataset_path: Path, kernel_path: Path) -> None:
    if not dataset_path.is_file():
        raise FileNotFoundError(f"Dataset metadata missing: {dataset_path}")
    if not kernel_path.is_file():
        raise FileNotFoundError(f"Kernel metadata missing: {kernel_path}")
        
    dataset = json.loads(dataset_path.read_text())
    kernel = json.loads(kernel_path.read_text())
    if not dataset.get("isPrivate"):
        print("[WARNING] Dataset is configured as PUBLIC (isPrivate: false)")
    if dataset.get("collaborators", []) != []:
        raise ValueError("Dataset has collaborators listed!")
        
    if not kernel.get("is_private"):
        print("[WARNING] Kernel is configured as PUBLIC (is_private: false)")
    if kernel.get("enable_gpu"):
        raise ValueError("Kernel has GPU enabled!")
    if kernel.get("enable_internet"):
        raise ValueError("Kernel has internet enabled!")


def upload_private(credentials_path: Path, staging_dir: Path) -> dict:
    dataset_meta = KAG_DIR / "kaggle" / "dataset-metadata.json"
    kernel_meta = KAG_DIR / "kaggle" / "kernel-metadata.json"
    
    validate_private_metadata(dataset_meta, kernel_meta)
    
    if not staging_dir.is_dir():
        raise NotADirectoryError(f"Staging directory missing: {staging_dir}")
        
    # Copy dataset-metadata.json into staging directory so Kaggle CLI can read it
    shutil.copy2(dataset_meta, staging_dir / "dataset-metadata.json")
    
    # Copy kernel-metadata.json into staging directory, along with the notebook itself
    shutil.copy2(kernel_meta, staging_dir / "kernel-metadata.json")
    
    # Copy the notebooks
    notebook_src2 = KAG_DIR / "2_active_fire_reliability_pilot.ipynb"
    if not notebook_src2.is_file():
        raise FileNotFoundError(f"Notebook missing: {notebook_src2}")
    shutil.copy2(notebook_src2, staging_dir / "2_active_fire_reliability_pilot.ipynb")
    
    notebook_src1 = KAG_DIR / "1_active_fire_eda.ipynb"
    if not notebook_src1.is_file():
        raise FileNotFoundError(f"Notebook missing: {notebook_src1}")
    shutil.copy2(notebook_src1, staging_dir / "1_active_fire_eda.ipynb")
    
    results = {}
    
    # Use temporary directory for credentials if provided
    with tempfile.TemporaryDirectory() as temp_dir:
        env = os.environ.copy()
        
        if credentials_path.is_file():
            # Validate credentials structure
            creds = json.loads(credentials_path.read_text())
            if not creds.get("username") or not creds.get("key"):
                raise ValueError("Credentials file must contain 'username' and 'key'")
            results["username"] = creds["username"]
            
            # Write to temporary kaggle.json
            temp_creds_file = Path(temp_dir) / "kaggle.json"
            temp_creds_file.write_text(json.dumps(creds))
            os.chmod(temp_creds_file, 0o600)
            
            # Set KAGGLE_CONFIG_DIR
            env["KAGGLE_CONFIG_DIR"] = temp_dir
            print(f"Temporary credentials set up for user: {creds['username']}")
        else:
            print("No --credentials path provided. Using default system/environment Kaggle configuration.")
            
        # 1. Dataset upload
        print("Staging dataset creation/version...")
        # Run kaggle datasets create/version
        # First, try to check if dataset exists or just create/version it
        # We can run `kaggle datasets status <dataset_slug>`
        dataset_id = json.loads(dataset_meta.read_text())["id"]
        
        # Check if the dataset already exists
        check_dataset = subprocess.run(
            ["kaggle", "datasets", "status", dataset_id],
            capture_output=True,
            text=True,
            env=env
        )
        
        if "NotFound" in check_dataset.stderr or check_dataset.returncode != 0:
            print("Dataset not found. Creating new dataset...")
            cmd = ["kaggle", "datasets", "create", "-p", str(staging_dir)]
        else:
            print("Dataset exists. Creating new version...")
            cmd = ["kaggle", "datasets", "version", "-p", str(staging_dir), "-m", "Version updated by automated pipeline"]
            
        dataset_run = subprocess.run(cmd, capture_output=True, text=True, env=env)
        if dataset_run.returncode != 0:
            results["dataset_status"] = "failed"
            results["dataset_error"] = dataset_run.stderr
            print(f"[ERROR] Dataset upload failed: {dataset_run.stderr}")
        else:
            results["dataset_status"] = "success"
            results["dataset_output"] = dataset_run.stdout
            print(f"[SUCCESS] Dataset upload complete: {dataset_run.stdout.strip()}")

            # `kaggle datasets version` above doesn't reliably apply
            # expectedUpdateFrequency/userSpecifiedSources/file descriptions
            # (see T-040) -- push them separately. Best-effort: don't fail
            # the whole run over this, the primary content already landed.
            print("Pushing dataset metadata extras (provenance, update frequency, file descriptions)...")
            try:
                extras_result = push_dataset_metadata_extras(
                    staging_dir / "dataset-metadata.json", config_dir=env.get("KAGGLE_CONFIG_DIR", "")
                )
            except Exception as extras_error:
                extras_result = {"status": "failed", "errors": [str(extras_error)]}
            results["dataset_metadata_extras"] = extras_result
            if extras_result["status"] == "success":
                print("[SUCCESS] Dataset metadata extras applied.")
            else:
                print(f"[WARNING] Dataset metadata extras failed (non-fatal): {extras_result.get('errors')}")

        # 2. Kernel push
        print("Pushing notebook kernel...")
        # Copy dataset metadata to staging is not needed for kernel push if it runs in staging
        kernel_run = subprocess.run(
            ["kaggle", "kernels", "push", "-p", str(staging_dir)],
            capture_output=True,
            text=True,
            env=env
        )
        if kernel_run.returncode != 0:
            results["kernel_status"] = "failed"
            results["kernel_error"] = kernel_run.stderr
            print(f"[ERROR] Kernel push failed: {kernel_run.stderr}")
        else:
            results["kernel_status"] = "success"
            results["kernel_output"] = kernel_run.stdout
            print(f"[SUCCESS] Kernel push complete: {kernel_run.stdout.strip()}")
            
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description="Upload dataset and kernel to Kaggle privately.")
    parser.add_argument("--credentials", type=str, default="", help="Path to kaggle.json credentials file")
    parser.add_argument("--staging", type=str, default="output/kaggle/active-fire-pilot", help="Staging directory containing data")
    args = parser.parse_args()
    
    credentials_path = Path(args.credentials) if args.credentials else Path("")
    staging_dir = KAG_DIR.parents[4] / args.staging
    
    print("=== KAGGLE PRIVATE UPLOAD ===")
    try:
        results = upload_private(credentials_path, staging_dir)
        print("Upload processing completed.")
        if results.get("dataset_status") == "failed" or results.get("kernel_status") == "failed":
            sys.exit(1)
        sys.exit(0)
    except Exception as e:
        print(f"[FATAL ERROR] {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
