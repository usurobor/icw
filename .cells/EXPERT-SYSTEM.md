# Expert system

An expert system answers a question with verdicts that are hard to produce and
cheap to check. An agent system (`PROTOCOL.md`) changes files; an expert system
keeps a register of verdicts. The design stays fixed from run to run; the
domain changes. First instance: O2, in `notes/CASES.md`.

## Core rule

Every output carries what makes it cheap to check: a citation, a script to
rerun, a diff, a link to the thread it came from. A claim that costs as much to
check as to make is not finished.

## Roles

| Role | Does | Never | Independent of |
|---|---|---|---|
| Owner | Sets targets for cases that state the theory's own claims; rules on probes; decides forks | Delegates those targets | — |
| Labeler | Labels literature cases: citation, plus one line translating the source's conclusion into the register's vocabulary | Decides what the theory claims; forces a label | Proposer (other model family) |
| Auditor | Checks each label: the source exists, the locator holds, the attribution is fair, the translation follows. Ends `AUDIT: PASS` or `AUDIT: CHANGES` | Re-labels from scratch | Labeler (other model) |
| Proposer | Proposes candidate definitions, literature first | Changes a candidate and a target in one round | Labeler |
| Evaluator | Applies a candidate to every case: a script where the domain can be computed, otherwise a blind panel | Sees targets (panel) | Panel members of different families, blind to each other |
| Hunter | Knows the candidate; proposes cases it gets wrong | Sets targets | — |
| Advisor | Before an owner decision: two or three options, one line each | Decides | — |

## Artifacts

- **Register.** One row per case: the pair, the target, who set it (owner, or
  literature with citation and translation), role (anchor+, anchor−, probe,
  regression, source, parked), evaluator, audit status.
- **Candidates.** One row per definition, with its source.
- **Findings.** Every decision and every label change, with the reason and the
  thread or commit it came from.
- **Audits.** `notes/audits/<date>-<name>.md`, one per audited batch.
- **Harness.** Scripts for the cases a program can evaluate.

## Loop

1. **Seed.** Cases from the project's own material, checked against its
   current definitions, plus a limited literature search.
2. **Label.** Owner labels the theory's own cases. Labeler labels the
   literature cases; Auditor audits; owner reads the translations once.
   Labels freeze.
3. **Fit.** Evaluator runs every candidate on every case, starting with a toy
   domain a script can decide. A candidate passes when every verdict matches its
   target.
4. **Hunt.** Hunter adds cases. Owner sets each new target before seeing the
   candidate's verdict. New cases go through step 2.
5. **Break the toy.** A passing candidate meets cases that break the toy
   domain's assumptions.
6. **Stop rule.** Three successive revisions fall to new counterexamples:
   question the form of the concept before revising again.

## Writing an output

For a README, post or pitch. The owner leads on substance; the expert leads on
craft (structure, first screen, one running example) and facts. On substance,
the expert holds accepted items steady and flags drift. Iteration follows
`DIALOGUE.md`.

1. **Lock theses first.** Before any draft, the expert sets out the owner's
   core claims as two or three candidate statements; the owner picks or
   rewrites. Picked theses are pinned in the understanding doc.
2. **Check before showing.** Every draft passes three checks before the owner
   reads it: the language guard below, the examination format where the
   domain has one, and a cold read by a model of another family.
3. **Run facts.** A claim a script can check is checked before it is
   written.
4. **Pinned theses stay.** Caveats follow them (`DIALOGUE.md` rule 10).
5. **Metric: regressions.** A regression is a round in which the owner
   restates an accepted item. Target zero. Rounds that add an accepted item
   are the work.

**Language guard (ICW).** Everyday wording carries the bottom-up picture ICW
questions, and drafts drift back to it.

- Out: "made of", "consists of"; possessives for elements ("its squares");
  "emerges from" outside a quoted claim; "stays the same" said of the whole;
  "real"; "base", "more basic" (except in denial); "view", "perspective";
  "description" for an articulation; anything "calculated from the squares"
  (the rule takes snapshot to snapshot).
- In: "told two ways"; "elemental telling", "pattern telling"; "lights",
  "shows up as"; "snapshot"; "produces" only for the reading ICW rejects.

**Examination format.** Whole first, then Element, Pattern, Claim, Open
(README, "How to examine a case").

## Invariants

- Targets are set before a candidate runs, by someone other than the
  Proposer.
- A candidate and a target never change in the same round. A label changes
  only with a logged reason.
- Success means matching the targets, never that every case passes.
- Refusals are answers: *no clean translation*, *unverified*, *void*.
- Roles that could share blind spots run on different model families:
  Labeler and Proposer, Labeler and Auditor, panel members.
- Every lesson written into a role's instructions cites the thread or commit
  it came from, so a bad one can be traced and removed.
- Every run reports its guards: share of cases refused, candidate length,
  record of probe predictions.

## Provenance

Assembled 16 Nov 2026 from the O2 sessions: the match-target rule and the
anchor/probe split; owner-only thesis labels; labels with citation and
translation line; a separate audit; the run of 16 Nov in which the labeler
corrected two seed targets (`notes/FINDINGS.md`).

Writing an output: the README dialogue of 16–17 Nov 2026, README 0.0.21 to
0.0.30 (commits `1aee04a` to `61e7eab`), record in
`runs/2026-11-16-readme-dialogue/`. Roughly a third of rounds were the expert
reintroducing wording the owner had rejected (squares as what changes, "made
of parts", "more real", "calculated from the squares"); about a sixth were
defensive edits by both models that buried the thesis. A cold read by a
second model found a factual error about the glider and six confusions in one
pass, after the owner had already read those drafts.
