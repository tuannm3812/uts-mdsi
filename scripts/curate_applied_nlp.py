from __future__ import annotations

import re
from collections import Counter, defaultdict
from pathlib import Path

import nbformat
from pypdf import PdfReader


REPO_ROOT = Path(__file__).resolve().parents[1]
SUBJECT = REPO_ROOT / "llm-wiki" / "02-subjects" / "36118-applied-natural-language-processing"
LECTURES_RAW = SUBJECT / "lectures" / "raw"
NOTEBOOKS_RAW = SUBJECT / "notebooks" / "raw"
ASSIGNMENTS_RAW = SUBJECT / "assignments" / "raw"


SESSION_TOPICS = {
    1: "NLP Foundations, Text Preprocessing, and Corpora",
    2: "Text Analysis, Topic Modelling, and Clustering",
    3: "Summarisation, Text Classification, and Sentiment Analysis",
    4: "Word Embeddings and Deep Learning Models",
    5: "BERT, Hugging Face Models, and Applied Interfaces",
    6: "LLM Prompting and Generative NLP Workflows",
    7: "Advanced Applied NLP and Project Development",
    8: "Evaluation, Responsible NLP, and Project Communication",
    10: "Final Applied NLP Integration",
}

SESSION_OBJECTIVES = {
    1: [
        "Explain the standard NLP pipeline from raw text to cleaned tokens and features.",
        "Identify corpus-level design decisions such as filtering, tokenisation, normalisation, and stopword handling.",
        "Connect notebook preprocessing choices to reproducible NLP analysis.",
    ],
    2: [
        "Compare exploratory text analysis, topic modelling, and clustering.",
        "Explain how document representations affect unsupervised text results.",
        "Evaluate whether discovered topics or clusters are meaningful for a task.",
    ],
    3: [
        "Explain summarisation, classification, and sentiment analysis as supervised or task-specific NLP workflows.",
        "Choose appropriate metrics and validation checks for text classification.",
        "Identify common sources of leakage, imbalance, and weak labelling.",
    ],
    4: [
        "Explain word embeddings and how they represent semantic similarity.",
        "Compare classical feature representations with neural representations.",
        "Understand how deep learning models consume token sequences.",
    ],
    5: [
        "Explain transformer/BERT-style fine-tuning for NLP tasks.",
        "Use Hugging Face-style workflows and simple interfaces for applied models.",
        "Evaluate pretrained model fit, limitations, and deployment tradeoffs.",
    ],
    6: [
        "Use prompting patterns for LLM-based NLP tasks.",
        "Evaluate generated outputs for relevance, factuality, bias, and task fit.",
        "Distinguish prompting from training or fine-tuning.",
    ],
    7: [
        "Connect advanced NLP methods to project design and assessment needs.",
        "Plan evidence, evaluation, and limitations for an applied NLP project.",
    ],
    8: [
        "Review evaluation and communication practices for applied NLP systems.",
        "Connect responsible AI concerns to text analysis and generation.",
    ],
    10: [
        "Synthesize the subject into a defensible applied NLP workflow.",
        "Prepare final project or presentation evidence.",
    ],
}

CONCEPTS = {
    "tokenisation": ["token", "tokenization", "tokenisation", "tokens"],
    "text preprocessing": ["preprocess", "preprocessing", "cleaning", "normalization", "normalisation", "stopword", "stemming", "lemmat"],
    "bag of words": ["bag of words", "bow", "countvectorizer", "tf-idf", "tfidf"],
    "topic modelling": ["topic model", "topic modeling", "topic modelling", "lda", "bertopic"],
    "clustering": ["clustering", "cluster", "k-means", "kmeans"],
    "text classification": ["classification", "classifier", "classify", "label"],
    "sentiment analysis": ["sentiment", "polarity"],
    "summarisation": ["summarization", "summarisation", "summary"],
    "word embeddings": ["embedding", "word2vec", "glove", "vector", "similarity"],
    "deep learning for text": ["rnn", "lstm", "gru", "cnn", "deep learning", "neural"],
    "transformers": ["transformer", "bert", "attention", "hugging face", "huggingface"],
    "large language models": ["llm", "large language model", "prompt", "openai", "gemini"],
    "evaluation": ["accuracy", "precision", "recall", "f1", "confusion matrix", "rouge", "bleu"],
    "responsible ai": ["bias", "fairness", "ethics", "privacy", "consent", "responsible"],
}

DEFINITIONS = {
    "tokenisation": "Splitting raw text into units such as words, subwords, or tokens that downstream NLP models can process.",
    "text preprocessing": "Cleaning and transforming text before analysis, including normalisation, stopword handling, stemming, lemmatisation, and filtering.",
    "bag of words": "A sparse representation that counts words or weighted word occurrences without modelling word order.",
    "topic modelling": "Unsupervised methods for discovering recurring themes or latent topics in a document collection.",
    "clustering": "Grouping documents or text units by representation similarity without using labelled classes.",
    "text classification": "Assigning one or more labels to text, usually with supervised learning and task-specific metrics.",
    "sentiment analysis": "Estimating opinion, polarity, or affect from text.",
    "summarisation": "Producing a shorter representation of text while preserving the important content for a task.",
    "word embeddings": "Dense vector representations that capture semantic or contextual relationships between words or text units.",
    "deep learning for text": "Neural models for sequence or text tasks, including RNNs, LSTMs, CNNs, and transformer-based models.",
    "transformers": "Attention-based neural architectures that power models such as BERT and many modern NLP systems.",
    "large language models": "Large pretrained language models used for generation, classification, extraction, summarisation, and reasoning-style workflows.",
    "evaluation": "Measuring output quality with task-appropriate metrics, validation data, qualitative review, and error analysis.",
    "responsible ai": "Considering bias, privacy, consent, fairness, transparency, and downstream impact in NLP systems.",
}


def clean_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def extract_pdf(path: Path, max_chars: int = 12000) -> str:
    try:
        reader = PdfReader(str(path))
        return clean_text("\n".join((page.extract_text() or "") for page in reader.pages[:12]))[:max_chars]
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
        return clean_text("\n".join(chunks))[:max_chars]
    except Exception as exc:
        return f"[Notebook extraction failed: {exc}]"


def session_from_path(path: Path) -> int | None:
    text = str(path)
    patterns = [
        r"session\s*(\d+)",
        r"week\s*(\d+)",
    ]
    for pattern in patterns:
        match = re.search(pattern, text, flags=re.I)
        if match:
            value = int(match.group(1))
            if 1 <= value <= 12:
                return value
    return None


def score_concepts(text: str) -> Counter:
    lowered = text.lower()
    scores = Counter()
    for concept, terms in CONCEPTS.items():
        for term in terms:
            scores[concept] += lowered.count(term)
    return scores


def collect_sources() -> dict[int, list[dict[str, str]]]:
    by_session: dict[int, list[dict[str, str]]] = defaultdict(list)
    for path in sorted(LECTURES_RAW.rglob("*.pdf")):
        session = session_from_path(path)
        if not session:
            continue
        by_session[session].append({"type": "lecture", "path": str(path.relative_to(SUBJECT)), "text": extract_pdf(path)})
    for path in sorted(LECTURES_RAW.rglob("*.pptx")):
        session = session_from_path(path)
        if not session:
            continue
        by_session[session].append({"type": "slides", "path": str(path.relative_to(SUBJECT)), "text": path.name})
    for path in sorted(NOTEBOOKS_RAW.rglob("*.ipynb")):
        session = session_from_path(path)
        if not session:
            continue
        by_session[session].append({"type": "notebook", "path": str(path.relative_to(SUBJECT)), "text": extract_notebook(path)})
    return by_session


def top_keywords(text: str, n: int = 12) -> list[str]:
    words = re.findall(r"[A-Za-z][A-Za-z0-9+-]{3,}", text.lower())
    stop = {
        "this", "that", "with", "from", "have", "will", "text", "data", "model", "session",
        "using", "part", "notebook", "python", "import", "output", "input",
    }
    counts = Counter(w for w in words if w not in stop)
    return [word for word, _ in counts.most_common(n)]


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def bullet(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)


def write_session_note(session: int, sources: list[dict[str, str]]) -> None:
    text = "\n".join(item["text"] for item in sources)
    concepts = [name for name, score in score_concepts(text).most_common() if score > 0][:8]
    source_lines = "\n".join(f"- `{item['path']}` ({item['type']})" for item in sources)
    concept_lines = "\n".join(f"- {c}: {DEFINITIONS.get(c, 'Verify definition from source material.')}" for c in concepts) or "- To be confirmed from source review."
    keyword_lines = bullet(top_keywords(text)) or "- To be confirmed"
    objective_lines = bullet(SESSION_OBJECTIVES.get(session, ["Review session source files and summarise the main applied NLP workflow."]))
    write(
        SUBJECT / "lectures" / f"session-{session:02d}.md",
        f"""---
type: lecture-note
subject: 36118-applied-natural-language-processing
session: {session}
status: draft
---

# Session {session:02d} - {SESSION_TOPICS.get(session, 'Applied NLP Topic')}

## Source Files

{source_lines}

## Working Summary

This is a first-pass curated note generated from copied slides, PDFs, and notebooks. Verify details against source files before using it for assessment.

## Study Objectives

{objective_lines}

## Likely Concepts

{concept_lines}

## Extracted Keywords

{keyword_lines}

## What To Understand

- What NLP task is being solved.
- How raw text becomes features, embeddings, prompts, or model inputs.
- Which model or method is appropriate for the task.
- How output quality should be evaluated.
- What responsible AI or data limitations apply.

## Assessment Relevance

- Link this session to AT1, AT2, AT3, or project evidence where relevant.
- Record which raw files support the assignment task, method, or evaluation.

## Revision Questions

- What is the main NLP workflow from this session?
- What representation of text is used?
- Which evaluation metric or qualitative check is appropriate?
- What could go wrong with this method in a real applied setting?

## LLM Follow-Up Prompt

Using the source files listed above, expand this draft into a precise study note with definitions, examples, code workflow, evaluation strategy, and assessment relevance. Keep claims traceable to source files.
""",
    )


def write_glossary(by_session: dict[int, list[dict[str, str]]]) -> None:
    text = "\n".join(item["text"] for sources in by_session.values() for item in sources)
    rows = []
    for concept, score in score_concepts(text).most_common():
        if score > 0:
            rows.append(f"| {concept} | {score} | {DEFINITIONS.get(concept, 'Add verified definition from lectures and notebooks.')} |")
    write(
        SUBJECT / "glossary.md",
        f"""---
type: glossary
subject: 36118-applied-natural-language-processing
status: draft
---

# 36118 Applied Natural Language Processing - Glossary

| Term | Evidence Count | Working Definition |
|---|---:|---|
{chr(10).join(rows)}

## Maintenance

- Replace working definitions with verified definitions and examples from slides/notebooks.
- Link durable terms to [Natural Language Processing](../../03-shared-concepts/natural-language-processing.md), [Machine Learning](../../03-shared-concepts/machine-learning.md), and [Deep Learning](../../03-shared-concepts/deep-learning.md).
""",
    )


def write_evidence_map(by_session: dict[int, list[dict[str, str]]]) -> None:
    session_rows = "\n".join(
        f"| Session {session:02d} | {SESSION_TOPICS.get(session, '')} | {len(sources)} | [note](../lectures/session-{session:02d}.md) |"
        for session, sources in sorted(by_session.items())
    )
    assignment_files = sorted(str(p.relative_to(SUBJECT)) for p in ASSIGNMENTS_RAW.rglob("*") if p.is_file())
    assignment_lines = "\n".join(f"- `{path}`" for path in assignment_files[:60])
    write(
        SUBJECT / "assignments" / "evidence-map.md",
        f"""---
type: evidence-map
subject: 36118-applied-natural-language-processing
status: draft
---

# 36118 Applied NLP - Assessment Evidence Map

## Session Evidence

| Session | Topic | Source Count | Curated Note |
|---|---|---:|---|
{session_rows}

## Assessment-To-Session Map

| Assessment | Most Relevant Sessions | Evidence Focus |
|---|---|---|
| AT1 | Sessions 1-4 | Text preprocessing, representation, analysis notebooks, and gender-equity submissions corpus. |
| AT2 | Sessions 4-7 | Embeddings, classification, BERT/Hugging Face workflows, prompting or applied model design. |
| AT3 | Sessions 6-10 | Project framing, evaluation, communication, responsible NLP, and final presentation evidence. |

## Assignment Source Files

{assignment_lines}
""",
    )


def update_indexes(by_session: dict[int, list[dict[str, str]]]) -> None:
    links = "\n".join(
        f"- [Session {session:02d} - {SESSION_TOPICS.get(session, 'Applied NLP Topic')}](session-{session:02d}.md)"
        for session in sorted(by_session)
    )
    readme = SUBJECT / "lectures" / "README.md"
    text = readme.read_text(encoding="utf-8")
    if "## Curated Session Notes" in text:
        text = text.split("## Curated Session Notes", 1)[0].rstrip()
    write(readme, text.rstrip() + f"\n\n## Curated Session Notes\n\n{links}\n")

    subject_readme = SUBJECT / "README.md"
    text = subject_readme.read_text(encoding="utf-8")
    if "[Glossary](glossary.md)" not in text and "## Curated Study Layer" in text:
        text = text.replace(
            "- [Revision Questions](questions/revision-questions.md)",
            "- [Revision Questions](questions/revision-questions.md)\n- [Glossary](glossary.md)\n- [Assessment Evidence Map](assignments/evidence-map.md)",
        )
    write(subject_readme, text)


def main() -> None:
    by_session = collect_sources()
    for session, sources in sorted(by_session.items()):
        write_session_note(session, sources)
    write_glossary(by_session)
    write_evidence_map(by_session)
    update_indexes(by_session)
    print(f"Generated {len(by_session)} session notes for 36118 Applied NLP")


if __name__ == "__main__":
    main()

