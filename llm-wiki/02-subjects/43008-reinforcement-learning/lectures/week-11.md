---
type: lecture-note
subject: 43008-reinforcement-learning
week: 11
status: draft
---

# Week 11 - Planning and Monte Carlo Tree Search

## Source Files

- `sources/raw/43008 Reinforcement Learning/rl_slides/Week11-Lecture-2025.pdf` (pdf)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week11/Lecture/Week11-Lecture-2025.pdf` (pdf)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week11/Lab/2025/43008-Week11-Part-A-MCTS-TicTacToe-Solution.ipynb` (notebook)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week11/Lab/2025/43008-Week11-Part-A-MCTS-TicTacToe.ipynb` (notebook)

## Working Summary

This is a first-pass curated note generated from copied module PDFs and notebooks. Verify details against the source files before using it for assessment.

## Study Objectives

- Explain planning through simulation.
- Understand Monte Carlo Tree Search at a high level.
- Connect search and RL in game-like environments.

## Likely Concepts

- agent-environment loop: The repeated interaction where an agent observes state, takes action, receives reward, and moves to a new state.
- monte carlo tree search: A planning method that uses simulated rollouts to estimate promising actions in a search tree.
- value function: An estimate of expected return from a state or state-action pair under a policy or optimal behaviour.
- policy: A rule or model that maps states or observations to actions or action probabilities.
- markov decision process: A formal model for sequential decision-making with states, actions, transition probabilities, and rewards.
- function approximation: Using parameterised models such as neural networks to estimate value functions or policies for large state spaces.
- preference optimisation: Learning from preference comparisons or human feedback rather than only scalar environment rewards.
- policy iteration: A dynamic programming method that alternates policy evaluation and policy improvement.
- value iteration: A dynamic programming method that repeatedly applies Bellman optimality updates to estimate optimal values.
- monte carlo methods: Sampling-based RL methods that estimate values from complete episodes.

## Extracted Keywords

- model
- mcts
- reference
- emma
- burnskill
- stanford
- course
- https
- youtu
- vdf1bywhql8
- slbfrtrgqlmh
- check

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
