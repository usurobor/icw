# Run contract: README under the process intent

Intents: `.cells/intents/readme.md` (the matter), `.cells/intents/process.md` (the process).
Status: written before round 1, 13 Nov 2026. Measures and failure criteria are fixed from here; changing them needs owner sign-off and a line in the LOG.

## Spec gate
Can the owner verify a README directly, reliably, with less attention than a spec? Yes. No spec; the owner reviews drafts.

## Design (owner decisions)

How the README meets `.cells/intents/readme.md` (PROTOCOL rule 9). Each line binds the working cell. Moved here from the intent on 14 Nov (run `2026-11-14-readme-intent-review`, round 2) and put in the kernel's terms (D10: *elemental*, sameness of what changes; *pattern*, sameness of the change across what changes), per the owner's decision after that run's round 1. Brackets name the intent property each line serves.

- **G1 Opening shape** (owner, 13 Nov, commit `52d397d`): "concrete examples first, then the general idea." Commit `12781fe` recast this as a hint the planning cell could decline; that recasting was Claude's, so the owner's wording stands. [I1, I3]
- **G2 Lead**: the glider leads (owner, 14 Nov, this run's LOG). *Proposed* (Claude, commit `12781fe`): the "emerges from" explanation leads with it. [I1, I4]
- **G3 Examples** (owner, 14 Nov): glider, then computer, then body. This replaces the 13 Nov second case, molecules flowing through a cell; molecules go to "read next". [I3, I5]
- **G4 Pairs** (owner, 14 Nov; D10 terms after round 1): each example pairs one elemental criterion with one pattern criterion. [I3, I7]
  - Glider: each square (elemental); the glider (pattern).
  - Computer: physics fixes every voltage (owner, 14 Nov). *Proposed* (round 2), one machine over time: each part of the machine, the same part as its voltage changes (elemental); the running program, the same run as its steps pass through different parts (pattern). Both directions: one memory cell holds one program's data, later another's; one run moves through different cells.
  - Body: the living body, followed through its turnover (pattern; owner, 14 Nov). The elemental side is unnamed: the 14 Nov near-miss, organs compared through transplants, rested on the withdrawn snapshot terms. *Owner to decide.*
- **G5 Causal sentences** (owner, 14 Nov, after round 1): "the glider destroyed the block", "the program crashed the machine": each is the one change described at either level, and R5 is presented as proposed. [I3, I7]
- **G6 Theseus** (owner, 14 Nov): the ship sits beside the body, in the section on where ICW stands. By pattern sameness the repaired ship is the original, and a ship rebuilt from the old planks begins at its assembly; by sameness of the planks, Hobbes's matter verdict, the rebuilt ship is the original, and that verdict holds within its own criterion. Ship and body both persist through turnover; others repair the ship, and the body repairs itself. Whether that difference is what "carried" means is open (O2). Fission is O4. [I7, I8]
- **G7 Outline for 1.0.0** (owner, 14 Nov), one line per section on what the reader then holds: [I3, I5, I6]
  0. Title and one-sentence claim: ICW offers a test, which anyone, an LLM included, can run on a claimed pair of levels (owner, 14 Nov). *Proposed* (round 2, for O2): it refuses a pair on stated grounds and cannot yet confirm one.
  1. The glider: two ways of counting one process.
  2. The computer: sufficient yet incomplete is ordinary.
  3. The test: the four checks in plain words, the reason each refusal names, and the open last check.
  4. The body: the question of causation between levels becomes a question of identity; mind and brain in one line (Kim).
  5. Where it stands: "carried" is open; ship beside body.
  6. Read next: examples, kernel, pairs still to examine.
  7. Prior art: a few lines on how ICW relates (Craver and Bechtel, Putnam and Fodor credited; Kim and Searle named); no novelty claims; full credits in `PRIOR-ART.md`. [I8]
  - *Owner to decide:* section 0 puts a general claim before the first concrete case, against G1.
- **Withdrawn** (owner, 14 Nov, after round 1): the snapshot and sequence criteria, the README line "Squares can be counted in one snapshot. A glider needs five.", and "no causation between them".

## Rounds
- **Round 0 (baseline):** a fresh agent writes the whole README in one shot from the README intent's purpose alone. Sealed until the end.
- **Round 1** (amended 14 Nov, owner): the glider leads, per the intent's 14 Nov decisions (now Design G2–G7); Theseus moves to the status section and molecules to "read next". α writes section 1 (the glider) under the 14 Nov outline. β checks I2 (plain words), I6 (succinct), I7 (true to the kernel) before the owner sees it. The owner gives a verdict.
- **Round 2 onward:** α extends the chosen opening to a full README. β checks again. The owner gives a verdict.
- **End:** the owner compares the accepted README and the baseline blind.

## Measures
Computed from the LOG verdicts after each round.

| | Measure | Property |
|---|---|---|
| M1 | rounds to first pass; run outcome | P1 |
| M2 | minutes from owner input to the next judgeable artifact | P2 |
| M3 | owner minutes per verdict | P3 |
| M4 | reversals, by type | P3, A3 |
| M5 | escapes: owner fails a draft on I2, I6 or I7 after β passed it | P3, A5 |
| M6 | fail causes by destination; same cause in consecutive rounds | learning |
| M7 | elements of the accepted README with no intent property | P4 |
| M8 | owner minutes on `.cells/` against owner minutes on verdicts | P3 |
| M9 | blind pick, process README against baseline | P5 |
| M10 | agent wall time per round | A1 |

## Failure criteria
Each names what it falsifies and where the change goes. Thresholds are first guesses.

| | Fails if | Falsifies | Change goes to |
|---|---|---|---|
| F1 | no pass in 3 rounds | P1 | stop; back to the README intent |
| F2 | median M3 above 10 minutes | P3 | production shape (smaller drafts) |
| F3 | any escape (M5 > 0) | the β check | β's properties or oracle |
| F4 | the same fail cause in two consecutive rounds | the learning loop | where the first lesson went |
| F5 | any `unverified` reversal | A7 | spec gate; what reaches the owner |
| F6 | an element in M7 the owner cannot explain | P4 | the README intent, or cut the element |
| F7 | M8 above 1 (more time on process than on verdicts) | P3 | PROTOCOL.md, process intent |
| F8 | the baseline wins or ties M9 | the process, for this matter | the process intent itself |
| F9 | a fail with cause `unknown` that a diagnosis cannot resolve | the shape (credit assignment) | the verdict format |

## What failing means
Every failure above names the part that broke, so a failed criterion is a lesson with an address. The run fails as an experiment only if it fails in a way none of these can attribute. F8 is the one that questions the whole process: if one shot matches it, the process is overhead for READMEs, and the next test should be matter the owner cannot judge in one read.
