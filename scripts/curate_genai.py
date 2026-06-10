from __future__ import annotations

import contextlib
import io
import re
import warnings
from collections import Counter
from pathlib import Path

from pypdf import PdfReader


REPO_ROOT = Path(__file__).resolve().parents[1]
SUBJECT = REPO_ROOT / "llm-wiki" / "02-subjects" / "genai"
SOURCE_RAW = SUBJECT / "sources" / "raw"


CONCEPTS = {
    "model evaluation": ["evaluation", "precision", "recall", "f1", "bias", "metric", "ground truth", "validation", "test set"],
    "model deployment": ["deployment", "endpoint", "serving", "latency", "throughput", "cost", "inference"],
    "prompting": ["prompt", "system prompt", "instruction", "few-shot", "chain-of-thought", "temperature", "top-p"],
    "retrieval": ["retrieval", "vector", "embedding", "chunk", "index", "search", "document"],
    "responsible ai": ["responsible", "hallucination", "safety", "privacy", "bias", "ethics", "oversight"],
    "MLOps": ["mlops", "vertex", "pipeline", "monitoring", "versioning", "ci", "cd", "registry"],
}

DEFINITIONS = {
    "model evaluation": "Systematic measurement of model behavior using validation data, metrics, and error inspection.",
    "model deployment": "Moving a trained workflow into a stable service with predictable response quality and operational controls.",
    "prompting": "Crafting instructions and context so a model returns outputs aligned with constraints.",
    "retrieval": "Finding and injecting relevant documents into prompts so generation is grounded in source evidence.",
    "responsible ai": "Designing systems to reduce harmful outputs, bias, privacy leaks, and unsafe behavior.",
    "MLOps": "Operational practices for versioning, monitoring, testing, and deploying machine learning systems.",
}


def clean(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def extract_pdf(path: Path, max_chars: int = 12000) -> str:
    try:
        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr):
            warnings.simplefilter("ignore")
            reader = PdfReader(str(path))
            return clean("\n".join((page.extract_text() or "") for page in reader.pages[:14]))[:max_chars]
    except Exception as exc:
        return f"[PDF extraction failed: {exc}]"


def score_concepts(text: str) -> Counter:
    lower = text.lower()
    scores = Counter()
    for concept, terms in CONCEPTS.items():
        for term in terms:
            scores[concept] += lower.count(term)
    return scores


def bullet(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)


def keywords(text: str, n: int = 12) -> list[str]:
    words = re.findall(r"[A-Za-z][A-Za-z0-9_+-]{3,}", text.lower())
    stop = {"this", "that", "from", "using", "their", "there", "what", "with", "these", "will", "your"}
    return [word for word, _ in Counter(w for w in words if w not in stop).most_common(n)]


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def collect_source_pdf() -> Path | None:
    pdfs = sorted(SOURCE_RAW.glob("*.pdf"))
    if not pdfs:
        return None
    return pdfs[0]


def write_session_note(source_pdf: Path) -> None:
    text = extract_pdf(source_pdf)
    sources = [f"- `{source_pdf.relative_to(SUBJECT)}` (pdf)"]
    concept_lines = [
        f"- {name}: {DEFINITIONS.get(name, 'Verify definition from source material.')}"
        for name, count in score_concepts(text).most_common()
        if count > 0
    ]
    write(
        SUBJECT / "lectures" / "session-01.md",
        f"""---
type: lecture-note
subject: genai
session: 01
status: draft
---

# Session 01 - MLOps Model Evaluation and Operational Patterns

## Source Files

{chr(10).join(sources)}

## Working Summary

This is a first-pass curated note generated from copied MLOps reading material. Verify details against source files before using it for assessment.

## Study Objectives

- Define what stable model evaluation looks like in generative systems.
- Explain where retrieval, prompts, and deployment controls can improve quality.
- Identify operational risks for model-serving and content governance.

## Likely Concepts

{chr(10).join(concept_lines) if concept_lines else '- To be confirmed from source review.'}

## Extracted Keywords

{bullet(keywords(text))}

## What To Understand

- Which metrics are appropriate for the generation task at hand.
- How evaluation should link to user-visible quality.
- What controls matter in production (versioning, prompt constraints, monitoring).
- How retrieval can reduce hallucination in enterprise workflows.

## Assessment Relevance

- Map this session to any GenAI assignment tasks requiring evaluation methodology.
- Use extracted snippets to draft checklist items for model quality and safety.

## Revision Questions

- What are the strongest indicators of a failing generative model in this module context?
- How do retrieval and prompt design interact in output quality control?
- What governance checks should be added before deployment?

## LLM Follow-Up Prompt

Using the source files listed above, expand this into a practical review note with concrete rubric-style criteria.
""",
    )


def write_questions() -> None:
    write(
        SUBJECT / "questions" / "revision-questions.md",
        """---
type: question-bank
subject: genai
code: GENAI
status: draft
---

# GENAI GenAI - Revision Questions

## Conceptual Questions

- What is the difference between model evaluation and model monitoring?
- Why can a well-scoring model still produce unsafe output in production?
- How do prompt design and retrieval each shape factual consistency?
- What is the trade-off between creativity and reliability in generative systems?
- Which risks justify stronger guardrails in enterprise GenAI deployments?

## Applied Questions

- Design a lightweight evaluation plan for a chatbot built on LLM responses.
- Describe how you would add retrieval to a model that currently hallucinates often.
- Propose a deployment checklist for a business-critical generative application.
- Build a simple rubric for grading generated text quality and safety.
- Compare a rule-based and LLM-based evaluation strategy for your context.

## Technical Questions

- Which telemetry signals would you monitor for latency spikes and regression?
- How would you version prompts, context sources, and model checkpoints?
- What validation test would you run before releasing a new prompt revision?
- How do you detect data drift affecting prompt+retrieval quality?
- Sketch a minimal MLOps pipeline for a model update from test to rollout.

## LLM Drill Prompt

Using the map and the session notes, generate:
- a concise viva exam set,
- a short answer key,
- and an improvement checklist for governance and deployment quality.
""",
    )


def update_learning_map() -> None:
    write(
        SUBJECT / "learning-map.md",
        """---
type: learning-map
subject: genai
code: GENAI
semester: Sem4 2026 Spring
status: active
---

# GENAI GenAI - Learning Map

## Purpose

Use this page as the curated entry point for the subject. Raw copied files are useful evidence, but this page should become the LLM-friendly map of what matters.

## Core Focus

- Generative AI workflows
- Prompting and retrieval
- Evaluation of generated outputs
- Responsible AI use

## Connected Concepts

- [Artificial Intelligence](../../03-shared-concepts/artificial-intelligence.md)
- [Natural Language Processing](../../03-shared-concepts/natural-language-processing.md)
- [Prompt Library](../../03-shared-concepts/prompt-library.md)

## Study Workflow

1. Review the weekly lecture material in [lectures](lectures/README.md).
2. Convert important source material into concise Markdown notes.
3. Link durable ideas to shared concepts.
4. Track assessment requirements in [assignments](assignments/README.md).
5. Use [questions](questions/README.md) for exam drills and unresolved questions.

## Imported Source Profile

| Bucket | Source Count |
|---|---:|
| Lectures | 1 |
| Assignments | 0 |
| Notebooks | 0 |
| Sources | 1 |

## Key Raw Files To Triage

### Lectures

- [session-01.md](lectures/session-01.md)

### Assignments

- No copied assignment files detected.

### Notebooks

- No copied notebook files detected.

## Assessment Links

- [Assessment Planning](assignments/assessment-planning.md)
- [Session 01 Notes](lectures/session-01.md)

## LLM Study Prompts

- Summarise the lecture files for this subject into weekly notes, key concepts, formulas, examples, and assessment relevance.
- Build a glossary for this subject and link each term to shared concepts where possible.
- Create a revision quiz from the learning map and the curated lecture notes.
- Identify which raw files are most useful for assessment preparation and why.

## Maintenance Checklist

- [x] Weekly notes created
- [ ] Assignment pages created
- [ ] Key notebooks explained
- [ ] Shared concepts linked
- [ ] Exam/revision questions added
""",
    )


def update_lecture_readme() -> None:
    readme = SUBJECT / "lectures" / "README.md"
    text = readme.read_text(encoding="utf-8")
    if "## Curated Session Notes" in text:
        text = text.split("## Curated Session Notes", 1)[0].rstrip()
    write(readme, text.rstrip() + "\n\n## Curated Session Notes\n\n- [Session 01 - MLOps Model Evaluation and Operational Patterns](session-01.md)\n")


def main() -> None:
    source_pdf = collect_source_pdf()
    if not source_pdf:
        print("No source PDF found for genai; nothing to curate.")
        return
    write_session_note(source_pdf)
    write_questions()
    update_learning_map()
    update_lecture_readme()


if __name__ == "__main__":
    main()
