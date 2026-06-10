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
SUBJECT = REPO_ROOT / "llm-wiki" / "02-subjects" / "94692-data-science-practice"
RAW_ROOT = SUBJECT / "sources" / "raw"


TOPICS = {
    1: {
        "title": "Subject Outline, Assessment Framing, and Delivery Expectations",
        "patterns": ["Subject Outline DSP.pdf"],
        "objectives": [
            "Identify subject aims, assessment expectations, and delivery milestones.",
            "Translate assessment requirements into an evidence checklist for project work.",
        ],
    },
    2: {
        "title": "Project Documentation and Reproducible Application Packaging",
        "patterns": ["DSP proj.docx", "README.md"],
        "objectives": [
            "Explain how a data science project should be documented for setup, execution, and review.",
            "Connect README structure, dependencies, and run instructions to reproducibility.",
        ],
    },
    3: {
        "title": "Streamlit Data Exploration Application",
        "patterns": ["Backup.txt"],
        "objectives": [
            "Understand the structure of a Streamlit data exploration application.",
            "Review tab-based workflows for dataframe, numeric, text, and datetime analysis.",
        ],
    },
    4: {
        "title": "Neo4j Graph Data Modelling and Cypher Practice",
        "patterns": ["ERD_DSP-1.pdf", "Neo4j Lecture Code.txt"],
        "objectives": [
            "Model data as nodes, labels, properties, and relationships.",
            "Use Cypher patterns to create, match, filter, and return graph data.",
        ],
    },
    5: {
        "title": "Visual Evidence, Sales Analysis, and Project Communication",
        "patterns": ["*.png"],
        "objectives": [
            "Use visual outputs as evidence for claims about sales, products, discounts, and stock.",
            "Turn chart outputs into concise findings and project recommendations.",
        ],
    },
    6: {
        "title": "Source Hygiene, Credentials, and Submission Readiness",
        "patterns": ["keys.txt", "Neo4j-f6314a71-Created-2024-10-23.txt"],
        "objectives": [
            "Recognise credential files and exclude secrets from notes, commits, and submissions.",
            "Prepare a project folder that separates source evidence from private configuration.",
        ],
    },
}

CONCEPTS = {
    "data science workflow": ["data science", "analysis", "exploration", "dataset", "project"],
    "stakeholder communication": ["recommendation", "communication", "report", "description", "future features"],
    "reproducibility": ["requirements", "setup", "run", "environment", "version", "package"],
    "streamlit": ["streamlit", "st.", "file_uploader", "selectbox", "tabs", "expander"],
    "exploratory data analysis": ["eda", "explore", "summary", "histogram", "frequent", "missing"],
    "graph database": ["neo4j", "cypher", "node", "relationship", "label", "property"],
    "cypher query": ["match", "create", "merge", "return", "where"],
    "entity relationship diagram": ["erd", "entity", "relationship", "keys", "schema"],
    "visual evidence": ["sales", "discount", "category", "stock", "chart", "visual"],
    "credential hygiene": ["password", "token", "secret", "credential", "key"],
}

DEFINITIONS = {
    "data science workflow": "A structured process for framing, exploring, modelling, validating, and communicating data work.",
    "stakeholder communication": "Explaining evidence, limitations, and recommendations in language useful to decision makers.",
    "reproducibility": "The ability for another person to set up, run, and verify project outputs from documented steps.",
    "streamlit": "A Python framework for building interactive data applications with simple UI primitives.",
    "exploratory data analysis": "Initial analysis used to understand data structure, quality, distributions, and relationships.",
    "graph database": "A database model that stores entities as nodes and relationships as first-class connections.",
    "cypher query": "A query written in Neo4j's graph pattern language for creating, matching, and returning graph data.",
    "entity relationship diagram": "A diagram that documents entities, attributes, relationships, and constraints in a data model.",
    "visual evidence": "Charts, tables, and figures used to support analytical claims and recommendations.",
    "credential hygiene": "Practices for keeping keys, passwords, and tokens out of shared notes, commits, and reports.",
}

SENSITIVE_NAMES = {"keys.txt", "neo4j-f6314a71-created-2024-10-23.txt"}


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
            return clean("\n".join((page.extract_text() or "") for page in reader.pages[:10]))[:max_chars]
    except Exception as exc:
        return f"[PDF extraction failed: {exc}]"


def extract_text(path: Path, max_chars: int = 12000) -> str:
    suffix = path.suffix.lower()
    if path.name.lower() in SENSITIVE_NAMES:
        return "[Sensitive credential-like source excluded from extraction.]"
    if suffix == ".docx":
        return extract_docx(path, max_chars=max_chars)
    if suffix == ".pdf":
        return extract_pdf(path, max_chars=max_chars)
    if suffix in {".md", ".txt", ".py"}:
        return clean(path.read_text(encoding="utf-8", errors="ignore"))[:max_chars]
    if suffix in {".png", ".jpg", ".jpeg"}:
        return f"Image evidence file: {path.name}"
    return ""


def matching_sources(patterns: list[str]) -> list[Path]:
    paths = []
    for pattern in patterns:
        paths.extend(RAW_ROOT.rglob(pattern))
    return sorted(set(path for path in paths if path.is_file()))


def source_type(path: Path) -> str:
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
    stop = {
        "this",
        "that",
        "with",
        "from",
        "data",
        "science",
        "practice",
        "project",
        "file",
        "source",
        "using",
        "return",
        "function",
    }
    return [word for word, _ in Counter(w for w in words if w not in stop).most_common(n)]


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def bullet(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)


def collect_topic(topic: dict[str, object]) -> list[dict[str, str]]:
    sources = []
    for path in matching_sources(topic["patterns"]):  # type: ignore[index]
        sources.append(
            {
                "path": str(path.relative_to(SUBJECT)),
                "type": source_type(path),
                "text": extract_text(path),
                "sensitive": str(path.name.lower() in SENSITIVE_NAMES),
            }
        )
    return sources


def write_session(number: int, topic: dict[str, object], sources: list[dict[str, str]]) -> None:
    title = topic["title"]
    all_text = "\n".join(item["text"] for item in sources)
    concept_lines = []
    for concept, count in score(all_text).most_common():
        if count > 0:
            concept_lines.append(f"- {concept}: {DEFINITIONS.get(concept, 'Verify definition from source material.')}")
    source_lines = "\n".join(
        f"- `{item['path']}` ({item['type']})" + (" - sensitive metadata only" if item["sensitive"] == "True" else "")
        for item in sources
    ) or "- No matching source files found."
    sensitive_note = ""
    if any(item["sensitive"] == "True" for item in sources):
        sensitive_note = "\n\n## Credential Hygiene Note\n\n- This topic intentionally does not extract or quote credential values.\n- Rotate any exposed local credentials before reuse.\n- Keep private configuration in environment variables or ignored local files."
    write(
        SUBJECT / "lectures" / f"session-{number:02d}.md",
        f"""---
type: lecture-note
subject: 94692-data-science-practice
session: {number}
status: draft
---

# Session {number:02d} - {title}

## Source Files

{source_lines}

## Working Summary

This is a first-pass curated note generated from copied project references, code snippets, diagrams, and documentation. Verify details against source files before using it for assessment.

## Study Objectives

{bullet(topic["objectives"])}

## Likely Concepts

{chr(10).join(concept_lines[:10]) or '- To be confirmed from source review.'}

## Extracted Keywords

{bullet(keywords(all_text))}

## What To Understand

- What project or delivery problem this source material supports.
- Which evidence is suitable for assessment, stakeholder communication, or implementation review.
- What assumptions, setup steps, risks, or limitations should be documented.
- How this source connects to the broader data science workflow.

## Assessment Relevance

- Use this topic as supporting evidence for project planning, technical implementation, or communication quality.
- Convert raw artefacts into concise claims, decisions, risks, and reproducible steps.
{sensitive_note}

## Revision Questions

- What is the practical purpose of this artefact?
- What evidence can be reused in an assessment submission?
- What setup, data, or credential assumptions must be made explicit?
- What would a reviewer need to reproduce or trust the result?

## LLM Follow-Up Prompt

Using the source files listed above, expand this draft into a precise Data Science Practice note with project context, evidence, setup details, risks, and assessment relevance. Do not reveal secrets or credential values.
""",
    )


def write_glossary(all_sources: list[dict[str, str]]) -> None:
    text = "\n".join(item["text"] for item in all_sources)
    rows = []
    for concept, count in score(text).most_common():
        if count > 0:
            rows.append(f"| {concept} | {count} | {DEFINITIONS.get(concept, 'Add verified definition from source material.')} |")
    write(
        SUBJECT / "glossary.md",
        f"""---
type: glossary
subject: 94692-data-science-practice
status: draft
---

# 94692 Data Science Practice - Glossary

| Term | Evidence Count | Working Definition |
|---|---:|---|
{chr(10).join(rows)}

## Maintenance

- Replace working definitions with precise source-grounded definitions and project examples.
- Link durable terms to [Data Science Workflow](../../03-shared-concepts/data-science-workflow.md), [Research Methods](../../03-shared-concepts/research-methods.md), and [Assessment Strategy](../../03-shared-concepts/assessment-strategy.md).
""",
    )


def write_evidence_map(topic_sources: dict[int, list[dict[str, str]]]) -> None:
    rows = "\n".join(
        f"| Session {number:02d} | {TOPICS[number]['title']} | {len(sources)} | [note](../lectures/session-{number:02d}.md) |"
        for number, sources in sorted(topic_sources.items())
    )
    sensitive_count = sum(1 for sources in topic_sources.values() for item in sources if item["sensitive"] == "True")
    write(
        SUBJECT / "assignments" / "evidence-map.md",
        f"""---
type: evidence-map
subject: 94692-data-science-practice
status: draft
---

# 94692 Data Science Practice - Assessment Evidence Map

## Topic Evidence

| Topic | Focus | Source Count | Curated Note |
|---|---|---:|---|
{rows}

## Assessment Evidence Strategy

- Use Sessions 1-2 for assessment planning, documentation, and reproducibility.
- Use Session 3 for Streamlit implementation evidence and user workflow review.
- Use Session 4 for graph data modelling and Cypher query evidence.
- Use Session 5 for chart-based findings and communication.
- Use Session 6 for submission hygiene, private configuration, and credential-risk checks.

## Source Hygiene

- Sensitive credential-like source files detected: {sensitive_count}.
- Credential values are intentionally excluded from generated notes.
- Raw sources remain ignored locally; do not force-add raw reference files to git.
""",
    )


def update_indexes(topic_sources: dict[int, list[dict[str, str]]]) -> None:
    links = "\n".join(
        f"- [Session {number:02d} - {TOPICS[number]['title']}](session-{number:02d}.md)"
        for number in sorted(topic_sources)
    )
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
            "- [Revision Questions](questions/revision-questions.md)\n- [Glossary](glossary.md)\n- [Assessment Evidence Map](assignments/evidence-map.md)",
        )
    write(subject_readme, text)


def main() -> None:
    topic_sources = {}
    all_sources = []
    for number, topic in TOPICS.items():
        sources = collect_topic(topic)
        topic_sources[number] = sources
        all_sources.extend(sources)
        write_session(number, topic, sources)
    write_glossary(all_sources)
    write_evidence_map(topic_sources)
    update_indexes(topic_sources)
    print(f"Generated {len(topic_sources)} session notes for 94692 Data Science Practice")


if __name__ == "__main__":
    main()
