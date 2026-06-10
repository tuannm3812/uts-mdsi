from __future__ import annotations

import csv
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


def main() -> None:
    status_by_subject, bucket_by_subject = load_manifest()

    for subject_dir in sorted(p for p in SUBJECTS.iterdir() if p.is_dir()):
        subject = subject_dir.name
        title = title_from_slug(subject)
        status = status_by_subject.get(subject, Counter())
        buckets = bucket_by_subject.get(subject, Counter())

        for bucket, description in BUCKET_DESCRIPTIONS.items():
            bucket_dir = subject_dir / bucket
            bucket_dir.mkdir(exist_ok=True)
            raw_count = len(list((bucket_dir / "raw").rglob("*"))) if (bucket_dir / "raw").exists() else 0
            write(
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

        inventory_link = "sources/drive-source-inventory.md"
        copied = status.get("copied", 0) + status.get("already-copied", 0)
        referenced = status.get("referenced-binary-file", 0) + status.get("referenced-large-file", 0)
        summary = f"""
## Import Summary

- Copied/readable files: {copied}
- Referenced large or binary files: {referenced}
- Source inventory: [{inventory_link}]({inventory_link})
"""
        readme = subject_dir / "README.md"
        text = readme.read_text(encoding="utf-8")
        marker = "## Import Summary"
        if marker in text:
            text = text.split(marker)[0].rstrip()
        write(readme, text.rstrip() + "\n\n" + summary)

    total = Counter()
    with MANIFEST.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            total[row["status"]] += 1
    status_rows = "".join(f"| {key} | {value} |\n" for key, value in sorted(total.items()))
    write(
        WIKI / "00-admin" / "import-summary.md",
        f"""# Import Summary

Source manifest: [drive-import-manifest.csv](drive-import-manifest.csv)

| Status | Count |
|---|---:|
{status_rows}

## Policy

- Copied files are readable course materials suitable for local search and LLM-assisted study.
- Referenced files are large datasets, archives, videos, model weights, or binaries that should stay in Drive and be opened only when needed.
""",
    )


if __name__ == "__main__":
    main()
