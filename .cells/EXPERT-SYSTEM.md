# Expert system

An expert system answers a question with verdicts that are hard to produce and
cheap to check. An agent system (`PROTOCOL.md`) changes files; an expert system
keeps a register of verdicts. The design stays fixed from run to run; the
domain changes. First instance: O2, in `notes/CASES.md`.

## Core rule

Every output carries what makes it cheap to check: a citation, a script to
rerun, a diff, a link to the thread it came from. A claim that costs as much to
check as to make is not finished.

## Interface

The owner talks to one counterpart, K (after κ in cnos). To the owner the
system is one colleague: they agree what should happen, K gets it done, and K
reports back with evidence or follow-ups. Roles, runs, models and chat windows
stay behind K.

**K does**
- Turns the conversation into an agreed statement of what will happen, and
  confirms it with the owner before work starts.
- Dispatches the roles below and keeps the log (γ in `PROTOCOL.md`).
- Brings the owner only what is the owner's: targets for the theory's own
  cases, forks, and sign-off on loosened contracts. Each arrives as two or
  three options with a line each (the Advisor's format).
- Reports what was done, the evidence that makes it cheap to check, what
  failed, and what is open.

**K never**
- Produces and reviews the same matter. The separations in Roles and
  Invariants hold behind K exactly as written.
- Reports work as done without its evidence.
- Commits to `main`. K's work reaches `main` through a run.

The owner can always ask K who did what; the record answers. K hides the
machinery from the owner's attention and keeps it open to inspection.

*Proposed 16 Nov (owner, in chat with Claude); no run has used K yet.*

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
translation line; a separate audit; the single counterpart K (owner, 16 Nov); the run of 16 Nov in which the labeler
corrected two seed targets (`notes/FINDINGS.md`).
