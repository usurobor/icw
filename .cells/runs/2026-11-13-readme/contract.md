# Run contract: README under the process intent

Intents: `.cells/intents/readme.md` (the matter), `.cells/intents/process.md` (the process).
Status: written before round 1, 13 Nov 2026. Measures and failure criteria are fixed from here; changing them needs owner sign-off and a line in the LOG.

## Spec gate
Can the owner verify a README directly, reliably, with less attention than a spec? Yes. No spec; the owner reviews drafts.

## Rounds
- **Round 0 (baseline):** a fresh agent writes the whole README in one shot from the README intent's purpose alone. Sealed until the end.
- **Round 1** (amended 14 Nov, owner): the glider leads, per the intent's 14 Nov decisions; Theseus moves to the status section and molecules to "read next". α writes section 1 (the glider) under the 14 Nov outline. β checks I2 (plain words), I6 (succinct), I7 (true to the kernel) before the owner sees it. The owner gives a verdict.
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
