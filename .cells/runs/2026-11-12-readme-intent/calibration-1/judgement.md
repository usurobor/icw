# Calibration run 1: judgement

Judge inputs: `intents/readme-key.md` (Calibration, I1–I4, E1–E3), `intents/readme.md`, `calib/fixtures.json`, `calib/answers.md`. Nothing under `log/` read.
Reader kind (as logged): fresh general-purpose LM instance (Claude Sonnet), no tools. That kind is allowed by the key.
Rule applied: a row holds if, for at least two of three readers, the reader's answer shows the row's required result **by the stated answer**. A failure for any other reason does not count. The run is void unless every row holds.

## Per-row, per-reader verdicts

### P: must pass I1 Step 1, I2 and I3 Step 1, by: A2 yes, quoting P; A1 meets E1–E3; A3 empty

| Reader | A2 yes, quoting P | A1 E1 | A1 E2 (stuff vs pattern, coming apart *both ways*: two cases or "both ways"; one direction does not count) | A1 E3 (neither is the real one + own change keeps both going) | A3 empty (ICW-only flag discarded) | Shows result? |
|---|---|---|---|---|---|---|
| P-1 | Yes. Q: "what are the steps of the test…"; quotes "Its step-by-step test asks whether the sea's own motion keeps both going…" (in P) | Yes: "what makes something count as 'one thing' when it keeps changing" | **No**: "a patch of water and a wave … are two different ways of picking out 'the same thing,' and they can disagree". This names the two by a case but gives no direction of coming apart: no two cases, no "both ways" | Yes: "doesn't treat either as the real one … whether the sea's own motion keeps both going" | **No**: 7 flags besides ICW, e.g. "what counts as one thing", "Two answers can disagree, both ways round", "no case has passed" | **No** (E2, A3) |
| P-2 | Yes. Same quoted sentence | Yes: "what makes something 'one thing' when it keeps changing" | **No**: "two different ways of picking out 'one thing', and they can disagree" | Yes: "neither is the real one and the other just a way of talking … whether the sea's motion keeps each of them going" | **No**: 7 flags besides ICW, e.g. "Two answers can disagree, both ways round", "no case has passed", plus "Changing Wholes" from the title | **No** (E2, A3) |
| P-3 | Yes. Same quoted sentence | Yes: "what makes something count as 'one thing' when it keeps changing" | **No**: "two different ways to pick out 'the same thing,' and they can disagree" | Yes: "doesn't say one is real and the other just a manner of speaking … whether the sea's own motion keeps both going" | **No**: 8 flags besides ICW, e.g. "counts as one thing", "step-by-step test", "no case has passed" | **No** (E2, A3) |

**Row P: 0/3. Does not hold.**

A note that does not count toward the verdict: under I2's exclusions, "two different ways of picking out" (3/3) is close to "the two are … ways of looking". P-1's "a grouping we impose" leans the same way. The stated answer for P is E1–E3 only, so these readings are noted but not scored.

### F1: must fail I1, by: A2 no

| Reader | A2 | Shows result? |
|---|---|---|
| F1-1 | "Yes, weakly" | **No** |
| F1-2 | "Yes" | **No** |
| F1-3 | "Yes, a weak yes" | **No** |

**Row F1: 0/3. Does not hold.** All three readers do fail I1 Step 1 by another clause: each question is about what the name means, e.g. "what does 'identity in changing wholes' mean" (F1-1) and "what is 'Identity in Changing Wholes', in plain terms" (F1-2). The key says that kind of failure does not count.

### F2: must fail I2, by: A1 has the wave emerge from, steer, or outrank the water

| Reader | Evidence (A1) | Shows result? |
|---|---|---|
| F2-1 | "a 'higher thing' that comes out of the water, steers it, and is more real than the water" | Yes |
| F2-2 | "comes out of the water, steers the water, and is more real than the water itself" | Yes |
| F2-3 | "arises out of the water, directs it, and is more real than the water itself" | Yes |

**Row F2: 3/3. Holds.**

### F3: must fail I3, by: A3 quotes a word or phrase

| Reader | Evidence (A3) | Shows result? |
|---|---|---|
| F3-1 | "cross-cutting", "continuities", "cohering", "Its order is rhythm" (13 phrases) | Yes |
| F3-2 | "differs", "identity", "cross-cutting", "cohering" (11 phrases) | Yes |
| F3-3 | "identity can persist", "cross-cutting", "continuities", "cohering" (10 phrases) | Yes |

**Row F3: 3/3. Holds.** (The log summarises each A3 ("13 phrases incl. …"), but the phrases it reproduces are enough to show the result.)

### F4: must fail I4, by: A5 quotes a unit of its second paragraph

| Reader | Evidence (A5) | Shows result? |
|---|---|---|
| F4-1 | "In short, ICW is about what stays the same when things change."; all four closing sentences quoted | Yes |
| F4-2 | Logged as "the whole closing paragraph (four sentences quoted)" | Yes (the evidence is the logger's description, not a verbatim quote) |
| F4-3 | Logged as "all four sentences of the closing paragraph" | Yes (same caveat) |

**Row F4: 3/3. Holds.**

## Run verdict: **VOID**

Rows P and F1 do not hold. Per the key: "If void, change the reader kind or revise fixtures."

## (a) Logged deviation: Step 2 was given only for F4

The deviation could not have changed any row's verdict.
- The stated answers for P, F1, F2 and F3 are A1, A2 or A3. These are collected before Step 2 is given.
- For P, F1, F2 and F3, the fixture README is just the title plus the opening (`fixtures.json`), so Step 2 would have shown the readers nothing new.
- Step 2 answers could only add other ways to fail, for example F1 failing I1 through A6 or F3 failing I3 through A4. Other ways of failing do not count.

It is still a breach of procedure: the Calibration section says readers "do the whole sheet". The log has two smaller gaps. F4's Step 1 answers are logged as "as for P", not verbatim. A3 for F3 and A5 for F4-2 and F4-3 are summarised. Neither gap changes a verdict.

## (b) Diagnosis of failing rows

**P: mainly a fixture problem for E2, and mainly a reader-kind or sheet-wording problem for A3.**
- E2 points to the fixture. Every P reader cut "Two answers can disagree, both ways round" down to "they can disagree". Every P reader also flagged that exact phrase in A3. It is the one flag that their A1 answers confirm they did not understand. The same reader kind got E2 from F3's plain statement "Each can hold where the other does not": "either can hold without the other" (F3-1), "which can come apart" (F3-2), "either without the other" (F3-3). So P's elliptical "both ways round", with its two cases packed into one sentence, does not deliver E2. The "two answers" framing also produced "ways of picking out" in 3/3 answers, which edges toward the reading I2 excludes.
- A3 points to the reader kind, or the sheet's "Quote every" wording. Most A3 flags conflict with the same reader's A1. P-1 flags "what counts as one thing" and "no case has passed", then paraphrases both correctly ("count as 'one thing'", "nothing has passed it yet"). P-2 flags "the real thing and the other a way of talking" and then reproduces it. P-3 flags "step-by-step test" and "counts as one thing", which are everyday phrases. These are not phrases the readers "could only guess at". The readers are flagging exhaustively. Rule factor: an exactly-empty A3 is a zero-tolerance bar, and the readers' over-flagging alone meets it. I still don't put the A3 failure on the rule, because "both ways round" is a real flag that a better fixture should remove. But with this reader kind and this sheet wording, P cannot pass even after a fixture fix.

**F1: mainly the rule (the stated-answer pin), with a reader-kind factor and a small fixture factor.**
- The fixture does fail I1 for all three readers, through the clause about what a word or name means. Only the narrower pin "A2 no" fails. So the row tests whether readers say no, not whether F1 fails I1.
- Reader kind: two of the three hedged ("weakly", "a weak yes") and still answered yes. With a binary A2, this kind seems to choose yes even with the sheet's "you have other things to do".
- Fixture: all three quoted "a list of misreadings" as what drew them in. That is a small hook in a fixture meant to be dull.

**Side note:** in rows that hold, F4-2 and F4-3 also flagged opening units in A5. F4-3 flagged "the whole first paragraph", which the readers had already seen in Step 1. So A5 is likely to flag any README's opening as "nothing new", and I4 may then fail even for clean READMEs. The sheet does not say whether "new" counts against Step 1.
