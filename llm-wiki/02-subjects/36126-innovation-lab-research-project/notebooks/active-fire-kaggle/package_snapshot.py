from pathlib import Path
import json
import hashlib
import shutil


def validate_manifest(manifest: dict) -> None:
    for source in manifest.get("sources", []):
        if source.get("licence_status") != "confirmed":
            raise ValueError(f"Source licence is unconfirmed: {source.get('source_id')}")
        for field in ("licence_name", "kaggle_license_name", "attribution", "reviewed_sha256", "allowed_files"):
            if not source.get(field):
                raise ValueError(f"Confirmed source is missing {field}: {source.get('source_id')}")


def package_snapshot(manifest_path: Path, source_dir: Path, output_dir: Path) -> list[Path]:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    validate_manifest(manifest)
    output_dir.mkdir(parents=True, exist_ok=True)
    packaged = []
    for source in manifest["sources"]:
        for name in source["allowed_files"]:
            src = source_dir / name
            if not src.is_file():
                raise FileNotFoundError(f"File not found in source directory: {src}")
            expected = source["reviewed_sha256"].get(name)
            actual = hashlib.sha256(src.read_bytes()).hexdigest()
            if expected != actual:
                raise ValueError(f"File differs from reviewed provenance: {name}")
            dst = output_dir / name
            shutil.copy2(src, dst)
            packaged.append(dst)
    checksums = {
        path.relative_to(output_dir).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in packaged
    }
    (output_dir / "snapshot-manifest.json").write_text(
        json.dumps({"sources": manifest["sources"], "sha256": checksums}, indent=2) + "\n",
        encoding="utf-8",
    )
    return packaged
