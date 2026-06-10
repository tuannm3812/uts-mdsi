---
type: lecture-note
subject: 43008-reinforcement-learning
week: 10
status: draft
---

# Week 10 - Actor-Critic and Policy Gradient Methods

## Source Files

- `sources/raw/43008 Reinforcement Learning/rl_slides/Week10-Lecture-2024.pdf` (pdf)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week10/Lecture/Week10-Lecture-2024.pdf` (pdf)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week10/Lab/2025/43008-Week10-Part-A-ActorCritic-BiPedalWalker-Solution.ipynb` (notebook)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week10/Lab/2025/43008-Week10-Part-A-ActorCritic-BiPedalWalker.ipynb` (notebook)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week10/Lab/2025/43008-Week10-Part-B-PPO-BiPedalWalker-Solution.ipynb` (notebook)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week10/Lab/2025/43008-Week10-Part-B-PPO-BiPedalWalker.ipynb` (notebook)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week10/Lab/2025/43008-Week10-Part-C-PPO-Atari-CustomCNN-Solution-Colab.ipynb` (notebook)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week10/Lab/2025/43008-Week10-Part-C-PPO-Atari-CustomCNN.ipynb` (notebook)

## Working Summary

This is a first-pass curated note generated from copied module PDFs and notebooks. Verify details against the source files before using it for assessment.

## Study Objectives

- Explain policy gradient and actor-critic framing.
- Understand PPO-style practical deep RL workflows.
- Compare value-based and policy-based methods.

## Likely Concepts

- agent-environment loop: The repeated interaction where an agent observes state, takes action, receives reward, and moves to a new state.
- policy: A rule or model that maps states or observations to actions or action probabilities.
- actor critic: A method family that combines a policy model (actor) with a value estimator (critic).
- value function: An estimate of expected return from a state or state-action pair under a policy or optimal behaviour.
- function approximation: Using parameterised models such as neural networks to estimate value functions or policies for large state spaces.
- deep q-network: A deep RL method that uses a neural network to approximate Q-values.

## Extracted Keywords

- import
- model
- stable
- baselines3
- function
- display
- environment
- videos
- common
- https
- training
- define

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
