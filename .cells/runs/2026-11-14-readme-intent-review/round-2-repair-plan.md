# Round 2 — α repair plan

Findings from `round-1-beta.md`, numbered by property in the order β gives
them. Owner decisions 1–3 in `LOG.md` bind. Files: the intent
`.cells/intents/readme.md`; Design is the new section of
`runs/2026-11-13-readme/contract.md`.

| ID | Finding | Disposition | Shown by |
|---|---|---|---|
| P1.1 | I7 added, unmarked | Fix: mark *proposed*, cite seed R6 | I7 heading |
| P1.2 | Priority tail unmarked | Fix: mark *proposed* | Status paragraph |
| P1.3 | "no jargon" weakened in I2 | Fix: quote the owner's 13 Nov words from `52d397d` verbatim; "no jargon" was Claude's paraphrase. Add a test for the "wherever … manage" clause | I2 text and test (b) |
| P1.4 | "Succinct" tested only by repeats | Fix: test the owner's reading, a sentence the reader would not miss, and a sentence serving no property | I6 "Shown by" |
| P1.5 | I8's 12 Nov quote has no record | Fix: replace with the recorded wording and its file. Defer to owner: confirm it as his | Sources |
| P1.6 | Owner words sit inside the matter | Fix: Sources points to records outside it (commits, LOG). Defer to owner: confirm every *owner* line | Sources |
| P2.1 | "concrete cases first" (109–112) | Fix: move to Design G1, owner wording restored | Design G1 |
| P2.2 | README line (131–132) | Fix: withdrawn by owner decision 1; recorded as withdrawn | Design "Withdrawn" |
| P2.3 | Pairing rule (133) | Fix: move to Design G4 in D10 terms | Design G4 |
| P2.4 | Example order (134–136) | Fix: move to Design G3 | Design G3 |
| P2.5 | Theseus placement (142) | Fix: move to Design G6 in D10 terms | Design G6 |
| P2.6 | Outline (149–162) | Fix: move to Design G7 | Design G7 |
| P2.7 | Unmarked ✅ at 67, 77 | Fix: mark *illustration* | I5, I6 |
| P2.8 | Owner how-decisions vs header | Fix: owner decision 3 and rule 9 send them to Design | Intent has none left |
| P2.9 | P2's test has no threshold; labels escape it | Defer: the review contract is γ's and the owner's. α's check: no intent line names order, placement or wording | `grep` of the intent |
| P3.1 | I1 has no blind judge | Reject: owner decision (13 Nov) and rule 6 put I1 with the owner; P1 protects that decision over P3 | I1 "Shown by" |
| P3.2 | I2 reader, ruler, pass unspecified | Fix: judge rules guesses, pass stated. Defer reader and calibration to planning (rule 5) | I2 "Shown by" |
| P3.3 | I3 no judge or rule; paragraph in view | Fix: paragraph handed back; judge marks parts 1–3 of one stated idea. Defer reader spec to planning | I3, "The idea" |
| P3.4 | I4 no reference answer | Fix: reference is the README's own statement and READING misreading 1 | I4 "Shown by" |
| P3.5 | I5 terms undefined, no pass | Fix: stops at each section's end; parts 1–3; pass stated | I5 |
| P3.6 | I6 no threshold | Fix: both lists empty | I6 |
| P3.7 | I7 runnable | No change needed | — |
| P3.8 | I8 needs sources the judge lacks | Fix: judge holds `PRIOR-ART.md`. Defer verifying its entries against sources to planning | I8 "Shown by" |
| P4.1 | I5's first stop is I3 | Fix: I5 starts after the first paragraph | I5 text |
| P4.2 | I8 overlaps I7 on ICW claims | Fix: I7 owns ICW and case claims; I8 owns credits and relations | I7, I8 |
| P4.3 | I6 test measures style | Fix: as P1.4 | I6 |
| P4.4 | Pairwise check reads headings only | Fix: α checks "Shown by" lines pairwise (round-2-alpha). Defer β's test to the review contract | round-2-alpha |
| P5.1 | I2: guessed jargon passes | Fix: test (b) fails any replaceable term | I2 (b) |
| P5.2 | I3: slogans parroted | Fix: paragraph handed back, plus one new case (*proposed*). Defer the case and the paragraph rule to planning | I3 |
| P5.3 | I4: reader names both by rote | Fix: reader names what it counts first and last | I4 |
| P5.4 | I5: no "complete" criterion | Fix: parts 1–3 | I5 |
| P5.5 | I6: digressions pass | Fix: sentence serving no property fails | I6 (b) |
| P5.6 | I7: case claims and no-claim README pass | Fix: case claims checked; a no-claim README fails I3 | I7 |
| P5.7 | I8: name-drop passes | Fix: each name needs a relation; new ❌ | I8 |
| P6.1 | Snapshot criterion vs D3, READING 3, A1 | Fix: withdrawn (decision 1); D10 terms | "The idea" part 1 |
| P6.2 | "no causation" vs R5 | Fix: R5 wording, marked proposed (decision 2) | "Supporting" |
| P6.3 | Section 0 vs O2 | Fix: refuses on stated grounds, cannot yet confirm (*proposed*) | Part 3; G7 §0 |
| P6.4 | "sufficient … incomplete" unbacked | Fix: *proposed* reading traced to R1. Defer to owner: confirm the reading | "Supporting" |
| P6.5 | Computer and body unbacked | Fix: I7 requires an application to be presented as one. Defer to owner: whether `examples/` gains them | I7 |
| P6.6 | "sequence criterion" only in O4 | Defer to owner: O4 in the kernel still uses the withdrawn terms; the kernel is outside this run | — |
| P6.7 | Conflict with owner decisions | Fix: resolved by decisions 1 and 2 | — |
| P7.1 | Three statements of the idea | Fix: one "The idea" section, used by I3, I5, I7 | "The idea" |
| P7.2 | I7 fails any README on the outline | Fix: as P6.5 | I7 |
| P7.3 | Pairing vs computer and body | Fix: computer on one machine (*proposed*). Defer to owner: the body's elemental side | Design G4 |
| P7.4 | "concrete first" vs section 0 | Defer to owner: two owner decisions conflict | Design G7 note |
| P7.5 | Status vs "each line is the owner's" | Fix: status defines *owner* and *proposed*; every line carries one | Status |
| P8.1 | 162 lines | Fix: at most 120 | `wc -l` |
| P8.2 | `wc -l` rewards long lines | Fix: wrap at 80 | line-length script |
