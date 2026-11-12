# Round 1 — α

Commit: `8fcc0c7` (parent 7e4f87e, the seed). Only `intents/readme.md` changed
against BASE. File: 119 lines.

## Converged or iterated

Iterated. The seed's four owner intents are kept; their tests were not
runnable blind or reproducibly.

## What changed and why

- **IDs R1–R6 → I1–I5.** The kernel numbers its results R1–R6; a judge holding
  both files would confuse "R2". Kernel items are now cited as kernel IDs.
- **No reference to skills anywhere.** The seed's intro mentioned skills; the
  task says the file must not refer to any.
- **Ground rules added** so tests are reproducible: what "paragraph one" is
  (any first block, so a tagline cannot dodge it); reading order (title and
  paragraph one judged before the rest, kernel last, so the judge's kernel
  knowledge cannot fill gaps); what a technical term is, with a fixed list;
  what "explained" means; a word-count rule that counts hidden text; every
  verdict must quote the README.
- **Misreadings M1–M8 inline.** The judge holds only this file, the README and
  the kernel, not specs/READING.md, so the excluded readings are summarised
  here with kernel IDs. M6 is report-only because READING marks it under review.
- **Owner priority stated.** The owner ranked clarity and drawing-in highest;
  the seed dropped that. Now: failing I1 or I3 ranks below passing both.
- **I1** replaced "would you read on? 1–5" (not reproducible, gameable by
  clickbait) with checks on case, question, stake, nothing before
  paragraph one, and promise kept. The seed's proposed R5 ("why it matters")
  overlapped I1 and is folded in as I1(c), marked proposed.
- **I2** now matches restatement against elements E1–E3 quoted from paragraph
  one, not against free wording; adds unfolding (no term before explanation,
  no stopping point that a later section must correct or that is a
  misreading); paragraph one capped at 100 words so "paragraph one" cannot
  swallow the README.
- **I3** strengthened, not weakened: seed allowed 2 unclear items; now zero
  technical terms in paragraph one, all explained elsewhere, plus a
  sentence-level paraphrase test (plain words can still be opaque).
- **I4** seed test inverted the cut question ("nothing essential flagged as
  cuttable"); now a closed list of what a sentence must do, and redundancy.
  600 words (current README is about 652 by the rule).
- **I5 (proposed) faithful**: seed R6, with explicit pass items: proposed or
  declared kernel items not presented as settled; README must say the carrying
  check cannot yet be passed; meaning-changing plain words fail (carried ≠ real).
- **Reference answer** rewritten. The seed's "two honest ways to say what
  stays the same" leaned towards articulation-as-description (D9 excludes,
  READING 2 and 4) and "when both count" was too vague to fail a wrong
  restatement. New text: two ways of staying the same (stuff, pattern), both
  directions, neither ranked real, the whole's own changing decides, last step
  open. Checked against READING 1–8.
- **Grounding**: Turing 1950, Bostrom 2003, semver.org 2.0.0, Goh/Distill 2017,
  Wikipedia "Ship of Theseus" lead; each opening verified by fetch on
  2026-11-12.

## Protocol gaps

- The contract says the judge holds only intent, README and kernel, but AC6
  checks against specs/READING.md; I resolved this by restating READING's
  misreadings inside the intent. β should check the restatement for fidelity.
- Who the "reader" is in a blind test is unstated by the contract; I made the
  judge the reader and required quoted evidence instead of simulated personas.
- The 600-word and 100-word thresholds are α's choice, not the owner's;
  owner may adjust.
