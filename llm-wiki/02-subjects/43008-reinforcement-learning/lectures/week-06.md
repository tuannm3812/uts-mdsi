---
type: lecture-note
subject: 43008-reinforcement-learning
week: 6
status: draft
---

# Week 06 - Monte Carlo Prediction and Control

## Source Files

- `sources/raw/43008 Reinforcement Learning/rl_slides/Week6-Lecture-2025.pdf` (pdf)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week6/Lecture/Week6-Lecture-2024.pdf` (pdf)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week6/Lecture/Week6-Lecture-2025.pdf` (pdf)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week6/Lab/2025/43008-Week6-MonteCarloMethods-Control-Solution.ipynb` (notebook)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week6/Lab/2025/43008-Week6-MonteCarloMethods-Control.ipynb` (notebook)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week6/Lab/2025/43008-Week6-MonteCarloMethods-Prediction-Solution.ipynb` (notebook)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week6/Lab/2025/43008-Week6-MonteCarloMethods-Prediction.ipynb` (notebook)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week6/Lab/43008-Week6-MonteCarloMethods-Prediction-Solution.ipynb` (notebook)

## Working Summary

This is a first-pass curated note generated from copied module PDFs and notebooks. Verify details against the source files before using it for assessment.

## Study Objectives

- Explain Monte Carlo prediction and control.
- Distinguish first-visit/every-visit reasoning and sampling-based updates.
- Understand episode-based value estimation.

## Likely Concepts

- agent-environment loop: The repeated interaction where an agent observes state, takes action, receives reward, and moves to a new state.
- policy: A rule or model that maps states or observations to actions or action probabilities.
- monte carlo methods: Sampling-based RL methods that estimate values from complete episodes.
- value function: An estimate of expected return from a state or state-action pair under a policy or optimal behaviour.
- markov decision process: A formal model for sequential decision-making with states, actions, transition probabilities, and rewards.
- policy iteration: A dynamic programming method that alternates policy evaluation and policy improvement.
- exploration exploitation: The tradeoff between trying uncertain actions to learn and choosing actions believed to perform well.
- q-learning: An off-policy temporal-difference control method for learning action-value estimates.
- value iteration: A dynamic programming method that repeatedly applies Bellman optimality updates to estimate optimal values.
- temporal difference learning: RL methods that update value estimates from bootstrapped predictions before an episode ends.

## Extracted Keywords

- episode
- import
- monte
- carlo
- algorithm
- return
- visit
- function
- rewards
- methods
- environment
- reward

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
