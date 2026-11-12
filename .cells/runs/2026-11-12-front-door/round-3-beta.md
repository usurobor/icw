# Round 3 — β

Commit reviewed: `a877881da448ba20bf82ab93d019a2e75e2b557f`
Base: `216a5d6b3b03a7c44655ad9ac3f3b4f00e95b9a2`

Working tree clean, HEAD = a877881 (branch `icw-fresh`).

## Mechanical checks run

- `python3 tools/lint.py`: `0 error(s)`.
- Relative links: 22, all resolve, including the anchors.
- `git diff --stat 216a5d6 a877881`: only README.md and examples/{glider,limits,ship,wave}.md.
- `git diff 8db7422 a877881`: confined to the five B2 fixes.
- `A < X > B` forms are spaced and in code. No predecessor project named.
  "Common case" is gone from both files.

## Properties

| Property | Result | Why |
|---|---|---|
| P1 Kernel fidelity | pass | Every claim traces to the kernel. R4 and R5 are marked proposed and conditional. No pair is said to hold. Verdict names are §6's. The terms entry now separates continuity (D1) from a criterion the whole bears (D9). |
| P2 Misreadings | pass | Checked against READING #1–8, carried ≠ real, ranking and agentive phrasing. None committed. |
| P3 Prior-art accuracy | pass | The mark criterion is now worded as Salmon's, taken from Reichenbach. All other credits were verified in rounds 1–2 and are unchanged. |
| P4 Novelty claims | fail | R4's stated addition (form, not kind) is already Quine 1950, which the README credits only for the two groupings (B3-1). Addition #1's sorting is standard refinement order, unflagged (B3-2). |
| P5 Examples | pass | The new glider witness (a second glider on the same track, same phase) is correct and canonical, as in a glider stream. All other facts and witnesses are as verified before. |
| P6 Clarity | pass | The first screen holds. Terms are defined before use. No filler found. |
| P7 Notation and mechanics | pass | Lint shows 0 errors, links resolve, notation is correct. |
| P8 Footprint and scope | pass | Only matter files changed. No predecessor mention. |

## Re-check of "What ICW adds"

As asked, I re-tested each remaining addition: does it say something true
that the credited prior art does not?

- **Intro.** Credits Quine (two groupings, both directions) and Dennett (the
  same glider, derivability), and states R2 as agreement. Accurate.
- **#1 A test that can refuse.** True, and no credited source has an ordered,
  whole-relative refusal test. But "coincide / nested / cross-cut" is the
  ordinary refinement order on equivalence relations: equal, comparable, or
  incomparable. A visitor may read the classification as ICW's (B3-2, minor).
- **#2 The carrying question, placed.** Now limited to the placement:
  carrying is the last check, on both members of a pair, over one named
  changing. The type is credited as shared with Salmon. True, and not in
  Russell, Salmon, Zimmerman or Goodman as far as the matter claims. Passes.
- **#3 R4 (composition).** Not passing. The stated addition is "R4 makes it a
  consequence of the pair's form rather than of the kind of thing". Quine
  1950 already does this. He groups one collection of stages two ways, and
  concludes "River stages are water stages, but rivers are not waters". That
  is: the river's momentary stage is water, the persisting river is no water.
  He gets this from how the stages are grouped, not from what rivers are, and
  extends the same relation to income groups and persons. The README credits
  Quine only for the groupings coming apart, not for this consequence (B3-1).
  I accepted this sentence in round 2. That was a miss on my part, not a
  regression by α.
- **#3 R5 (causation).** The Davidson credit is correct. The two differences
  are true and are not Davidson's claims: criteria pick out different
  persistences in one change, and carrying is required. The first difference
  is Quine's structure again, but it is offered as a contrast with Davidson,
  not as a novelty. Passes.

## Findings

### Majors

**B3-1** · major · P4 · README.md "What ICW adds" #3, *Composition* (R4)
bullet (lines 137–141).
*Problem.* "R4 makes it a consequence of the pair's form rather than of the
kind of thing" is claimed as ICW's addition. Quine 1950 §1 already says it.
Following SEP and the FLPV text verified in round 1, he treats one collection
of stages grouped two ways and concludes "River stages are water stages, but
rivers are not waters". At a stage, the river is water; the persisting river
is no water. This follows from the groupings, not the kind, and Quine applies
the same pattern elsewhere (income groups and persons, §3). Locke's oak and
statue/clay are credited at R4, but the nearest prior art is Quine, and he is
not.
*Change.* Credit Quine at R4, e.g. "Quine already has river stages that are
water stages and rivers that are not waters." Then either:
(a) Reword the addition as "makes precise", naming what is precise and not in
Quine. Candidate: R4 is a claim about the identity-fixing reading of "consists
of", not about identity. It concedes the footprint reading and holds for any
articulated pair. Verify against Quine's text that he does not already make
that composition/identity distinction.
or
(b) Move R4 out of "What ICW adds" into the intro as agreement with Quine,
like R2.

### Minors

**B3-2** · minor · P4 · README.md "What ICW adds" #1 (lines 122–125), read
with "The test" table.
*Problem.* Checks 2 and 3 apply the ordinary refinement order on equivalence
relations: two are equal, comparable, or incomparable. That is standard
mathematics, and nothing says so. A visitor can read the coincident / nested
/ cross-cut classification as ICW's.
*Change.* Add one clause. Example: "The checks use the ordinary refinement
order on sameness relations; the addition is to run them in order, in a named
changing whole, as stated grounds for refusing a pair." No citation needed.

## Round-2 findings: status in the matter at a877881

| ID | Status | Evidence |
|---|---|---|
| B2-1 | resolved | README 107: "Today the test stops at check 4 for every pair that cross-cuts." limits.md 3–4: "A pair that cross-cuts it cannot yet refuse (O2)." "Common case" absent everywhere. |
| B2-2 | resolved | README 129–135: the addition is limited to placement; the type is credited as shared with Salmon; the contrast with causal lines and immanent causation is removed. |
| B2-3 | resolved | README 55–56: "A mark criterion that Salmon (1984) takes from Reichenbach". *The Direction of Time* is no longer implied as its source. |
| B2-4 | resolved | glider.md 54–56: second glider on the same sites in the same phase, giving same cells and arrangement but a different glider. Correct, and it supplies the missing witness. |
| B2-5 | resolved | README 74–77: continuity (D1) is a candidate; a criterion the whole bears is the carrying question (D9). |

Round-1 findings: all resolved as recorded in round-2-beta.md. B1-5's residue
was B2-2, now resolved. No regressions found.

## Protocol gaps

α reports none new. My round-2 position on α's earlier gaps stands.

## Counts

Blocker 0 · Major 1 · Minor 1

Verdict: REQUEST CHANGES
