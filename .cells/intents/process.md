# Intent: the process

**Purpose.** Build anything with AI agents (a README, a pitch, code, a theory) so that each run ends in something the owner uses, at a pace the owner's attention can sustain.

**Why now.** Agents make production nearly free. The scarce resource is the owner's judgment. Most AI-augmented processes fail at that point: output grows faster than anyone can check it, and review turns into rubber-stamping.

**Priority.** P1 is the goal. P3 is the constraint: every rule in PROTOCOL.md is tuned for it. P2 follows from P3.

Status: draft, 13 Nov 2026. P1–P3 stated by the owner; P4 proposed by Claude, owner to confirm.

## Properties

### P1 Converges on a useful outcome
- **Invariant:** every run ends in an output the owner accepts and uses, or in an explicit stop with the reason recorded.
- **Oracle:** the last line of each run's LOG: `accepted`, `stopped: <reason>`, or neither. Neither is a failure.
- ✅ `tools/lint.py`: written once, runs on every commit, caught the unspaced `A<X>B` render bug.
- ❌ cnos: months of rounds, a 3,588-line CDS.md marked "v0.1 complete", nothing used outside cnos.
- ❌ Run 2026-11-12-readme-intent: five rounds, ended with an intent awaiting confirmation and no README.
- **Surface:** `.cells/runs/<id>/LOG.md`.
- **Known gap:** "uses" shows up after shipping. The LOG records acceptance; use is checked later by the owner.

### P2 Iterations are quick
- **Invariant:** the time from an owner input to the next thing the owner can judge is short.
- **Oracle:** LOG timestamps, owner input → next owner-judgeable artifact.
- ✅ Three README openings in front of the owner within one session.
- ❌ Two days of intent rounds before the owner saw any README.
- **Surface:** LOG timestamps.
- **Known gap:** no target number yet. The owner sets one after a few runs.

### P3 Human verification is cheap
- **Invariant:** everything put in front of the owner can be judged directly and reliably in minutes. Everything else is checked by β or a machine before it reaches the owner.
- **Oracle:** owner minutes per verdict; verdicts the owner later reverses (an unreliable judgment counts as an expensive one).
- ✅ README drafts reviewed directly, three at a time, pass/fail with a one-line critique.
- ❌ A 2,000-line agent diff approved after a skim.
- ❌ γ condensed reader answers into a summary; the owner could not check it against the raw answers.
- **Surface:** what the run puts in front of the owner, and the owner's verdicts in the LOG.
- **Known gap:** owner minutes are self-reported.
- **Spec gate (follows from P3):** planning asks whether the owner can verify the output directly, reliably, with less attention than a spec. Yes → no spec; the owner reviews outputs, and the labels become properties in the intent. No → a contract with an oracle per AC; the owner reviews the contract.

### P4 The process stays smaller than its product (*proposed by Claude*)
- **Invariant:** the owner spends less attention on the process than on the outputs it produces.
- **Oracle:** owner time on `.cells/` (protocol, intents, skills) against owner time on outputs, per run.
- ✅ PROTOCOL.md fits on one page.
- ❌ cnos: protocol doctrine grew far larger than any product it shipped.
- **Surface:** `.cells/` size and the LOG.
- **Known gap:** early runs invest in the process on purpose. Judge over several runs.

## Non-goals
- Agile ceremonies or vocabulary for their own sake.
- A generic process before a second instance (README is the first, pitch the likely second).

## Lineage
Agile's short iterations with a customer in the loop (P2), Lean and the Theory of Constraints (P3 as the constraint everything serves), Husain's critique shadowing and Shankar's criteria drift (owner labels on outputs become the spec).
