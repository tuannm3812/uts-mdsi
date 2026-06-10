from __future__ import annotations

import argparse
import hashlib
import re
from pathlib import Path
from collections import defaultdict
import csv


ROOT = Path(__file__).resolve().parents[1]
SUBJECTS_ROOT = ROOT / "llm-wiki" / "02-subjects"
MANIFEST_PATH = ROOT / "llm-wiki" / "00-admin" / "drive-import-manifest.csv"
RAW_BUCKETS = ("assignments", "lectures", "notebooks", "sources")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Rename conflicting raw files inside llm-wiki subjects to unique names.",
    )
    parser.add_argument("--subject", action="append", default=[], help="Limit to one or more subject folders")
    parser.add_argument("--subject-regex", help="Regex applied to subject folder names")
    parser.add_argument("--dry-run", action="store_true", help="Print planned renames without making changes")
    parser.add_argument(
        "--bucket",
        action="append",
        choices=RAW_BUCKETS,
        default=list(RAW_BUCKETS),
        help="Only normalize selected raw buckets (default: all)",
    )
    return parser.parse_args()


def _slugify(value: str) -> str:
    lowered = value.lower().strip()
    lowered = lowered.replace(" ", "_")
    lowered = re.sub(r"[^a-z0-9._-]", "_", lowered)
    lowered = re.sub(r"_+", "_", lowered).strip("._-")
    return lowered or "bucket"


def _file_signature(path: Path) -> tuple[int, str]:
    hasher = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            hasher.update(chunk)
    return path.stat().st_size, hasher.hexdigest()


def _candidate_new_name(path: Path, raw_dir: Path) -> str:
    parent = path.relative_to(raw_dir).parent
    stem = path.stem
    suffix = path.suffix
    parent_slug = _slugify("__".join(parent.parts)) if parent.parts else "root"
    return f"{stem}__{parent_slug}{suffix}"


def _ensure_unique(candidate: Path) -> Path:
    root = candidate.parent
    stem = candidate.stem
    suffix = candidate.suffix
    i = 1

    while candidate.exists():
        i += 1
        candidate = root / f"{stem}_{i}{suffix}"
    return candidate


def _resolve_subjects(selected: list[str], subject_regex: str | None) -> list[Path]:
    import re as _re

    target = _re.compile(subject_regex) if subject_regex else None
    subject_names = [s.name for s in sorted(SUBJECTS_ROOT.iterdir()) if s.is_dir() and not s.name.startswith(".")]

    if selected:
        selected_set = {s.strip() for s in selected if s.strip()}
        subject_names = [name for name in subject_names if name in selected_set]

    if target:
        subject_names = [name for name in subject_names if target.search(name)]

    return [SUBJECTS_ROOT / name for name in subject_names]


def _normalize_manifest_renames(renames: list[tuple[Path, Path]], dry_run: bool) -> None:
    if not renames:
        return
    if not MANIFEST_PATH.exists():
        return

    manifest_rows: list[dict[str, str]] = []
    with MANIFEST_PATH.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        manifest_rows = [row for row in reader]

    if not manifest_rows:
        return

    lookup = {str(old): str(new) for old, new in renames}
    changed = 0
    for row in manifest_rows:
        repo_file = row.get("repo_file")
        if repo_file in lookup:
            row["repo_file"] = lookup[repo_file]
            changed += 1

    if not changed:
        return

    if dry_run:
        for old, new in renames:
            if str(old) in lookup:
                print(f"[dry-run] manifest: {old} -> {new}")
        return

    with MANIFEST_PATH.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=manifest_rows[0].keys(),
        )
        writer.writeheader()
        writer.writerows(manifest_rows)


def main() -> int:
    args = parse_args()
    subject_dirs = _resolve_subjects(args.subject, args.subject_regex)

    if not subject_dirs:
        print("No matching subject folders found.")
        return 0

    total_renames = 0
    total_groups = 0
    renames: list[tuple[Path, Path]] = []

    for subject_dir in subject_dirs:
        for bucket in args.bucket:
            raw_dir = subject_dir / bucket / "raw"
            if not raw_dir.exists():
                continue

            buckets: dict[str, list[Path]] = defaultdict(list)
            for path in raw_dir.rglob("*"):
                if path.is_file():
                    buckets[path.name.lower()].append(path)

            duplicates = {name: files for name, files in buckets.items() if len(files) > 1}
            if not duplicates:
                continue

            for name, files in sorted(duplicates.items()):
                total_groups += 1
                files_sorted = sorted(files, key=lambda p: p.as_posix().lower())
                signatures = {_file_signature(file) for file in files_sorted}
                if len(signatures) == 1:
                    continue

                keep = files_sorted[0]

                for path in files_sorted[1:]:
                    candidate_name = _candidate_new_name(path, raw_dir)
                    candidate = path.with_name(candidate_name)
                    candidate = _ensure_unique(candidate)
                    if candidate == path:
                        continue

                    total_renames += 1
                    renames.append((path, candidate))
                    if args.dry_run:
                        print(f"[dry-run] {keep.name!r} kept; {path} -> {candidate}")
                    else:
                        path.rename(candidate)
                        print(f"renamed: {path} -> {candidate}")

    _normalize_manifest_renames(renames, dry_run=args.dry_run)

    print(f"Duplicate basename groups checked: {total_groups}")
    print(f"Renames {'planned' if args.dry_run else 'performed'}: {total_renames}")
    if args.dry_run:
        print("Run without --dry-run to apply changes.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
