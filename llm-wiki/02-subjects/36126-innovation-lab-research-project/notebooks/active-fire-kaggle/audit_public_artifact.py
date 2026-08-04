import json
import re
import hashlib
import sys
from pathlib import Path
from typing import Dict, List, Tuple

BLACKLIST_TERMS = [
    r"\bfalse\s+positive(s)?\b",
    r"\bfalse\s+alarm(s)?\b",
]

# Pattern to detect typical macOS or Linux home directory paths, or absolute path patterns
ABSOLUTE_PATH_PATTERN = r"/(?:Users|home|tmp|private|var)/[a-zA-Z0-9_\-\./]+"


def calculate_sha256(file_path: Path) -> str:
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        while True:
            data = f.read(65536)
            if not data:
                break
            sha256.update(data)
    return sha256.hexdigest()


def run_hash_audit(manifest: dict, data_dir: Path) -> dict:
    errors = []
    sources = manifest.get("sources", [])
    for source in sources:
        reviewed_hashes = source.get("reviewed_sha256", {})
        for filename, expected_hash in reviewed_hashes.items():
            file_path = data_dir / filename
            if not file_path.is_file():
                errors.append(f"File missing: {filename} at {file_path}")
                continue
                
            actual_hash = calculate_sha256(file_path)
            if actual_hash != expected_hash:
                errors.append(f"Hash mismatch for {filename}: expected {expected_hash}, got {actual_hash}")
                
    return {
        "passed": len(errors) == 0,
        "errors": errors
    }


def scan_language(text: str) -> List[str]:
    found = []
    for pattern in BLACKLIST_TERMS:
        matches = re.finditer(pattern, text, re.IGNORECASE)
        for m in matches:
            found.append(f"Language violation: matched '{m.group(0)}' at character index {m.start()}")
    return found


def scan_absolute_paths(text: str) -> List[str]:
    found = []
    matches = re.finditer(ABSOLUTE_PATH_PATTERN, text)
    for m in matches:
        found.append(m.group(0))
    return found


def audit_notebook(notebook_path: Path) -> List[str]:
    errors = []
    if not notebook_path.is_file():
        errors.append(f"Notebook file not found: {notebook_path}")
        return errors
        
    try:
        with open(notebook_path, "r", encoding="utf-8") as f:
            nb = json.load(f)
    except Exception as e:
        errors.append(f"Failed to parse notebook JSON: {e}")
        return errors
        
    cells = nb.get("cells", [])
    for idx, cell in enumerate(cells):
        cell_type = cell.get("cell_type", "")
        # Combine lines of source
        source_lines = cell.get("source", [])
        if isinstance(source_lines, list):
            source = "".join(source_lines)
        else:
            source = str(source_lines)
            
        # 1. Check claim language (mostly in markdown, but check all cells)
        lang_issues = scan_language(source)
        for issue in lang_issues:
            errors.append(f"Cell {idx} ({cell_type}): {issue}")
            
        # 2. Check absolute paths (mostly in code, but check all cells)
        path_issues = scan_absolute_paths(source)
        for issue in path_issues:
            # Allow standard URLs or non-sensitive paths
            if "hotspots.dea.ga.gov.au" in issue or "data.nsw.gov.au" in issue or "mapprod3.environment.nsw.gov.au" in issue:
                continue
            errors.append(f"Cell {idx} ({cell_type}): Contains absolute local path '{issue}'")
            
    return errors


def main():
    # Audit notebooks
    kag_dir = Path(__file__).resolve().parent
    notebook_paths = [
        kag_dir / "2_active_fire_reliability_pilot.ipynb",
        kag_dir / "1_active_fire_eda.ipynb"
    ]
    manifest_path = kag_dir / "licence-manifest.json"
    
    print("=== STARTING ARTIFACT AUDIT ===")
    
    any_errors = False
    
    # 1. Audit Notebooks
    for notebook_path in notebook_paths:
        if not notebook_path.is_file():
            continue
        print(f"Auditing notebook at: {notebook_path}")
        nb_errors = audit_notebook(notebook_path)
        if nb_errors:
            print(f"\n[FAIL] Notebook {notebook_path.name} audit failed with errors:")
            for err in nb_errors:
                print(f" - {err}")
            any_errors = True
        else:
            print(f"[PASS] Notebook {notebook_path.name} audit successful.")
        print()
        
    # 2. Audit Provenance Hashes
    if manifest_path.is_file():
        print(f"Auditing provenance hashes using: {manifest_path}")
        with open(manifest_path, "r") as f:
            manifest = json.load(f)
            
        # The raw data is in tmp/ during staging
        tmp_dir = kag_dir.parents[4] / "tmp"
        if tmp_dir.is_dir():
            hash_results = run_hash_audit(manifest, tmp_dir)
            if not hash_results["passed"]:
                print("\n[FAIL] Hash audit failed:")
                for err in hash_results["errors"]:
                    print(f" - {err}")
            else:
                print("[PASS] Hash audit successful.")
        else:
            print(f"[WARN] Local tmp directory {tmp_dir} not found. Skipping hash audit.")
            
    if any_errors:
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
