import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
import argparse

KAG_DIR = Path(__file__).resolve().parent


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
