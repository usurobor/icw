# Intent: the process

**Purpose.** An iterative process for work where agents produce and a human owner judges. Each run ends in something the owner uses, and the owner comes out understanding what they built and why.

This file is the owner's theory of the process: what it is and why each part is there. P4 applies to it.

Status: draft, 13 Nov 2026.

## Shape

The process is a learning loop with two learners. The verification step is its center.

- **Verification step.** In: the output, its evidence, the intent's properties. Out: a verdict in the format below, with its cost measured.
- **Learning.** Each verdict routes a lesson to one place. The owner learns what the product is and why (the intent). The agents learn to make the next verification cheaper and more reliable (skills, checks, the judge).
- **Production.** Shaped for the next verification: small outputs, several variants, evidence attached.

## Assumptions

The properties follow from these. When one fails, the process changes as noted.

- **A1 Production is cheap.** Agents produce a draft in minutes at negligible cost next to the owner's attention.
  *If false* (long compute, physical work): fewer variants, more planning before producing.
- **A2 The owner's attention is the binding constraint.** Every artifact the owner must read costs it, process documents included.
  *If false* (a team of reviewers): spread verification; the principal still decides.
- **A3 The owner discovers what they want by judging outputs.** Criteria cannot be fully stated before seeing drafts.
  *If false* (criteria fixed and known): write the spec first and verify against it.
- **A4 One principal decides what is useful.** Others advise; one verdict counts.
  *If false* (stakeholders conflict): settle who the principal is before running.
- **A5 Agent output is fluent and unreliable, and agents misjudge their own work.**
  *If false*: none known yet. This is why β is independent of α.
- **A6 Agents keep nothing between runs except files.** Whatever the process learns must be written down: intents, skills, labels.
  *If false* (agents with durable memory): files stay the record the owner can check.
- **A7 The owner can judge the output directly and reliably.**
  *If false* (too large, too technical, effects hidden): the spec gate under P3 applies.
- **A8 Drafts are reversible until the owner accepts them.**
  *If false* (sending, deploying, publishing): verification moves before the action; the owner approves each irreversible step.
- **A9 The owner's understanding decays when they only approve.** Delegating without explaining leaves the owner unable to catch wrong output. A7 holds only while the owner's theory is current.
  *If false*: none known yet. This is why every verdict carries a written critique.

## Properties

Priority: P1 is the goal and ranks above P3, because a process tuned for cheap checks drifts toward outputs that are easy to check. P3 is the constraint. P4 keeps P3 reliable. P2 sets the pace. P5 makes all of them checkable.

### P1 Converges on a useful outcome
- **Why:** the owner judges the process by what it ships (A3, A4).
- **Invariant:** every run ends in an output the owner accepts and uses, or in an explicit stop with the reason recorded.
- **Oracle:** the last line of each run's LOG: `accepted`, `stopped: <reason>`, or neither. Neither is a failure.
- **Stop trigger:** after N rounds without a pass (default 3, owner sets), the run stops producing and returns to the intent.
- ✅ A run ends with the owner merging the output and using it the same week.
- ❌ A run keeps refining its own planning documents and never puts an output in front of the owner.
- ❌ A run stops responding and leaves no recorded reason.
- **Surface:** `.cells/runs/<id>/LOG.md`.
- **Known gap:** use shows up after shipping. The LOG records acceptance; use is checked later.

### P2 The owner judges often
- **Why:** the owner's criteria form by judging (A3), so the learning rate is set by how often a verdict happens.
- **Invariant:** the time from an owner input to the next thing the owner can judge is short.
- **Oracle:** LOG timestamps, owner input → next owner-judgeable artifact.
- ✅ Three variants in front of the owner within the session that produced the input.
- ❌ Several internal rounds over days before the owner sees any output.
- **Surface:** LOG timestamps.
- **Known gap:** no target number. The owner sets one after a few runs.

### P3 Each verdict is cheap and reliable
- **Why:** owner attention is the constraint (A2); agent output needs an independent check (A5); the owner must be able to judge (A7).
- **Invariant:** everything put in front of the owner can be judged directly and reliably in minutes. β or a machine checks everything else before it reaches the owner.
- **Oracle:** owner minutes per verdict; verdicts reversed as `unverified` (see Verdict format).
- ✅ Three short drafts, each marked pass/fail with a one-line critique.
- ❌ A large diff approved after a skim.
- ❌ A summary of evidence in place of the evidence, which the owner cannot check against its source.
- ❌ Process documents that grow faster than the outputs they govern.
- **Surface:** what the run puts in front of the owner, and the verdicts in the LOG.
- **Known gap:** owner minutes are self-reported.
- **Spec gate:** planning asks whether the owner can verify the output directly, reliably, with less attention than a spec. Yes → no spec; the owner reviews outputs, and the labels become properties in the intent. No → a contract with an oracle per AC; the owner reviews the contract.

### P4 The owner can say what the product is and why
- **Why:** the owner's theory of the product is half of what the process produces, and it is what keeps verification reliable (A9).
- **Invariant:** every element of the output traces to a property in the intent, and every property states its why.
- **Oracle:** an agent maps each element of the output to a property. An element with no property is a gap in the owner's theory or scope creep; the owner decides which.
- ✅ The owner reads an accepted output and can name, for each part, the property it serves and why that property holds.
- ❌ An accepted output contains a section nobody asked for, and the owner cannot say why it is there.
- ❌ An intent lists properties with no why.
- **Surface:** the intent file and the accepted output.
- **Known gap:** tracing shows coverage. Whether the owner holds the theory shows up when they explain it, which only the owner can do.

### P5 Every run is measured
- **Why:** the process is itself learned, and only what is measured can be improved. Measuring must not cost the owner attention (A2).
- **Invariant:** each run's contract states its measures and its failure criteria before the first round. A script computes the measures from the LOG after each round.
- **Oracle:** the contract has both sections before round 1; the measures file is regenerated from the LOG with no owner input.
- ✅ A contract names "owner minutes per verdict above 10 fails P3" before any draft exists.
- ❌ Failure criteria written after seeing the results.
- ❌ Measures the owner has to tally by hand.
- **Surface:** `.cells/runs/<id>/contract.md`, `.cells/runs/<id>/measures.md`.
- **Known gap:** the thresholds are guesses until several runs exist.
- **Baseline:** every run is compared against the same output produced in one shot with no process. The owner judges both blind. A process that does not beat its baseline is overhead.

## Verdict format

Each verdict in the LOG answers three questions. The answers route the lesson.

```
verdict:  pass | fail
critique: one line, the owner's words
cost:     owner minutes
reversal: none | criteria-changed | unverified
cause:    intent | production | check | process | unknown     (fail only)
```

| Answer | Lesson goes to |
|---|---|
| pass | ✅ label in the intent; calibration set for the judge |
| fail, cause intent | intent amendment, owner signs off |
| fail, cause production | α's skill |
| fail, cause check | β's properties or oracle; fix α too if α deviated |
| fail, cause process; or cost too high | PROTOCOL.md |
| fail, cause unknown | a short diagnosis before the next round |
| reversal criteria-changed | intent amendment (learning, counted as good) |
| reversal unverified | PROTOCOL.md (counts against P3) |

## Non-goals
- Agile ceremonies or vocabulary for their own sake.
- A generic process before a second instance.

## Lineage
Agile: short iterations with a customer in the loop (P1, P2). Lean and the Theory of Constraints: tune everything to the binding constraint (A2, P3). Karpathy's generation-verification loop and Wei's verifier's law: verification is the lever, and it can be made cheaper by front-loading work (shape, P3). Husain's critique shadowing and Shankar's criteria drift: owner labels on outputs become the spec (A3, verdict format). Naur, "Programming as Theory Building" (1985), and comprehension debt: the owner's theory is part of the product (A9, P4). Self-preference bias in LLM judges (A5).
