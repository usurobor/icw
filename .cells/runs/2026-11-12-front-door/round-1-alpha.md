# Round 1 — α

Commit: `9ec0b37fb7778a6e2dab7a5d7943f7eec82a46b8` (base `216a5d6`). Only
README.md and examples/*.md changed. `python3 tools/lint.py`: 0 errors. All
relative links and anchors resolve.

## Changes

README.md
- First screen: the question, three canonical cases (wave, glider, ship), and
  ICW's next question (sustained by the changing vs laid across it).
- Prior art rewritten from verified sources. Added Hobbes's own answer
  (identity depends on what the name is given for: matter or form, De Corpore
  II.11.7). This is prior art for criterion-relativity, so ICW does not claim it.
  Added Quine 1950 in both directions ("same river twice without the same water;
  same water twice in two rivers"), Lewin 1922 / Reichenbach 1956 (genidentity),
  constitution (Gibbard 1975), and Geach vs Wiggins kept apart (relative identity
  vs sortal dependence without it). Dropped "no entity without identity": it is
  from "Speaking of Objects" (1958), not the 1950 paper it was cited to.
- Terms defined before use: criterion/continuity, footprint, refines,
  cross-cut, carried, articulated, `A < X > B`. Where IDs appear is explained.
- Test table uses only §6 verdict names. Every cross-cutting pair, cell/glider
  included, is reported as **uncarried** (pending O2). "Cross-cuts" is named as
  the strongest available finding. "holds" appears only as the unreached row.
- Novelty narrowed: Quine is credited with the two-groupings structure. ICW's
  claims are now the ordered refusing test, the carrying question placed as the
  last check (with Goodman credited for the natural/gerrymandered problem), the
  R1–R3 separations, and R4/R5. R4 and R5 are marked proposed and conditional on
  a pair passing. Removed the agentive "two criteria articulate one whole".
- Removed the old claim "still not made of cells" as an unconditional fact. It
  needs R4, which is proposed and conditional.

examples/
- glider: A1 now marked proposed. The glider criterion no longer reads
  "same organization" (READING #6: not arrangement-sameness). The
  "replace every cell" wording is replaced by a checkable fact (no shared cell
  after 16 steps). R4/R5 are conditional. The verdict is stated. Davidson (1970)
  is noted as nearest prior art for R5, and Dennett's reality claim is kept
  separate from ICW's question.
- wave: physics corrected to near-closed orbits with a small net drift. Both
  witnesses are stated. The whole is named as the sea. The verdict is stated.
  R4/R5 are conditional. Uses of "carry" in its ordinary sense are removed
  (D8 collision).
- ship: Hobbes's answer is credited, so ICW no longer claims to dissolve the
  puzzle. Its addition is limited to the checkable cross-cut and the open
  carrying question. R4 is conditional.
- limits: charge/field in electrostatics removed. Electrostatics is static, so
  check 1 makes it untyped, not coincident; it also needs boundary conditions
  for charge to fix the field. It is replaced by Locke's mass/atoms (coincident
  by Locke's own definition). The colour/shape-of-cars pair (invented, AC3) is
  replaced by Goodman's green/grue, with both witness directions.

## Protocol gaps (read-only files; not edited)

1. **"Cross-cuts" vs §6 names.** The brief says "cross-cuts" is the strongest
   verdict. REVIEW-PROPERTIES P1 says verdict names must match §6, which has no
   "cross-cuts" verdict: a cross-cutting pair gets **uncarried**. The matter
   uses "uncarried" as the verdict and "cross-cuts" as the furthest check
   passed. The §6 "holds" row is unreachable while O2 is open. The kernel could
   say so.
2. **D9 makes "articulation" presuppose carrying.** Every use of "two
   articulations" for a specific pair therefore asserts carrying. The kernel's
   own Statement ("Each can hold where the other does not") uses "hold" for
   continuities, which collides with the "holds" verdict. READING's probe
   wording "two articulations of one grid" (#7) does the same.
3. **R4/R5 are conditional on `A < X > B`, which no pair can reach while O2 is
   open.** Their applications in READING (#1, probes) and FINDINGS read as
   unconditional ("composition does not hold across quotients at all").
4. **REVIEW-PROPERTIES P5 cites Gauss's law**, which implies the charge/field
   example. That example fails check 1 (electrostatics has no changing).
5. **READING's probe `colour < cars > shape`** is an invented case. AC3 bars
   such cases from the matter only.
6. **FINDINGS ("Carrying cannot be another relation", Source paragraph)
   names a predecessor project.** AC7 bars this from the matter only. Visitors
   following the README link to FINDINGS will still see it.
7. **Reichenbach locator.** I could confirm that *The Direction of Time*
   (1956) contrasts material with functional genidentity, but not the section
   number or a water-wave example. The matter therefore cites the book without
   a locator and claims no example.
