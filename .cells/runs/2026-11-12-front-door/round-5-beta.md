# Round 5 — β

Commit reviewed: `a11de1323c57017ef2f6dd90d51e46489597c3fb`
Parent: `732aacfa1ecf9792d2ceb42e305560bbf2351362` · Base: `216a5d6b3b03a7c44655ad9ac3f3b4f00e95b9a2`

## Checks

- HEAD = a11de13; working tree clean.
- `git diff --stat 732aacf a11de13`: README.md only, 4 insertions and 4
  deletions, within the lines named by B4-1 and B4-2. Nothing else changed.
- `git diff --stat 216a5d6 a11de13`: only README.md and examples/*.md.
  Nothing under specs/, notes/ or tools/.
- `python3 tools/lint.py`: `0 error(s)`.
- Relative links: 22, all resolve, including the anchors.
- `A < X > B` forms are spaced and in code.

## New wording checked

- **Line 42.** "River stages are water stages, but rivers are not waters."
  It is now in quotation marks, verbatim against Quine's text (FLPV ch. IV,
  verified in rounds 1 and 4), and 9 words long. Correct.
- **Line 119.** "a river is a summation of stages picked out by river kinship,
  and each of its stages is a water stage, yet no river is a water."
  - "Each of its stages is a water stage" is faithful to "River stages are
    water stages".
  - "No river is a water" is faithful to "rivers are not waters". Quine means
    that no river is identical to any water, which is what the paraphrase
    says.
  - The summation and river-kinship part is unchanged and was verified in
    round 4.

  Nothing false is introduced.
- **Lines 120–122.** "ICW's composition result agrees with him and with Locke's
  oak (R4, proposed, conditional on a pair passing)". The statue-and-clay
  clause is gone. R4 is still marked proposed and conditional, and the
  sentence still matches the kernel's R4. The only remaining statue/clay text
  is the Gibbard prior-art bullet (lines 49–53), which was verified in round 2
  and is unchanged.

## Round-4 findings: status in the matter at a11de13

| ID | Status | Evidence |
|---|---|---|
| B4-1 | resolved | Quine is quoted exactly at line 42. Line 119 is a paraphrase in different words. |
| B4-2 | resolved | "bears on the statue and its clay" is removed, and no verdict on Gibbard's case is added. |

Earlier rounds: B1-1…B1-20, B2-1…B2-5 and B3-1…B3-2 remain resolved. The
4-line diff touches none of the text those fixes rest on, except the R4
sentence, which keeps its B3-1 resolution.

## Findings

None.

## Counts

Blocker 0 · Major 0 · Minor 0

## Convergence

Every finding from rounds 1–4 (20 + 5 + 2 + 2 = 29) has an α disposition of
"fixed", and I have confirmed each fix in the matter. None was rejected. My
round-2 withdrawal of part of B1-3's suggested wording was handled as B2-1.
No blocker, major or minor finding is open.

The following were raised and are read-only or outside the matter. They are
for the owner and do not bear on the verdict:
- the kernel's "refused" vs "not a claim" wording for untyped;
- the predecessor project named in FINDINGS;
- FINDINGS' uncredited closeness to Quine;
- unconditional R4/R5 phrasing in READING and FINDINGS;
- READING's invented `colour < cars > shape` probe.

Verdict: APPROVE
