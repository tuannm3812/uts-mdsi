---
type: lecture-note
subject: 43008-reinforcement-learning
week: 7
status: draft
---

# Week 07 - Temporal-Difference Methods, SARSA, and Q-Learning

## Source Files

- `sources/raw/43008 Reinforcement Learning/rl_slides/Week7-Lecture-2025.pdf` (pdf)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week7/Lecture/Q-learning-Explained.pdf` (pdf)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week7/Lecture/Week7-Lecture-2025.pdf` (pdf)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week7/Lab/2025/43008-Week7-TD-Methods-Part-A-Prediction-Gymnasium-Solution.ipynb` (notebook)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week7/Lab/2025/43008-Week7-TD-Methods-Part-A-Prediction-Gymnasium.ipynb` (notebook)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week7/Lab/2025/43008-Week7-TD-Methods-Part-B-Gymnasium-SARSA.ipynb` (notebook)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week7/Lab/2025/43008-Week7-TD-Methods-Part-B-SARSA-Gymnasium-Solution.ipynb` (notebook)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week7/Lab/2025/43008-Week7-TD-Methods-Part-C-Gymnasium-QLearning.ipynb` (notebook)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week7/Lab/2025/43008-Week7-TD-Methods-Part-C-QLearning-Gymnasium-Solution.ipynb` (notebook)

## Working Summary

This is a first-pass curated note generated from copied module PDFs and notebooks. Verify details against the source files before using it for assessment.

## Study Objectives

- Compare Monte Carlo and temporal-difference learning.
- Explain SARSA versus Q-learning.
- Understand on-policy and off-policy learning at a practical level.

## Likely Concepts

- agent-environment loop: The repeated interaction where an agent observes state, takes action, receives reward, and moves to a new state.
- value function: An estimate of expected return from a state or state-action pair under a policy or optimal behaviour.
- temporal difference learning: RL methods that update value estimates from bootstrapped predictions before an episode ends.
- policy: A rule or model that maps states or observations to actions or action probabilities.
- q-learning: An off-policy temporal-difference control method for learning action-value estimates.
- policy iteration: A dynamic programming method that alternates policy evaluation and policy improvement.
- exploration exploitation: The tradeoff between trying uncertain actions to learn and choosing actions believed to perform well.
- monte carlo methods: Sampling-based RL methods that estimate values from complete episodes.
- markov decision process: A formal model for sequential decision-making with states, actions, transition probabilities, and rewards.

## Extracted Keywords

- import
- plot
- display
- episode
- function
- video
- algorithm
- q-learning
- control
- image
- time
- model

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
