from __future__ import annotations

import contextlib
import io
import re
import warnings
from collections import Counter, defaultdict
from pathlib import Path

import nbformat
from pypdf import PdfReader


REPO_ROOT = Path(__file__).resolve().parents[1]
SUBJECT = REPO_ROOT / "llm-wiki" / "02-subjects" / "43008-reinforcement-learning"
RAW_ROOT = SUBJECT / "sources" / "raw"


WEEK_TOPICS = {
    0: "Mathematical and Probability Prerequisites",
    1: "Introduction, Python Setup, and Gymnasium Environments",
    2: "Multi-Armed Bandits and Exploration",
    3: "MDPs and POMDPs",
    4: "Policy Iteration",
    5: "Value Iteration and Solving MDPs",
    6: "Monte Carlo Prediction and Control",
    7: "Temporal-Difference Methods, SARSA, and Q-Learning",
    8: "Function Approximation and Deep Q-Learning",
    9: "Deep Q-Networks and Atari-Style Deep RL",
    10: "Actor-Critic and Policy Gradient Methods",
    11: "Planning and Monte Carlo Tree Search",
    12: "Hierarchical RL, Preference Optimisation, and RLHF",
}

WEEK_OBJECTIVES = {
    0: [
        "Review linear algebra and probability notation used by RL algorithms.",
        "Understand why expectation, value, and optimisation appear throughout RL.",
    ],
    1: [
        "Describe the agent-environment loop.",
        "Set up Gymnasium/OpenAI Gym style environments.",
        "Identify states, actions, rewards, episodes, and policies in examples.",
    ],
    2: [
        "Explain exploration versus exploitation.",
        "Compare epsilon-greedy, UCB, and bandit evaluation ideas.",
        "Understand regret and action-value estimates.",
    ],
    3: [
        "Formulate sequential decision problems as MDPs.",
        "Explain state transitions, rewards, policies, and value functions.",
        "Recognise when partial observability changes the problem.",
    ],
    4: [
        "Explain policy evaluation and policy improvement.",
        "Trace policy iteration step by step.",
        "Understand convergence intuition for dynamic programming methods.",
    ],
    5: [
        "Explain Bellman optimality updates.",
        "Implement or trace value iteration.",
        "Connect gridworld examples to general MDP solution methods.",
    ],
    6: [
        "Explain Monte Carlo prediction and control.",
        "Distinguish first-visit/every-visit reasoning and sampling-based updates.",
        "Understand episode-based value estimation.",
    ],
    7: [
        "Compare Monte Carlo and temporal-difference learning.",
        "Explain SARSA versus Q-learning.",
        "Understand on-policy and off-policy learning at a practical level.",
    ],
    8: [
        "Explain why function approximation is needed for large state spaces.",
        "Connect neural networks to value-function approximation.",
        "Understand Double Q-learning and DQN building blocks.",
    ],
    9: [
        "Explain DQN training workflows and replay-style deep RL ideas.",
        "Recognise deep RL instability and diagnostic needs.",
        "Connect CNN-based policies or value functions to Atari-style inputs.",
    ],
    10: [
        "Explain policy gradient and actor-critic framing.",
        "Understand PPO-style practical deep RL workflows.",
        "Compare value-based and policy-based methods.",
    ],
    11: [
        "Explain planning through simulation.",
        "Understand Monte Carlo Tree Search at a high level.",
        "Connect search and RL in game-like environments.",
    ],
    12: [
        "Explain hierarchical RL and preference optimisation themes.",
        "Connect RLHF/DPO ideas to modern AI systems.",
        "Identify limitations and evaluation concerns in preference-based optimisation.",
    ],
}

CONCEPTS = {
    "agent-environment loop": ["agent", "environment", "state", "action", "reward", "episode"],
    "policy": ["policy", "policies", "pi("],
    "value function": ["value function", "state-value", "action-value", "v(", "q("],
    "bellman equation": ["bellman", "optimality equation"],
    "exploration exploitation": ["exploration", "exploitation", "epsilon", "ucb", "bandit"],
    "markov decision process": ["mdp", "markov decision process", "transition probability"],
    "partially observable mdp": ["pomdp", "partial observability", "belief state"],
    "policy iteration": ["policy iteration", "policy evaluation", "policy improvement"],
    "value iteration": ["value iteration"],
    "monte carlo methods": ["monte carlo", "first-visit", "every-visit"],
    "temporal difference learning": ["temporal difference", "td learning", "td(", "sarsa"],
    "q-learning": ["q-learning", "q learning"],
    "function approximation": ["function approximation", "neural network", "approximation"],
    "deep q-network": ["dqn", "deep q-network", "deep q network", "replay"],
    "actor critic": ["actor-critic", "actor critic", "ppo", "policy gradient"],
    "monte carlo tree search": ["mcts", "monte carlo tree search"],
    "hierarchical reinforcement learning": ["hierarchical", "hrl", "options"],
    "preference optimisation": ["preference", "rlhf", "dpo", "direct preference optimization"],
}

DEFINITIONS = {
    "agent-environment loop": "The repeated interaction where an agent observes state, takes action, receives reward, and moves to a new state.",
    "policy": "A rule or model that maps states or observations to actions or action probabilities.",
    "value function": "An estimate of expected return from a state or state-action pair under a policy or optimal behaviour.",
    "bellman equation": "A recursive relationship that decomposes value into immediate reward plus discounted future value.",
    "exploration exploitation": "The tradeoff between trying uncertain actions to learn and choosing actions believed to perform well.",
    "markov decision process": "A formal model for sequential decision-making with states, actions, transition probabilities, and rewards.",
    "partially observable mdp": "An MDP variant where the agent does not fully observe the true state and must reason from observations or beliefs.",
    "policy iteration": "A dynamic programming method that alternates policy evaluation and policy improvement.",
    "value iteration": "A dynamic programming method that repeatedly applies Bellman optimality updates to estimate optimal values.",
    "monte carlo methods": "Sampling-based RL methods that estimate values from complete episodes.",
    "temporal difference learning": "RL methods that update value estimates from bootstrapped predictions before an episode ends.",
    "q-learning": "An off-policy temporal-difference control method for learning action-value estimates.",
    "function approximation": "Using parameterised models such as neural networks to estimate value functions or policies for large state spaces.",
    "deep q-network": "A deep RL method that uses a neural network to approximate Q-values.",
    "actor critic": "A method family that combines a policy model (actor) with a value estimator (critic).",
    "monte carlo tree search": "A planning method that uses simulated rollouts to estimate promising actions in a search tree.",
    "hierarchical reinforcement learning": "RL methods that organise decisions into higher-level skills, options, or subtasks.",
    "preference optimisation": "Learning from preference comparisons or human feedback rather than only scalar environment rewards.",
}


def clean(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def extract_pdf(path: Path, max_chars: int = 12000) -> str:
    try:
        stderr = io.StringIO()
        with warnings.catch_warnings(), contextlib.redirect_stderr(stderr):
            warnings.simplefilter("ignore")
            reader = PdfReader(str(path))
            return clean("\n".join((page.extract_text() or "") for page in reader.pages[:14]))[:max_chars]
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


def week_from_path(path: Path) -> int | None:
    match = re.search(r"Week\s*(\d+)", str(path), flags=re.I)
    if match:
        value = int(match.group(1))
        if 0 <= value <= 12:
            return value
    return None


def collect() -> dict[int, list[dict[str, str]]]:
    by_week: dict[int, list[dict[str, str]]] = defaultdict(list)
    for path in sorted(RAW_ROOT.rglob("*.pdf")):
        week = week_from_path(path)
        if week is None:
            continue
        by_week[week].append({"type": "pdf", "path": str(path.relative_to(SUBJECT)), "text": extract_pdf(path)})
    for path in sorted(RAW_ROOT.rglob("*.ipynb")):
        week = week_from_path(path)
        if week is None:
            continue
        by_week[week].append({"type": "notebook", "path": str(path.relative_to(SUBJECT)), "text": extract_notebook(path)})
    return by_week


def score(text: str) -> Counter:
    lower = text.lower()
    counts = Counter()
    for concept, terms in CONCEPTS.items():
        for term in terms:
            counts[concept] += lower.count(term)
    return counts


def keywords(text: str, n: int = 12) -> list[str]:
    words = re.findall(r"[A-Za-z][A-Za-z0-9+-]{3,}", text.lower())
    stop = {"this", "that", "with", "from", "week", "lecture", "part", "solution", "learning", "reinforcement", "value", "policy", "state", "action"}
    return [word for word, _ in Counter(w for w in words if w not in stop).most_common(n)]


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def bullet(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)


def write_week(week: int, sources: list[dict[str, str]]) -> None:
    all_text = "\n".join(item["text"] for item in sources)
    concept_lines = []
    for concept, count in score(all_text).most_common():
        if count > 0:
            concept_lines.append(f"- {concept}: {DEFINITIONS.get(concept, 'Verify definition from source material.')}")
    source_lines = "\n".join(f"- `{item['path']}` ({item['type']})" for item in sources)
    write(
        SUBJECT / "lectures" / f"week-{week:02d}.md",
        f"""---
type: lecture-note
subject: 43008-reinforcement-learning
week: {week}
status: draft
---

# Week {week:02d} - {WEEK_TOPICS.get(week, 'Reinforcement Learning Topic')}

## Source Files

{source_lines}

## Working Summary

This is a first-pass curated note generated from copied module PDFs and notebooks. Verify details against the source files before using it for assessment.

## Study Objectives

{bullet(WEEK_OBJECTIVES.get(week, ['Review the source files and identify the main RL method.']))}

## Likely Concepts

{chr(10).join(concept_lines[:10]) or '- To be confirmed from source review.'}

## Extracted Keywords

{bullet(keywords(all_text))}

## What To Understand

- What decision problem is being modelled.
- What the state, action, reward, and policy are.
- Whether the method is model-based, model-free, on-policy, or off-policy.
- How values, policies, or models are updated.
- What failure modes or evaluation issues matter.

## Assessment Relevance

- Link this week to assessment tasks involving algorithm explanation, implementation, or experiment analysis.
- Use notebook sources to verify algorithm steps and expected outputs.

## Revision Questions

- What problem does this RL method solve?
- What update equation or algorithm loop is central?
- What assumptions does the method make?
- How would you evaluate whether the learned policy is good?

## LLM Follow-Up Prompt

Using the source files listed above, expand this draft into a precise study note with definitions, equations, algorithm steps, notebook implementation details, and assessment relevance. Keep claims traceable to source files.
""",
    )


def write_glossary(by_week: dict[int, list[dict[str, str]]]) -> None:
    text = "\n".join(item["text"] for sources in by_week.values() for item in sources)
    rows = []
    for concept, count in score(text).most_common():
        if count > 0:
            rows.append(f"| {concept} | {count} | {DEFINITIONS.get(concept, 'Add verified definition from source material.')} |")
    write(
        SUBJECT / "glossary.md",
        f"""---
type: glossary
subject: 43008-reinforcement-learning
status: draft
---

# 43008 Reinforcement Learning - Glossary

| Term | Evidence Count | Working Definition |
|---|---:|---|
{chr(10).join(rows)}

## Maintenance

- Replace working definitions with precise definitions and equations from lectures.
- Link durable terms to [Reinforcement Learning](../../03-shared-concepts/reinforcement-learning.md), [Artificial Intelligence](../../03-shared-concepts/artificial-intelligence.md), and [Machine Learning](../../03-shared-concepts/machine-learning.md).
""",
    )


def write_evidence_map(by_week: dict[int, list[dict[str, str]]]) -> None:
    rows = "\n".join(
        f"| Week {week:02d} | {WEEK_TOPICS.get(week, '')} | {len(sources)} | [note](../lectures/week-{week:02d}.md) |"
        for week, sources in sorted(by_week.items())
    )
    write(
        SUBJECT / "assignments" / "evidence-map.md",
        f"""---
type: evidence-map
subject: 43008-reinforcement-learning
status: draft
---

# 43008 Reinforcement Learning - Assessment Evidence Map

## Weekly Evidence

| Week | Topic | Source Count | Curated Note |
|---|---|---:|---|
{rows}

## Assessment Evidence Strategy

- Use early weeks for conceptual definitions and problem formulation.
- Use Weeks 4-8 for dynamic programming, Monte Carlo, TD, SARSA, Q-learning, and function approximation evidence.
- Use Weeks 9-12 for deep RL, actor-critic/PPO, planning, MCTS, hierarchical RL, and preference optimisation evidence.
- Link each assessment task to the weekly notes that justify algorithms, experiment design, and evaluation.
""",
    )


def update_indexes(by_week: dict[int, list[dict[str, str]]]) -> None:
    links = "\n".join(f"- [Week {week:02d} - {WEEK_TOPICS.get(week, 'RL Topic')}](week-{week:02d}.md)" for week in sorted(by_week))
    readme = SUBJECT / "lectures" / "README.md"
    text = readme.read_text(encoding="utf-8")
    if "## Curated Weekly Notes" in text:
        text = text.split("## Curated Weekly Notes", 1)[0].rstrip()
    write(readme, text.rstrip() + f"\n\n## Curated Weekly Notes\n\n{links}\n")

    subject_readme = SUBJECT / "README.md"
    text = subject_readme.read_text(encoding="utf-8")
    if "[Glossary](glossary.md)" not in text and "## Curated Study Layer" in text:
        text = text.replace(
            "- [Revision Questions](questions/revision-questions.md)",
            "- [Revision Questions](questions/revision-questions.md)\n- [Glossary](glossary.md)\n- [Assessment Evidence Map](assignments/evidence-map.md)",
        )
    write(subject_readme, text)


def main() -> None:
    by_week = collect()
    for week, sources in sorted(by_week.items()):
        write_week(week, sources)
    write_glossary(by_week)
    write_evidence_map(by_week)
    update_indexes(by_week)
    print(f"Generated {len(by_week)} weekly notes for 43008 Reinforcement Learning")


if __name__ == "__main__":
    main()
