# Round 6 — α (under Amendment 1)

Commit: `01f1e3b5a9cb3916fbf5a1bec1eed30343a2e695`. The main change is
`7246e82`; `01f1e3b` only re-wraps one line in PRIOR-ART.md. Against base
`216a5d6`, only README.md, PRIOR-ART.md (new) and examples/*.md changed.
`python3 tools/lint.py`: 0 errors. 24 relative links, all resolving,
anchors included.

## v_form.py output

```
ok    README words 647 <= 650
ok    README first screen words 133 <= 150
ok    README has no reference list (credits live in PRIOR-ART.md)
ok    PRIOR-ART.md exists and README links to it
ok    glider.md words 494 <= 500
ok    limits.md words 460 <= 500
ok    ship.md words 412 <= 500
ok    wave.md words 264 <= 500
```

## What moved where

**README → PRIOR-ART.md, moved verbatim.**
- "A conversation 2,500 years old", every bullet: Heraclitus, Plutarch,
  Hobbes, Locke, Geach/Wiggins, Quine, Lewin/Reichenbach, Constitution
  (Gibbard), Causal persistence (Russell, Salmon/Reichenbach, Zimmerman),
  Dennett. Now under "The conversation".
- "What ICW adds": the inherited paragraph (Quine with R4 as agreement,
  Dennett with R2) and additions #1–#3 (the test, the carrying question
  placed, R5 with Davidson). Now under "What ICW inherits and what it adds".
- The full reference list. Now under "References".

**Edits made in transit.**
- "causal accounts of persistence above" became "… listed above".
- "Checks 2 and 3" became "Checks 2 and 3 of the README's test", so the file
  stands alone.

**New in PRIOR-ART.md.** Three conversation entries for works the examples
cite but the README conversation did not list:
- Goodman 1955: defined grue; "It poses his new riddle of induction".
  Verified round 1.
- Davidson 1970: one event under a mental and a physical description.
  Verified round 1.
- Gardner 1970: described Life in his *Scientific American* column. LifeWiki
  dates his first column October 1970.

All are in the existing reference list. No credit was dropped or reworded.

**README, now 647 words.**
- First screen (133 words): the three cases, the two ways of counting, the
  question, and the test with its open last check.
- "Two ways of counting" holds the terms, compressed. The continuity bullet
  still separates a continuity (D1) from what the whole bears (D9).
- "The test": §6 verdicts; the intro names "two criteria in a named whole".
- "Where this sits" is one paragraph. It names the tradition and says what is
  inherited and the narrow addition, then links PRIOR-ART.md.
- "Examples" and "What ICW does not claim" are shorter.
- The repository table became one sentence.
- Removed from the README: the conversation bullets, the additions
  discussion, the references, and the per-row "whole" phrases in the test
  table. Wholes are still named in examples/limits.md, and the test intro
  requires one.

**Examples.**
- glider.md was cut from 667 to 494 words.
  - The Davidson differences now live in PRIOR-ART.md #3; glider.md points
    there.
  - The "Derivable" section is two sentences.
  - Kept: the B3/S23 rule, both witnesses, the same-sites-same-phase witness,
    the A1 (proposed) note, R4/R5 marked proposed and conditional, and the
    Dennett credit.
- In all four examples, the header links now point to
  `../README.md#two-ways-of-counting` and `../PRIOR-ART.md`. The old anchors
  `#icws-terms` and `#references` no longer exist.
- wave, ship and limits are otherwise unchanged.

## Protocol gaps

1. **Caps leave no room for the tables.** The README is 3 words under its
   650 cap. v_form counts table rows as prose, so the test table costs about
   60 words. Any later finding that needs README text will have to be paid
   for by cutting elsewhere, as the amendment intends.
