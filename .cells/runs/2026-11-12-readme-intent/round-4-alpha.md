# Round 4 — α

Commit: `39049a9` (parent 67a2515). Changed against BASE: `intents/readme.md`
(27 lines) and `intents/readme-key.md` (139 lines, 122 excluding
Grounding). Together that is 149 lines excluding Grounding, under the 150
limit.

## Design

- **Two labels.** *In force* means proposed by the writer and counted until
  the owner changes it. *Reported* means scored, not counted. Only I5 is
  reported; everything else counts. **Owner to approve** marks what the owner
  must ratify; it stays in force meanwhile.
- **Calibration** is now a procedure someone can run literally.
  - Each fixture is a short README with a fixed title,
    `# Identity in Changing Wholes`.
  - Each fixture gets three fresh readers of the run's kind, used for nothing
    else. They do the whole sheet on it exactly as on a README.
  - Each fixture has one row stating what must happen and which answer must
    show it. A fail for another reason does not count. If any row does not
    hold for two of three readers, the run is void.
- **Fixtures**, all owner to approve:
  - P, the reference opening: must pass I1 Step 1, I2 and I3 Step 1.
  - F1 for I1 (plain, accurate, dull inventory): must draw A2 "no".
  - F2 for I2 (plain, engaging, gives the emergence and "more real" misreading):
    A1 must repeat that misreading.
  - F3 for I3 (the kernel's Statement): A3 must flag something.
  - F4 for I4 (P followed by a paragraph that restates it): A5 must flag the
    restatement.

## Dispositions

| ID | Sev | Disposition | What changed |
|---|---|---|---|
| B3-1 | major | Fixed | "Proposed" is replaced by two defined labels. In force: reader kind, administration, scoring, the opening rule (25 and 100), the 600-word limit and I1's A6 clause; all of these count. I5 alone is reported. "Overall" now says that in force clauses count. |
| B3-2 | major | Fixed | Adds F1, an opening that is plain, accurate and dull, which must draw A2 "no" from two of three readers. A panel that says yes to everything now voids the run. Every fixture's row states the clause it must fail and the answer that must show it, so a fail for the wrong reason does not calibrate. Each reader-based intent has its own known fail (F1 for I1, F2 for I2, F3 for I3, F4 for I4), as Amendment 3 requires. |
| B3-3 | minor | Fixed | (i) Fixtures use a fixed title that spells out the name, so calibration no longer depends on the README under test. A flag on the name ICW alone is discarded, for readers as well as for the judge. (ii) The calibration section, P and F1–F4 are all marked "owner to approve". |
| B3-4 | minor | Fixed | I1's A6 also fails an answer that says both ways are real or carried, or that claims a result the kernel does not state. |
| B3-5 | minor | Fixed | (i) I1 notes that its kernel part moves to I5 if the owner approves I5. (ii) I3(b) is stated to back up A4. F4 calibrates A5, and the key says that A5 is otherwise backed only by the word limit, so a clean A5 is weak evidence. |

## Executable checks

- The opening rule on F4 yields P, since P's first block is 98 words, above
  the 25-word join threshold.
- F1 is 29 words, a single block of at least 25 words, so its opening is the
  whole fixture.
- F3, the kernel Statement joined as one paragraph, is 59 words.
- The Unicode word rule is unchanged from round 3 and was checked there.

## Gaps

- **Calibration not run.** Under Amendment 3 the orchestrator must run it,
  with 15 fresh readers (five fixtures × three) and a fresh judge, before β
  can approve. The likeliest failures:
  - F1 drawing "yes" from yes-biased model readers. The run is then void and
    the reader kind should change, for example to a different model or a
    human.
  - P failing the I2 minimum for E2 (both directions) or for E3(b). The owner
    then revises P.
- **Owner decisions.** The owner should ratify P, F1–F4, and the in-force
  numbers: 25, 100 and 600 words, and two of three readers.
- **No line headroom.** The two files are at 149 of 150 lines excluding
  Grounding. Any further addition needs an equal cut.
