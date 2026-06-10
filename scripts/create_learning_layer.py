from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
WIKI = REPO_ROOT / "llm-wiki"
SUBJECTS_ROOT = WIKI / "02-subjects"
MANIFEST = WIKI / "00-admin" / "drive-import-manifest.csv"


SUBJECTS = {
    "36100-data-science-for-innovation": {
        "code": "36100",
        "title": "Data Science for Innovation",
        "semester": "Sem1 2025 Autumn",
        "focus": [
            "Data science problem framing",
            "Innovation-oriented analysis",
            "Evidence-based recommendations",
            "Communication of insight",
        ],
        "concepts": [
            "../../03-shared-concepts/data-science-workflow.md",
            "../../03-shared-concepts/research-methods.md",
            "../../03-shared-concepts/data-visualisation.md",
        ],
    },
    "36103-statistical-thinking-for-data-science": {
        "code": "36103",
        "title": "Statistical Thinking for Data Science",
        "semester": "Sem2 2025 Spring",
        "focus": [
            "Statistical reasoning under uncertainty",
            "Sampling, inference, and assumptions",
            "Model interpretation",
            "Evidence strength and limitations",
        ],
        "concepts": [
            "../../03-shared-concepts/statistics.md",
            "../../03-shared-concepts/research-methods.md",
            "../../03-shared-concepts/data-science-workflow.md",
        ],
    },
    "36104-data-visualisation-and-narratives": {
        "code": "36104",
        "title": "Data Visualisation and Narratives",
        "semester": "Sem3 2026 Autumn",
        "focus": [
            "Visual encoding choices",
            "Narrative structure",
            "Chart critique",
            "Evidence-backed communication",
        ],
        "concepts": [
            "../../03-shared-concepts/data-visualisation.md",
            "../../03-shared-concepts/data-science-workflow.md",
            "../../03-shared-concepts/academic-integrity.md",
        ],
    },
    "36106-machine-learning-algorithms-and-applications": {
        "code": "36106",
        "title": "Machine Learning Algorithms and Applications",
        "semester": "Sem1 2025 Autumn",
        "focus": [
            "Supervised and unsupervised learning",
            "Model evaluation",
            "Feature engineering and preprocessing",
            "Applied machine learning workflows",
        ],
        "concepts": [
            "../../03-shared-concepts/machine-learning.md",
            "../../03-shared-concepts/statistics.md",
            "../../03-shared-concepts/python.md",
        ],
    },
    "36118-applied-natural-language-processing": {
        "code": "36118",
        "title": "Applied Natural Language Processing",
        "semester": "Sem4 2026 Spring",
        "focus": [
            "Text preprocessing and representation",
            "Classical and neural NLP",
            "Language model evaluation",
            "Applied NLP pipelines",
        ],
        "concepts": [
            "../../03-shared-concepts/natural-language-processing.md",
            "../../03-shared-concepts/machine-learning.md",
            "../../03-shared-concepts/deep-learning.md",
        ],
    },
    "36120-advanced-machine-learning-application": {
        "code": "36120",
        "title": "Advanced Machine Learning Application",
        "semester": "Sem2 2025 Spring",
        "focus": [
            "Advanced model selection",
            "Experiment design",
            "Operational ML application",
            "Evaluation and deployment tradeoffs",
        ],
        "concepts": [
            "../../03-shared-concepts/machine-learning.md",
            "../../03-shared-concepts/deep-learning.md",
            "../../03-shared-concepts/statistics.md",
        ],
    },
    "36121-artificial-intelligence-principles-and-applications": {
        "code": "36121",
        "title": "Artificial Intelligence Principles and Applications",
        "semester": "Sem3 2026 Autumn",
        "focus": [
            "AI problem formulation",
            "Search, reasoning, and learning",
            "Applied AI systems",
            "Responsible evaluation of AI outputs",
        ],
        "concepts": [
            "../../03-shared-concepts/artificial-intelligence.md",
            "../../03-shared-concepts/machine-learning.md",
            "../../03-shared-concepts/deep-learning.md",
        ],
    },
    "36122-python-programming": {
        "code": "36122",
        "title": "Python Programming",
        "semester": "Sem1 2025 Autumn",
        "focus": [
            "Python syntax and control flow",
            "Data structures and functions",
            "Notebook-based analysis",
            "Debugging and reproducibility",
        ],
        "concepts": [
            "../../03-shared-concepts/python.md",
            "../../03-shared-concepts/data-science-workflow.md",
            "../../03-shared-concepts/academic-integrity.md",
        ],
    },
    "43008-reinforcement-learning": {
        "code": "43008",
        "title": "Reinforcement Learning",
        "semester": "Sem4 2026 Spring",
        "focus": [
            "Sequential decision-making",
            "Policies, rewards, and value functions",
            "Exploration and exploitation",
            "RL algorithms and evaluation",
        ],
        "concepts": [
            "../../03-shared-concepts/reinforcement-learning.md",
            "../../03-shared-concepts/artificial-intelligence.md",
            "../../03-shared-concepts/machine-learning.md",
        ],
    },
    "94691-deep-learning": {
        "code": "94691",
        "title": "Deep Learning",
        "semester": "Sem3 2026 Autumn",
        "focus": [
            "Neural network architectures",
            "Training, regularisation, and optimisation",
            "Computer vision and representation learning",
            "Model diagnostics and experiment tracking",
        ],
        "concepts": [
            "../../03-shared-concepts/deep-learning.md",
            "../../03-shared-concepts/machine-learning.md",
            "../../03-shared-concepts/python.md",
        ],
    },
    "94692-data-science-practice": {
        "code": "94692",
        "title": "Data Science Practice",
        "semester": "Sem3 2026 Autumn",
        "focus": [
            "End-to-end data science projects",
            "Stakeholder framing",
            "Evidence quality and limitations",
            "Professional data science communication",
        ],
        "concepts": [
            "../../03-shared-concepts/data-science-workflow.md",
            "../../03-shared-concepts/research-methods.md",
            "../../03-shared-concepts/assessment-strategy.md",
        ],
    },
    "94693-big-data-engineering": {
        "code": "94693",
        "title": "Big Data Engineering",
        "semester": "Sem2 2025 Spring",
        "focus": [
            "Data pipelines and storage",
            "Distributed processing",
            "Batch and streaming tradeoffs",
            "Reliability and scalability",
        ],
        "concepts": [
            "../../03-shared-concepts/big-data.md",
            "../../03-shared-concepts/data-science-workflow.md",
            "../../03-shared-concepts/python.md",
        ],
    },
    "genai": {
        "code": "GENAI",
        "title": "GenAI",
        "semester": "Sem4 2026 Spring",
        "focus": [
            "Generative AI workflows",
            "Prompting and retrieval",
            "Evaluation of generated outputs",
            "Responsible AI use",
        ],
        "concepts": [
            "../../03-shared-concepts/artificial-intelligence.md",
            "../../03-shared-concepts/natural-language-processing.md",
            "../../03-shared-concepts/prompt-library.md",
        ],
    },
}


def read_manifest() -> tuple[dict[str, Counter], dict[str, list[dict[str, str]]]]:
    counts: dict[str, Counter] = defaultdict(Counter)
    rows: dict[str, list[dict[str, str]]] = defaultdict(list)
    with MANIFEST.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            subject = row["repo_subject"]
            counts[subject][row["target_bucket"]] += 1
            counts[subject][row["status"]] += 1
            rows[subject].append(row)
    return counts, rows


def source_name(path: str) -> str:
    return Path(path).name


def detect_assessments(rows: list[dict[str, str]]) -> list[str]:
    names = []
    seen = set()
    patterns = [
        re.compile(r"\b(at\s*[\-_ ]?\d+)\b", re.I),
        re.compile(r"\b(assignment\s*[\-_ ]?\d+)\b", re.I),
        re.compile(r"\b(assessment\s*[\-_ ]?\d+)\b", re.I),
    ]
    for row in rows:
        if row["target_bucket"] != "assignments":
            continue
        text = row["source_file"]
        for pattern in patterns:
            match = pattern.search(text)
            if not match:
                continue
            label = re.sub(r"[\s_]+", "-", match.group(1).lower())
            label = label.replace("assignment-", "assignment-").replace("assessment-", "assessment-")
            if label not in seen:
                seen.add(label)
                names.append(label)
    return names[:6]


def top_files(rows: list[dict[str, str]], bucket: str, limit: int = 8) -> list[str]:
    selected = [
        row for row in rows
        if row["target_bucket"] == bucket and row["status"] in {"copied", "already-copied"}
    ]
    selected.sort(key=lambda r: int(r["bytes_copied"]), reverse=True)
    return [source_name(row["source_file"]) for row in selected[:limit]]


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def concept_links(concepts: list[str]) -> str:
    return "\n".join(f"- [{Path(c).stem.replace('-', ' ').title()}]({c})" for c in concepts)


def bullet_list(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)


def main() -> None:
    counts, rows_by_subject = read_manifest()

    for slug, data in SUBJECTS.items():
        subject_dir = SUBJECTS_ROOT / slug
        rows = rows_by_subject.get(slug, [])
        count = counts.get(slug, Counter())
        assessments = detect_assessments(rows)
        learning_map_assessment_links = [
            f"- [{name.upper().replace('-', ' ')}](assignments/{name}.md)"
            for name in assessments
        ]
        assignment_dashboard_links = [
            f"- [{name.upper().replace('-', ' ')}]({name}.md)"
            for name in assessments
        ]
        if not learning_map_assessment_links:
            learning_map_assessment_links = ["- [Assessment Planning](assignments/assessment-planning.md)"]
            assignment_dashboard_links = ["- [Assessment Planning](assessment-planning.md)"]

        write(
            subject_dir / "learning-map.md",
            f"""---
type: learning-map
subject: {slug}
code: {data['code']}
semester: {data['semester']}
status: active
---

# {data['code']} {data['title']} - Learning Map

## Purpose

Use this page as the curated entry point for the subject. Raw copied files are useful evidence, but this page should become the LLM-friendly map of what matters.

## Core Focus

{bullet_list(data['focus'])}

## Connected Concepts

{concept_links(data['concepts'])}

## Study Workflow

1. Review the weekly lecture material in [lectures](lectures/README.md).
2. Convert important source material into concise Markdown notes.
3. Link durable ideas to shared concepts.
4. Track assessment requirements in [assignments](assignments/README.md).
5. Use [questions](questions/README.md) for exam drills and unresolved questions.

## Imported Source Profile

| Bucket | Source Count |
|---|---:|
| Lectures | {count.get('lectures', 0)} |
| Assignments | {count.get('assignments', 0)} |
| Notebooks | {count.get('notebooks', 0)} |
| Sources | {count.get('sources', 0)} |

## Key Raw Files To Triage

### Lectures

{bullet_list(top_files(rows, 'lectures') or ['No copied lecture files detected.'])}

### Assignments

{bullet_list(top_files(rows, 'assignments') or ['No copied assignment files detected.'])}

### Notebooks

{bullet_list(top_files(rows, 'notebooks') or ['No copied notebook files detected.'])}

## Assessment Links

{chr(10).join(learning_map_assessment_links)}

## LLM Study Prompts

- Summarise the lecture files for this subject into weekly notes, key concepts, formulas, examples, and assessment relevance.
- Build a glossary for this subject and link each term to shared concepts where possible.
- Create a revision quiz from the learning map and the curated lecture notes.
- Identify which raw files are most useful for assessment preparation and why.

## Maintenance Checklist

- [ ] Weekly notes created
- [ ] Assignment pages created
- [ ] Key notebooks explained
- [ ] Shared concepts linked
- [ ] Exam/revision questions added
""",
        )

        assignment_index = subject_dir / "assignments" / "README.md"
        existing = assignment_index.read_text(encoding="utf-8") if assignment_index.exists() else ""
        write(
            assignment_index,
            f"""# {data['code']} {data['title']} - Assignments

Assessment briefs, rubric checklists, draft reviews, and copied raw assessment files.

## Assessment Pages

{chr(10).join(assignment_dashboard_links)}

## Standard Review Workflow

1. Copy the official task and rubric into the assessment page.
2. Convert the rubric into a checklist.
3. Draft against the checklist.
4. Ask the LLM for strict marker-style feedback.
5. Verify claims, citations, code, calculations, and academic integrity requirements.

## Raw Imports

Raw copied files, when present, live in `raw/`.

Imported or referenced source count for this bucket: {count.get('assignments', 0)}

## LLM Review Prompt

Act as a strict UTS marker. Compare my draft against the official task and rubric. Return missing requirements, weak evidence, unclear reasoning, citation issues, and concrete revisions.
""",
        )

        target_assessments = assessments or ["assessment-planning"]
        for name in target_assessments:
            title = name.upper().replace("-", " ")
            write(
                subject_dir / "assignments" / f"{name}.md",
                f"""---
type: assessment
subject: {slug}
code: {data['code']}
status: planning
---

# {data['code']} {title}

## Official Task

- Source:
- Due date:
- Weight:
- Submission format:

## Rubric Checklist

- [ ] Requirement 1:
- [ ] Requirement 2:
- [ ] Requirement 3:
- [ ] Evidence and citations checked
- [ ] Code, calculations, or outputs verified
- [ ] Academic integrity requirements checked

## Working Plan

| Step | Output | Status |
|---|---|---|
| Understand task | Brief summary | Not started |
| Gather sources | Relevant raw files and notes | Not started |
| Draft | Initial response or notebook | Not started |
| Review | Rubric-based critique | Not started |
| Final check | Submission-ready work | Not started |

## LLM Review Notes


## Final Verification

- [ ] Answer addresses the task directly
- [ ] All claims are supported
- [ ] Citations are verified
- [ ] Code/notebook runs from a clean state where relevant
- [ ] Final submission matches required format
""",
            )

        write(
            subject_dir / "questions" / "revision-questions.md",
            f"""---
type: question-bank
subject: {slug}
code: {data['code']}
status: draft
---

# {data['code']} {data['title']} - Revision Questions

## Conceptual Questions

- 

## Applied Questions

- 

## Calculation Or Code Questions

- 

## LLM Drill Prompt

Create 20 questions for this subject using the learning map, lecture notes, notebooks, and assignment pages. Split them into conceptual, applied, and code/calculation questions. Provide answers separately.
""",
        )

        readme = subject_dir / "README.md"
        text = readme.read_text(encoding="utf-8")
        insert = "\n## Curated Study Layer\n\n- [Learning Map](learning-map.md)\n- [Assignment Dashboard](assignments/README.md)\n- [Revision Questions](questions/revision-questions.md)\n"
        if "## Curated Study Layer" not in text:
            parts = text.split("\n## Import Summary", 1)
            if len(parts) == 2:
                text = parts[0].rstrip() + "\n" + insert + "\n## Import Summary" + parts[1]
            else:
                text = text.rstrip() + "\n" + insert
            write(readme, text)


if __name__ == "__main__":
    main()
