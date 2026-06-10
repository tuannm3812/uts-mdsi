from __future__ import annotations

import contextlib
import io
import re
import warnings
import zipfile
from collections import Counter
from pathlib import Path
from xml.etree import ElementTree

from pypdf import PdfReader


REPO_ROOT = Path(__file__).resolve().parents[1]
SUBJECT = REPO_ROOT / "llm-wiki" / "02-subjects" / "36100-data-science-for-innovation"
RAW_ROOT = SUBJECT / "sources" / "raw"


SESSIONS = {
    1: {
        "title": "Course Framing and Assignment Stage 1 Brief",
        "patterns": ["36100_DSI_Assignment_Stage-1.pdf"],
        "objectives": [
            "Identify the required deliverables and evaluation criteria for Stage 1.",
            "Translate assignment requirements into a concrete task list and timeline.",
        ],
    },
    2: {
        "title": "Sample Report Standards for Innovation Deliverables",
        "patterns": ["Sample report.pdf"],
        "objectives": [
            "Extract report structure expected by the subject.",
            "Distinguish concise evidence, findings, and recommendation language.",
        ],
    },
    3: {
        "title": "Peer Review Process and Feedback Framing",
        "patterns": ["Peer_Review.docx", "peer review"],
        "objectives": [
            "Map peer review expectations, response standards, and scoring logic.",
            "Summarise actionable feedback patterns for improving iterative project drafts.",
        ],
    },
}

CONCEPTS = {
    "problem statement": ["problem", "question", "business", "innovation", "goal", "stakeholder"],
    "data science workflow": ["data", "workflow", "pipeline", "requirements", "analysis", "insights"],
    "assignment": ["assignment", "submission", "deadline", "criteria", "rubric", "stage"],
    "evaluation": ["evaluation", "assessment", "mark", "score", "grading", "criterion", "feedback"],
    "report": ["report", "introduction", "method", "methodology", "results", "conclusion", "references"],
    "peer review": ["peer", "review", "feedback", "comment", "improve", "revise"],
    "innovation": ["innovation", "opportunity", "value", "impact", "prototype", "solution"],
    "data quality": ["quality", "missing", "clean", "outlier", "bias", "validation"],
    "visualisation": ["visual", "figure", "chart", "plot", "table", "illustration"],
}

DEFINITIONS = {
    "problem statement": "The specific issue, question, or opportunity the project is designed to solve.",
    "data science workflow": "A repeatable sequence from data understanding through interpretation and communication.",
    "assignment": "An assessed task with explicit requirements, due dates, and output constraints.",
    "evaluation": "How quality is measured against criteria, usually through grading rubrics and feedback.",
    "report": "A structured written artefact that documents methods, outputs, rationale, and recommendations.",
    "peer review": "Structured feedback from peers to improve quality and align work with assessment goals.",
    "innovation": "Creating improved methods, solutions, or value through applied evidence and implementation.",
    "data quality": "The fitness of data for analysis, including completeness, consistency, and suitability.",
    "visualisation": "The transformation of findings into readable charts or tables for communication.",
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


def extract_text(path: Path) -> str:
    if path.suffix.lower() == ".pdf":
        return extract_pdf(path)
    if path.suffix.lower() == ".docx":
        return extract_docx(path)
    if path.suffix.lower() in {".md", ".txt"}:
        return clean(path.read_text(encoding="utf-8", errors="ignore"))
    return ""


def matching_sources(patterns: list[str]) -> list[Path]:
    paths = []
    for pattern in patterns:
        if any(ch in pattern for ch in ("*", "?")):
            paths.extend(RAW_ROOT.rglob(pattern))
        else:
            paths.extend(RAW_ROOT.rglob(f"**/{pattern}"))
    return sorted(set(p for p in paths if p.is_file()))


def file_type(path: Path) -> str:
    return path.suffix.lower().lstrip(".") or "file"


def score(text: str) -> Counter:
    lower = text.lower()
    counts = Counter()
    for concept, terms in CONCEPTS.items():
        for term in terms:
            counts[concept] += lower.count(term)
    return counts


def keywords(text: str, n: int = 12) -> list[str]:
    words = re.findall(r"[A-Za-z][A-Za-z0-9_+-]{3,}", text.lower())
    stop = {"this", "that", "with", "from", "that", "about", "using", "their", "there", "where", "should", "would", "could"}
    return [word for word, _ in Counter(w for w in words if w not in stop).most_common(n)]


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def bullet(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)


def write_session(number: int, session: dict[str, object], sources: list[Path]) -> None:
    source_payload = []
    for path in sources:
        text = extract_text(path)
        source_payload.append({"path": str(path.relative_to(SUBJECT)), "type": file_type(path), "text": text if text is not None else ""})
    all_text = "\n".join(item["text"] for item in source_payload)
    concepts = [
        f"- {concept}: {DEFINITIONS.get(concept, 'Verify definition from source material.')}"
        for concept, count in score(all_text).most_common()
        if count > 0
    ]
    source_lines = "\n".join(f"- `{item['path']}` ({item['type']})" for item in source_payload) or "- No matching source files found."
    write(
        SUBJECT / "lectures" / f"session-{number:02d}.md",
        f"""---
type: lecture-note
subject: 36100-data-science-for-innovation
session: {number}
status: draft
---

# Session {number:02d} - {session["title"]}

## Source Files

{source_lines}

## Working Summary

This is a first-pass curated note generated from copied assignment and reference material. Verify details against source files before using it for assessment.

## Study Objectives

{bullet(session["objectives"])} 

## Likely Concepts

{chr(10).join(concepts[:10]) or '- To be confirmed from source review.'}

## Extracted Keywords

{bullet(keywords(all_text))}

## What To Understand

- How this source sets expectations for analysis, quality, and communication.
- Which evidence points are strong enough for direct inclusion in assessment artefacts.
- Which assumptions and limitations should be documented explicitly.
- How the source helps with your project review cycle.

## Assessment Relevance

- Use these notes to build task checklists, review rubrics, and report structure.
- Turn dense sections into actionable implementation and writing items.

## Revision Questions

- What are the top 3 requirements this source changes in your work plan?
- How will you make this document traceable in your submission evidence?
- What is your action list for improving weak evidence sections?

## LLM Follow-Up Prompt

Using the source files listed above, expand this draft into a precise study note with assignment mapping, report standards, and review-ready summary language.
""",
    )


def write_glossary(items: list[dict[str, str]]) -> None:
    text = "\n".join(item["text"] for item in items)
    rows = []
    for concept, count in score(text).most_common():
        if count > 0:
            rows.append(f"| {concept} | {count} | {DEFINITIONS.get(concept, 'Add verified definition from source material.')} |")
    write(
        SUBJECT / "glossary.md",
        f"""---
type: glossary
subject: 36100-data-science-for-innovation
status: draft
---

# 36100 Data Science for Innovation - Glossary

| Term | Evidence Count | Working Definition |
|---|---:|---|
{chr(10).join(rows)}

## Maintenance

- Replace working definitions with source-grounded definitions and concrete examples.
- Link durable terms to [Data Science Workflow](../../03-shared-concepts/data-science-workflow.md), [Research Methods](../../03-shared-concepts/research-methods.md), and [Data Visualisation](../../03-shared-concepts/data-visualisation.md).
""",
    )


def write_evidence_map(session_payload: dict[int, list[dict[str, str]]]) -> None:
    rows = "\n".join(
        f"| Session {session:02d} | {SESSIONS[session]['title']} | {len(sources)} | [note](../lectures/session-{session:02d}.md) |"
        for session, sources in sorted(session_payload.items())
    )
    write(
        SUBJECT / "assignments" / "evidence-map.md",
        f"""---
type: evidence-map
subject: 36100-data-science-for-innovation
status: draft
---

# 36100 Data Science for Innovation - Assessment Evidence Map

## Session Evidence

| Session | Topic | Source Count | Curated Note |
|---|---|---:|---|
{rows}

## Assessment Evidence Strategy

- Use Session 1 for assignment requirements and milestones.
- Use Session 2 for reporting shape and communication standards.
- Use Session 3 for peer-review-driven improvement planning.
""",
    )


def update_indexes(session_payload: dict[int, list[dict[str, str]]]) -> None:
    links = "\n".join(f"- [Session {session:02d} - {SESSIONS[session]['title']}](session-{session:02d}.md)" for session in sorted(session_payload))
    lecture_readme = SUBJECT / "lectures" / "README.md"
    text = lecture_readme.read_text(encoding="utf-8")
    if "## Curated Session Notes" in text:
        text = text.split("## Curated Session Notes", 1)[0].rstrip()
    write(lecture_readme, text.rstrip() + f"\n\n## Curated Session Notes\n\n{links}\n")

    subject_readme = SUBJECT / "README.md"
    text = subject_readme.read_text(encoding="utf-8")
    if "[Glossary](glossary.md)" not in text and "## Curated Study Layer" in text:
        text = text.replace(
            "- [Revision Questions](questions/revision-questions.md)",
            "- [Revision Questions](questions/revision-questions.md)\n- [Glossary](glossary.md)\n- [Assessment Evidence Map](assignments/evidence-map.md)",
        )
    write(subject_readme, text)


def main() -> None:
    session_payload: dict[int, list[dict[str, str]]] = {}
    all_items: list[dict[str, str]] = []
    for number, session in SESSIONS.items():
        paths = matching_sources(session["patterns"])  # type: ignore[index]
        write_session(number, session, paths)
        items = []
        for path in paths:
            text = extract_text(path)
            items.append({"path": str(path.relative_to(SUBJECT)), "type": file_type(path), "text": text})
        all_items.extend(items)
        session_payload[number] = items
    write_glossary(all_items)
    write_evidence_map(session_payload)
    update_indexes(session_payload)
    print(f"Generated {len(SESSIONS)} session notes for 36100 Data Science for Innovation")


if __name__ == "__main__":
    main()
