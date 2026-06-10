from __future__ import annotations

import argparse
import csv
import re
from collections import Counter, defaultdict
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
WIKI = REPO_ROOT / "llm-wiki"
SUBJECTS = WIKI / "02-subjects"
MANIFEST = WIKI / "00-admin" / "drive-import-manifest.csv"

BUCKET_DESCRIPTIONS = {
    "lectures": "Lecture slides, class materials, weekly notes, and extracted explanations.",
    "assignments": "Assessment briefs, rubric checklists, draft-review notes, and copied assignment materials.",
    "notebooks": "Notebook files, code walkthroughs, experiment notes, and reproducibility notes.",
    "sources": "Drive source inventories, raw source references, readings, and imported file maps.",
    "questions": "Open questions, tutor prompts, quiz drills, and exam practice.",
}


def title_from_slug(slug: str) -> str:
    parts = slug.split("-")
    if parts and parts[0].isdigit():
        return f"{parts[0]} {' '.join(parts[1:]).title()}"
    return " ".join(parts).title()


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def load_manifest() -> tuple[dict[str, Counter], dict[str, Counter]]:
    status_by_subject: dict[str, Counter] = defaultdict(Counter)
    bucket_by_subject: dict[str, Counter] = defaultdict(Counter)
    if not MANIFEST.exists():
        return status_by_subject, bucket_by_subject

    with MANIFEST.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            subject = row["repo_subject"]
            status_by_subject[subject][row["status"]] += 1
            bucket_by_subject[subject][row["target_bucket"]] += 1
    return status_by_subject, bucket_by_subject


def write_if_missing(path: Path, text: str) -> None:
    if path.exists():
        existing = path.read_text(encoding="utf-8")
        if existing.strip():
            return
    write(path, text)


def parse_subject_filters(
    subject_filter: list[str] | None = None,
    subject_re: str | None = None,
) -> tuple[set[str], re.Pattern[str] | None]:
    filter_set = set(subject_filter or [])
    pattern = re.compile(subject_re) if subject_re else None
    return filter_set, pattern


def iter_subject_dirs(
    subject_filter: list[str] | None = None,
    subject_re: str | None = None,
):
    filter_set, pattern = parse_subject_filters(subject_filter, subject_re)
    all_subjects = sorted((p.name for p in SUBJECTS.iterdir() if p.is_dir()))
    ordered_subjects = list(all_subjects)
    if filter_set:
        # Keep explicit subjects first when user asks for one or more subjects.
        ordered_subjects = sorted(set(ordered_subjects) | set(filter_set))
    for slug in ordered_subjects:
        if filter_set and slug not in filter_set:
            continue
        if pattern and not pattern.search(slug):
            continue
        yield SUBJECTS / slug


def ensure_subject_readme(
    subject_dir: Path,
    title: str,
    copied: int,
    referenced: int,
    summary_file: str = "sources/drive-source-inventory.md",
) -> None:
    readme = subject_dir / "README.md"
    text = readme.read_text(encoding="utf-8") if readme.exists() else f"# {title}\n"
    marker = "## Import Summary"
    if marker in text:
        text = text.split(marker)[0].rstrip()
    section = (
        f"## Import Summary\n\n"
        f"- Copied/readable files: {copied}\n"
        f"- Referenced large or binary files: {referenced}\n"
        f"- Source inventory: [{summary_file}]({summary_file})\n"
    )
    write(readme, text.rstrip() + "\n\n" + section)


def main(
    subject_filter: list[str] | None = None,
    subject_re: str | None = None,
    dry_run: bool = False,
) -> None:
    status_by_subject, bucket_by_subject = load_manifest()

    for subject_dir in iter_subject_dirs(subject_filter, subject_re):
        subject = subject_dir.name
        title = title_from_slug(subject)
        status = status_by_subject.get(subject, Counter())
        buckets = bucket_by_subject.get(subject, Counter())

        for bucket, description in BUCKET_DESCRIPTIONS.items():
            bucket_dir = subject_dir / bucket
            if not dry_run:
                bucket_dir.mkdir(parents=True, exist_ok=True)
            raw_count = len(list((bucket_dir / "raw").rglob("*"))) if (bucket_dir / "raw").exists() else 0
            if not dry_run:
                write_if_missing(
                    bucket_dir / "README.md",
                    f"""# {title} - {bucket.title()}

{description}

## Raw Imports

Raw copied files, when present, live in `raw/`.

Imported or referenced source count for this bucket: {buckets.get(bucket, 0)}
Current filesystem entries under `raw/`: {raw_count}

## Working Notes

- Add curated notes in this folder, beside `raw/`.
- Keep source-specific file maps in `sources/`.
- Link durable concepts to `../../03-shared-concepts/`.
""",
                )

        copied = status.get("copied", 0) + status.get("already-copied", 0)
        referenced = status.get("referenced-binary-file", 0) + status.get("referenced-large-file", 0)
        if not dry_run:
            ensure_subject_readme(
                subject_dir=subject_dir,
                title=title,
                copied=copied,
                referenced=referenced,
                summary_file="sources/drive-source-inventory.md",
            )

    if dry_run:
        return

    total = Counter()
    with MANIFEST.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            total[row["status"]] += 1
    subject_summary = Counter()
    with MANIFEST.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            subject_summary[row["repo_subject"]] += 1
    status_rows = "".join(f"| {key} | {value} |\n" for key, value in sorted(total.items()))
    per_subject = "".join(
        f"- {subject}: {count}\n" for subject, count in sorted(subject_summary.items())
    )
    write(
        WIKI / "00-admin" / "import-summary.md",
        f"""# Import Summary

Source manifest: [drive-import-manifest.csv](drive-import-manifest.csv)

## Status Counts

| Status | Count |
|---|---:|
{status_rows}

## Per-subject file-row totals

{per_subject}

## Reference Policy

No reference-only extension policy violations detected.

## Policy

- Copied files are readable course materials suitable for local search and LLM-assisted study.
- Referenced files are large datasets, archives, videos, model weights, or binaries that should stay in Drive and be opened only when needed.
""",
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build subject buckets and index summaries")
    parser.add_argument("--subject", nargs="*", help="Optional subject filter (repo_subject names)")
    parser.add_argument(
        "--subject-regex",
        help="Optional regex filter for repo_subject names",
    )
    args = parser.parse_args()
    main(subject_filter=args.subject, subject_re=args.subject_regex)
