# Calibration run 2: judgement

Key: `repo/intents/readme-key.md` at fb2b212 (Calibration section, I1–I4, scoring rule, reference E1–E3). Sheet: `repo/intents/readme.md`. Answers: `calib2/answers.md`. Kernel consulted only where the key's discard rule refers to it ("the meaning the text intends (per the README and kernel)"): `specs/ARTICULATION.md`. Nothing under `log/` or `calib/` was read.

Reader kind (as recorded in answers.md): fresh Claude Sonnet instances, no tools, one fixture each, three per fixture.

## Verdict: VOID

Row P holds for 0 of 3 readers. F1–F4 hold for 3 of 3. The key voids a run unless every row holds for two of three.

## Per row, per reader

### P: must pass I1 Step 1, I2, I3 Step 1. By: A2 yes, quoting P; A1 meets E1–E3, no I2 fault; no A3 flag counts

| Reader | A2 yes? | A1 E1 / E2 / E3, I2 fault | A3 flags counted | Row |
|---|---|---|---|---|
| P-1 | No: "A2: Maybe." | E1 yes ("what makes something 'the same thing' when it keeps changing"). E2 yes (water stays while waves pass; "the wave stays while it moves through new water"). E3 **no**: "a test for deciding which kind counts, or whether one is just a way of sorting"; no "neither is the real one", no "keeps both going"; "which kind counts" is the "which is right" reading E3 rules out. | **"Its test"**, guess "a procedure for checking which kind of sameness is real": wrong (P: "ICW does not call either one the real thing. Its test asks whether the sea's own movement keeps both going"), and "doesn't know what it consists of". Discarded: "ICW" (name); "what counts as one thing", "Two ways … come apart", "the real thing", "the sea's own movement", "keeps both going", "just a way of sorting it" (guesses are the intended meaning; "not something we impose" / "a label we apply" match D8/D9); "The test's last step is unfinished" (guess "method still being developed" is the intent; see note on "passed"). | Fail |
| P-2 | No: "A2: Maybe." | E1 yes. E2 yes ("water stays while waves pass through it, and a wave persists while the water under it is replaced"). E3 **half**: has "a test for whether the sea's own movement keeps both going or whether one is just a way of sorting things", but A1 never says neither is the real one (it appears only as A2's quoted words). No I2 fault. | **"The test's last step is unfinished…"**, guess "multi-step check not yet run; doesn't know what 'passed' means": not the intended meaning (the last check cannot yet be run, carrying being undefined, D8/O2), and no guess for "passed". Discarded: "ICW"; "Its test asks whether…" (guess matches; "can't tell what 'sorting' means" but guesses "a label"); "Two ways … come apart" (guess is D7 almost verbatim); "Whole" (title, outside the opening). | Fail |
| P-3 | No: "A2: Maybe." | E1 yes. E2 **no by the letter**: "Water and waves each stay 'the same' in a different way, and the two can separate": neither two cases nor "both ways" (borderline). E3 yes: "ICW doesn't pick a winner. It has a test for whether the sea's own movement keeps both going." No I2 fault. | **"Its test"**, guess "a procedure for deciding whether something counts as a real thing; doesn't know what it measures": not the intended meaning (it tests whether both are kept going, not whether a thing is real) and partly unguessed. Discarded: "ICW"; "Two ways of staying the same", "does not call either one the real thing", "keeps both going", "one is just a way of sorting it" (intended); "the sea's own movement" (currents, tides: a fair literal reading of the case); "Wholes" (title). | Fail |

Note on "passed": P-1, P-2 and P-3 all give a guess for "The test's last step is unfinished…" yet say they do not know what "passed" means. If that is read as a missing guess, each P reader gains one more counted flag. The row result does not change either way.

P holds for 0/3. It fails on A2 alone for all three, and also on A1 (all three miss part of E2 or E3 by the letter) and on A3 (each has one counted flag).

### F1: must fail I1 Step 1. By: A2 maybe or no, or its question only asks what a word, name or the project means

| Reader | Evidence | Row |
|---|---|---|
| F1-1 | "A2: Maybe." (question also only asks the meaning: "what is 'Identity in Changing Wholes' about, and what is it for?") | Holds |
| F1-2 | "A2: Maybe." ("what does 'identity in changing wholes' actually mean…") | Holds |
| F1-3 | "A2: Maybe." ("what does 'identity in changing wholes' actually mean…") | Holds |

F1 holds for 3/3.

### F2: must fail I2. By: A1 has the wave emerge from, steer, or outrank the water

| Reader | Evidence | Row |
|---|---|---|
| F2-1 | "ICW says the wave is a higher thing that emerges from the water, steers it, and is more real than the water" | Holds |
| F2-2 | "ICW claims the wave is a 'higher thing' that comes out of the water, steers it, and is more real than the water" | Holds |
| F2-3 | "ICW says the wave is a higher thing that emerges from the water, steers it, and is more real than the water" | Holds |

F2 holds for 3/3.

### F3: must fail I3 Step 1. By: an A3 flag counts (no guess, or a wrong one)

| Reader | Flags counted | Row |
|---|---|---|
| F3-1 | "Its order is rhythm", guess "repeating or beat-like, as in music": wrong (rhythm is the order of cohering, its structure open: D12, O3). "cohering", guess "holding together": not the kernel's sense (the one change that carries both, D12). "through what changes; through the change across what changes": "I am not sure of the difference" (no guess for the distinction). | Holds |
| F3-2 | "Its order is rhythm", guess "repeating beat or pulse": wrong, as above. "identity", guess offered "or maybe a person's sense of self": wrong alternative. "through the change across what changes": "unsure what 'across' means". | Holds |
| F3-3 | "its changing differs without division": "I have no real guess" (missing). "through what changes; through the change across what changes": "I can't tell these two apart". "cohering" (holding together), wrong as above. | Holds |

F3 holds for 3/3. F3-3 holds on a missing guess with no kernel judgement needed. F3-1 and F3-2 hold on wrong guesses judged against the kernel, as the discard rule directs.

### F4: must fail I4. By: A5 quotes a unit of its second paragraph

| Reader | Evidence | Row |
|---|---|---|
| F4-1 | A5 quotes all four: "In short, ICW is about what stays the same when things change."; "Water and waves each stay the same in their own way."; "ICW does not pick one as the real thing."; "Its test is not finished." | Holds |
| F4-2 | A5: "the four sentences of the 'In short' paragraph, each matched to the earlier unit it repeats" (condensed in the log, not shown verbatim) | Holds (on the log's description) |
| F4-3 | Same as F4-2 | Holds (on the log's description) |

F4 holds for 3/3. F4-1 alone is verbatim; the 2-of-3 threshold needs one of the condensed answers.

## Diagnosis of the failing row (P)

**A2 (main cause): the reader kind, possibly also the rule.** All 15 readers answer "Maybe" to A2. That includes the six who saw P as their opening (P-1–3, and F4-1–3 in Step 1). The reference opening P and the dull F1 get the same answer. The readers still extract the idea from P (E1 and E2 hold for 5 of 6 by the letter), and they ask questions about the subject (P-2: "is there any fact about which is really the thing, or is it only how we choose to describe it?"). So "Maybe" looks like this reader kind's hedge under the sheet's "came across this project by chance and have other things to do". It does not look like a judgement on P. If the owner considers hedged interest the honest ceiling for a chance visitor, the rule ("yes, not maybe") is the problem rather than the reader. The answers cannot separate these two causes. They do rule out the fixture as the A2 cause, because P and F1 cannot be told apart.

**A1/E3 and A3 (secondary): the fixture, at one sentence.** Two of three readers misread "Its test asks whether the sea's own movement keeps both going, or one is just a way of sorting it" as a test of which way is real:
- P-1 A1: "deciding which kind counts".
- P-1 A3: "checking which kind of sameness is real".
- P-3 A3: "whether something counts as a real thing".

This happens even though the sentence directly follows "ICW does not call either one the real thing." The misreading costs P-1 its E3 and gives both readers their counted A3 flag. P-2's counted flag ("not yet run") comes from "The test's last step is unfinished", which says what is unfinished but not why.

**A3 (also): the rule.** Most counted P flags say the reader does not know what the test *consists of* ("doesn't know what it consists of", "doesn't know what it measures", "doesn't know what 'passed' looks like"). That is content the opening rightly leaves for later, not a word the reader could not follow. Because the rule counts any flag with a missing or partial guess, a curious reader can fail I3 on a clear opening. The rule may need to discard flags whose guess is right and whose only gap is "what does it consist of", or the sheet may need to separate unclear words from open questions.

**E2/E3 strictness.** P-2 has "neither is the real one" only in A2. P-3 says "the two can separate" rather than giving both directions. Both fail by the letter of E1–E3. Neither failure is needed to void the run: A2 already fails every P reader.

## What would make a VALID verdict untrustworthy here

1. **A2 does not discriminate.** Fifteen of fifteen readers say "Maybe". F1 holds trivially. A run in which P also held would rest on a single A2 judgement that this reader kind returns the same way regardless of input.
2. **The log is not verbatim.** The key requires every answer logged verbatim, but answers.md is condensed in several ways:
   - "[list]", "same content" and "same idea" stand in for the readers' text.
   - The F4-2 and F4-3 A3 entries read only "[list with guesses]".
   - The F4-2 and F4-3 A5 answers are described, not quoted.
   - Many F3 flags appear without their guesses.

   Every A3 count here depends on which guesses the condenser kept, and F4 reaches 2 of 3 only on described answers.
3. **Fixtures are not recorded.** `calib2/fx.json` holds only P and F1; it matches the key for both. The F2, F3 and F4 texts actually given to readers are not recorded in this run. The answers are consistent with the key's texts, but administration cannot be checked.
4. **Readers are correlated.** All 15 readers are the same model, and their answers are close to identical within a fixture (F1-2 and F1-3 match nearly word for word). The 2-of-3 rule then acts like a single sample, not three independent readers.
5. **Judgement-dependent counts.** The F3-1 and F3-2 counts rely on judging "rhythm" and "cohering" guesses wrong against the kernel's declared, still-open meanings. That is defensible under the discard rule, but it is a judgement call. F3-3 is the only F3 count that needs no kernel judgement.
