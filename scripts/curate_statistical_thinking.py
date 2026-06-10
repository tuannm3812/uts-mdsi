from __future__ import annotations

import contextlib
import csv
import io
import re
import warnings
import zipfile
from collections import Counter
from pathlib import Path
from xml.etree import ElementTree

import nbformat
from pypdf import PdfReader


REPO_ROOT = Path(__file__).resolve().parents[1]
SUBJECT = REPO_ROOT / "llm-wiki" / "02-subjects" / "36103-statistical-thinking-for-data-science"
RAW_ROOT = SUBJECT / "sources" / "raw"


SESSIONS = {
    1: {
        "title": "Report Writing Standards for Statistical Work",
        "patterns": ["report_writing_guide.pdf", "report_writing_guide (1)-1.docx", "report_writing_guide (1)-1.docx"],
        "objectives": [
            "Identify report structure expected for statistical analysis tasks.",
            "Understand how to align methods, assumptions, and limitations with audience-ready writing.",
        ],
    },
    2: {
        "title": "Exploratory Data Analysis and Data Quality Signals",
        "patterns": ["old data/01_EDA_25v2.ipynb"],
        "objectives": [
            "Run EDA workflows to inspect distributions, missingness, and data shape.",
            "Record decisions that affect sampling bias, cleaning choices, and downstream inference.",
        ],
    },
    3: {
        "title": "Housing Data Inference Readiness and Modelling Context",
        "patterns": ["old data/Tu1HousingPriceData.csv"],
        "objectives": [
            "Summarise variable types and initial hypothesis opportunities in the housing dataset.",
            "Prepare a statistical story that distinguishes what can be inferred versus what is descriptive only.",
        ],
    },
}

CONCEPTS = {
    "inferential statistics": ["inferential", "confidence", "hypothesis", "p-value", "p value", "test", "significance"],
    "descriptive statistics": ["mean", "median", "mode", "distribution", "summary", "statistics", "describe"],
    "assumptions": ["assumption", "normality", "iid", "independence", "linearity", "homoscedastic"],
    "data quality": ["missing", "outlier", "duplicate", "null", "na", "clean", "preprocess"],
    "eda": ["eda", "exploratory", "histogram", "scatter", "boxplot", "correlation"],
    "reporting": ["report", "abstract", "method", "results", "discussion", "conclusion", "recommendation"],
    "visualisation": ["plot", "chart", "histogram", "bar", "scatter", "heatmap"],
    "sampling": ["sample", "population", "random", "bias", "stratify", "stratified", "sampled"],
    "variable type": ["numeric", "categorical", "binary", "datetime", "dtype", "type"],
    "model": ["model", "regression", "coefficient", "predictor", "response", "target", "rmse", "mae"],
}

DEFINITIONS = {
    "inferential statistics": "Methods for drawing conclusions about broader populations from sampled data.",
    "descriptive statistics": "Numeric summaries and visualisations that describe observed data directly.",
    "assumptions": "Conditions under which a statistical method is valid and interpretation is trustworthy.",
    "data quality": "Checks and decisions around missing values, noise, duplicates, and outliers.",
    "eda": "Initial exploration phase used to inspect structure, distribution, and anomalies before modelling.",
    "reporting": "Structured communication of goals, methods, evidence, limits, and recommendations.",
    "visualisation": "Figures used to support analysis claims and make distributions, relationships, and trends readable.",
    "sampling": "How data are selected and whether selected records represent the target population.",
    "variable type": "Variable classification that drives the statistical technique and interpretation.",
    "model": "A formalized relationship used to describe, predict, or explain outcomes.",
}


def clean(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def xml_text(xml: bytes) -> str:
    root = ElementTree.fromstring(xml)
    return " ".join(node.text for node in root.iter() if node.text)


def extract_docx(path: Path, max_chars: int = 12000) -> str:
    try:
        chunks = []
        with zipfile.ZipFile(path) as archive:
            for name in sorted(archive.namelist()):
                if name.startswith("word/") and name.endswith(".xml"):
                    chunks.append(xml_text(archive.read(name)))
        return clean("\n".join(chunks))[:max_chars]
    except Exception as exc:
        return f"[DOCX extraction failed: {exc}]"


def extract_pdf(path: Path, max_chars: int = 12000) -> str:
    try:
        stderr = io.StringIO()
        with warnings.catch_warnings(), contextlib.redirect_stderr(stderr):
            warnings.simplefilter("ignore")
            reader = PdfReader(str(path))
            return clean("\n".join((page.extract_text() or "") for page in reader.pages[:12]))[:max_chars]
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
                if "import " in source or "from " in source:
                    chunks.append("\n".join(line for line in source.splitlines() if line.startswith(("import ", "from "))))
                comment_lines = [line.strip() for line in source.splitlines() if line.strip().startswith("#")]
                if comment_lines:
                    chunks.append("\n".join(comment_lines))
        return clean("\n".join(chunks))[:max_chars]
    except Exception as exc:
        return f"[Notebook extraction failed: {exc}]"


def extract_csv(path: Path, max_chars: int = 12000) -> str:
    try:
        rows = []
        with path.open("r", encoding="utf-8", errors="ignore") as handle:
            reader = csv.reader(handle)
            header = next(reader)
            rows.append("Header: " + ", ".join(header))
            count = 0
            for row in reader:
                rows.append("Row: " + ", ".join(row[:8]))
                count += 1
                if count >= 40:
                    break
        return clean("\n".join(rows))[:max_chars]
    except Exception as exc:
        return f"[CSV extraction failed: {exc}]"


def extract_text(path: Path, max_chars: int = 12000) -> str:
    suffix = path.suffix.lower()
    if suffix == ".pdf":
        return extract_pdf(path, max_chars=max_chars)
    if suffix == ".docx":
        return extract_docx(path, max_chars=max_chars)
    if suffix == ".ipynb":
        return extract_notebook(path, max_chars=max_chars)
    if suffix == ".csv":
        return extract_csv(path, max_chars=max_chars)
    if suffix in {".md", ".txt"}:
        return clean(path.read_text(encoding="utf-8", errors="ignore"))[:max_chars]
    return ""


def matching_sources(patterns: list[str]) -> list[Path]:
    paths = []
    for pattern in patterns:
        if any(ch in pattern for ch in ("*", "?")):
            paths.extend(RAW_ROOT.rglob(pattern))
        else:
            if "*" in pattern:
                paths.extend(RAW_ROOT.rglob(pattern))
            else:
                paths.extend(RAW_ROOT.rglob(f"**/{pattern}"))
    return sorted(set(path for path in paths if path.is_file()))


def score(text: str) -> Counter:
    lower = text.lower()
    counts = Counter()
    for concept, terms in CONCEPTS.items():
        for term in terms:
            counts[concept] += lower.count(term)
    return counts


def keywords(text: str, n: int = 12) -> list[str]:
    words = re.findall(r"[A-Za-z][A-Za-z0-9_+-]{2,}", text.lower())
    stop = {"this", "that", "from", "with", "their", "there", "using", "will", "this", "where", "what", "into", "also"}
    return [word for word, _ in Counter(w for w in words if w not in stop).most_common(n)]


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def bullet(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)


def write_session(number: int, session: dict[str, object], source_paths: list[Path]) -> None:
    source_payload = []
    for path in source_paths:
        source_payload.append({
            "path": str(path.relative_to(SUBJECT)),
            "type": path.suffix.lower().lstrip(".") or "file",
            "text": extract_text(path),
        })
    all_text = "\n".join(item["text"] for item in source_payload)
    concept_lines = []
    for concept, count in score(all_text).most_common():
        if count > 0:
            concept_lines.append(f"- {concept}: {DEFINITIONS.get(concept, 'Verify definition from source material.')}")
    source_lines = "\n".join(f"- `{item['path']}` ({item['type']})" for item in source_payload)
    if not source_lines:
        source_lines = "- No matching source files found."
    write(
        SUBJECT / "lectures" / f"session-{number:02d}.md",
        f"""---
type: lecture-note
subject: 36103-statistical-thinking-for-data-science
session: {number}
status: draft
---

# Session {number:02d} - {session['title']}

## Source Files

{source_lines}

## Working Summary

This is a first-pass curated note generated from copied materials and notebooks. Verify details against source files before using it for assessment.

## Study Objectives

{bullet(session['objectives'])}

## Likely Concepts

{chr(10).join(concept_lines[:10]) or '- To be confirmed from source review.'}

## Extracted Keywords

{bullet(keywords(all_text))}

## What To Understand

- Which assumptions are explicit and which must be checked before inference.
- How to interpret uncertainty and avoid over-claiming from sample findings.
- How reporting style changes with audience and evidence strength.
- How to connect data quality checks to analytical trustworthiness.

## Assessment Relevance

- Use this note to convert material into checklists, method explanations, and evidence-backed conclusions.
- Keep source-linked claims for rubrics and report review quality.

## Revision Questions

- What are the assumptions behind each method used?
- What statistical conclusion is supported by the data and what is not?
- Which figure or test best supports each key claim?

## LLM Follow-Up Prompt

Using the source files listed above, expand this draft into a precise study note with assumptions, inference rules, validation checks, and assessment-ready summaries.
""",
    )


def write_glossary(all_items: list[dict[str, str]]) -> None:
    text = "\n".join(item["text"] for item in all_items)
    rows = []
    for concept, count in score(text).most_common():
        if count > 0:
            rows.append(f"| {concept} | {count} | {DEFINITIONS.get(concept, 'Add verified definition from source material.')} |")
    write(
        SUBJECT / "glossary.md",
        f"""---
type: glossary
subject: 36103-statistical-thinking-for-data-science
status: draft
---

# 36103 Statistical Thinking for Data Science - Glossary

| Term | Evidence Count | Working Definition |
|---|---:|---|
{chr(10).join(rows)}

## Maintenance

- Replace working definitions with precise formulas, examples, and assumptions from source material.
- Link durable terms to [Statistics](../../03-shared-concepts/statistics.md), [Research Methods](../../03-shared-concepts/research-methods.md), and [Data Science Workflow](../../03-shared-concepts/data-science-workflow.md).
""",
    )


def write_evidence_map(session_payload: dict[int, list[Path]]) -> None:
    rows = "\n".join(
        f"| Session {session:02d} | {SESSIONS[session]['title']} | {len(paths)} | [note](../lectures/session-{session:02d}.md) |"
        for session, paths in sorted(session_payload.items())
    )
    write(
        SUBJECT / "assignments" / "evidence-map.md",
        f"""---
type: evidence-map
subject: 36103-statistical-thinking-for-data-science
status: draft
---

# 36103 Statistical Thinking for Data Science - Assessment Evidence Map

| Session | Topic | Source Count | Curated Note |
|---|---|---:|---|
{rows}

## Assessment Evidence Strategy

- Use Session 1 for report quality, structure, and presentation standards.
- Use Session 2 for EDA workflow quality and analysis sequencing.
- Use Session 3 for dataset interpretation and statistical inference readiness.
""",
    )


def update_indexes(session_payload: dict[int, list[Path]]) -> None:
    links = "\n".join(f"- [Session {session:02d} - {SESSIONS[session]['title']}](session-{session:02d}.md)" for session in sorted(session_payload))
    lectures_readme = SUBJECT / "lectures" / "README.md"
    text = lectures_readme.read_text(encoding="utf-8")
    if "## Curated Session Notes" in text:
        text = text.split("## Curated Session Notes", 1)[0].rstrip()
    write(lectures_readme, text.rstrip() + f"\n\n## Curated Session Notes\n\n{links}\n")

    subject_readme = SUBJECT / "README.md"
    text = subject_readme.read_text(encoding="utf-8")
    if "[Glossary](glossary.md)" not in text and "## Curated Study Layer" in text:
        text = text.replace(
            "- [Revision Questions](questions/revision-questions.md)",
            "- [Revision Questions](questions/revision-questions.md)\n- [Glossary](glossary.md)\n- [Assignment Evidence Map](assignments/evidence-map.md)",
        )
    write(subject_readme, text)


def main() -> None:
    session_payload: dict[int, list[Path]] = {}
    all_items = []
    for session_id, session in SESSIONS.items():
        paths = matching_sources(session["patterns"])  # type: ignore[index]
        write_session(session_id, session, paths)
        payload_items = []
        for path in paths:
            payload_items.append({"path": str(path), "text": extract_text(path)})
            all_items.append({"path": str(path), "text": extract_text(path)})
        session_payload[session_id] = paths
    write_glossary(all_items)
    write_evidence_map(session_payload)
    update_indexes(session_payload)
    print(f"Generated {len(SESSIONS)} session notes for 36103 Statistical Thinking for Data Science")


if __name__ == "__main__":
    main()
