---
type: lecture-note
subject: 43008-reinforcement-learning
week: 1
status: active
---

# Week 01 - Introduction, Python Setup, and Gymnasium Environments

## Subject Logistics (from Week 1 slides)

- Subject Coordinator & Lecturer: A/Prof. Nabin Sharma (Nabin.Sharma@uts.edu.au)
- Tutorial staff: Shudarshan Kongkham, Rozhin Vosoughi
- Labs/tutorials: 2hr tutor-guided implementation (Python, Google Colab/AWS SageMaker Studio) + 1hr project consultation
- Consultation: every Thursday 13:00–14:00 (Zoom or face-to-face)
- RL frameworks used: OpenAI Gym, TensorFlow Agents
- Project groups (for AT3) must be formed by Week 3 Friday

## Subject Objectives

- Introduction to Reinforcement Learning fundamentals.
- Understand the difference between supervised, unsupervised, and reinforcement learning.
- Design RL algorithms to solve classic RL problems.
- Apply state-of-the-art and customised RL algorithms to real-world problems.
- Communicate effectively in a team, orally and in writing.

## Assessment Overview (see [assignments/assessment-planning.md](../assignments/assessment-planning.md) for full detail)

- AT1 (35%, individual): MDP formulation + Dynamic Programming — due Fri 5 Sep 2025
- AT2 (35%, individual): RL problem via DQN/Q-learning — due Fri 17 Oct 2025
- AT3 (30%, group): Final project with operational UI — due Fri 24 Oct 2025

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

## What is Reinforcement Learning

RL is learning how to make a good *sequence* of decisions by interacting with an environment — trial-and-error, with feedback (reward) on how good or bad an action was. Framed as "the fundamental challenge in AI & ML: learn how to make good decisions in uncertain conditions."

Illustrative case studies from the slides: training a dog with instructions/rewards, learning to cycle by trial and error, and Pavlov's classical-conditioning experiments (stimulus → response, reinforced over repetition).

## Key Elements (RL Framework)

- **Agent**: the learner/decision-maker that interacts with the environment.
- **Environment**: the external context/world the agent operates and learns in.
- **State**: a representation of the current situation.
- **Action**: a decision made by the agent.
- **Reward**: feedback from the environment on the desirability of an action.
- **Policy**: the strategy/rule set the agent uses to choose actions; "associates past experience to actions" (e.g. a drone-usage policy: use safety nets indoors).

Loop: agent observes **state** → picks **action** (via its **policy**) → environment returns **reward** and new **state** → repeat.

## Key Characteristics

- **Trial and error** based learning.
- **Optimization**: find good *sequences* of actions/decisions, not single ones.
- **Delayed consequences/reward**: the value of an action may only become clear much later (e.g. extra super-fund contributions now vs. retirement outcome later; starting a project in Week 1 vs. finishing on time).
- **Exploration**: trying new actions to discover their effects (e.g. a child learning to balance a bicycle).
- **Exploitation**: choosing the action with the highest expected reward given current knowledge; risk of missing better unexplored actions if overused.
- **Exploration vs. exploitation must be balanced.**
- **Generalization**: applying learned strategies effectively to new/unseen situations.

## How RL Differs from Other Learning Paradigms

| Paradigm | Labelled data | Exploration | Delayed reward |
|---|---|---|---|
| Supervised ML | Yes (labels from a supervisor) | No | No |
| Unsupervised ML | No (find patterns) | No | No |
| Imitation Learning | Demonstrations of a good policy | No | Yes |
| Reinforcement Learning | No (learns from reward signal) | Yes | Yes |

Imitation Learning limitations noted in the slides: demonstration data collection can be expensive and learning is limited to the data collected; combining IL + RL is called out as "a promising area."

## RL — The Big Picture (technique map)

- **Model-based**: Markov Decision Process (Policy Iteration, Value Iteration); Dynamic Programming (Bellman optimality). Overlaps with Actor-Critic and Deep MPC toward Deep-RL.
- **Model-free, gradient-free**:
  - Off-policy: DQN, Q-Learning
  - On-policy: TD, Monte Carlo, SARSA
- **Model-free, gradient-based**: Policy Gradient optimization, DPN (policy networks).
- **Deep-RL** sits at the intersection of these (e.g. Actor-Critic, Deep MPC, DQN as deep extensions).

This maps directly onto the assessment sequence: AT1 = model-based (MDP + Dynamic Programming), AT2 = model-free (DQN/Q-learning).

## Examples Cited

- Stanford Autonomous Helicopter, Cart-pole swing-up (classic control benchmarks).
- AlphaGo / AlphaZero (game-tree search + RL; AlphaZero searches ~10,000s of positions per move vs. ~100s for a human grandmaster and ~10,000,000s for classical chess engines).
- ChatGPT/LLM alignment: RLHF pipeline — supervised fine-tuning → train a reward model from ranked comparisons → optimize the policy against the reward model using PPO (a policy-gradient RL algorithm).

## RL Libraries Mentioned

Gym (OpenAI Gym/Gymnasium), TensorFlow (Agents), TorchRL, Stable-Baselines-style toolkits, MATLAB RL Toolbox. The subject specifically uses **OpenAI Gym/Gymnasium** and **TensorFlow Agents**, run initially via Google Colab or AWS SageMaker Studio.

## Lab Notebooks (Week 1)

- `43008-GoogleDrive_Setup.ipynb` — environment/Drive setup.
- `43008-Week1-Python-Warmup(-Solution).ipynb` — Python refresher.
- `43008-OpenAIGym-Tutorial-PartA.ipynb`, `43008-OpenAIGym-Tutorial-PartB(-Solution).ipynb` — introduces Gym/Gymnasium environments (agent-environment loop in code).

## Revision Questions

- What are the six key elements of the RL framework, and how do they connect in the loop?
- Why can't RL be reduced to supervised or unsupervised learning? What's missing from each?
- Give an original example (not from lecture) of delayed consequences in a real decision problem.
- Where does AT1 (MDP + Dynamic Programming) sit on the model-based vs. model-free map, and where does AT2 (DQN/Q-learning) sit?

## LLM Follow-Up Prompt

Using the Week 1 lab notebooks (`43008-OpenAIGym-Tutorial-PartA/B`), write a short walkthrough of how the agent-environment loop shown in these slides is actually implemented in Gymnasium code (`env.reset()`, `env.step()`, etc.), keeping claims traceable to the notebook contents.
