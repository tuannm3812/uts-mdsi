from __future__ import annotations

import re
from collections import Counter, defaultdict
from pathlib import Path

import nbformat
from pypdf import PdfReader

REPO_ROOT = Path(__file__).resolve().parents[1]
SUBJECT = REPO_ROOT / "llm-wiki" / "02-subjects" / "36121-artificial-intelligence-principles-and-applications"
LECTURE_RAW = SUBJECT / "lectures" / "raw"
NOTES_RAW = SUBJECT / "notebooks" / "raw"
ASSIGNMENTS_RAW = SUBJECT / "assignments" / "raw" / "assignments"
SOURCE_RAW = SUBJECT / "sources" / "raw"

SESSION_TOPICS = {
    1: "General problem solving and search",
    2: "Decision making and constraint-driven reasoning",
    3: "Logic, representation, and structural AI",
    4: "Probabilistic reasoning and Bayesian models",
    5: "Neural methods for classification and pattern extraction",
    6: "Learning, uncertainty, and planning",
    7: "Reinforcement learning and multilayer networks",
    8: "Applied AI systems and real-world case studies",
    9: "Systems integration and practice",
    10: "Practice and capstone preparation",
}

SESSION_OBJECTIVES = {
    1: [
        "Explain problem formalisation and solution search strategies.",
        "Identify assumptions and limitations in early AI problem models.",
    ],
    2: [
        "Compare deterministic and stochastic decision methods.",
        "Evaluate when a heuristic approach is more appropriate than exhaustive search.",
    ],
    3: [
        "Explain knowledge representation choices for decision problems.",
        "Trace how symbolic models map to rule-based inference.",
    ],
    4: [
        "Interpret Bayesian and probabilistic reasoning from visual and notebook evidence.",
        "Describe how uncertainty is represented and updated.",
    ],
    5: [
        "Connect neural methods to practical classification and ranking tasks.",
        "Check where interpretation limitations might affect deployment decisions.",
    ],
    6: [
        "Frame tasks with uncertainty and trade-offs.",
        "Identify where planning, inference, and evaluation should sit in a pipeline.",
    ],
    7: [
        "Summarise reinforcement-style learning workflows and model fit risks.",
        "Explain value estimation, exploration, and stability concerns.",
    ],
    8: [
        "Map AI techniques to real-world application constraints.",
        "Evaluate safety, bias, and robustness assumptions.",
    ],
    9: [
        "Synthesize techniques from the course into a decision-ready workflow.",
        "Prepare assessment-ready evidence and rationale.",
    ],
    10: [
        "Use review sessions to consolidate concepts, workflows, and evaluation criteria.",
    ],
}

CONCEPTS = {
    "search": ["search", "heuristic", "heuristics", "path", "state", "goal"],
    "problem solving": ["problem", "search problem", "solution", "tree", "graph"],
    "knowledge representation": ["knowledge", "representation", "ontology", "symbolic", "logic"],
    "reasoning": ["reasoning", "inference", "rule", "forward", "backward"],
    "bayesian": ["bayesian", "bayes", "prior", "posterior", "likelihood", "evidence"],
    "probability": ["probability", "probabilistic", "uncertainty"],
    "neural network": ["neural", "network", "cnn", "layer", "activation", "backprop"],
    "reinforcement learning": ["reinforcement", "reward", "policy", "agent", "environment", "q-learning", "value"],
    "machine learning": ["machine", "learning", "train", "validation", "metric"],
    "classification": ["classification", "classifier", "accuracy", "recall", "precision", "f1", "confusion"],
    "clustering": ["clustering", "cluster"],
    "graph": ["graph", "node", "edge", "network", "path"],
    "evaluation": ["evaluation", "validation", "metric", "accuracy", "f1", "auc", "precision", "recall"],
    "fairness": ["bias", "fairness", "equity", "responsible", "ethics", "safety"],
}

DEFINITIONS = {
    "search": "Systematic exploration of possible states or solutions with constraints and evaluation rules.",
    "problem solving": "The process of transforming a real task into formal states, actions, and goal conditions.",
    "knowledge representation": "How facts, rules, and structure are encoded so software can reason about a domain.",
    "reasoning": "Using stored knowledge and rules to derive new facts or action choices.",
    "bayesian": "A probability-based framework for updating belief when new evidence appears.",
    "probability": "Quantifying uncertainty about likely outcomes or hidden states.",
    "neural network": "Layered computational models that learn representations and mappings from data.",
    "reinforcement learning": "Learning by feedback, where an agent improves actions from rewards and penalties.",
    "machine learning": "Algorithms that improve performance on tasks through patterns in data.",
    "classification": "Predicting discrete categories or classes for each input sample.",
    "clustering": "Grouping similar examples without explicit labels.",
    "graph": "A structure of connected nodes used to represent relationships.",
    "evaluation": "Assessing whether model behavior meets task goals and constraints.",
    "fairness": "Reducing avoidable bias and inequity in AI outputs and decisions.",
}


def clean_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def extract_pdf(path: Path, max_chars: int = 14000) -> str:
    try:
        reader = PdfReader(str(path))
        return clean_text("\n".join((page.extract_text() or "") for page in reader.pages[:16]))[:max_chars]
    except Exception as exc:
        return f"[PDF extraction failed: {exc}]"


def extract_notebook(path: Path, max_chars: int = 14000) -> str:
    try:
        nb = nbformat.read(path, as_version=4)
        chunks: list[str] = []
        for cell in nb.cells:
            source = str(cell.source)
            if cell.cell_type == "markdown":
                chunks.append(source)
            elif cell.cell_type == "code":
                imports = "\n".join(line for line in source.splitlines() if line.startswith(("import ", "from ")))
                comments = "\n".join(
                    line.strip("# ")
                    for line in source.splitlines()
                    if line.strip().startswith("#")
                )
                if imports:
                    chunks.append("Code imports:\n" + imports)
                if comments:
                    chunks.append(comments)
        return clean_text("\n".join(chunks))[:max_chars]
    except Exception as exc:
        return f"[Notebook extraction failed: {exc}]"


def extract_text(path: Path) -> tuple[str, str]:
    suffix = path.suffix.lower()
    if suffix == ".pdf":
        return "pdf", extract_pdf(path)
    if suffix == ".ipynb":
        return "notebook", extract_notebook(path)
    if suffix in {".md", ".txt"}:
        return suffix.lstrip("."), clean_text(path.read_text(encoding="utf-8", errors="ignore"))
    if suffix == ".csv":
        return "csv", clean_text(path.read_text(encoding="utf-8", errors="ignore"))[:4000]
    return "file", f"[Unsupported file: {path.name}]"


def session_from_path(path: Path) -> int | None:
    text = path.name.lower()
    for pattern in (r"session[_\s-]*(\d+)", r"session\s+(\d+)", r"module[_\s-]*(\d+)", r"module\s+(\d+)"):
        match = re.search(pattern, text, flags=re.I)
        if match:
            value = int(match.group(1))
            if 1 <= value <= 10:
                return value
    return None


def collect_sources() -> tuple[dict[int, list[dict[str, str]]], dict[str, list[dict[str, str]]], list[dict[str, str]]]:
    lecture_sources: dict[int, list[dict[str, str]]] = defaultdict(list)
    notebook_sources: dict[int, list[dict[str, str]]] = defaultdict(list)
    assignments: dict[str, list[dict[str, str]]] = defaultdict(list)
    all_raw_items: list[dict[str, str]] = []

    for path in sorted(LECTURE_RAW.rglob("*")):
        if not path.is_file():
            continue
        if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".svg", ".gif"}:
            continue
        source_type, text = extract_text(path)
        item = {"path": str(path.relative_to(SUBJECT)), "type": source_type, "text": text}
        all_raw_items.append(item)
        session = session_from_path(path)
        if session:
            if "materials" in path.parts or "materials" in str(path).lower() or source_type == "pdf":
                lecture_sources[session].append(item)
            elif "notes" in path.parts or "ai_notes" in str(path):
                lecture_sources[session].append(item)
            else:
                lecture_sources[session].append(item)
        elif "notes" in str(path).lower():
            lecture_sources[10].append(item)

    for path in sorted(NOTES_RAW.rglob("*.ipynb")):
        source_type, text = extract_text(path)
        item = {"path": str(path.relative_to(SUBJECT)), "type": source_type, "text": text}
        all_raw_items.append(item)
        session = session_from_path(path)
        if session:
            notebook_sources[session].append(item)
        else:
            notebook_sources[1].append(item)

    for path in sorted(ASSIGNMENTS_RAW.rglob("*")):
        if not path.is_file():
            continue
        source_type, text = extract_text(path)
        item = {"path": str(path.relative_to(SUBJECT)), "type": source_type, "text": text}
        lower_name = path.as_posix().lower()
        if "ai_at1" in lower_name or "/ai_at1/" in lower_name:
            assignments["01"].append(item)
        elif "ai_at3" in lower_name or "/ai_at3/" in lower_name:
            assignments["03"].append(item)
        elif "assignment 1" in lower_name or "assignment-1" in lower_name:
            assignments["01"].append(item)
        elif "assignment-3" in lower_name or "assignment 3" in lower_name or "at3" in lower_name:
            assignments["03"].append(item)

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
        "this", "that", "with", "from", "have", "will", "their", "there", "these", "what", "when", "where",
        "about", "which", "using", "their", "model", "models", "session", "value",
    }
    counts = Counter(w for w in words if w not in stop)
    return [word for word, _ in counts.most_common(n)]


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
                "subject: 36121-artificial-intelligence-principles-and-applications",
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
                "This is a first-pass curated note generated from copied lectures and notebooks. Verify details against source files before using this for assessment.",
                "",
                "## Study Objectives",
                "",
                bullet(SESSION_OBJECTIVES.get(session, ["Extract key learning points and map them to assessment tasks."])),
                "",
                "## Likely Concepts",
                "",
                "\n".join(concept_lines[:9]) or "- To be confirmed from source review.",
                "",
                "## Extracted Keywords",
                "",
                bullet(top_keywords(merged)),
                "",
                "## What To Understand",
                "",
                "- What problem each method is solving and what assumptions are made.",
                "- How uncertainty, evidence, and constraints shape model choice.",
                "- Where evaluation signals are strongest and where they can mislead.",
                "- Which source details are exam-relevant.",
                "",
                "## Assessment Relevance",
                "",
                "- Map this session to AT1/AT3 evidence using the evidence map.",
                "- Note claims that should be cross-checked against notebooks and outputs.",
                "",
                "## Revision Questions",
                "",
                "- What is the session’s main AI method and where does it fail?",
                "- Which assumptions are explicit versus implicit?",
                "- How would you validate this session’s outputs on a new problem?",
                "",
                "## LLM Follow-Up Prompt",
                "",
                "Using the source files listed above, expand this draft into a concise exam-ready note with examples, trade-offs, and a short evidence checklist.",
            ]
        ),
    )


def write_glossary(all_payloads: list[dict[str, str]]) -> None:
    merged = "\n".join(item["text"] for item in all_payloads)
    rows = [
        f"| {concept} | {count} | {DEFINITIONS.get(concept, 'Add verified definition from source material.')} |"
        for concept, count in score_concepts(merged).most_common()
        if count > 0
    ]
    write(
        SUBJECT / "glossary.md",
        "\n".join(
            [
                "---",
                "type: glossary",
                "subject: 36121-artificial-intelligence-principles-and-applications",
                "status: draft",
                "---",
                "",
                "# 36121 Artificial Intelligence Principles and Applications - Glossary",
                "",
                "| Term | Evidence Count | Working Definition |",
                "|---|---:|---|",
            ]
            + rows
            + [
                "",
                "## Maintenance",
                "",
                "- Replace working definitions with validated formulas, assumptions, and examples.",
                "- Link durable terms to [Artificial Intelligence](../../03-shared-concepts/artificial-intelligence.md),",
                "  [Machine Learning](../../03-shared-concepts/machine-learning.md), and [Statistics](../../03-shared-concepts/statistics.md).",
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
        if line.startswith("| already-copied") or line.startswith("| referenced-large-file"):
            parts = [col.strip() for col in line.strip().strip("|").split("|")]
            if len(parts) >= 4:
                bucket = parts[1].lower()
                total[bucket] += 1
    return {k: total.get(k, 0) for k in default_counts}


def write_evidence_map(lecture_sources: dict[int, list[dict[str, str]]], assignment_payloads: dict[str, list[dict[str, str]]]) -> None:
    session_rows = "\n".join(
        f"| Session {session:02d} | {SESSION_TOPICS.get(session, '')} | {len(sources)} | [note](../lectures/session-{session:02d}.md) |"
        for session, sources in sorted(lecture_sources.items())
    )
    assignment_rows = "\n".join(
        f"| AT{int(at)} | {len(assignment_payloads.get(at, []))} source files | [AT{int(at)}](../assignments/at{int(at)}.md) |"
        for at in ["01", "03"]
    )
    write(
        SUBJECT / "assignments" / "evidence-map.md",
        "\n".join(
            [
                "---",
                "type: evidence-map",
                "subject: 36121-artificial-intelligence-principles-and-applications",
                "status: draft",
                "---",
                "",
                "# 36121 Artificial Intelligence Principles and Applications - Evidence Map",
                "",
                "## Session Evidence",
                "",
                "| Session | Topic | Source Count | Curated Note |",
                "|---|---|---:|---|",
                session_rows,
                "",
                "## Assessment Evidence",
                "",
                "| Assessment | Source File Count | Curated Task Note |",
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
                "subject: 36121-artificial-intelligence-principles-and-applications",
                "code: 36121",
                "status: draft",
                "---",
                "",
                "# 36121 Artificial Intelligence Principles and Applications - Revision Questions",
                "",
                "## Conceptual Questions",
                "",
                "- How does the same AI task change when uncertainty is introduced?",
                "- When is a symbolic approach preferable to a statistical approach?",
                "- What does a Bayesian model add that a deterministic rule approach cannot provide?",
                "- Compare search-based and learning-based reasoning for a task with incomplete data.",
                "- Why do real-world constraints often dominate purely technical performance goals?",
                "",
                "## Applied Questions",
                "",
                "- Build a high-level workflow for AT1 using one source notebook and two lecture notes.",
                "- Choose two AI techniques from different sessions and map each to a concrete use case.",
                "- Propose an AT3 evaluation checklist for model outputs and decision fairness.",
                "",
                "## Technical Questions",
                "",
                "- Which notebook signals best indicate reproducibility risk?",
                "- What are the most common validity threats in the provided assessment code?",
                "- How would you check for data leakage or label noise in the shared materials?",
                "",
                "## LLM Drill Prompt",
                "",
                "Generate:",
                "- a 12-question exam drill set grouped by conceptual/applied/technical,",
                "- concise answer notes for each question,",
                "- and an evidence-linked revision checklist.",
            ]
        ),
    )


def assignment_rows(assignments: list[dict[str, str]]) -> list[str]:
    return [f"- `{item['path']}` ({item['type']})" for item in sorted(assignments, key=lambda item: item["path"])] or ["- No files copied."]


def write_assignment_pages(assignment_payloads: dict[str, list[dict[str, str]]]) -> None:
    for at_code in ("01", "03"):
        payload = assignment_payloads.get(at_code, [])
        title = "AT1" if at_code == "01" else "AT3"
        write(
            SUBJECT / "assignments" / f"at{int(at_code)}.md",
            "\n".join(
                [
                    "---",
                    "type: assessment",
                    "subject: 36121-artificial-intelligence-principles-and-applications",
                    f"code: 36121",
                    "status: planning",
                    "---",
                    "",
                    f"# 36121 {title} - Assessment Draft",
                    "",
                    "## Official Task Evidence",
                    "",
                    f"Mapped source files copied into `assignments/raw/assignments/AI_at{int(at_code)}/`.",
                    "",
                    "## Raw Source Files",
                    "",
                    *assignment_rows(payload),
                    "",
                    "## Rubric Checklist",
                    "",
                    "- [ ] Task requirements are fully interpreted and split into subtasks.",
                    "- [ ] Data/code evidence is linked to each claim.",
                    "- [ ] Results include methodology, assumptions, and limitations.",
                    "- [ ] Ethics and safety checks are explicit.",
                    "- [ ] Submission format constraints are verified.",
                    "",
                    "## Working Plan",
                    "",
                    "| Step | Output | Status |",
                    "|---|---|---|",
                    "| Understand task | Task paraphrase and success criteria | Not started |",
                    "| Map evidence | Linked session and notebook files | Not started |",
                    "| Draft response | First full draft | Not started |",
                    "| Self-review | Rubric-based self-check | Not started |",
                    "| Finalise | Revision-ready artifact | Not started |",
                    "",
                    "## LLM Review Prompt",
                    "",
                    "Act as a strict marker. Review the draft against the official task and rubric. Highlight missing requirements, weak evidence, and concrete edits.",
                ]
            ),
        )


def write_notebook_notes(notebook_sources: dict[int, list[dict[str, str]]]) -> None:
    rows = []
    for session in sorted(notebook_sources):
        rows.append(f"- Session {session:02d}: {len(notebook_sources[session])} notebook files")
    write(
        SUBJECT / "notebooks" / "lab-notes.md",
        "\n".join(
            [
                "---",
                "type: notebook-notes",
                "subject: 36121-artificial-intelligence-principles-and-applications",
                "status: draft",
                "---",
                "",
                "# 36121 Artificial Intelligence Principles and Applications - Lab Notes",
                "",
                "## Notebook Evidence Summary",
                "",
                "This file tracks notebook-heavy evidence for reproducibility and implementation detail.",
                "",
                "### Grouped Notebooks",
                "",
                *rows,
                "",
                "## Key Notebook Files",
                "",
                "- " + "\n- ".join(
                    f"`{item['path']}` ({item['type']})" for item in sorted(
                        [item for items in notebook_sources.values() for item in items],
                        key=lambda item: item["path"],
                    )
                )
                if any(item for items in notebook_sources.values() for item in items)
                else "No notebook files detected.",
                "",
                "## Practical Note",
                "",
                "- Prefer extracting reproducible blocks (imports, seeds, splits, metrics) into session notes.",
                "- Keep notebook evidence in sync with lecture claims and assessment notes.",
            ]
        ),
    )


def update_learning_map(
    lecture_sources: dict[int, list[dict[str, str]]],
    notebook_sources: dict[int, list[dict[str, str]]],
    assignment_payloads: dict[str, list[dict[str, str]]],
) -> None:
    manifest_counts = read_manifest_counts()
    lecture_files = [item["path"] for bucket in [lecture_sources.get(i, []) for i in sorted(lecture_sources)] for item in bucket]
    assignment_files = [item["path"] for at in ["01", "03"] for item in assignment_payloads.get(at, [])]
    notebook_files = sorted([item["path"] for session in sorted(lecture_sources) for item in []])

    lines = [
        "---",
        "type: learning-map",
        "subject: 36121-artificial-intelligence-principles-and-applications",
        "code: 36121",
        "semester: Sem3 2026 Autumn",
        "status: active",
        "---",
        "",
        "# 36121 Artificial Intelligence Principles and Applications - Learning Map",
        "",
        "## Purpose",
        "",
        "Use this page as the curated entry point for the subject. Raw copied files are useful evidence, but this page should become the LLM-friendly map of what matters.",
        "",
        "## Core Focus",
        "",
        "- AI problem formulation and symbolic approaches.",
        "- Probabilistic and deep methods for inference and pattern learning.",
        "- AI applications, limitations, and assessment evidence mapping.",
        "- Reproducibility and implementation quality.",
        "",
        "## Connected Concepts",
        "",
        "- [Artificial Intelligence](../../03-shared-concepts/artificial-intelligence.md)",
        "- [Machine Learning](../../03-shared-concepts/machine-learning.md)",
        "- [Statistics](../../03-shared-concepts/statistics.md)",
        "",
        "## Study Workflow",
        "",
        "1. Review the weekly lecture material in [lectures](lectures/README.md).",
        "2. Convert session source material into concise notes and concept summaries.",
        "3. Link durable ideas to shared concepts and assessment requirements.",
        "4. Track assessment evidence in [assignments](assignments/evidence-map.md).",
        "5. Use notebook summaries for reproducibility details in [notebooks](notebooks/lab-notes.md).",
        "6. Use [revision questions](questions/revision-questions.md) for drill and retrieval.",
        "",
        "## Imported Source Profile",
        "",
        "| Bucket | Source Count |",
        "|---|---:|",
        f"| Lectures | {manifest_counts.get('lectures', len(lecture_files))} |",
        f"| Assignments | {manifest_counts.get('assignments', len(assignment_files))} |",
        f"| Notebooks | {manifest_counts.get('notebooks', 0)} |",
        f"| Sources | {manifest_counts.get('sources', 0)} |",
        "",
        "## Key Raw Files To Triage",
        "",
        "### Lectures",
        "",
    ]
    lines.extend(f"- {item['path']}" for item in sorted([item for items in lecture_sources.values() for item in items], key=lambda item: item["path"])[:24])
    lines.extend(["", "### Assignments", ""])
    if assignment_files:
        lines.extend(f"- {name}" for name in assignment_files)
    else:
        lines.append("- No copied assignment files detected.")
    lines.extend(["", "### Notebooks", ""])
    notebook_paths = sorted([item["path"] for items in notebook_sources.values() for item in items], key=str)
    if notebook_paths:
        lines.extend(f"- {name}" for name in notebook_paths[:24])
    else:
        lines.append("- No copied notebook files detected.")
    lines.extend(
        [
            "",
            "## Assessment Links",
            "",
            "- [AT1](assignments/at1.md)",
            "- [AT3](assignments/at3.md)",
            "- [Evidence Map](assignments/evidence-map.md)",
            "",
            "## LLM Study Prompts",
            "",
            "- Summarise session notes and convert them into one-page revisions.",
            "- Build assessment-linked evidence chains from sessions to AT1 and AT3 outputs.",
            "- Highlight bias, uncertainty, and deployment constraints for applied AI tasks.",
            "",
            "## Maintenance Checklist",
            "",
            "- [ ] Weekly notes created",
            "- [ ] Assignment pages created",
            "- [x] Glossary created",
            "- [ ] Notebook notes linked to sessions",
            "- [ ] Revision questions created",
        ]
    )
    write(SUBJECT / "learning-map.md", "\n".join(lines))


def update_indexes(lecture_count: int, notebook_count: int, assignment_payloads: dict[str, list[dict[str, str]]]) -> None:
    lecture_links = []
    for session in sorted(set(range(1, 11))):
        if session <= 10:
            lecture_links.append(f"- [Session {session:02d} - {SESSION_TOPICS[session]}](session-{session:02d}.md)")
    write(
        SUBJECT / "lectures" / "README.md",
        "\n".join(
            [
                "# 36121 Artificial Intelligence Principles And Applications - Lectures",
                "",
                "Lecture slides, lab scripts, and concise extraction notes.",
                "",
                "## Curated Notes",
                "",
                *lecture_links[:lecture_count],
                "",
                "## Raw Imports",
                "",
                "Raw copied files, when present, live in `raw/`.",
                "",
                f"Imported or referenced source count for this bucket: {lecture_count}",
            ]
        ),
    )
    write(
        SUBJECT / "notebooks" / "README.md",
        "\n".join(
            [
                "# 36121 Artificial Intelligence Principles And Applications - Notebooks",
                "",
                "Notebook files, code walkthroughs, and reproducibility notes.",
                "",
                "## Curated Notes",
                "",
                "- [Lab Notes](lab-notes.md)",
                f"- Imported notebook files: {notebook_count}",
                "",
                "## Raw Imports",
                "",
                "Raw copied files, when present, live in `raw/`.",
            ]
        ),
    )
    assignment_links = "- [AT1](at1.md)\n- [AT3](at3.md)\n- [Evidence Map](evidence-map.md)"
    write(
        SUBJECT / "assignments" / "README.md",
        "\n".join(
            [
                "# 36121 Artificial Intelligence Principles and Applications - Assignments",
                "",
                "Assessment briefs, rubric checklists, and evidence links.",
                "",
                "## Assessment Pages",
                "",
                assignment_links,
                "",
                "## Standard Review Workflow",
                "",
                "1. Copy the official task and rubric into the assessment page.",
                "2. Convert the rubric into a checklist.",
                "3. Draft against the checklist.",
                "4. Ask the LLM for strict marker-style feedback.",
                "5. Verify claims, citations, code, calculations, and format requirements.",
                "",
                f"Imported or referenced source count for this bucket: {sum(len(v) for v in assignment_payloads.values())}",
                "",
                "## Raw Imports",
                "",
                f"- AT1 source files: {len(assignment_payloads.get('01', []))}",
                f"- AT3 source files: {len(assignment_payloads.get('03', []))}",
            ]
        ),
    )
    write(
        SUBJECT / "questions" / "README.md",
        "\n".join(
            [
                "# 36121 Artificial Intelligence Principles And Applications - Questions",
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
                "",
                "Imported or referenced source count for this bucket: 17",
            ]
        ),
    )


def update_subject_readme(lecture_count: int, assignment_payloads: dict[str, list[dict[str, str]]], notebook_count: int) -> None:
    write(
        SUBJECT / "README.md",
        "\n".join(
            [
                "# 36121 Artificial Intelligence Principles and Applications",
                "",
                "Semester: [Sem3 2026 Autumn](../../01-semesters/sem3-2026-autumn.md)",
                "Source folder: `/Users/tuanm.nguyen/Library/CloudStorage/GoogleDrive-tuannm3812@gmail.com/My Drive/01_Study/0. Master/6. UTS Drive/Sem3_2026 Autumn/36121 Artificial Intelligence Principles and Applications`",
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
                "- AI foundations, search, symbolic reasoning, and applied machine-learning concepts.",
                "- Evaluation under uncertainty and practical deployment constraints.",
                "",
                "## Source Subfolders",
                "",
                "- `materials`",
                "- `assignments`",
                "- `notebooks`",
                "",
                "## Key Concepts",
                "",
                "- [Artificial Intelligence](../../03-shared-concepts/artificial-intelligence.md)",
                "- [Machine Learning](../../03-shared-concepts/machine-learning.md)",
                "- [Deep Learning](../../03-shared-concepts/deep-learning.md)",
                "",
                "## Assessments",
                "",
                "| Assessment | Due Date | Weight | Status | Notes |",
                "|---|---:|---:|---|---|",
                "| AT1 |  |  | Draft created | Evidence pages are linked. |",
                "| AT3 |  |  | Draft created | Evidence pages are linked. |",
                "",
                "## LLM Tutor Prompts",
                "",
                "- Explain AI methods as a selection and evaluation workflow.",
                "- Build evidence links from lectures and notebooks to each AT.",
                "- Generate short viva-style questions per topic cluster.",
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
                "- Referenced large or binary files: 1",
                "- Source inventory: [sources/drive-source-inventory.md](sources/drive-source-inventory.md)",
            ]
        ),
    )


def main() -> None:
    lecture_sources, notebook_sources, assignment_payloads = collect_sources()

    all_payloads: list[dict[str, str]] = [item for group in lecture_sources.values() for item in group]
    all_payloads += [item for items in notebook_sources.values() for item in items]
    all_payloads += [item for items in assignment_payloads.values() for item in items]

    session_count = 0
    for session, items in sorted(lecture_sources.items()):
        write_session_note(session, items)
        session_count += 1
    for session, items in sorted(notebook_sources.items()):
        if session not in lecture_sources:
            write_session_note(session, items)
            session_count += 1

    write_glossary(all_payloads)
    write_evidence_map(lecture_sources, assignment_payloads)
    write_questions()
    write_assignment_pages(assignment_payloads)
    write_notebook_notes(notebook_sources)
    write(
        SUBJECT / "assignments" / "evidence-map.md",
        (SUBJECT / "assignments" / "evidence-map.md").read_text(encoding="utf-8"),
    )
    update_learning_map(lecture_sources, notebook_sources, assignment_payloads)
    update_indexes(session_count, len([item for items in notebook_sources.values() for item in items]), assignment_payloads)
    update_subject_readme(len([item for items in lecture_sources.values() for item in items]), assignment_payloads, len([item for items in notebook_sources.values() for item in items]))
    print(f"Generated 36121 curated notes for {session_count} sessions and {len([item for items in notebook_sources.values() for item in items])} notebooks.")


if __name__ == "__main__":
    main()
