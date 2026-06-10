from __future__ import annotations

import contextlib
import csv
import io
import re
import warnings
from collections import Counter, defaultdict
from pathlib import Path

import nbformat
from pypdf import PdfReader


REPO_ROOT = Path(__file__).resolve().parents[1]
SUBJECT = REPO_ROOT / "llm-wiki" / "02-subjects" / "94693-big-data-engineering"
MANIFEST = REPO_ROOT / "llm-wiki" / "00-admin" / "drive-import-manifest.csv"

LECTURE_RAW = SUBJECT / "lectures" / "raw" / "bde_slides"
NOTEBOOK_RAW = SUBJECT / "notebooks" / "raw" / "bde_notebooks"
ASSIGNMENT_RAW = SUBJECT / "assignments" / "raw" / "bde_assignment"
SOURCE_RAW = SUBJECT / "sources" / "raw"


LECTURE_TOPICS = {
    1: "Big Data Engineering Framing and Architecture",
    2: "Ingestion, Storage, and File Formats",
    3: "Spark and Distributed Processing",
    4: "SQL, Warehousing, and Query Workflows",
    5: "Pipelines, Orchestration, and DAG Design",
    6: "Operational Data Quality and Reliability",
    7: "Cost, Performance, and Scaling Trade-Offs",
    8: "Applied Big-Data Project Architecture",
}

LECTURE_OBJECTIVES = {
    1: [
        "Explain why big data architecture uses layered storage and processing approaches.",
        "Differentiate batch and stream orientation in data movement.",
        "Identify common reliability and correctness risks in distributed pipelines.",
    ],
    2: [
        "Summarise data ingestion patterns for structured and semi-structured inputs.",
        "Explain key storage decisions for lake, warehouse, and lakehouse structures.",
        "Map quality checks to ingestion and early-stage transformation.",
    ],
    3: [
        "Describe key advantages and constraints of distributed compute.",
        "Outline Spark-like processing patterns for large-scale transformation.",
        "Assess when partitioning and shuffling are essential.",
    ],
    4: [
        "Describe SQL patterns used in large-scale analysis and reporting.",
        "Identify cost-aware querying and indexing patterns.",
        "Connect SQL query design to downstream reproducibility.",
    ],
    5: [
        "Explain DAG-based pipeline design and dependency management.",
        "Trace task ordering and failure handling in a processing chain.",
        "Document observability checkpoints for end-to-end workflows.",
    ],
    6: [
        "Explain data quality controls in production workflows.",
        "Prioritise monitoring strategies for drift, missingness, and outliers.",
        "Define fallback and recovery paths for failed stages.",
    ],
    7: [
        "Evaluate performance trade-offs and resource scaling options.",
        "Identify bottlenecks in compute, I/O, and orchestration.",
        "Estimate how choices affect reliability and execution cost.",
    ],
    8: [
        "Integrate architecture, quality, and workflow choices into project design.",
        "Prepare a concise design explanation for an assessment report.",
        "Turn complex source material into evidence-based recommendations.",
    ],
}

CONCEPTS = {
    "big data architecture": ["big data", "architecture", "distributed", "cluster", "clustered", "node"],
    "pipeline": ["pipeline", "workflow", "dag", "orchestration", "task", "dependency"],
    "data lake": ["data lake", "raw", "bronze", "silver", "gold", "parquet", "delta"],
    "streaming": ["stream", "streaming", "real-time", "window", "kafka", "consumer", "producer"],
    "batch processing": ["batch", "batching", "cron", "scheduled", "offline", "airflow"],
    "storage": ["storage", "warehouse", "s3", "object", "blob", "table", "database", "schema"],
    "query": ["query", "sql", "select", "join", "aggregate", "group by", "index"],
    "quality": ["quality", "validation", "schema", "null", "missing", "duplica", "clean", "anomaly"],
    "monitoring": ["monitor", "log", "metric", "alert", "failure", "retry", "error"],
    "performance": ["performance", "scalability", "latency", "throughput", "partition", "shuffle"],
    "spark": ["spark", "parquet", "delta", "cluster", "executor", "rdd", "transform"],
    "reproducibility": ["reproducible", "reproducibility", "seed", "version", "lineage", "audit"],
}

DEFINITIONS = {
    "big data architecture": "A system design for processing and storing data at scale across multiple stages and services.",
    "pipeline": "A chain of dependent tasks that moves, transforms, validates, and delivers data and insights.",
    "data lake": "A central repository that stores raw and processed data in a flexible, scalable layout.",
    "streaming": "Continuous processing of events with low-latency ingestion and near-real-time outputs.",
    "batch processing": "Periodic processing of data in groups, usually on a schedule rather than in event-time.",
    "storage": "The physical and logical layer where data is persisted, versioned, and queried.",
    "query": "A language-driven operation that retrieves, aggregates, or transforms data.",
    "quality": "Checks and controls for correctness, consistency, completeness, and trustworthiness.",
    "monitoring": "Operational visibility into workflow success, latency, failures, and data drift.",
    "performance": "How quickly and efficiently a system handles data volume, complexity, and concurrency.",
    "spark": "A distributed compute platform commonly used for scalable batch and streaming analytics.",
    "reproducibility": "The ability to re-run analysis or pipelines and obtain verifiable, auditable results.",
}


def read_manifest_counts() -> tuple[Counter, Counter]:
    bucket_counts: Counter = Counter()
    status_counts: Counter = Counter()
    if not MANIFEST.exists():
        return bucket_counts, status_counts
    with MANIFEST.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("repo_subject") != SUBJECT.name:
                continue
            bucket_counts[row["target_bucket"]] += 1
            status_counts[row["status"]] += 1
    return bucket_counts, status_counts


def clean(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def extract_pdf(path: Path, max_chars: int = 12000) -> str:
    try:
        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr):
            warnings.simplefilter("ignore")
            reader = PdfReader(str(path))
            text = "\n".join((page.extract_text() or "") for page in reader.pages[:14])
        return clean(text)[:max_chars]
    except Exception as exc:
        return f"[PDF extraction failed: {exc}]"


def extract_notebook(path: Path, max_chars: int = 12000) -> str:
    try:
        nb = nbformat.read(path, as_version=4)
        chunks = []
        for cell in nb.cells:
            source = str(cell.source)
            if cell.cell_type == "markdown":
                chunks.append(source)
            elif cell.cell_type == "code":
                imports = "\n".join(line for line in source.splitlines() if line.startswith(("import ", "from ")))
                comments = "\n".join(line.strip("# ") for line in source.splitlines() if line.strip().startswith("#"))
                if imports:
                    chunks.append("Code imports:\n" + imports)
                if comments:
                    chunks.append(comments)
        return clean("\n".join(chunks))[:max_chars]
    except Exception as exc:
        return f"[Notebook extraction failed: {exc}]"


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def bullet(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)


def keywords(text: str, n: int = 12) -> list[str]:
    words = re.findall(r"[A-Za-z][A-Za-z0-9_+-]{3,}", text.lower())
    stop = {
        "this", "that", "with", "from", "this", "their", "about",
        "using", "using", "where", "should", "would", "could", "there",
        "lecture", "session", "chapter", "part", "files", "file",
    }
    return [word for word, _ in Counter(w for w in words if w not in stop).most_common(n)]


def score_concepts(text: str) -> Counter:
    lowered = text.lower()
    scores = Counter()
    for concept, terms in CONCEPTS.items():
        for term in terms:
            scores[concept] += lowered.count(term)
    return scores


def parse_session_from_name(name: str) -> int | None:
    match = re.search(r"lecture\s*(\d+)", name, flags=re.I)
    if not match:
        return None
    value = int(match.group(1))
    return value if 1 <= value <= 12 else None


def collect_lecture_sources() -> dict[int, list[dict[str, str]]]:
    by_session: dict[int, list[dict[str, str]]] = defaultdict(list)
    for path in sorted(LECTURE_RAW.rglob("*.pdf")):
        session = parse_session_from_name(path.name)
        if session is None:
            continue
        by_session[session].append(
            {"type": "pdf", "path": str(path.relative_to(SUBJECT)), "text": extract_pdf(path)}
        )
    return by_session


def parse_lab_key(name: str) -> tuple[int, int, str]:
    normalized = name.lower().replace("_", " ")
    match = re.search(r"lab\s*([0-9]+).*exercise\s*([0-9]+)", normalized)
    if match:
        return int(match.group(1)), int(match.group(2)), normalized
    return 0, 0, normalized


def collect_notebook_sources() -> dict[str, list[dict[str, str]]]:
    notebooks: dict[str, list[dict[str, str]]] = defaultdict(list)
    for path in sorted(NOTEBOOK_RAW.rglob("*.ipynb")):
        lab, exercise, normalized = parse_lab_key(path.name)
        lab_key = f"Lab {lab:02d} Exercise {exercise:02d}" if lab and exercise else f"Notebook {path.stem}"
        notebooks[lab_key].append(
            {
                "type": "notebook",
                "path": str(path.relative_to(SUBJECT)),
                "text": extract_notebook(path),
                "order": f"{lab:02d}-{exercise:02d}-{normalized}",
            }
        )
    return notebooks


def lab_sort_key(lab_key: str) -> tuple[int, int, str]:
    match = re.search(r"Lab\s*(\d+)\s*Exercise\s*(\d+)", lab_key, flags=re.I)
    if not match:
        return (999, 999, lab_key)
    return (int(match.group(1)), int(match.group(2)), lab_key)


def write_session_notes(by_session: dict[int, list[dict[str, str]]]) -> None:
    for session in sorted(by_session):
        sources = by_session[session]
        all_text = "\n".join(item["text"] for item in sources)
        concept_lines = [
            f"- {name}: {DEFINITIONS.get(name, 'Verify definition from source material.')}"
            for name, score in score_concepts(all_text).most_common()
            if score > 0
        ]
        source_lines = "\n".join(f"- `{item['path']}` ({item['type']})" for item in sources) or "- No matching source files found."
        write(
            SUBJECT / "lectures" / f"session-{session:02d}.md",
            f"""---
type: lecture-note
subject: 94693-big-data-engineering
session: {session}
status: draft
---

# Session {session:02d} - {LECTURE_TOPICS.get(session, f'Big Data Engineering Session {session:02d}')}

## Source Files

{source_lines}

## Working Summary

This is a first-pass curated note generated from copied slide PDFs. Verify details against source files before using it for assessment.

## Study Objectives

{bullet(LECTURE_OBJECTIVES.get(session, [f'Review lecture {session} sources and identify big-data engineering implications.']))}

## Likely Concepts

{chr(10).join(concept_lines[:10]) if concept_lines else '- To be confirmed from source review.'}

## Extracted Keywords

{bullet(keywords(all_text))}

## What To Understand

- Which data assumptions each lesson makes (source freshness, schema, and quality).
- How architecture, storage, and compute choices affect cost and reliability.
- Where observability and rollback checkpoints are most valuable.
- Which part of this session maps to assignment deliverables.

## Assessment Relevance

- Use these notes when mapping lecture ideas to assignment solutions and project architecture.
- Turn this session into 1–2 concrete design choices with justifications.

## Revision Questions

- What production risk does this topic add if implemented incorrectly?
- Which trade-off (cost, latency, quality, or reliability) is most likely in this session?
- What evidence from the slides directly supports your design decisions?

## LLM Follow-Up Prompt

Using the source files listed above, expand this into an assessment-ready study note with pipeline examples, failure modes, and design alternatives.
""",
        )


def assignment_number_from_path(path: Path) -> str | None:
    rel = path.as_posix().lower()
    match = re.search(r"bde_at(\d+)", rel)
    if match:
        return match.group(1).zfill(2)
    return None


def collect_assignment_payloads() -> dict[str, list[str]]:
    payloads = defaultdict(list)
    for path in sorted(ASSIGNMENT_RAW.rglob("*")):
        if path.is_dir():
            continue
        assignment = assignment_number_from_path(path)
        if not assignment:
            continue
        payloads[assignment].append(str(path.relative_to(SUBJECT)))
    return payloads


def write_assignment_pages(payloads: dict[str, list[str]]) -> None:
    for assignment in ["01", "02", "03"]:
        paths = sorted(payloads.get(assignment, []))
        if not paths:
            source_lines = "- No copied source files were detected in this assignment folder."
            task_guess = "Source files were not detected automatically. Populate this assignment using your final handover and spec documents."
            checklist = [
                "Task scope and required outputs are defined in official task files.",
                "Data inputs and schemas are identified and checked for consistency.",
                "Pipeline logic and SQL/analytics flow are reproducible.",
                "Final deliverables are checked against due date and required format.",
            ]
            at_link = ""
        else:
            source_lines = "\n".join(f"- `{path}`" for path in paths[:120])
            if assignment == "01":
                task_guess = (
                    "AT1 appears to focus on trending-data ingestion, transformation, and query deliverables. "
                    "Expected evidence includes SQL scripts, screenshots of handover, and architecture notes."
                )
            elif assignment == "02":
                task_guess = (
                    "AT2 appears to cover NYC taxi trip workflow and Databricks analytics refinement. "
                    "Expected evidence includes notebooks, SQL/data exploration, and model/report documentation."
                )
            else:
                task_guess = (
                    "AT3 appears to be a final integration task. Confirm source brief and rubric files before assessment drafting."
                )
            checklist = [
                "Convert raw outputs into reproducible notebook steps.",
                "Document assumptions, schema interpretation, and edge-case handling.",
                "Prepare one concise evidence map linking each deliverable to rubric requirements.",
                "Review for consistency with grading criteria and word-count limits.",
            ]

        write(
            SUBJECT / "assignments" / f"assignment-{int(assignment)}.md",
            f"""---
type: assessment
subject: 94693-big-data-engineering
code: 94693
status: planning
---

# 94693 ASSIGNMENT {int(assignment)}

## Official Task

{task_guess}

## Evidence Sources

{source_lines}

## Assessment Checklist

{bullet(checklist)}

## Working Plan

| Step | Output | Status |
|---|---|---|
| Confirm official task requirements | Requirement summary | Not started |
| Link source files to each rubric area | Evidence map draft | Not started |
| Build reproducible pipeline or notebook evidence | Draft outputs | Not started |
| Perform quality and plausibility checks | Review notes | Not started |
| Finalise submission with references | Final submission | Not started |

## LLM Review Notes

- Capture rubric wording and ask LLM for strict marker-style feedback against each checklist line.
- Keep sensitive configuration and local credentials out of notes and commits.
- Verify all SQL/analysis claims with source file lines.

## Final Verification

- [ ] Task requirements are fully interpreted from official files.
- [ ] Source files are mapped to assessment criteria.
- [ ] Outputs are reproducible from a clean environment.
- [ ] Technical claims are supported and cited.
- [ ] Submission format matches the official requirement.
""",
        )


def write_notebook_catalog() -> None:
    notebooks = collect_notebook_sources()
    rows = []
    for lab_key in sorted(notebooks, key=lab_sort_key):
        entries = notebooks[lab_key]
        source_lines = "\n".join(f"  - `{entry['path']}` ({entry['type']})" for entry in entries)
        rows.append(f"### {lab_key}\n\n" + source_lines)
    write(
        SUBJECT / "notebooks" / "lab-notes.md",
        f"""---
type: notebook-catalog
subject: 94693-big-data-engineering
status: draft
---

# 94693 Big Data Engineering - Notebook Notes

## Scope

This index links notebook sources copied from bde_notebooks to a concise study-entry map.

{chr(10).join(rows) if rows else '- No notebooks were detected in the raw folder.'}

## Maintenance

- Expand this list into per-lab notes as the course progresses.
- Keep source file paths and extracted insights near the related assessment tasks.
""",
    )

    notebooks_readme = SUBJECT / "notebooks" / "README.md"
    readme = notebooks_readme.read_text(encoding="utf-8")
    if "## Curated Notebook Notes" in readme:
        readme = readme.split("## Curated Notebook Notes", 1)[0].rstrip()
    write(notebooks_readme, readme.rstrip() + "\n\n## Curated Notebook Notes\n\n- [Lab Notes](lab-notes.md)\n")


def write_questions() -> None:
    concepts = [name.replace("_", " ") for name in CONCEPTS]
    write(
        SUBJECT / "questions" / "revision-questions.md",
        f"""---
type: question-bank
subject: 94693-big-data-engineering
code: 94693
status: draft
---

# 94693 Big Data Engineering - Revision Questions

## Conceptual Questions

- What is the practical difference between a lake, a warehouse, and a lakehouse in a data pipeline design?
- Why is partitioning important for cost and query performance?
- How does DAG design support reliability and reproducibility?
- How do you decide whether a component should be batch or streaming?
- What does pipeline observability include beyond basic logging?

## Applied Questions

- Draft a pipeline design for a trending-analytics dataset that can scale from one region to multiple regions.
- Choose between at least two storage layouts for the same workload and justify the trade-offs.
- Build a checkpoint and retry strategy for a multi-stage notebook workflow.
- Design a quality gate before loading raw CSV/JSON into analytical tables.
- Sketch a failure-handling approach for a dropped stage in batch processing.

## Technical Questions

- Given a notebook with imports and markdown comments, list five lines you would inspect to confirm reproducibility.
- Which SQL clause patterns best reduce unnecessary table scans at scale?
- How would you profile a slow Spark-style transformation?
- Which indicators tell you a data migration job is dropping records?
- How do you document data lineage for assessment defensibility?

## LLM Prompt

Using these concepts and the curated lecture notes, generate:
- a 10-question viva-style exam set,
- a short model answer key,
- and a scoring rubric with common failure modes.

{chr(10).join(f"- {concept}" for concept in concepts)}
""",
    )


def update_learning_map(by_session: dict[int, list[dict[str, str]]], payloads: dict[str, list[str]]) -> None:
    bucket_counts, _ = read_manifest_counts()
    lecture_files = [p.name for p in sorted(LECTURE_RAW.glob("*.pdf"))]
    notebook_files = [p.name for p in sorted(NOTEBOOK_RAW.rglob("*.ipynb"))]

    assignment_files = []
    for assignment in ["01", "02", "03"]:
        assignment_files.extend(
            sorted(path for path in payloads.get(assignment, []) if path.endswith((".pdf", ".ipynb", ".sql", ".md")))
        )

    source_files = [p.name for p in sorted(SOURCE_RAW.rglob("*.pdf"))]
    readme_lines = [
        "---",
        "type: learning-map",
        "subject: 94693-big-data-engineering",
        "code: 94693",
        "semester: Sem2 2025 Spring",
        "status: active",
        "---",
        "",
        "# 94693 Big Data Engineering - Learning Map",
        "",
        "## Purpose",
        "",
        "Use this page as the curated entry point for the subject. Raw copied files are useful evidence, but this page should become the LLM-friendly map of what matters.",
        "",
        "## Core Focus",
        "",
        "- Data pipelines and storage",
        "- Distributed processing",
        "- Batch and streaming trade-offs",
        "- Reliability and scalability",
        "",
        "## Connected Concepts",
        "",
        "- [Big Data](../../03-shared-concepts/big-data.md)",
        "- [Data Science Workflow](../../03-shared-concepts/data-science-workflow.md)",
        "- [Python](../../03-shared-concepts/python.md)",
        "",
        "## Study Workflow",
        "",
        "1. Review the weekly lecture material in [lectures](lectures/README.md).",
        "2. Convert important source material into concise Markdown notes.",
        "3. Link durable ideas to shared concepts.",
        "4. Track assessment requirements in [assignments](assignments/README.md).",
        "5. Use [questions](questions/README.md) for exam drills and unresolved questions.",
        "",
        "## Imported Source Profile",
        "",
        "| Bucket | Source Count |",
        "|---|---:|",
        f"| Lectures | {bucket_counts.get('lectures', len(lecture_files))} |",
        f"| Assignments | {bucket_counts.get('assignments', 0)} |",
        f"| Notebooks | {bucket_counts.get('notebooks', 0)} |",
        "| Sources | " + str(len(source_files)) + " |",
        "",
        "## Key Raw Files To Triage",
        "",
        "### Lectures",
        "",
    ]

    if lecture_files:
        readme_lines.extend(f"- {name}" for name in lecture_files)
    else:
        readme_lines.append("- No copied lecture files detected.")

    readme_lines.extend([
        "",
        "### Assignments",
        "",
    ])
    if assignment_files:
        readme_lines.extend(f"- {name.rsplit('/', 1)[-1]}" for name in sorted(assignment_files))
    else:
        readme_lines.append("- No copied assignment files detected.")

    readme_lines.extend(["", "### Notebooks", ""])
    if notebook_files:
        readme_lines.extend(f"- {name}" for name in notebook_files[:24])
    else:
        readme_lines.append("- No copied notebook files detected.")

    readme_lines.extend([
        "",
        "## Assessment Links",
        "",
        "- [ASSIGNMENT 1](assignments/assignment-1.md)",
        "- [ASSIGNMENT 2](assignments/assignment-2.md)",
        "- [ASSIGNMENT 3](assignments/assignment-3.md)",
        "",
        "## LLM Study Prompts",
        "",
        "- Summarise the lecture files into weekly notes, key concepts, and assessment relevance.",
        "- Build a glossary for this subject and link each term to shared concepts where possible.",
        "- Create a revision quiz from the learning map and the curated lecture notes.",
        "- Identify which raw files are most useful for assessment preparation and why.",
        "",
        "## Maintenance Checklist",
        "",
        f"- [x] Weekly notes created ({len(by_session)} sessions)",
        "- [x] Assignment pages created",
        "- [x] Notebook source index created",
        "- [x] Shared concepts linked",
        "- [x] Revision questions added",
    ])
    write(SUBJECT / "learning-map.md", "\n".join(readme_lines) + "\n")


def update_subject_links() -> None:
    subject_readme = SUBJECT / "README.md"
    text = subject_readme.read_text(encoding="utf-8")
    if "lab-notes.md" not in text:
        text = text.replace(
            "- [Assignment Dashboard](assignments/README.md)",
            "- [Assignment Dashboard](assignments/README.md)\n- [Notebook Notes](notebooks/lab-notes.md)",
        )
    subject_readme.write_text(text.rstrip() + "\n", encoding="utf-8")


def update_lectures_readme(by_session: dict[int, list[dict[str, str]]]) -> None:
    lecture_readme = SUBJECT / "lectures" / "README.md"
    text = lecture_readme.read_text(encoding="utf-8")
    links = "\n".join(
        f"- [Session {session:02d} - {LECTURE_TOPICS.get(session, 'Big Data Engineering Topic')}](session-{session:02d}.md)"
        for session in sorted(by_session)
    )
    if "## Curated Session Notes" in text:
        text = text.split("## Curated Session Notes", 1)[0].rstrip()
    write(lecture_readme, text.rstrip() + "\n\n## Curated Session Notes\n\n" + links + "\n")


def main() -> None:
    by_session = collect_lecture_sources()
    write_session_notes(by_session)
    payloads = collect_assignment_payloads()
    write_assignment_pages(payloads)
    write_notebook_catalog()
    write_questions()
    update_learning_map(by_session, payloads)
    update_subject_links()
    update_lectures_readme(by_session)
    print(f"Generated {len(by_session)} lecture session notes for 94693 Big Data Engineering.")


if __name__ == "__main__":
    main()
