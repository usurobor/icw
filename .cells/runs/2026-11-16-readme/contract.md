# Run 2026-11-16-readme

**Request (owner, 16 Nov, in chat).** Generate the README from the intent
with subagents. The work acceptor reviews the intent first: it accepts it, or
enters an iterate-and-converge loop with the requester. Once accepted, the
builder builds and the reviewer reviews.

**Input.** `.cells/intents/readme.md` at `7e9c99c`.
**Matter.** `README.md`; linked `examples/*.md` only where the README needs it.
**Skills.** `.cells/skills/readme`, `.cells/skills/write`, `.cells/skills/review`.
**Sources of truth.** `specs/ARTICULATION.md`, `specs/READING.md`, `PRIOR-ART.md`.

## Steps

1. **Intent acceptance.** A fresh agent decides whether the intent is
   buildable: `ACCEPT`, or `REQUEST` with numbered questions. Requests the
   requester can answer from the record are answered with the source; the
   rest go to the owner. Intent edits need owner ratification (rule 3).
2. **Build.** A fresh agent writes the README from the accepted intent.
3. **Review.** A fresh agent, with no view of the builder's reasoning, gives
   one verdict per property with one line of evidence. A cold reader reads
   only the first paragraph and restates it (I3).
4. **Rounds.** One builder commit and one reviewer verdict per round.
5. **Owner.** Reads once and rules (I1 is the owner's alone).

## Agents

All agents here are Claude models started from the requester's chat; none is
from another model family. The cross-family review is the owner's paste to
GPT. Each file in this folder names the agent and model that wrote it.

## Baseline

`runs/2026-11-12-front-door`: 8 rounds, README not accepted.
