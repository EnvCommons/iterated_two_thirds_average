# IteratedTwoThirdsAverage

[![OpenReward Environment](https://img.shields.io/badge/%E2%AD%90%20OpenReward-Environment-f7e6cc)](https://openreward.ai/GeneralReasoning/IteratedTwoThirdsAverage)

## Description

**IteratedTwoThirdsAverage** is an environment for evaluating agents on strategic reasoning about iterated dominance and opponent modeling. This environment wraps the IteratedTwoThirdsAverage implementation from [TextArena](https://github.com/LeonGuertler/TextArena), a framework for text-based game environments.

## Capabilities

- Strategic depth-of-reasoning analysis
- Opponent modeling and prediction
- Iterated dominance understanding
- Competitive gameplay against an LLM opponent

## Compute Requirements

IteratedTwoThirdsAverage does not require a sandbox. It has minimal compute requirements.

## License

[MIT](https://github.com/LeonGuertler/TextArena/blob/main/LICENSE).

## Tasks

There are two splits: train (150 tasks) and test (150 tasks). Each split contains 50 tasks across each of 3 variants:

- **IteratedTwoThirdsAverage-v0**
- **IteratedTwoThirdsAverage-v0-train**
- **IteratedTwoThirdsAverage-v0-raw**

Each task is seeded for reproducibility.

## Reward Structure

This is a sparse reward environment. Rewards are mapped from TextArena's native range of {-1, 0, 1} to {0.0, 0.5, 1.0} via `(raw + 1) / 2`.

We do not use LLM graders for this environment; reward is determined programmatically.

## Data

Game state is generated procedurally by the TextArena engine using seeded randomness. No external data files are required.

## Tools

Agents are given a single tool:

- `guess_number(number)`: Guess a number between 0.0 and 100.0. The winner is closest to 2/3 of the average.

## Time Horizon

IteratedTwoThirdsAverage is a multi-turn environment.

## Environment Difficulty

Medium-Hard - requires recursive reasoning about opponent sophistication levels and the ability to balance theoretical game theory predictions with practical opponent modeling.

## Other Environment Requirements

This environment requires an OpenAI API key (passed via secrets) to power the LLM opponent.

## Safety

Agents in IteratedTwoThirdsAverage interact only with a game theory simulation and have no access to external systems, the internet, or sensitive data. The environment does not present safety risks.

## Citations

```bibtex
@software{textarena2024,
  author    = {Guertler, Leon and Banting, Wilfried and Pignatelli, Eduardo},
  title     = {TextArena},
  year      = {2024},
  publisher = {GitHub},
  url       = {https://github.com/LeonGuertler/TextArena}
}
```
