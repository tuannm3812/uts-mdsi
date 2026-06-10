from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import shutil
from collections import Counter
from pathlib import Path
from datetime import datetime


DRIVE_ROOT = Path(
    "/Users/tuanm.nguyen/Library/CloudStorage/GoogleDrive-tuannm3812@gmail.com/"
    "My Drive/01_Study/0. Master/6. UTS Drive"
)

REPO_ROOT = Path(__file__).resolve().parents[1]
SUBJECTS_ROOT = REPO_ROOT / "llm-wiki" / "02-subjects"
MANIFEST_PATH = REPO_ROOT / "llm-wiki" / "00-admin" / "drive-import-manifest.csv"
IMPORT_SUMMARY_PATH = REPO_ROOT / "llm-wiki" / "00-admin" / "import-summary.md"
IMPORT_AUDIT_ROOT = REPO_ROOT / "docs" / "superpowers" / "audit"
MAX_COPY_BYTES = 100 * 1024 * 1024
REFERENCE_ONLY_EXTENSIONS = {
    ".7z",
    ".avi",
    ".bin",
    ".dmg",
    ".gz",
    ".h5",
    ".heic",
    ".mov",
    ".mp4",
    ".parquet",
    ".pth",
    ".pt",
    ".rar",
    ".tar",
    ".tgz",
    ".zip",
}


STATUS_COPIED = "copied"
STATUS_ALREADY_COPIED = "already-copied"
STATUS_REFERENCED_BINARY = "referenced-binary-file"
STATUS_REFERENCED_LARGE = "referenced-large-file"
STATUS_MISSING = "missing"
STATUS_DUPLICATE = "duplicate-destination"
STATUS_ERROR = "error"


SUBJECTS = [
    (
        "Sem1_2025 Autumn",
        "36100 Data Science for Innovation",
        "36100-data-science-for-innovation",
    ),
    (
        "Sem1_2025 Autumn",
        "36106 Machine Learning Algorithms and Applications",
        "36106-machine-learning-algorithms-and-applications",
    ),
    ("Sem1_2025 Autumn", "36122 Python Programming", "36122-python-programming"),
    (
        "Sem2_2025 Spring",
        "36103 Statistical Thinking for Data Science",
        "36103-statistical-thinking-for-data-science",
    ),
    (
        "Sem2_2025 Spring",
        "36120 Advanced Machine Learning Application",
        "36120-advanced-machine-learning-application",
    ),
    ("Sem2_2025 Spring", "94693 Big Data Engineering", "94693-big-data-engineering"),
    (
        "Sem3_2026 Autumn",
        "36104 Data Visualisation and Narratives",
        "36104-data-visualisation-and-narratives",
    ),
    (
        "Sem3_2026 Autumn",
        "36121 Artificial Intelligence Principles and Applications",
        "36121-artificial-intelligence-principles-and-applications",
    ),
    ("Sem3_2026 Autumn", "94691 Deep Learning", "94691-deep-learning"),
    ("Sem3_2026 Autumn", "94692 Data Science Practice", "94692-data-science-practice"),
    (
        "Sem4_2026 Spring",
        "36118 Applied Natural Language Processing",
        "36118-applied-natural-language-processing",
    ),
    ("Sem4_2026 Spring", "43008-Reinforcement-Learning", "43008-reinforcement-learning"),
    ("Sem4_2026 Spring", "GenAI", "genai"),
]


def target_bucket(path: Path) -> str:
    name = path.name.lower()
    if "assignment" in name or name.startswith("at"):
        return "assignments"
    if "notebook" in name or "colab" in name:
        return "notebooks"
    if "slide" in name or "material" in name or name in {"from it"}:
        return "lectures"
    return "sources"


def _checksum(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def _normalise_bucket(source_item: Path) -> str:
    return target_bucket(source_item)


def should_skip(path: Path) -> bool:
    ignored_parts = {
        ".git",
        ".ipynb_checkpoints",
        ".mypy_cache",
        ".pytest_cache",
        ".ruff_cache",
        ".venv",
        "__MACOSX",
        "__pycache__",
        "node_modules",
    }
    parts = set(path.parts)
    return (
        path.name == ".DS_Store"
        or path.name.startswith("._")
        or any(part.startswith("venv") for part in path.parts)
        or bool(parts & ignored_parts)
    )


def iter_subject_entries(src_subject: Path) -> list[tuple[str, Path, Path, str]]:
    """Return deterministic tuples of:
    (bucket, relative_path, source_file, source_item_name)
    relative_path is relative to the source subject folder.
    """
    entries: list[tuple[str, Path, Path, str]] = []
    if not src_subject.exists():
        return entries

    top_level_items = [p for p in src_subject.iterdir() if not should_skip(p)]
    for item in sorted(top_level_items, key=lambda p: p.name.lower()):
        bucket = _normalise_bucket(item)
        source_name = item.name
        if item.is_file():
            entries.append((bucket, Path(item.name), item, source_name))
            continue

        child_files = [
            child
            for child in item.rglob("*")
            if not child.is_dir() and not should_skip(child)
        ]
        for child in sorted(child_files, key=lambda p: p.as_posix().lower()):
            rel_path = Path(source_name) / child.relative_to(item)
            entries.append((bucket, rel_path, child, source_name))
    return entries


def evaluate_file(
    source_file: Path,
    dest_file: Path,
    dry_run: bool,
) -> tuple[str, int, str | None, str | None, int]:
    """Return status, size, source checksum, destination checksum, and bytes copied."""
    size = source_file.stat().st_size

    if source_file.suffix.lower() in REFERENCE_ONLY_EXTENSIONS:
        return (STATUS_REFERENCED_BINARY, size, None, None, 0)
    if size > MAX_COPY_BYTES:
        return (STATUS_REFERENCED_LARGE, size, None, None, 0)

    source_sha = None
    if not dry_run:
        dest_file.parent.mkdir(parents=True, exist_ok=True)

    if not dest_file.exists():
        if not dry_run:
            shutil.copy2(source_file, dest_file)
        return (STATUS_COPIED, size, None, None, size)

    if not dest_file.is_file():
        raise IsADirectoryError(f"Destination exists and is not a file: {dest_file}")

    dest_size = dest_file.stat().st_size
    if dest_size == size:
        source_sha = _checksum(source_file)
        dest_sha = _checksum(dest_file)
        if source_sha == dest_sha:
            return (
                STATUS_ALREADY_COPIED,
                size,
                source_sha,
                dest_sha,
                0,
            )

    if not dry_run:
        shutil.copy2(source_file, dest_file)
    return (STATUS_COPIED, size, None, None, size)


def validate_reference_policy(results: list[dict[str, str]]) -> tuple[list[dict[str, str]], int]:
    exceptions = []
    total_reference_candidates = 0
    for row in results:
        source = Path(row["source_file"]) if row["source_file"] else None
        if not source:
            continue
        ext = source.suffix.lower()
        if ext in REFERENCE_ONLY_EXTENSIONS:
            total_reference_candidates += 1
            if row["status"] not in {STATUS_REFERENCED_BINARY}:
                exceptions.append(row)
    return exceptions, total_reference_candidates


def write_error_log(errors: list[dict[str, str]], dry_run: bool) -> Path:
    IMPORT_AUDIT_ROOT.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y-%m-%d")
    prefix = "dry-run-" if dry_run else ""
    path = IMPORT_AUDIT_ROOT / f"import-errors-{prefix}{stamp}.json"
    payload = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "dry_run": dry_run,
        "error_count": len(errors),
        "errors": errors,
    }
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return path


def write_manifest(rows: list[dict[str, str]], write_files: bool) -> None:
    if not write_files:
        return

    fieldnames = [
        "semester",
        "drive_subject",
        "repo_subject",
        "target_bucket",
        "source_file",
        "repo_file",
        "status",
        "bytes_copied",
        "source_checksum",
        "repo_checksum",
    ]

    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    with MANIFEST_PATH.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_subject_inventory(
    subject_rows: list[dict[str, str]],
    dst_subject: Path,
    write_files: bool,
) -> None:
    if not write_files:
        return

    inventory = dst_subject / "sources" / "drive-source-inventory.md"
    inventory.parent.mkdir(parents=True, exist_ok=True)
    with inventory.open("w", encoding="utf-8") as f:
        f.write("# Drive Source Inventory\n\n")
        f.write(f"Source subject: `{dst_subject}`\n\n")
        f.write("| Status | Bucket | Size | Source |\n")
        f.write("|---|---|---:|---|\n")
        for row in subject_rows:
            f.write(
                f"| {row['status']} | {row['target_bucket']} | {row['bytes_copied']} | `{row['source_file']}` |\n"
            )


def write_import_summary(
    rows: list[dict[str, str]],
    policy_exceptions: list[dict[str, str]],
    write_files: bool,
) -> None:
    if not write_files:
        return

    total = Counter(row["status"] for row in rows)
    status_rows = "".join(f"| {status} | {count} |\n" for status, count in sorted(total.items()))
    subject_summary = Counter(row["repo_subject"] for row in rows)
    per_subject = "".join(
        f"- {subject}: {count}\n" for subject, count in sorted(subject_summary.items())
    )
    exception_rows = "".join(
        f"| {row['repo_subject']} | {row['source_file']} | {row['status']} |\n"
        for row in policy_exceptions
    )

    content = (
        "# Import Summary\n\n"
        "Source manifest: [drive-import-manifest.csv](drive-import-manifest.csv)\n\n"
        "## Status Counts\n\n"
        "| Status | Count |\n|---|---:|\n"
        f"{status_rows}\n"
        "## Per-subject file-row totals\n\n"
        f"{per_subject}\n"
        "## Reference Policy\n\n"
    )
    if policy_exceptions:
        content += (
            "### Reference-only extension policy exceptions\n\n"
            "| Subject | Source File | Status |\n|---|---|---|\n"
            f"{exception_rows}\n\n"
        )
    else:
        content += "No reference-only extension policy violations detected.\n\n"

    content += (
        "## Policy\n\n"
        "- Copied files are readable course materials suitable for local search and LLM-assisted study.\n"
        "- Referenced files are large datasets, archives, videos, model weights, or binaries that should stay in Drive and be opened only when needed.\n"
    )

    IMPORT_SUMMARY_PATH.parent.mkdir(parents=True, exist_ok=True)
    IMPORT_SUMMARY_PATH.write_text(content.rstrip() + "\n", encoding="utf-8")


def print_summary(rows: list[dict[str, str]], errors: list[dict[str, str]]) -> None:
    total = Counter(row["status"] for row in rows)
    total_bytes = sum(int(row.get("bytes_copied", 0)) for row in rows)

    print(f"Source rows: {len(rows)}")
    print("Status counts:")
    for status, count in sorted(total.items()):
        print(f" - {status}: {count}")
    print(f"Payload bytes planned/copied: {total_bytes / (1024 ** 3):.2f} GiB")
    print(f"Manifest path: {MANIFEST_PATH}")
    if errors:
        print(f"Errors: {len(errors)}")
        for error in errors[:5]:
            print(f" - {error['subject']} | {error['stage']} | {error['message']}")
        if len(errors) > 5:
            print(f" - ... and {len(errors) - 5} more")


def main() -> None:
    parser = argparse.ArgumentParser(description="Import master Drive content into the LLM wiki")
    parser.add_argument("--dry-run", action="store_true", help="Report changes without writing files")
    parser.add_argument("--summary", action="store_true", help="Print compact summary output")
    parser.add_argument(
        "--subject",
        nargs="*",
        help="Optional subject filter (repo_subject names)",
    )
    parser.add_argument("--subject-regex", help="Optional regex filter for repo_subject names")
    parser.add_argument(
        "--skip-errors",
        action="store_true",
        help="Continue importing when a copy/write error is encountered",
    )
    args = parser.parse_args()

    subject_filter = set(args.subject or [])
    subject_re = re.compile(args.subject_regex) if args.subject_regex else None

    rows: list[dict[str, str]] = []
    errors: list[dict[str, str]] = []

    for semester, drive_subject, repo_subject in SUBJECTS:
        if subject_filter and repo_subject not in subject_filter:
            continue
        if subject_re and not subject_re.search(repo_subject):
            continue

        src_subject = DRIVE_ROOT / semester / drive_subject
        dst_subject = SUBJECTS_ROOT / repo_subject
        subject_rows: list[dict[str, str]] = []
        seen_dest_paths: set[Path] = set()

        if not src_subject.exists():
            row = {
                "semester": semester,
                "drive_subject": drive_subject,
                "repo_subject": repo_subject,
                "target_bucket": "missing",
                "source_file": "",
                "repo_file": "",
                "status": STATUS_MISSING,
                "bytes_copied": "0",
                "source_checksum": "",
                "repo_checksum": "",
            }
            rows.append(row)
            subject_rows.append(row)
            errors.append(
                {
                    "subject": repo_subject,
                    "source_file": "",
                    "stage": "missing_subject",
                    "message": f"Source subject path not found: {src_subject}",
                }
            )
            continue

        for bucket, rel_file, source_file, source_name in iter_subject_entries(src_subject):
            destination = dst_subject / bucket / "raw" / rel_file
            if destination in seen_dest_paths:
                row = {
                    "semester": semester,
                    "drive_subject": drive_subject,
                    "repo_subject": repo_subject,
                    "target_bucket": bucket,
                    "source_file": str(source_file),
                    "repo_file": str(destination),
                    "status": STATUS_DUPLICATE,
                    "bytes_copied": "0",
                    "source_checksum": "",
                    "repo_checksum": "",
                }
                subject_rows.append(row)
                rows.append(row)
                errors.append(
                    {
                        "subject": repo_subject,
                        "source_file": str(source_file),
                        "stage": "duplicate_destination",
                        "message": f"Duplicate destination path for '{source_name}' -> {destination}",
                    }
                )
                continue
            seen_dest_paths.add(destination)

            try:
                status, size, source_sha, repo_sha, bytes_count = evaluate_file(
                    source_file,
                    destination,
                    args.dry_run,
                )
            except Exception as exc:
                row = {
                    "semester": semester,
                    "drive_subject": drive_subject,
                    "repo_subject": repo_subject,
                    "target_bucket": bucket,
                    "source_file": str(source_file),
                    "repo_file": str(destination),
                    "status": STATUS_ERROR,
                    "bytes_copied": "0",
                    "source_checksum": "",
                    "repo_checksum": "",
                }
                rows.append(row)
                subject_rows.append(row)
                errors.append(
                    {
                        "subject": repo_subject,
                        "source_file": str(source_file),
                        "stage": "copy",
                        "message": str(exc),
                    }
                )
                if not args.skip_errors:
                    raise
                continue

            row = {
                "semester": semester,
                "drive_subject": drive_subject,
                "repo_subject": repo_subject,
                "target_bucket": bucket,
                "source_file": str(source_file),
                "repo_file": str(destination),
                "status": status,
                "bytes_copied": str(bytes_count),
                "source_checksum": source_sha or "",
                "repo_checksum": repo_sha or "",
            }
            rows.append(row)
            subject_rows.append(row)

        write_subject_inventory(subject_rows, dst_subject, not args.dry_run)

    rows = sorted(
        rows,
        key=lambda r: (
            r["repo_subject"],
            r["target_bucket"],
            r["source_file"],
        ),
    )

    policy_exceptions, policy_candidates = validate_reference_policy(rows)
    write_manifest(rows, not args.dry_run)
    write_import_summary(rows, policy_exceptions, not args.dry_run)
    error_log = write_error_log(errors, args.dry_run)

    if args.summary:
        print_summary(rows, errors)
        print(
            f"Reference-only policy exceptions: {len(policy_exceptions)} (checked {policy_candidates} candidates)"
        )
        print(f"Error log: {error_log}")
        if args.dry_run:
            print("DRY RUN active - no file writes to repo subject folders.")
    else:
        print(f"Manifest: {MANIFEST_PATH}")
        print(f"Error log: {error_log}")


if __name__ == "__main__":
    main()
