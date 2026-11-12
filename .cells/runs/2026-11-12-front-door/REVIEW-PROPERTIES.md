# β review properties

Review the matter (README.md, examples/*.md at a named commit) against
CONTRACT.md. Be adversarial: your job is to find what is wrong, not to confirm
what is right. Check every property on every round, not only the findings you
raised before.

## P1 Kernel fidelity (AC4)
- Every substantive claim traces to an item in `specs/ARTICULATION.md`. Cited
  IDs exist and say what the matter claims they say.
- Proposed items (A1, R4, R5) are marked proposed wherever they are relied on.
- No pair is said to hold / co-articulate / pass while carrying (D8) is
  undefined. "Cross-cuts" is the strongest verdict available today.
- Verdict names match §6 of the kernel.

## P2 Misreadings (AC5)
Check the matter against every entry in `specs/READING.md`: levels (causation
or production between articulations), substrate vs description, instant vs
whole, observer creates the inventory, determination confused with identity,
configuration as a form's state, the signs read as arrows/sameness/order, the
whole as articulator. Also: *carried* read as *real*; any ranking of one
articulation above another; any agentive phrasing ("X articulates itself").

## P3 Prior-art accuracy (AC2)
- Each attribution is correct: right author, right work, right claim. Verify
  by web search; do not trust memory. Check locators (fragment numbers,
  chapter/section numbers, years).
- No misattribution between neighbours (e.g. Geach's relative identity vs
  Wiggins's sortal dependence, which Wiggins holds without relative identity).
- Paraphrases are faithful. Quotations, if any, are exact and under 15 words.
- Relevant prior art is not omitted where ICW's claims overlap it
  (e.g. genidentity: Lewin, Reichenbach; Dennett's "Real Patterns" on Life
  gliders; constitution debates such as statue and clay).

## P4 Novelty claims (AC2)
- Every "ICW adds" claim is something the credited prior art does not already
  say. If prior art says it, the claim must be withdrawn or reworded as
  "makes precise" with the precise addition named.
- No overclaiming in tone ("solves", "dissolves") where the kernel only
  conditions.

## P5 Examples (AC3)
- Only widely known cases. Flag anything niche, invented, or contested.
- Each example's two criteria are stated, and witnesses are given in **both**
  directions (same A, different B; same B, different A).
- The whole X in `A < X > B` is a changing whole that plausibly contains both
  continuities' occurrences.
- Technical facts are correct (e.g. Life glider period and displacement; water
  parcels in a deep-water wave move in near-closed orbits; Gauss's law;
  temperature as a function of microstate).

## P6 Clarity (AC1, AC6)
- First screen states the question and earns the next screen.
- A careful non-specialist can follow every paragraph. Terms are defined
  before use; IDs in the README are either explained or unnecessary.
- No filler, no repetition, no hedging that carries no information.

## P7 Notation and mechanics (AC8)
- `A < X > B` spaced or in code everywhere; read as "X is articulated as A
  and B".
- Run `python3 tools/lint.py` and check every relative link resolves.

## P8 Footprint and scope (AC7, read-only files)
- Nothing outside README.md and examples/ was changed (check `git diff
  --stat` against the base).
- No section or file without a job. No mention of any predecessor project.

## Severity
- **blocker**: false, misattributed, contradicts the kernel, or commits a
  listed misreading.
- **major**: overclaims, omits needed prior art, unclear at a point a visitor
  must understand, example lacks a direction.
- **minor**: wording, compression, ordering.

## Verdict
- **APPROVE** only if there are no open blocker or major findings and every
  prior finding is resolved or its rejection is acceptable to you.
- Otherwise **REQUEST CHANGES**.

---

## Amendment 1 (ε, after round 5)

These change how form is judged. Apply them every round.

## P9 Form (AC1, AC6, AC7, AC9)
- Run `python3 /home/claude/icw-cell/v_form.py /home/claude/icw-cell/repo`.
  Any FAIL is a **blocker**.
- **First-time reader test.** Read only the README's first screen, as a smart
  non-specialist who has never heard of ICW. In one line, write what it made
  you want to read next. If the honest answer is "nothing", that is a
  **major** finding (AC1).
- A README that reads as a literature review before it shows the idea is a
  **major** finding (AC6), whatever its accuracy.
- Prior art in the README beyond a brief naming of the tradition, with a link,
  is a **major** finding: it belongs in PRIOR-ART.md.

## Severity changes
- Form defects that a first-time visitor would hit (hook, clarity of the
  central idea, length) are **major**, not minor.
- A fix to a P3/P4 finding that adds README text past the caps does not
  resolve it.

## Accuracy still applies
P1–P5 apply to PRIOR-ART.md as well as README and examples. Moving text must
not lose or distort a credit.
