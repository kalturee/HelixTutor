# LumenTide

LumenTide is a personal daydream: a solo explorer's toolkit for grabbing disparate signals from tiny automation scripts, combining them into a narrative timeline, and keeping a growing journal of ideas.

## Why this project
- Capture micro-project sparks without losing the context (logs, drift notes, inspiration sources).
- Blend Web2 tooling (cron-friendly scripts, shell helpers) with Web3 experiment notes (minting hypotheses, on-chain signals) so that later work feels connected.
- Build in a way that mirrors how a developer actually iterates: short lived scripts, messy data, intentionally simple dashboards.

## Components
1. `src/scene.md` keeps a log of the current scene, including signal sources and pending experiments.
2. `tools/mixchain.py` stitches together sample data points and prints short prompts for prototypes.
3. `scripts/deploy.sh` is a scaffolding helper to simulate mission runs.
4. A lightweight journal in `notes/` and some entry templates for experiments.

## Next steps
1. Introduce a CLI entry point that can spin up a random station log.
2. Add sample data generators that mimic live signals (price jumps, bot replies, sensor blips).
3. Connect the journal entries to an automated mailer that can send weekly summaries.
