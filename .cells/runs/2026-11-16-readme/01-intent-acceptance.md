# Intent acceptance, round 1
Agent: work acceptor, fresh context. Model: Claude Opus (subagent).
Verdict: REQUEST

Input: `.cells/intents/readme.md` at `7e9c99c`. Kernel read at the same commit.

## A. Buildable

A builder would guess at these points.

1. Whose words the leading question is. Part 0 cites the owner for *that* the question leads ("the core question matters more than everything else"); Sources say "he left the opening to Claude ('your call')". The builder cannot tell whether "where do we tell a story of one level producing another…" is fixed wording or a draft to improve.
2. What answers the leading question. Part 0 asks about the production story; parts 1–3 answer what levels are and what the test does. The direct answer (one change, read twice) is R5, which the intent keeps in "Supporting", outside what I3 and I5 mark.
3. Which Design binds. Line 5 sends "how" to `runs/2026-11-13-readme/contract.md` Design. G7 item 0 is "Title and one-sentence claim: ICW offers a test"; G3 is "glider, then computer, then body", with molecules sent to "read next"; G1 is "concrete examples first, then the general idea". Part 0 departs from all three. The 16 Nov contract names no Design.
4. Layout of the opening. I3: "The opening line before it states part 0." Contract step 3: "A cold reader reads only the first paragraph." The builder cannot tell whether the opening line is a paragraph of its own (and so withheld from the I3 reader) or the first sentence of paragraph one.
5. How far to take part 0's domains. "molecules and living things, a trained network's features, and experience" have no example page for molecules or networks (`examples/` holds glider, limits, mind, ship, wave), and G4's computer and body are absent from the list.

## B. Consistent

1. Part 0 vs part 1, part 3 and O2. Part 0: "when one changing whole is staying the same in two ways at once" states a held pair. Part 1: "can be two ways". Part 3: "cannot yet confirm one". O2: carrying unanswered, so no pair holds yet. Kernel Statement: "identity can persist".
2. Part 0 and I4 vs HYPOTHESES. I4 ✅: "'Gliders emerge from the cells' starts out counting squares and ends up counting gliders" finds the slip in the sentence itself. HYPOTHESES §"The three questions": "'Cells produce a glider' can mean any of three questions, so its words alone show no confusion"; ICW's contribution concerns Q3 and "must leave Q1 and Q2 intact". H6 (that any real explanation makes this move) is untested. READING probe: "A glider can arise in time; that is a change in the one history." I4's "where it slips" and part 0's "story of one level producing another" read as Q1 as easily as Q3.
3. Supporting line vs scoped R1. Intent: "R1: it fixes all that happens and leaves open what counts as one." R1 now: "Carrying (D8) is the exception: it is read off the rule." D9: an articulation, a carried continuity, "fixes what counts as one". So the rule bears on what counts as one. The line held under the 14 Nov R1 and needs restating.
4. Part 3 vs D8 (16 Nov). "its last check, whether the change keeps both going, is open" glosses carrying through the change. D8 *Decided*: "read off the rule, not off the history alone". The gloss holds if "the change" means the rule-generated change; a builder rendering it as "whether both keep going" states the history reading D8 rules out. Note for the builder; no request.
5. Part 1 vs D10: consistent ("sameness of what changes … sameness of the change across what changes"). D10 is *informal*; nothing in the intent claims more.
6. Part 2 vs D7: consistent. Case claim checked with `tools/gol`: an isolated glider has 2 newly live squares at each of steps 1–8.
7. Supporting R5 line vs R5: consistent ("can be true … one change … proposed"). R5 holds only "where `A < X > B`", which O2 leaves unconfirmed; same root as B1.
8. Part 0 vs I1 ✅ and I3 ✅/❌, I7 ✅/❌, I8 ✅: no contradiction. I1 ✅ ("how the glider moves when no square does") and I3 ✅ now describe paragraph one rather than the opening line; they remain usable as illustrations.
9. Part 0 "experience" vs H8: "Bridge required: … That cannot be assumed"; H8 held until H4–H7 have results. Naming experience as where the story is told is true; presenting it as where ICW applies is not yet supported.

## C. Checkable

- I1: owner only, by design (contract step 5). No agent check in this run.
- I2: executable with a fresh Claude reader and a judge. A Claude "non-specialist" knows Life and its terms, so (a) will under-flag; uncalibrated (rule 5).
- I3: executable. The judge marks parts 1–3 only, so nothing checks that the opening line states part 0. "Applies it to one case it did not name" needs a key per case; the judge has one only for cases in the kernel or READING.
- I4: not executable as written. The key "READING misreading 1" says nothing about what the explanation "counts first and what last"; it refuses production and constraint as a second cause.
- I5, I6: executable.
- I7: executable. Life claims by `tools/gol` (`run`, `board`, `GLIDER`); molecules, networks and experience have no runnable check.
- I8: executable against `PRIOR-ART.md`.
- All: intent line 10 leaves readers, judges, calibration and Pass to "the planning cell"; this run has no Planning step, so every check runs uncalibrated against PROTOCOL rule 5.

## D. Proposed lines the build depends on

- Part 0, second sentence: the domains (*proposed*); and in effect the question's wording (Sources: "your call").
- Part 3: the refusal grounds and "cannot yet confirm one" (*proposed*, for O2).
- Supporting: the R1 reading, "sufficient … and still incomplete" (*proposed*).
- Priority after I1, I2: "then I3–I6 and I8; I7 always" (*proposed*).
- I1: "for its subject" (*proposed*).
- I2: "explain a needed term at once" (*proposed*).
- I4 whole property (*proposed*; owner direction 16 Nov).
- I5 whole property, "Claude's reading of 'top-down'" (*proposed*; owner to confirm).
- I7 whole property (*proposed*; owner to confirm).
- I8: "millennia old, with full respect to prior art", owner to confirm as his wording.
- Every reader, judge, calibration and Pass (*proposed*, line 10).

## Requests

1. [owner] Part 0: "where do we tell a story of one level producing another, when one changing whole is staying the same in two ways at once?" Is this wording yours and fixed, or Claude's draft ("your call") that the builder may rephrase?
2. [owner] Part 0 "is staying the same in two ways at once" asserts a held pair; part 1 says "can be", part 3 "cannot yet confirm one", O2 is open. May the opening line state it as fact, or must it stay conditional ("can stay the same")?
3. [owner] Part 0 is answered by R5 ("one change … described at either level"), which sits in "Supporting", outside the "parts 1–3" that I3 and I5 mark; I5 ❌ is "the answer comes three sections later". Must the first paragraph answer the leading question, making R5 (proposed) part of the idea?
4. [record] I4 ✅: "'Gliders emerge from the cells' starts out counting squares and ends up counting gliders." Which of Q1–Q3 is part 0's "story", and may the README say the familiar story slips? I think `notes/HYPOTHESES.md` §"The three questions" (Q3 only; "its words alone show no confusion"; leave Q1, Q2 intact) and H6 (untested) answer it, with READING's first probe; the answer changes I4's ✅ and its "Shown by" key.
5. [record] Supporting: "R1: it fixes all that happens and leaves open what counts as one." Under the 16 Nov R1 ("Carrying (D8) is the exception: it is read off the rule") and D9, what does the rule leave open? I think `specs/ARTICULATION.md` R1, D8 *Decided* and D9 answer it: the history alone leaves carrying open; the rule does not.
6. [owner] Line 5 binds "how" to `runs/2026-11-13-readme/contract.md` Design. Part 0 conflicts with G1 ("concrete examples first"), G3 ("glider, then computer, then body"; molecules to "read next") and G7 item 0 ("ICW offers a test" as the title claim). Does that Design bind this build, and which of G1, G3, G7 does part 0 replace?
7. [record] Part 0: "molecules and living things, a trained network's features, and experience are where the story matters." May the README present these only as places the production story is told, or as places ICW applies? I think `notes/HYPOTHESES.md` H8 ("Bridge required … cannot be assumed") and the intent's I7 ("a case the kernel lacks is an application") answer it: named as where the story is told, no ICW claim.
8. [owner] I3: "The opening line before it states part 0" and contract step 3: "A cold reader reads only the first paragraph." Is the opening line part of the first paragraph the I3 reader gets?
