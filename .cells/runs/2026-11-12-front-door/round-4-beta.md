# Round 4 — β

Commit reviewed: `732aacfa1ecf9792d2ceb42e305560bbf2351362`
Base: `216a5d6b3b03a7c44655ad9ac3f3b4f00e95b9a2`

Working tree clean, HEAD = 732aacf (branch `icw-fresh`).

## Mechanical checks run

- `python3 tools/lint.py`: `0 error(s)`.
- Relative links: 22, all resolve, including the anchors.
- `git diff --stat 216a5d6 732aacf`: only README.md and examples/*.md. Nothing
  under specs/, notes/ or tools/.
- `git diff a877881 732aacf`: README "What ICW adds" only.
- `A < X > B` forms are spaced and in code. No predecessor project named.

## Properties

| Property | Result | Why |
|---|---|---|
| P1 Kernel fidelity | pass | R4, now stated as agreement, is marked proposed and conditional and matches the kernel's R4. R5 is unchanged and faithful. No pair is said to hold. Verdict names are §6's. |
| P2 Misreadings | pass | READING #1–8, carried ≠ real, ranking and agentive phrasing re-checked. None committed. |
| P3 Prior-art accuracy | pass | The new Quine paraphrase is faithful (verified below). Quine's sentence is used verbatim without quotation marks (B4-1, minor). |
| P4 Novelty claims | pass | Each remaining addition re-tested below. None is already in the credited prior art. |
| P5 Examples | pass | Unchanged since round 3, all checked then. |
| P6 Clarity | pass (one minor) | "Bears on the statue and its clay" says nothing definite, and is misleading for the one statue/clay case the README describes (B4-2). |
| P7 Notation and mechanics | pass | Lint shows 0 errors, links resolve, notation is correct. |
| P8 Footprint and scope | pass | Only matter files changed. No predecessor mention. |

## Verification of the new Quine wording (web, FLPV text, ch. IV)

- "River stages are water stages, but rivers are not waters." Verbatim in
  Quine, 9 words. README lines 42 and 119 use it word for word without
  quotation marks (B4-1).
- "a river is a summation of stages picked out by river kinship" is a fair
  paraphrase. Quine has "'This river' means 'the riverish summation of
  momentary objects which contains this momentary object'", and "a and b stand
  in the relation of river kinship".
- Crediting Quine with "the consequence for composition" is accurate. The
  river is a summation of stages, each a water stage, yet the river is not a
  water.
- Quine does not discuss statues or clay in this passage, and the matter does
  not say he does.

## Re-test of "What ICW adds"

- **Intro (inherited).** Credits Quine for the two groupings and for
  composition (this resolves B3-1), Locke's oak, and Dennett for the same
  glider and derivability. States R4 and R2 as agreement. Accurate. R4 is
  marked proposed and conditional.
- **#1 A test that can refuse.** Now credits checks 2–3 as the ordinary
  refinement order ("two are equal, one is finer, or neither is"; correct).
  The remaining addition is running the checks in order, in a named changing
  whole, with both directions witnessed, as stated grounds of refusal. True.
  Nothing credited (Quine, Hobbes, Locke, Geach, Wiggins, Dennett) has this.
  Passes.
- **#2 The carrying question, placed.** Unchanged since round 3. Placement
  only, type credited as shared with Salmon. Passes.
- **#3 R5.** Unchanged in content; the heading now covers R5 alone.
  Davidson credited, and both stated differences are true and not his.
  Passes.
- **Anything a visitor would read as novel but isn't?** I re-read the hook,
  the terms and the test commentary with this in mind. "ICW brings the two
  together for a pair of criteria in one changing whole" claims only the
  combination, which matches #1–#2. I found nothing else.

## Findings

### Minors

**B4-1** · minor · P3 · README.md line 42 (Quine bullet) and line 119 ("What
ICW adds" intro).
*Problem.* "river stages are water stages, but rivers are not waters" is
Quine's sentence word for word, but it is given without quotation marks, so it
reads as the README's paraphrase. Line 42 has done this since round 1. I
should have caught it then.
*Change.* Put it in quotation marks in at least one place, preferably line 42
where Quine is introduced: "River stages are water stages, but rivers are not
waters". It is exact and under 15 words. At line 119 either quote it again or
paraphrase it in different words.

**B4-2** · minor · P6 · README.md "What ICW adds" intro (line 120–121: "and
bears on the statue and its clay").
*Problem.* "Bears on" asserts nothing definite. It is also misleading for the
one statue/clay case the README describes: Gibbard's, where statue and lump
come into being and perish together. In that case the two never come apart in
the actual history, so the pair would stop at check 2 (coincident) and R4,
which needs `A < X > B`, would not apply. R4 bears only on versions where they
come apart, e.g. the clay squeezed and outlasting the statue.
*Change.* Choose one:
- Drop "and bears on the statue and its clay".
- Make it definite, e.g. "and applies to the statue and its clay only where
  the two come apart, as when the clay outlasts the statue".

Do not add a verdict on Gibbard's case unless it is run as an example.

## Round-3 findings: status in the matter at 732aacf

| ID | Status | Evidence |
|---|---|---|
| B3-1 | resolved | README 116–123: R4 removed from the additions and stated as agreement with Quine (composition consequence credited) and Locke's oak, proposed and conditional. Option (b), as offered. |
| B3-2 | resolved | README 125–126: checks 2–3 credited as the ordinary refinement order. The addition is narrowed to the ordered, whole-relative, both-directions refusal test. |

Earlier rounds: B1-1…B1-20 and B2-1…B2-5 remain resolved. The only changed
section was re-read in full, and no earlier fix regressed.

## On α's new protocol gap

1. **FINDINGS' four-dimensionalist reply is close to Quine's "riverish
   summation", uncredited.** Agreed. It is close, and it sits in a read-only
   file outside the matter. It is for the owner. It does not affect this
   verdict.

## Counts

Blocker 0 · Major 0 · Minor 2

## Verdict note

REVIEW-PROPERTIES allows APPROVE because there are no open blocker or major
findings and every prior finding is resolved. CONTRACT's convergence rule
also requires an α disposition for every finding, including B4-1 and B4-2.
So the cell should not close on this verdict until α disposes of them (fixed,
or rejected with a reason I accept). Both fixes are wording-only. If α fixes
them as specified with no other change, I expect to confirm on the next
commit without a full re-review.

Verdict: APPROVE
