from __future__ import annotations

import csv
import shutil
from pathlib import Path


DRIVE_ROOT = Path(
    "/Users/tuanm.nguyen/Library/CloudStorage/GoogleDrive-tuannm3812@gmail.com/"
    "My Drive/01_Study/0. Master/6. UTS Drive"
)

REPO_ROOT = Path(__file__).resolve().parents[1]
SUBJECTS_ROOT = REPO_ROOT / "llm-wiki" / "02-subjects"
MANIFEST_PATH = REPO_ROOT / "llm-wiki" / "00-admin" / "drive-import-manifest.csv"
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


def iter_files(src: Path) -> list[tuple[Path, Path]]:
    if should_skip(src):
        return []
    if src.is_file():
        return [(src, Path(src.name))]
    files = []
    for child in src.rglob("*"):
        if should_skip(child) or child.is_dir():
            continue
        files.append((child, child.relative_to(src)))
    return files


def copy_or_reference(src: Path, dest: Path) -> tuple[str, int]:
    size = src.stat().st_size
    if src.suffix.lower() in REFERENCE_ONLY_EXTENSIONS:
        return ("referenced-binary-file", size)
    if size > MAX_COPY_BYTES:
        return ("referenced-large-file", size)
    if dest.exists() and dest.stat().st_size == size:
        return ("already-copied", size)
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dest)
    return ("copied", size)


def main() -> None:
    rows = []
    total_files = 0
    total_bytes = 0

    for semester, drive_subject, repo_subject in SUBJECTS:
        src_subject = DRIVE_ROOT / semester / drive_subject
        dst_subject = SUBJECTS_ROOT / repo_subject
        if not src_subject.exists():
            rows.append([semester, drive_subject, repo_subject, "missing", "", 0, 0])
            continue

        subject_rows = []
        for item in sorted(src_subject.iterdir(), key=lambda p: p.name.lower()):
            if should_skip(item):
                continue
            bucket = target_bucket(item)
            for source_file, rel_file in iter_files(item):
                if item.is_file():
                    dest = dst_subject / bucket / "raw" / rel_file
                else:
                    dest = dst_subject / bucket / "raw" / item.name / rel_file
                status, bytes_count = copy_or_reference(source_file, dest)
                if status in {"copied", "already-copied"}:
                    total_files += 1
                    total_bytes += bytes_count
                row = [
                    semester,
                    drive_subject,
                    repo_subject,
                    bucket,
                    str(source_file),
                    str(dest) if status != "referenced-large-file" else "",
                    status,
                    bytes_count,
                ]
                rows.append(row)
                subject_rows.append(row)

        inventory = dst_subject / "sources" / "drive-source-inventory.md"
        inventory.parent.mkdir(parents=True, exist_ok=True)
        with inventory.open("w", encoding="utf-8") as f:
            f.write(f"# Drive Source Inventory\n\n")
            f.write(f"Source subject: `{src_subject}`\n\n")
            f.write("| Status | Bucket | Size | Source |\n")
            f.write("|---|---|---:|---|\n")
            for row in subject_rows:
                _, _, _, bucket, source, _, status, size = row
                f.write(f"| {status} | {bucket} | {size} | `{source}` |\n")

    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    with MANIFEST_PATH.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(
            [
                "semester",
                "drive_subject",
                "repo_subject",
                "target_bucket",
                "source_file",
                "repo_file",
                "status",
                "bytes_copied",
            ]
        )
        writer.writerows(rows)

    print(f"Copied {total_files} files ({total_bytes / (1024 ** 3):.2f} GiB)")
    print(f"Manifest: {MANIFEST_PATH}")


if __name__ == "__main__":
    main()
