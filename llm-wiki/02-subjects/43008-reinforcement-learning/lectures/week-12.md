---
type: lecture-note
subject: 43008-reinforcement-learning
week: 12
status: draft
---

# Week 12 - Hierarchical RL, Preference Optimisation, and RLHF

## Source Files

- `sources/raw/43008 Reinforcement Learning/rl_slides/Week12-Lecture-2024.pdf` (pdf)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week12/Lecture/A Comprehensive Survey of DPO.pdf` (pdf)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week12/Lecture/A Survey of Direct Preference Optimization.pdf` (pdf)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week12/Lecture/FeudalNetwrok_HRL.pdf` (pdf)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week12/Lecture/HRL-review-2022.pdf` (pdf)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week12/Lecture/NIPS-1992-feudal-reinforcement-learning-Paper.pdf` (pdf)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week12/Lecture/NIPS-1997-reinforcement-learning-with-hierarchies-of-machines-Paper.pdf` (pdf)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week12/Lecture/SPS-aij.pdf` (pdf)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week12/Lecture/Week12-Lecture-2024.pdf` (pdf)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week12/Lecture/recent-advances-hrl-2003.pdf` (pdf)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week12/Lab/43008_Week12_RLHF_SLM_Example.ipynb` (notebook)

## Working Summary

This is a first-pass curated note generated from copied module PDFs and notebooks. Verify details against the source files before using it for assessment.

## Study Objectives

- Explain hierarchical RL and preference optimisation themes.
- Connect RLHF/DPO ideas to modern AI systems.
- Identify limitations and evaluation concerns in preference-based optimisation.

## Likely Concepts

- agent-environment loop: The repeated interaction where an agent observes state, takes action, receives reward, and moves to a new state.
- preference optimisation: Learning from preference comparisons or human feedback rather than only scalar environment rewards.
- hierarchical reinforcement learning: RL methods that organise decisions into higher-level skills, options, or subtasks.
- markov decision process: A formal model for sequential decision-making with states, actions, transition probabilities, and rewards.
- policy: A rule or model that maps states or observations to actions or action probabilities.
- actor critic: A method family that combines a policy model (actor) with a value estimator (critic).
- value function: An estimate of expected return from a state or state-action pair under a policy or optimal behaviour.
- exploration exploitation: The tradeoff between trying uncertain actions to learn and choosing actions believed to perform well.
- q-learning: An off-policy temporal-difference control method for learning action-value estimates.
- function approximation: Using parameterised models such as neural networks to estimate value functions or policies for large state spaces.

## Extracted Keywords

- c101
- c116
- c111
- c110
- c105
- c114
- c115
- c108
- c104
- c109
- reward
- c100

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
