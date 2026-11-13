# Intent: the process

**Purpose.** An iterative process for work where agents produce and a human owner judges: each run ends in something the owner uses, and the owner learns what they want by judging outputs.

Status: draft, 13 Nov 2026.

## Assumptions

The properties follow from these. When one fails, the process changes as noted.

- **A1 Production is cheap.** Agents produce a draft in minutes at negligible cost next to the owner's attention.
  *If false* (long compute, physical work): fewer variants, more planning before producing.
- **A2 The owner's attention is the binding constraint.** Every artifact the owner must read costs it, process documents included.
  *If false* (a team of reviewers): spread verification, and the principal still decides.
- **A3 The owner discovers what they want by judging outputs.** Criteria cannot be fully stated before seeing drafts.
  *If false* (the criteria are fixed and known): write the spec first and verify against it.
- **A4 One principal decides what is useful.** Others advise; one verdict counts.
  *If false* (stakeholders conflict): settle who the principal is before running.
- **A5 Agent output is fluent and unreliable, and agents misjudge their own work.** A plausible draft can be wrong, and a producer grading itself is biased.
  *If false*: none known yet. This assumption is why β is independent of α.
- **A6 Agents keep nothing between runs except files.** Whatever the process learns must be written down: intents, skills, labels.
  *If false* (agents with durable memory): files remain the record the owner can check.
- **A7 The owner can judge the output directly and reliably.**
  *If false* (too large, too technical, effects hidden): the spec gate under P3 applies.
- **A8 Drafts are reversible until the owner accepts them.** Nothing reaches anyone else before a verdict.
  *If false* (sending, deploying, publishing): verification moves before the action, and the owner approves each irreversible step.

## Properties

### P1 Converges on a useful outcome (A3, A4)
- **Invariant:** every run ends in an output the owner accepts and uses, or in an explicit stop with the reason recorded.
- **Oracle:** the last line of each run's LOG: `accepted`, `stopped: <reason>`, or neither. Neither is a failure.
- ✅ A run ends with the owner merging the output and using it the same week.
- ❌ A run keeps refining its own planning documents and never puts an output in front of the owner.
- ❌ A run stops responding and leaves no recorded reason.
- **Surface:** `.cells/runs/<id>/LOG.md`.
- **Known gap:** use shows up after shipping. The LOG records acceptance; use is checked later.

### P2 The owner judges often (A3)
- **Invariant:** the time from an owner input to the next thing the owner can judge is short.
- **Oracle:** LOG timestamps, owner input → next owner-judgeable artifact.
- ✅ Three variants in front of the owner within the session that produced the input.
- ❌ Several internal rounds over days before the owner sees any output.
- **Surface:** LOG timestamps.
- **Known gap:** no target number. The owner sets one after a few runs.

### P3 Each judgment is cheap (A2, A5, A7)
- **Invariant:** everything put in front of the owner can be judged directly and reliably in minutes. β or a machine checks everything else before it reaches the owner.
- **Oracle:** owner minutes per verdict; verdicts the owner later reverses (an unreliable judgment counts as an expensive one).
- ✅ Three short drafts, each marked pass/fail with a one-line critique.
- ❌ A large diff approved after a skim.
- ❌ A summary of evidence in place of the evidence, which the owner cannot check against its source.
- ❌ Process documents that grow faster than the outputs they govern.
- **Surface:** what the run puts in front of the owner, and the verdicts in the LOG.
- **Known gap:** owner minutes are self-reported.
- **Spec gate:** planning asks whether the owner can verify the output directly, reliably, with less attention than a spec. Yes → no spec; the owner reviews outputs, and the labels become properties in the intent. No → a contract with an oracle per AC; the owner reviews the contract.

P2 and P3 are independent. P2 sets how often the owner judges; P3 sets what each judgment costs. Together they set how fast the owner learns what they want per unit of attention.

## Non-goals
- Agile ceremonies or vocabulary for their own sake.
- A generic process before a second instance.

## Lineage
Agile: short iterations with a customer in the loop (P1, P2). Lean and the Theory of Constraints: tune everything to the binding constraint (A2, P3). Husain's critique shadowing and Shankar's criteria drift (A3: owner labels on outputs become the spec). Self-preference bias in LLM judges (A5).
