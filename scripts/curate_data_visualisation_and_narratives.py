from __future__ import annotations

import re
from collections import Counter
from pathlib import Path
import nbformat
from pypdf import PdfReader


REPO_ROOT = Path(__file__).resolve().parents[1]
SUBJECT = REPO_ROOT / "llm-wiki" / "02-subjects" / "36104-data-visualisation-and-narratives"
RAW_ROOT = SUBJECT / "sources" / "raw"


SESSIONS = {
    1: {
        "title": "Python Foundations for Data Visualisation",
        "patterns": ["week2_python/amm.py"],
        "objectives": [
            "Understand the data visualisation script structure and reusable data-processing flow.",
            "Identify plotting setup, data transforms, and output expectations.",
        ],
    },
    2: {
        "title": "Gapminder Data Story Narrative Flow",
        "patterns": ["week2_python/gapminder.py"],
        "objectives": [
            "Trace visual narrative construction from filtered data to plotted insight.",
            "Assess readability, ordering, and narrative clarity for assessment outputs.",
        ],
    },
}

CONCEPTS = {
    "visualisation": ["plot", "chart", "figure", "axis", "xlabel", "ylabel", "title", "legend", "style"],
    "narrative": ["story", "insight", "message", "trend", "conclusion", "annotation", "caption"],
    "data cleaning": ["dropna", "fillna", "transform", "rename", "filter", "sort", "groupby"],
    "python": ["import", "pandas", "numpy", "matplotlib", "seaborn", "plt", "ax", "df", "dataframe"],
    "chart": ["line", "bar", "scatter", "hist", "plot", "subplot", "size", "color", "scale"],
    "communication": ["label", "legend", "explain", "interpret", "audience", "message"],
}

DEFINITIONS = {
    "visualisation": "Graphic representation of data designed to make relationships and patterns legible.",
    "narrative": "An ordered sequence of claims and visuals that explains the story in the data.",
    "data cleaning": "Preprocessing steps to make data consistent and analysis-ready.",
    "python": "Programming language used here to load, transform, and plot structured datasets.",
    "chart": "A mapped view of one or more variables for comparison or trend communication.",
    "communication": "The act of turning plotted patterns into understandable decisions and conclusions.",
}


def clean(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def extract_notebook(path: Path, max_chars: int = 12000) -> str:
    try:
        nb = nbformat.read(path, as_version=4)
        chunks = []
        for cell in nb.cells:
            source = str(cell.source)
            if cell.cell_type == "markdown":
                chunks.append(source)
            elif cell.cell_type == "code":
                if source.strip().startswith(("%", "#")):
                    chunks.append(source)
                imports = "\n".join(line for line in source.splitlines() if line.startswith(("import ", "from ")))
                comments = "\n".join(line.strip("# ") for line in source.splitlines() if line.strip().startswith("#"))
                if imports:
                    chunks.append("Code imports:\n" + imports)
                if comments:
                    chunks.append(comments)
        return clean("\n".join(chunks))[:max_chars]
    except Exception as exc:
        return f"[Notebook extraction failed: {exc}]"


def extract_python(path: Path, max_chars: int = 12000) -> str:
    try:
        return clean(path.read_text(encoding="utf-8", errors="ignore"))[:max_chars]
    except Exception as exc:
        return f"[Python extraction failed: {exc}]"


def extract_text(path: Path) -> str:
    if path.suffix.lower() == ".ipynb":
        return extract_notebook(path)
    if path.suffix.lower() == ".py":
        return extract_python(path)
    if path.suffix.lower() == ".pdf":
        try:
            reader = PdfReader(str(path))
            return clean("\n".join((page.extract_text() or "") for page in reader.pages[:12]))[:12000]
        except Exception as exc:
            return f"[PDF extraction failed: {exc}]"
    return ""


def score(text: str) -> Counter:
    lower = text.lower()
    counts = Counter()
    for concept, terms in CONCEPTS.items():
        for term in terms:
            counts[concept] += lower.count(term)
    return counts


def keywords(text: str, n: int = 12) -> list[str]:
    words = re.findall(r"[A-Za-z][A-Za-z0-9_+-]{3,}", text.lower())
    stop = {"this", "that", "with", "from", "using", "their", "there", "where", "value", "data"}
    return [word for word, _ in Counter(w for w in words if w not in stop).most_common(n)]


def bullet(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def matching_sources(patterns: list[str]) -> list[Path]:
    paths = []
    for pattern in patterns:
        paths.extend((RAW_ROOT / pattern).parents[0].glob(Path(pattern).name) if not any(ch in pattern for ch in "*?[]") else RAW_ROOT.rglob(pattern))
    return sorted(set(p for p in paths if p.is_file()))


def find_sources() -> dict[int, list[Path]]:
    return {
        session_id: sorted((RAW_ROOT / pattern) for pattern in session["patterns"] if (RAW_ROOT / pattern).exists())
        for session_id, session in SESSIONS.items()
    }


def write_session(session_id: int, session: dict[str, object], source_paths: list[Path]) -> None:
    source_payload = [{"path": str(path.relative_to(SUBJECT)), "type": path.suffix.lower().lstrip(".") or "file", "text": extract_text(path)} for path in source_paths]
    all_text = "\n".join(item["text"] for item in source_payload)
    concept_lines = []
    for concept, count in score(all_text).most_common():
        if count > 0:
            concept_lines.append(f"- {concept}: {DEFINITIONS.get(concept, 'Verify definition from source material.')}")
    source_lines = "\n".join(f"- `{item['path']}` ({item['type']})" for item in source_payload) or "- No matching source files found."
    write(
        SUBJECT / "lectures" / f"session-{session_id:02d}.md",
        f"""---
type: lecture-note
subject: 36104-data-visualisation-and-narratives
session: {session_id}
status: draft
---

# Session {session_id:02d} - {session["title"]}

## Source Files

{source_lines}

## Working Summary

This is a first-pass curated note generated from the copied visualisation scripts. Verify details against source files before using it for assessment.

## Study Objectives

{bullet(session["objectives"])}

## Likely Concepts

{chr(10).join(concept_lines[:10]) or '- To be confirmed from source review.'}

## Extracted Keywords

{bullet(keywords(all_text))}

## What To Understand

- What message the script intends to communicate.
- Which data filters and transformations shape the narrative.
- How visual defaults impact interpretation.
- What is needed to make the visualisation audience-ready.

## Assessment Relevance

- Use this note as a template for reproducible plots and report narrative structure.
- Translate each visual claim into evidence-backed conclusions.

## Revision Questions

- What is the primary claim in this session’s visual narrative?
- Which assumptions are made by filtering and scaling?
- What would improve interpretability for a non-technical audience?

## LLM Follow-Up Prompt

Using the source files listed above, expand this draft into a precise study note with figure-by-figure interpretation, narrative framing, and reusable coding improvements.
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
subject: 36104-data-visualisation-and-narratives
status: draft
---

# 36104 Data Visualisation and Narratives - Glossary

| Term | Evidence Count | Working Definition |
|---|---:|---|
{chr(10).join(rows)}

## Maintenance

- Replace working definitions with exact plotting and communication examples from source files.
- Link durable terms to [Data Visualisation](../../03-shared-concepts/data-visualisation.md), [Data Science Workflow](../../03-shared-concepts/data-science-workflow.md), and [Statistics](../../03-shared-concepts/statistics.md).
""",
    )


def write_evidence_map(session_sources: dict[int, list[Path]]) -> None:
    rows = "\n".join(
        f"| Session {session:02d} | {SESSIONS[session]['title']} | {len(paths)} | [note](../lectures/session-{session:02d}.md) |"
        for session, paths in sorted(session_sources.items())
    )
    write(
        SUBJECT / "assignments" / "evidence-map.md",
        f"""---
type: evidence-map
subject: 36104-data-visualisation-and-narratives
status: draft
---

# 36104 Data Visualisation and Narratives - Assessment Evidence Map

| Session | Topic | Source Count | Curated Note |
|---|---|---:|---|
{rows}

## Assessment Evidence Strategy

- Use Session 1 for visual foundations and reproducible scripting structure.
- Use Session 2 for narrative plot construction and insight communication.
""",
    )


def update_indexes(session_sources: dict[int, list[Path]]) -> None:
    links = "\n".join(f"- [Session {session:02d} - {SESSIONS[session]['title']}](session-{session:02d}.md)" for session in sorted(session_sources))
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
    session_sources = find_sources()
    all_items = []
    for session_id, session in SESSIONS.items():
        paths = session_sources.get(session_id, [])
        write_session(session_id, session, paths)
        for path in paths:
            all_items.append({"path": str(path.relative_to(SUBJECT)), "text": extract_text(path)})
    write_glossary(all_items)
    write_evidence_map(session_sources)
    update_indexes(session_sources)
    print(f"Generated {len(SESSIONS)} session notes for 36104 Data Visualisation and Narratives")


if __name__ == "__main__":
    main()
