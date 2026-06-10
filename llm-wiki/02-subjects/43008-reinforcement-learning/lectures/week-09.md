---
type: lecture-note
subject: 43008-reinforcement-learning
week: 9
status: draft
---

# Week 09 - Deep Q-Networks and Atari-Style Deep RL

## Source Files

- `sources/raw/43008 Reinforcement Learning/rl_slides/Week9-Lecture-2023.pdf` (pdf)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week9/Lecture/Sagemaker User Guide 2025.pdf` (pdf)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week9/Lecture/Week9-Lecture-2023.pdf` (pdf)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week9/Lab/2025/43008-Week9-Part-B-Simple-Deep-Q-Network-Solution-Colab.ipynb` (notebook)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week9/Lab/2025/43008-Week9-Part-C-DQN-LunarLander-Solution-Gymnasium.ipynb` (notebook)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week9/Lab/2025/43008-Week9-Part-D-DQN-Atari-CustomCNN-Solution-Colab.ipynb` (notebook)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week9/Lab/43008-Week9-Part-A-Simple-Custom-CNN.ipynb` (notebook)

## Working Summary

This is a first-pass curated note generated from copied module PDFs and notebooks. Verify details against the source files before using it for assessment.

## Study Objectives

- Explain DQN training workflows and replay-style deep RL ideas.
- Recognise deep RL instability and diagnostic needs.
- Connect CNN-based policies or value functions to Atari-style inputs.

## Likely Concepts

- agent-environment loop: The repeated interaction where an agent observes state, takes action, receives reward, and moves to a new state.
- deep q-network: A deep RL method that uses a neural network to approximate Q-values.
- policy: A rule or model that maps states or observations to actions or action probabilities.
- value function: An estimate of expected return from a state or state-action pair under a policy or optimal behaviour.
- function approximation: Using parameterised models such as neural networks to estimate value functions or policies for large state spaces.
- policy iteration: A dynamic programming method that alternates policy evaluation and policy improvement.
- exploration exploitation: The tradeoff between trying uncertain actions to learn and choosing actions believed to perform well.
- temporal difference learning: RL methods that update value estimates from bootstrapped predictions before an episode ends.
- actor critic: A method family that combines a policy model (actor) with a value estimator (critic).
- q-learning: An off-policy temporal-difference control method for learning action-value estimates.

## Extracted Keywords

- import
- model
- your
- function
- space
- environment
- stable
- code
- agent
- will
- training
- baselines3

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
