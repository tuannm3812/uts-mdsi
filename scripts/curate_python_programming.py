from __future__ import annotations

import re
from collections import Counter, defaultdict
from pathlib import Path

import nbformat
from pypdf import PdfReader

REPO_ROOT = Path(__file__).resolve().parents[1]
SUBJECT = REPO_ROOT / "llm-wiki" / "02-subjects" / "36122-python-programming"
LECTURE_RAW = SUBJECT / "lectures" / "raw" / "materials"
NOTEBOOK_RAW = SUBJECT / "notebooks" / "raw"
ASSIGNMENTS_RAW = SUBJECT / "assignments" / "raw" / "assignment"
SOURCE_RAW = SUBJECT / "sources" / "raw"

SESSION_TOPICS = {
    1: "Python environment and language fundamentals",
    2: "Conditions, decision logic, and loops",
    3: "Functions and dictionaries",
    4: "Strings, regex, and file operations",
    5: "Object-oriented programming and classes",
    6: "Web scraping and structured input/output",
    7: "Hands-on lab consolidation",
    8: "UI and practical examples",
    9: "Integration patterns",
    10: "Testing and troubleshooting workflows",
    11: "Project architecture review",
    12: "Plotting, reporting, and wrap-up",
}

SESSION_OBJECTIVES = {
    1: [
        "Set up Python runtime, data types, and basic syntax confidently.",
        "Explain differences between expressions, control flow, and script structure.",
    ],
    2: [
        "Implement conditionals and loops for branching and repetition.",
        "Reason about edge cases and off-by-one behavior.",
    ],
    3: [
        "Use functions and dictionaries for reusable processing.",
        "Understand parameter design and return semantics.",
    ],
    4: [
        "Parse text and files with robust string handling.",
        "Build small utilities for cleaning and transformation.",
    ],
    5: [
        "Use classes and objects to structure logic.",
        "Choose where OOP improves maintainability.",
    ],
    6: [
        "Build script workflows for network and scraping tasks.",
        "Validate reliability and failure behavior in external requests.",
    ],
    7: [
        "Summarize labs around repeated patterns and coding practice.",
        "Check reproducibility in local notebooks.",
    ],
    8: [
        "Translate UI-level examples into robust implementation patterns.",
    ],
    9: [
        "Integrate snippets into a larger workflow.",
        "Track variable flow and dependencies.",
    ],
    10: [
        "Review test and debug strategy.",
        "Write concise checks and recovery logic.",
    ],
    11: [
        "Inspect project-level files for architecture consistency.",
    ],
    12: [
        "Use plotting and summarization outputs for concise reporting.",
    ],
}

CONCEPTS = {
    "python": ["python", "py"],
    "variables": ["variable", "var", "assignment"],
    "functions": ["function", "def ", "return", "args", "kwargs"],
    "conditionals": ["if", "else", "elif", "condition", "loop", "while", "for"],
    "data structures": ["list", "dict", "tuple", "set", "array"],
    "string": ["string", "str", "split", "regex", "replace", "strip"],
    "classes": ["class", "object", "init", "method", "__init__"],
    "io": ["open(", "read", "write", "file", "csv", "pathlib", "path"],
    "notebook": ["notebook", "ipynb", "cell", "output", "markdown"],
    "web scraping": ["requests", "beautifulsoup", "soup", "url", "html", "scrape"],
    "plotting": ["plot", "matplotlib", "figure", "chart", "ax", "subplot", "numpy", "pandas"],
    "debugging": ["debug", "error", "exception", "try", "except", "assert"],
}

DEFINITIONS = {
    "python": "A general-purpose programming language used for scripting, data analysis, and automation.",
    "variables": "Named storage locations used to hold values and intermediate state.",
    "functions": "Reusable code blocks with inputs, optional defaults, and returned outputs.",
    "conditionals": "Branching logic that changes behavior based on boolean checks.",
    "data structures": "Core containers for organizing values and relationships in memory.",
    "string": "Text type and operations for parsing and transformation.",
    "classes": "Templates for creating objects with shared behavior and state.",
    "io": "Input/output mechanics for reading and writing local or external files.",
    "notebook": "A literate programming environment that combines code, markdown, and outputs.",
    "web scraping": "Automated extraction of structured content from web pages.",
    "plotting": "Visualization of analysis results using numeric and charting libraries.",
    "debugging": "Locating and fixing defects through checks, error traces, and targeted tests.",
}


def clean_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def parse_session_number(name: str) -> int | None:
    match = re.match(r"^0*(\d{1,2})[_.-]", name)
    if match:
        value = int(match.group(1))
        if 1 <= value <= 12:
            return value

    match = re.search(r"(?:(?<=^)|(?<=[^a-z0-9]))(?:week|w)[_-]?(0*[1-9]|1[0-2])(?=[^a-z0-9]|$)", name)
    if match:
        value = int(match.group(1))
        if 1 <= value <= 12:
            return value
    return None


def extract_pdf(path: Path, max_chars: int = 12000) -> str:
    try:
        reader = PdfReader(str(path))
        return clean_text("\n".join((page.extract_text() or "") for page in reader.pages[:20]))[:max_chars]
    except Exception as exc:
        return f"[PDF extraction failed: {exc}]"


def extract_notebook(path: Path, max_chars: int = 12000) -> str:
    try:
        nb = nbformat.read(path, as_version=4)
        chunks: list[str] = []
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
        return clean_text("\n".join(chunks))[:max_chars]
    except Exception as exc:
        return f"[Notebook extraction failed: {exc}]"


def extract_text(path: Path, max_chars: int = 12000) -> str:
    suffix = path.suffix.lower()
    if suffix == ".pdf":
        return extract_pdf(path, max_chars=max_chars)
    if suffix == ".ipynb":
        return extract_notebook(path, max_chars=max_chars)
    if suffix in {".md", ".txt", ".py", ".html", ".json"}:
        try:
            return clean_text(path.read_text(encoding="utf-8", errors="ignore"))[:max_chars]
        except Exception:
            return f"[Text read failed: {path.name}]"
    if suffix == ".csv":
        try:
            return clean_text(path.read_text(encoding="utf-8", errors="ignore")[:3000])
        except Exception:
            return f"[CSV read failed: {path.name}]"
    return ""


def session_from_path(path: Path, fallback: int | None = None) -> int | None:
    value = parse_session_number(path.name.lower())
    if value is not None:
        return value
    return fallback


def collect() -> tuple[
    dict[int, list[dict[str, str]]],
    dict[int, list[dict[str, str]]],
    dict[str, list[dict[str, str]]],
]:
    lecture_sources: dict[int, list[dict[str, str]]] = defaultdict(list)
    notebook_sources: dict[int, list[dict[str, str]]] = defaultdict(list)
    assignments: dict[str, list[dict[str, str]]] = defaultdict(list)

    for path in sorted(LECTURE_RAW.rglob("*")):
        if not path.is_file() or path.suffix.lower() != ".pdf":
            continue
        item = {
            "path": str(path.relative_to(SUBJECT)),
            "type": "pdf",
            "text": extract_pdf(path),
        }
        session = session_from_path(path, fallback=None)
        if session:
            lecture_sources[session].append(item)
        else:
            # fallback for combined module docs without numeric prefix
            lecture_sources[12].append(item)

    for path in sorted(NOTEBOOK_RAW.rglob("*")):
        if not path.is_file():
            continue
        if path.suffix.lower() not in {".ipynb", ".py", ".txt", ".html"}:
            continue
        if any(part.startswith("solutions") for part in path.parts):
            session = session_from_path(path, fallback=1)
        else:
            session = session_from_path(path, fallback=1)
        source_type = path.suffix.lower().lstrip(".")
        item = {"path": str(path.relative_to(SUBJECT)), "type": source_type, "text": extract_text(path)}
        notebook_sources[session].append(item)

    for path in sorted(ASSIGNMENTS_RAW.rglob("*")):
        if not path.is_file():
            continue
        rel = str(path.relative_to(ASSIGNMENTS_RAW)).lower()
        text = extract_text(path)
        item = {"path": str(path.relative_to(SUBJECT)), "type": path.suffix.lower().lstrip("."), "text": text}

        if "week" in rel:
            week = parse_session_number(path.name.lower())
            if week is not None:
                assignments[f"week-{week:02d}"].append(item)
            else:
                assignments["other"].append(item)
        elif "news_aggregator" in rel or "project" in rel or "demo" in rel:
            assignments["project"].append(item)
        elif "readme" in rel or "untitled" in rel:
            assignments["project"].append(item)
        else:
            assignments["other"].append(item)
    return lecture_sources, notebook_sources, assignments


def score_concepts(text: str) -> Counter:
    lowered = text.lower()
    scores = Counter()
    for concept, terms in CONCEPTS.items():
        for term in terms:
            scores[concept] += lowered.count(term)
    return scores


def top_keywords(text: str, n: int = 12) -> list[str]:
    words = re.findall(r"[A-Za-z][A-Za-z0-9_+-]{3,}", text.lower())
    stop = {
        "this", "that", "with", "from", "have", "they", "their", "there", "these", "those",
        "will", "data", "file", "using", "while", "for", "from", "then", "here", "there",
    }
    return [word for word, _ in Counter(w for w in words if w not in stop).most_common(n)]


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def bullet(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)


def write_session_note(session: int, sources: list[dict[str, str]]) -> None:
    merged = "\n".join(item["text"] for item in sources)
    source_lines = "\n".join(f"- `{item['path']}` ({item['type']})" for item in sources) or "- No source files identified."
    concept_lines = [
        f"- {concept}: {DEFINITIONS.get(concept, 'Verify definition from source material.')}"
        for concept, count in score_concepts(merged).most_common()
        if count > 0
    ]

    write(
        SUBJECT / "lectures" / f"session-{session:02d}.md",
        "\n".join(
            [
                "---",
                "type: lecture-note",
                "subject: 36122-python-programming",
                f"session: {session}",
                "status: draft",
                "---",
                "",
                f"# Session {session:02d} - {SESSION_TOPICS.get(session, f'Session {session}')}",
                "",
                "## Source Files",
                "",
                source_lines,
                "",
                "## Working Summary",
                "",
                "This is a first-pass curated note generated from copied lecture material and notebooks. Verify details against source files before using it for assessment.",
                "",
                "## Study Objectives",
                "",
                bullet(SESSION_OBJECTIVES.get(session, ["Convert source material into reproducible programming patterns."])),
                "",
                "## Likely Concepts",
                "",
                "\n".join(concept_lines[:10]) or "- To be confirmed from source review.",
                "",
                "## Extracted Keywords",
                "",
                bullet(top_keywords(merged)),
                "",
                "## What To Understand",
                "",
                "- What the code is solving and what assumptions are made.",
                "- How implementation choices affect readability and reproducibility.",
                "- Which checks catch the most likely runtime errors.",
                "- Which sources support assignment and project tasks.",
                "",
                "## Assessment Relevance",
                "",
                "- Link this session to assignment pages using the evidence map.",
                "- Keep each claim tied to code artifacts and outputs.",
                "",
                "## Revision Questions",
                "",
                "- What is the practical purpose of the main constructs in this session?",
                "- Which design trade-off is most visible in this material?",
                "- What minimal evidence validates the method shown?",
                "",
                "## LLM Follow-Up Prompt",
                "",
                "Using the source files listed above, expand this draft into a concise revision note with examples, edge cases, and quality checks.",
            ]
        ),
    )


def write_glossary(payloads: list[dict[str, str]]) -> None:
    merged = "\n".join(item["text"] for item in payloads)
    rows = [
        f"| {term} | {count} | {DEFINITIONS.get(term, 'Add verified definition from source material.')} |"
        for term, count in score_concepts(merged).most_common()
        if count > 0
    ]
    write(
        SUBJECT / "glossary.md",
        "\n".join(
            [
                "---",
                "type: glossary",
                "subject: 36122-python-programming",
                "status: draft",
                "---",
                "",
                "# 36122 Python Programming - Glossary",
                "",
                "| Term | Evidence Count | Working Definition |",
                "|---|---:|---|",
            ]
            + rows
            + [
                "",
                "## Maintenance",
                "",
                "- Add exact examples, mini code snippets, and edge case notes.",
                "- Link durable terms to [Python](../../03-shared-concepts/python.md), [Programming Fundamentals](../../03-shared-concepts/programming.md), and [Data Science Workflow](../../03-shared-concepts/data-science-workflow.md).",
            ]
        ),
    )


def assignment_filename(bucket: str) -> str:
    if bucket.startswith("week-"):
        return f"assignments/{bucket}.md"
    if bucket == "project":
        return "assignments/project.md"
    return "assignments/other.md"


def write_assignment_pages(assignment_payloads: dict[str, list[dict[str, str]]]) -> None:
    for bucket, payload in sorted(assignment_payloads.items()):
        file_lines = [f"- `{item['path']}` ({item['type'] or 'file'})" for item in sorted(payload, key=lambda item: item["path"])] or ["- No files copied."]
        write(
            SUBJECT / assignment_filename(bucket),
            "\n".join(
                [
                    "---",
                    "type: assessment",
                    "subject: 36122-python-programming",
                    "code: 36122",
                    "status: planning",
                    "---",
                    "",
                    f"# 36122 {bucket.replace('_', ' ').title()} - Assignment",
                    "",
                    "## Official Task",
                    "",
                    "Source files are mapped from `assignments/raw/assignment/`.",
                    "",
                    "## Raw Source Files",
                    "",
                    *file_lines,
                    "",
                    "## Rubric Checklist",
                    "",
                    "- [ ] Code implements required task in Python.",
                    "- [ ] Inputs and outputs are validated.",
                    "- [ ] Edge cases are handled and tested.",
                    "- [ ] Evidence is documented and reproducible.",
                    "- [ ] Final submission format is correct.",
                    "",
                    "## Working Plan",
                    "",
                    "| Step | Output | Status |",
                    "|---|---|---|",
                    "| Understand task | Summary and scope | Not started |",
                    "| Collect evidence | Linked source files and output references | Not started |",
                    "| Draft solution | First draft | Not started |",
                    "| Self-review | Checklist-based check | Not started |",
                    "| Final check | Submission-ready version | Not started |",
                    "",
                    "## LLM Review Prompt",
                    "",
                    "Act as a strict marker and return missing requirements, risky assumptions, and concrete revision steps.",
                ]
            ),
        )


def write_evidence_map(lecture_sources: dict[int, list[dict[str, str]]], assignment_payloads: dict[str, list[dict[str, str]]]) -> None:
    session_rows = "\n".join(
        f"| Session {session:02d} | {SESSION_TOPICS.get(session, '')} | {len(sources)} | [note](../lectures/session-{session:02d}.md) |"
        for session, sources in sorted(lecture_sources.items())
    )
    assignment_rows = "\n".join(
        f"| {name} | {len(payload)} source files | [{name}](../{assignment_filename(name)}) |"
        for name, payload in sorted(assignment_payloads.items())
    )
    write(
        SUBJECT / "assignments" / "evidence-map.md",
        "\n".join(
            [
                "---",
                "type: evidence-map",
                "subject: 36122-python-programming",
                "status: draft",
                "---",
                "",
                "# 36122 Python Programming - Evidence Map",
                "",
                "## Session Evidence",
                "",
                "| Session | Topic | Source Count | Curated Note |",
                "|---|---|---:|---|",
                session_rows,
                "",
                "## Assignment Evidence",
                "",
                "| Assignment | Source File Count | Curated Task Note |",
                "|---|---:|---|",
                assignment_rows,
            ]
        ),
    )


def write_questions() -> None:
    write(
        SUBJECT / "questions" / "revision-questions.md",
        "\n".join(
            [
                "---",
                "type: question-bank",
                "subject: 36122-python-programming",
                "code: 36122",
                "status: draft",
                "---",
                "",
                "# 36122 Python Programming - Revision Questions",
                "",
                "## Conceptual Questions",
                "",
                "- Why does small input validation matter for code quality?",
                "- When is a function better than inlined repeated code?",
                "- What makes a notebook reproducible versus exploratory only?",
                "- How do you balance readability and concision in instructional code?",
                "",
                "## Applied Questions",
                "",
                "- Design a Python workflow for a small assignment using one week notebook and one lecture topic.",
                "- Build a reproducibility checklist from your assignment notebooks.",
                "- Compare two coding approaches and justify one with maintainability and reliability.",
                "",
                "## Technical Questions",
                "",
                "- What exception handling strategy should you add to a scraper script?",
                "- Which outputs prove that a function is robust?",
                "- How do you check file-path portability across environments?",
                "",
                "## LLM Drill Prompt",
                "",
                "Generate a short exam set of 12 conceptual/applied/technical questions with concise model answers.",
            ]
        ),
    )


def write_notebook_notes(notebook_sources: dict[int, list[dict[str, str]]]) -> None:
    rows = [f"- Session {session:02d}: {len(items)} notebook files" for session, items in sorted(notebook_sources.items())]
    notebook_files = [item["path"] for items in sorted(notebook_sources.values(), key=len) for item in items]
    write(
        SUBJECT / "notebooks" / "lab-notes.md",
        "\n".join(
            [
                "---",
                "type: notebook-notes",
                "subject: 36122-python-programming",
                "status: draft",
                "---",
                "",
                "# 36122 Python Programming - Lab Notes",
                "",
                "## Notebook Evidence Summary",
                "",
                "This file tracks notebook and script evidence for reproducibility.",
                "",
                "### Grouped Sources",
                "",
                *rows,
                "",
                "### Key Files",
                "",
                "- " + "\n- ".join(notebook_files[:25]) if notebook_files else "- No notebook files detected.",
                "",
                "## Practical Note",
                "",
                "- Pull reusable patterns into the session notes.",
                "- Flag code that fails without specific local setup.",
            ]
        ),
    )


def read_manifest_counts() -> dict[str, int]:
    default_counts = {"lectures": 0, "assignments": 0, "notebooks": 0, "sources": 0}
    manifest = SUBJECT / "sources" / "drive-source-inventory.md"
    if not manifest.exists():
        return default_counts
    total = Counter()
    for line in manifest.read_text(encoding="utf-8").splitlines():
        if line.startswith("| already-copied") or line.startswith("| referenced-large-file") or line.startswith("| referenced-binary-file"):
            parts = [col.strip().lower() for col in line.strip().strip("|").split("|")]
            if len(parts) >= 4:
                total[parts[1]] += 1
    return {k: total.get(k, 0) for k in default_counts}


def update_learning_map(lecture_sources: dict[int, list[dict[str, str]]], notebook_sources: dict[int, list[dict[str, str]]], assignment_payloads: dict[str, list[dict[str, str]]]) -> None:
    counts = read_manifest_counts()
    lecture_file_count = sum(len(v) for v in lecture_sources.values())
    notebook_file_count = sum(len(v) for v in notebook_sources.values())
    assignment_file_count = sum(len(v) for v in assignment_payloads.values())
    write(
        SUBJECT / "learning-map.md",
        "\n".join(
            [
                "---",
                "type: learning-map",
                "subject: 36122-python-programming",
                "code: 36122",
                "semester: Sem1 2025 Autumn",
                "status: active",
                "---",
                "",
                "# 36122 Python Programming - Learning Map",
                "",
                "## Purpose",
                "",
                "Use this as the LLM-friendly map for the course materials. Raw files are evidence; notes should become the assessment-ready layer.",
                "",
                "## Core Focus",
                "",
                "- Python fundamentals and syntax",
                "- Data structures, control flow, and function patterns",
                "- Notebook workflows and reproducibility",
                "- File I/O, scraping, and project integration",
                "",
                "## Connected Concepts",
                "",
                "- [Python](../../03-shared-concepts/python.md)",
                "- [Programming Fundamentals](../../03-shared-concepts/programming.md)",
                "- [Data Science Workflow](../../03-shared-concepts/data-science-workflow.md)",
                "",
                "## Study Workflow",
                "",
                "1. Review each session in [lectures](lectures/README.md).",
                "2. Convert examples into concise notes and reusable patterns.",
                "3. Map session content to assignment evidence.",
                "4. Track project and weekly deliverables in [assignments](assignments/README.md).",
                "5. Use [questions](questions/revision-questions.md) for regular drill.",
                "",
                "## Imported Source Profile",
                "",
                "| Bucket | Source Count |",
                "|---|---:|",
                f"| Lectures | {counts.get('lectures', lecture_file_count)} |",
                f"| Assignments | {counts.get('assignments', assignment_file_count)} |",
                f"| Notebooks | {counts.get('notebooks', notebook_file_count)} |",
                f"| Sources | {counts.get('sources', 0)} |",
                "",
                "## Key Raw Files To Triage",
                "",
                "### Lectures",
                "",
                *[f"- {item['path'].split('/', 1)[1]}" for session in sorted(lecture_sources) for item in lecture_sources[session]],
                "",
                "### Assignments",
                "",
                *[f"- {name}" for payload in assignment_payloads.values() for item in payload for name in [item['path'].split('/', 2)[2]]][:40],
                "",
                "### Notebooks",
                "",
                *[f"- {item['path'].split('/', 2)[2]}" for session in sorted(notebook_sources) for item in notebook_sources[session]],
                "",
                "## Assessment Links",
                "",
                *[f"- [{name}](assignments/{name}.md)" for name in sorted(assignment_payloads)],
                "- [Evidence Map](assignments/evidence-map.md)",
                "- [Glossary](glossary.md)",
                "",
                "## LLM Study Prompts",
                "",
                "- Build a compact cheat sheet for Python fundamentals in your own words.",
                "- Connect session concepts to each assignment and project artifact.",
                "- Produce a concise exam revision sheet from all notes.",
            ]
        ),
    )


def update_indexes(lecture_count: int, notebook_count: int, assignment_payloads: dict[str, list[dict[str, str]]]) -> None:
    assignment_links = [f"- [{name}](./{name})" for name in sorted(assignment_payloads.keys())]
    assignment_links.append("- [Evidence Map](evidence-map.md)")
    write(
        SUBJECT / "lectures" / "README.md",
        "\n".join(
            [
                "# 36122 Python Programming - Lectures",
                "",
                "Course materials, slide evidence, and curated notes.",
                "",
                "## Curated Notes",
                *(f"- [Session {session:02d} - {SESSION_TOPICS.get(session, '')}](session-{session:02d}.md)" for session in sorted(range(1, 13))),
                "",
                "## Raw Imports",
                "Raw copied files, when present, live in `raw/`.",
                f"Imported or referenced source count for this bucket: {lecture_count}",
            ]
        ),
    )
    write(
        SUBJECT / "notebooks" / "README.md",
        "\n".join(
            [
                "# 36122 Python Programming - Notebooks",
                "",
                "Notebook files, code scripts, and reproducibility notes.",
                "",
                "## Curated Notes",
                "",
                "- [Lab Notes](lab-notes.md)",
                f"- Imported notebook files: {notebook_count}",
                "",
                "## Raw Imports",
                "Raw copied files, when present, live in `raw/`.",
            ]
        ),
    )
    write(
        SUBJECT / "assignments" / "README.md",
        "\n".join(
            [
                "# 36122 Python Programming - Assignments",
                "",
                "Assessment briefs, rubric checklists, and evidence links.",
                "",
                "## Assessment Pages",
                "",
                *assignment_links,
                "",
                "## Source Count",
                "",
                f"Imported or referenced assignment source files: {sum(len(v) for v in assignment_payloads.values())}",
            ]
        ),
    )
    write(
        SUBJECT / "questions" / "README.md",
        "\n".join(
            [
                "# 36122 Python Programming - Questions",
                "",
                "Open questions, tutor prompts, quiz drills, and exam practice.",
                "",
                "## Curated Questions",
                "",
                "- [Revision Questions](revision-questions.md)",
                "",
                "## Raw Imports",
                "",
                "Raw copied files, when present, live in `raw/`.",
            ]
        ),
    )


def write_subject_readme(lecture_sources: dict[int, list[dict[str, str]]], notebook_sources: dict[int, list[dict[str, str]]], assignment_payloads: dict[str, list[dict[str, str]]]) -> None:
    lecture_count = sum(len(v) for v in lecture_sources.values())
    notebook_count = sum(len(v) for v in notebook_sources.values())
    assignment_rows = sorted(assignment_payloads)
    write(
        SUBJECT / "README.md",
        "\n".join(
            [
                "# 36122 Python Programming",
                "",
                "Semester: [Sem1 2025 Autumn](../../01-semesters/sem1-2025-autumn.md)",
                "Source folder: `/Users/tuanm.nguyen/Library/CloudStorage/GoogleDrive-tuannm3812@gmail.com/My Drive/01_Study/0. Master/6. UTS Drive/Sem1_2025 Autumn/36122 Python Programming`",
                "",
                "## Folder Convention",
                "",
                "- `lectures/`: weekly lecture summaries and extracted concepts",
                "- `assignments/`: assessment briefs, rubric checklists, evidence maps",
                "- `notebooks/`: notebook explanations, code review notes, reproducibility evidence",
                "- `sources/`: source-file inventories and reading notes tied to this subject",
                "- `questions/`: exam drills, open questions, and tutor prompts",
                "",
                "## What This Subject Is About",
                "",
                "- Python foundations and programming habits.",
                "- Data processing, file workflows, scraping, and plotting.",
                "",
                "## Source Subfolders",
                "",
                "- `materials`",
                "- `assignment`",
                "- `notebooks`",
                "",
                "## Key Concepts",
                "",
                "- [Python](../../03-shared-concepts/python.md)",
                "- [Programming Fundamentals](../../03-shared-concepts/programming.md)",
                "- [Data Science Workflow](../../03-shared-concepts/data-science-workflow.md)",
                "",
                "## Assessments",
                "",
                "| Assessment | Due Date | Weight | Status | Notes |",
                "|---|---:|---:|---|---|",
                *[f"| {name} |  |  | Draft created | Evidence pages are linked. |" for name in assignment_rows],
                "",
                "## LLM Tutor Prompts",
                "",
                "- Explain this code with edge-case checks.",
                "- Find bugs, assumptions, and hidden constraints.",
                "- Generate short exercises for each session.",
                "",
                "## Curated Study Layer",
                "",
                "- [Learning Map](learning-map.md)",
                "- [Assignments](assignments/README.md)",
                "- [Revision Questions](questions/revision-questions.md)",
                "- [Glossary](glossary.md)",
                "",
                "## Import Summary",
                "",
                f"- Copied/readable files: {lecture_count + notebook_count + sum(len(v) for v in assignment_payloads.values())}",
                "- Referenced large or binary files: 2",
                "- Source inventory: [sources/drive-source-inventory.md](sources/drive-source-inventory.md)",
            ]
        ),
    )


def main() -> None:
    lecture_sources, notebook_sources, assignment_payloads = collect()
    all_payloads = [item for items in lecture_sources.values() for item in items]
    all_payloads += [item for items in notebook_sources.values() for item in items]
    all_payloads += [item for items in assignment_payloads.values() for item in items]

    for session, items in sorted(lecture_sources.items()):
        write_session_note(session, items)
    write_glossary(all_payloads)
    write_assignment_pages(assignment_payloads)
    write_evidence_map(lecture_sources, assignment_payloads)
    write_questions()
    write_notebook_notes(notebook_sources)
    update_learning_map(lecture_sources, notebook_sources, assignment_payloads)
    update_indexes(
        lecture_count=sum(len(v) for v in lecture_sources.values()),
        notebook_count=sum(len(v) for v in notebook_sources.values()),
        assignment_payloads=assignment_payloads,
    )
    write_subject_readme(lecture_sources, notebook_sources, assignment_payloads)
    print(f"Generated 36122 Python Programming notes for {len(lecture_sources)} sessions and {sum(len(v) for v in notebook_sources.values())} notebooks.")


if __name__ == "__main__":
    main()
