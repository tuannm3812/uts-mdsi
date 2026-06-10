---
type: lecture-note
subject: 43008-reinforcement-learning
week: 1
status: draft
---

# Week 01 - Introduction, Python Setup, and Gymnasium Environments

## Source Files

- `sources/raw/43008 Reinforcement Learning/rl_slides/Week1-Introduction-2025.pdf` (pdf)
- `sources/raw/43008 Reinforcement Learning/rl_slides/Week1-Lecture-New-2025.pdf` (pdf)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week1/43008-Week1-Checklist.pdf` (pdf)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week1/Lecture/Week1-Introduction-2025.pdf` (pdf)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week1/Lecture/Week1-Lecture-New-2024.pdf` (pdf)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week1/Lecture/Week1-Lecture-New-2025.pdf` (pdf)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week1/Lab/2024/43008-OpenAIGym-Tutorial-PartB-Solution.ipynb` (notebook)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week1/Lab/2024/43008-OpenAIGym-Tutorial-PartB.ipynb` (notebook)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week1/Lab/2025/43008-GoogleDrive_Setup.ipynb` (notebook)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week1/Lab/2025/43008-OpenAIGym-Tutorial-PartA.ipynb` (notebook)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week1/Lab/2025/43008-OpenAIGym-Tutorial-PartB-Solution.ipynb` (notebook)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week1/Lab/2025/43008-OpenAIGym-Tutorial-PartB.ipynb` (notebook)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week1/Lab/2025/43008-Week1-Python-Warmup-Solution.ipynb` (notebook)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week1/Lab/2025/43008-Week1-Python-Warmup.ipynb` (notebook)

## Working Summary

This is a first-pass curated note generated from copied module PDFs and notebooks. Verify details against the source files before using it for assessment.

## Study Objectives

- Describe the agent-environment loop.
- Set up Gymnasium/OpenAI Gym style environments.
- Identify states, actions, rewards, episodes, and policies in examples.

## Likely Concepts

- agent-environment loop: The repeated interaction where an agent observes state, takes action, receives reward, and moves to a new state.
- exploration exploitation: The tradeoff between trying uncertain actions to learn and choosing actions believed to perform well.
- value function: An estimate of expected return from a state or state-action pair under a policy or optimal behaviour.
- markov decision process: A formal model for sequential decision-making with states, actions, transition probabilities, and rewards.
- policy: A rule or model that maps states or observations to actions or action probabilities.
- q-learning: An off-policy temporal-difference control method for learning action-value estimates.
- deep q-network: A deep RL method that uses a neural network to approximate Q-values.
- actor critic: A method family that combines a policy model (actor) with a value estimator (critic).

## Extracted Keywords

- import
- environment
- openai
- create
- function
- step
- python
- code
- actions
- display
- video
- using

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
