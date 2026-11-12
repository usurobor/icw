# δ — boundary validation: README intent cell

Validator: δ, a separate agent that took no part in the cell. Read-only on the
matter and the record; this file is δ's only write. δ recommends; the owner
decides.

Read in full: CONTRACT.md (Amendments 1–3), REVIEW-PROPERTIES.md, log/ (LOG,
BASE, SEED, round-1..5-alpha, round-1..3-beta), calib/, calib2/, the matter at
HEAD `fb2b212` (`intents/readme.md`, `intents/readme-key.md`), git history
since BASE `2b155ac`, the kernel, specs/READING.md, README.md,
skills/readme (for the independence check only).

**Verdict in one line: the cell did not converge. Recommend accept part, as a
draft baseline only; nothing here may yet be used to score a skill.**

---

## 1. Receipt validation

Checked mechanically unless marked (read).

| Check | Result | Evidence |
|---|---|---|
| Scope against BASE | **pass** | `git diff --stat 2b155ac HEAD`: only `intents/readme.md`, `intents/readme-key.md`. Every one of the 7 commits touches only those paths. Tree clean. Key file is in scope only under Amendment 1 G1 (unratified). |
| Seed | pass | `7e4f87e:intents/readme.md` is byte-identical to SEED-intent.md. |
| Every β finding has an α disposition | **pass for matter findings** | B1-1..14 → 14 rows in round-2-alpha. B2-1..8 → 8 rows in round-3-alpha. B3-1..5 → 5 rows in round-4-alpha. 27 of 27. |
| Contract findings dispositioned | by γ, not α | C-1..C-5 were answered by γ writing Amendments 2 and 3. No party is named by the contract to disposition them. |
| Calibration-judge findings dispositioned | run 1 yes, **run 2 no** | Run-1 diagnosis answered in round-5-alpha. Run-2 judgement (5 trust findings, 4 diagnoses) has no disposition: cap reached. |
| β's last verdict names a commit | yes | REQUEST CHANGES on `67a2515d…` (round 3). |
| HEAD matches that commit | **no** | HEAD is `fb2b212`, two commits later. `git diff 67a2515 HEAD`: 116 insertions, 109 deletions across the two files; the key (139 lines) is in effect rewritten. No round-4-beta or round-5-beta exists. |
| β APPROVE on a named commit | **no** | Three verdicts, all REQUEST CHANGES. |
| No open blocker or major | **no** | B3-1, B3-2 (major) are "fixed" by α's word only. C-5 (major) is open: its gate failed. |
| Rounds ≤ 5 | at cap | α used rounds 1–5 (+2b). β reviewed 1–3 only. |
| Line caps at HEAD | passes **only under Amendment 2** | readme 27; key 139, of which Grounding 17 → 122. Original AC7 (one file < 120): 166 lines, fail. Amendment 1 G2 (each < 120 excl. Grounding): key 122, fail. Amendment 2 C-2 (combined < 150 excl. Grounding): 149, pass. |
| No test refers to a skill (AC2) | pass | `grep -i skill intents/*.md`: none. |
| AC1 "added intents marked *proposed*" | **fails by the letter** | At HEAD I5 is marked *reported*; the word *proposed* survives only inside the definition of *in force*. The A6 clause, α's addition, sits *in force* inside owner intent I1. β required this labelling (B3-1) but never saw the result. |
| AC6 "owner to approve" | pass | Heading of the reference answer. |
| Word rule reproducible | pass | δ's own script: P = 95 words, README.md = 664. Matches α and β. |
| Calibration sheets match the commits under test | pass | calib/sheet.txt = sheet at `39049a9`; calib2/sheet.txt = sheet at HEAD. calib/fixtures.json = fixture texts in the key at `39049a9`. calib2/fx.json P and F1 = key at HEAD; **F2–F4 not recorded**. |
| Amendment 3 gate | **failed twice** | Run 1 on `39049a9`: VOID (P 0/3, F1 0/3). Run 2 on `fb2b212`: VOID (P 0/3). The known-pass opening has never passed. |
| Amendment 3 "exactly as the key specifies" | **not met in either run** | See §2. |

**Convergence condition: not met on any of its three limbs** (no APPROVE; open
majors; HEAD unreviewed). **Amendment 3 gate: not met.** γ's closure entry
("NOT CONVERGED") states this correctly.

---

## 2. Integrity of the record

| # | Fault | Responsible | Consequence |
|---|---|---|---|
| R1 | **Reader answers are not verbatim.** Run 1's file is headed "verbatim, lightly trimmed of formatting" yet contains "13 phrases incl. …", "Step 1 answers as for P", and two A5 answers described rather than quoted. Run 2 marks condensation ("[list]", "same content", "same idea", "[list with guesses]") after the key at `fb2b212` had made verbatim logging a rule. | γ | Every counted A3 flag depends on what the condenser kept. F4 reaches 2 of 3 in **both** runs only on γ's descriptions (one verbatim reader each). No raw transcript, prompt, model ID, sampling setting or timestamp per reader exists anywhere in the record. δ cannot verify that any reader said what is logged. |
| R2 | **γ administered and logged; the judge scored γ's log.** The key says the judge gives the sheet, collects answers and logs them. Amendment 3 says γ "runs" the run "exactly as the key specifies". The two texts conflict and γ took the reading that puts the condenser between reader and judge. | γ (and the amendment's wording) | The "fresh judge" is fresh but not first-hand. |
| R3 | **Run 1 deviated from the key under test**: Step 2 given only to F4 though `39049a9` said "do the whole sheet". Logged as a deviation. Round 5 then rewrote the key to match what γ had done ("It matches what the run did"). | γ, then α | The procedure was fitted to the deviation. Result: P never goes through Step 2, so A4, A5 and A6 have no known-pass, and A6 (in force, inside the top-priority intent) has no calibration of either sign. |
| R4 | **Run 2 fixtures F2–F4 not stored.** | γ | Administration of 9 of 15 readers cannot be checked. |
| R5 | **β did not review rounds 4 and 5.** After round 4 γ ran calibration first; the void result went to α, not β. | γ (sequencing); the contract (no rule) | A calibration judge, an uncontracted role, acted as reviewer for two rounds. Its findings carry no severity and need no disposition. |
| R6 | **Round-5 changes reverse a β requirement without β.** B3-2 required the dull fixture to draw A2 "no" from two of three, so that a yes-to-everything panel voids the run. `fb2b212` widens F1's row to "maybe or no, **or** its question only asks what a word, name or the project means". F1 now holds whatever A2 says. | α | The calibration no longer detects the fault it was added for. Run 2's "F1 3/3" is the widened row holding, not discrimination. |
| R7 | **I3 loosened in round 5, unreviewed.** "Nothing in A3" became "no flag counts", a flag being discarded when the judge finds the guess right. α argues this is not weakening; β never ruled. Q1 makes weakening an owner intent a blocker. | α; unreviewed because of R5 | Owner fidelity at HEAD is unverified, not passed. β's Q1 passes cover `8fcc0c7`, `495a48e`, `67a2515` only. |
| R8 | **γ's closure overstates what is settled.** "F2, F3, F4 discriminate reliably" and "I2 elements and I4 repetition check work". See §4: only the fail side was ever shown; the I2 elements failed the reference opening 6 of 6. | γ | The LOG's summary should not be relied on. |
| R9 | **Q3 not re-run each round.** REVIEW-PROPERTIES says check every property every round; β fetched in round 1 and relied on that in rounds 2–3 (disclosed in round 3). Grounding text was condensed in round 2 and is unchanged from `495a48e` to HEAD. | β (disclosed) | Low. δ confirmed by search only that the Goh and Bostrom sources exist; δ did not re-verify quotations. |
| R10 | **Seed carried skill wording.** The skill's description says "pulls a stranger in" and "a smart non-specialist". The seed says "Draws a stranger in" and "Clear to a smart non-specialist". The owner's words are "visitor" and "non-specialist". | γ (drafted the seed) | The Goal says the intent "must not be derived from any skill". β removed "smart" (B1-11) on fidelity grounds without knowing its source; "stranger" is also gone at HEAD. The I2 method (fresh reader restates from paragraph one) coincides with the skill's own eval 4.1; it also follows from the owner's intent 2, so δ does not call it derived, but the owner should know. No α attestation about reading `skills/` exists, and the contract's scope permits α to read it. |
| R11 | Clerical. Seed commit authored as "alpha" though γ drafted it. LOG's table rows are interleaved with prose. REVIEW-PROPERTIES was never amended (Q7 still says 120 lines, one file); it is patched by "read as" clauses in the contract. Amendment 1 is headed "after round 2" but round 2b was committed under it (β's C-4). | γ | Low. |

Not faults: α's and β's round files are complete and specific; β named
commits by full hash every round, ran executable checks, and refused to pass
Q2 on assertion (C-5). That refusal is the reason the cell did not close on
an untested instrument.

---

## 3. Amendments for ratification

All three were written by γ. None has owner sign-off. The contract has no
amendment procedure.

| Amendment | What it changed | Direction | Requested by | Recommendation |
|---|---|---|---|---|
| **1 / G1** key file | Scope widened: α may create `intents/readme-key.md`. Goal's deliverable becomes two files. | relaxes scope | α (writer) | **Ratify.** It is the structural fix for β's B1-1 (a judge primed by the reference answer in the file being applied). A cut line in one file is not a seal. |
| **1 / G2** size | AC7: each file < 120, Grounding excluded. | relaxes AC7 (about double) | α | **Do not ratify; superseded by 2 / C-2.** HEAD fails it anyway (key 122). |
| **1 / G3** readers + judge | AC2's single reader-judge becomes several fresh readers plus a judge. | relaxes AC2 | α | **Ratify only together with 2 / C-1 and 3.** Alone it lets any test move onto a panel and pass AC2 on paper (β's C-1). It is also the change that created every later problem in this cell; the owner should ratify it knowingly. |
| **2 / C-1** calibration required | Reader, administration and a pass/fail calibration must be specified. | tightens | β | **Ratify, with a change:** require a known pass **and** a known fail on the same answer field for each reader-based clause, and require them to differ. See ε-2. |
| **2 / C-2** size | Combined < 150 excluding Grounding. | relaxes original AC7; tightens G2 | β | **Owner's call; δ leans to replace.** The matter sat at cap − 1 in four of five rounds (119/120, 119/120, 149/150, 149/150) and totals 166 lines. The cap is acting as a compressor on the key, not as a guard on what readers bear. Suggest: cap the reader sheet (27 lines now), drop the cap on the key or set it in words. |
| **2 / C-3** wording | "Reader-judge" read as "the roles specified"; AC6's "R2" read as the top-down intent. | clerical | β | **Ratify.** Then edit the texts instead of reading them through a patch. |
| **2 / C-4** ratification | Amendments provisional until the owner ratifies at δ. | procedural | β | **Ratify.** This table discharges it. |
| **3 / C-5** calibration must run | A logged calibration-only run with fresh readers and a fresh judge before APPROVE; a known fail per reader-based intent. | tightens convergence | β | **Ratify. Strongest amendment of the three**: without it the cell could have closed on a reference opening that has never passed its own test. Changes needed: say who administers and who logs (R2); require raw transcripts (R1); say what a void run triggers and whether it consumes a round (ε-3). |
| **3 / Q7 wording** | "Only the files in scope under the amendments changed". | clerical | β | **Ratify.** |

Relaxations requested by the writer and granted by the orchestrator: G1, G2,
G3. β flagged this itself (C-4). δ agrees it is a process fault whatever the
merits (ε-3).

---

## 4. What the cell established and what it did not

### Supported by run results

1. **Self-reported "would you read on" from this reader kind is a constant,
   set by the answer scale, not by the opening.** Run 1 (yes/no): 15 of 15
   "yes", including the folder inventory F1 ("Yes, weakly", "a weak yes"),
   the planted misreading F2 and the kernel jargon F3. Run 2 (yes/maybe/no):
   15 of 15 "Maybe", including the reference opening P. n = 30, one model
   (Claude Sonnet), one persona, two scale wordings. Within those limits the
   result is unambiguous.
2. **At HEAD, I1 is unpassable with this reader kind**, not gameable: it needs
   "yes, not maybe" and the panel never says yes. At `39049a9` it was
   trivially passable. Neither state measures the owner's intent 1.
3. **The reference opening has never passed, in either wording.** P row 0/3
   and 0/3. By the letter of E1–E3, 0 of 6 dedicated P readers met the
   minimum: run 1 all three missed E2; run 2 P-1 missed E3, P-2 half of E3,
   P-3 E2. The F4 readers' Step-1 answers on the same text point the same way
   (condensed, unscored).
4. **Rewording helped E2.** "Both ways round" delivered both directions to
   0/3; two plain clauses delivered them to 2/3. Weak (n = 3 each) but it is
   the one fixture revision with a measured effect.
5. **P's test sentence invites the reading E3 excludes.** Run 2: P-1
   "deciding which kind counts", "checking which kind of sameness is real";
   P-3 "whether something counts as a real thing". 2 of 3, directly after
   "ICW does not call either one the real thing". This is evidence **against**
   AC6's "plain enough for a non-specialist" at HEAD.
6. **Readers repeat a misreading stated outright.** F2: 6 of 6 across both
   runs restate emerge / steer / more real. This shows I2's fault list
   catches a README that says the wrong thing in plain words. It is a
   far-end case.
7. **Readers flag exhaustively.** P drew 7–8 flags per reader in run 1 and
   5–9 in run 2, many on phrases the same reader paraphrased correctly.
8. **Question type separated the inventory from openings with content.** F1:
   6 of 6 asked only what the name means. P: 5 of 6 asked about the test or
   the subject (run 2 P-3 is mixed). But F3 readers (jargon) also asked
   subject questions 6 of 6, so this separates "no content" from "content",
   not pull from no pull. Post hoc; it was not a scored row in run 1.
9. **The mechanical rules are reproducible.** Opening rule and word count:
   three independent scripts (α, β, δ) agree on 664 and on P's count.
10. **Structural separation of sheet and key** answers B1-1; β verified it at
    `495a48e` and `67a2515`.

### Asserted only

- **"F2, F3, F4 discriminate" (γ closure).** Discrimination needs a pass and
  a fail on the same field. For I3 Step 1, P failed too in both runs (3/3
  with flags; 3/3 with a counted flag under the guess rule), so P and F3 are
  not told apart. For I2, P failed. For I4's A5 there is no pass-side fixture
  at all, and in run 1 two of three F4 readers also flagged the opening.
  Run 2's pattern (F1–F4 hold 12/12, P 0/3) is exactly what a panel and
  judge that fail everything would produce.
- **"I2 elements work" (γ closure).** Contradicted by item 3.
- **A6 is "sound" (β round 3).** A thought experiment. Every logged A6 is
  "none" (F4 only). The clause has never been exercised on a README.
- **B3-1..5 fixed; round-5 fixes are "not tuning or weakening" (α).** No β
  verification. The round-5 rules and fixtures were chosen after reading
  run-1 answers; run 2 used new readers, which is proper, but P has now been
  revised once against data and still fails.
- **Two of three readers gives robustness.** Same model; answers within a
  fixture are near-identical (run 1 P-1..3 open with nearly the same sentence; run 2
  F1-2 and F1-3 match almost word for word). Treat a same-model triple as
  n = 1.
- **A model told "you have no training in philosophy" is a non-specialist.**
  Untested. Run-2 guesses include restatements the judge calls "D7 almost
  verbatim".
- **Two judges reach the same verdict (AC2, Q2).** Never tested: one judge
  per run, a different one each time. The run-2 judge says its F3 counts for
  two of three readers are "a judgement call" on kernel meanings; the guess
  rule moved I3 from a mechanical count to the judge's reading of the kernel.
- **"A model instance or an adult" are interchangeable readers** (key).
  Asserted in one line; no human has read anything.
- **600 / 100 / 25 words.** α's numbers. The current README is 664, so it
  fails I4 by construction. No exemplar supports the numbers (β B1-12; the
  key now says so).
- **P is faithful to the kernel at HEAD.** α's self-check only. δ's own
  reading against D7, D8, D9, R2, R3, O2 and §6 row 4 and READING 1–8 finds
  no contradiction; δ is one unblinded reader and that is not a β review.
- **Owner fidelity at HEAD.** See R7.

---

## 5. Recommendation

**Accept part.** The cell did not converge and cannot be accepted as the
intent of record. Accept the following as a **draft baseline for a further
cell**, not as an instrument in force:

- the two-file structure (reader sheet / judge-only key);
- the opening rule and the word-count rule;
- I2–I4 as statements of intent (their tests are not accepted);
- I5 as a reported, proposed check;
- the Grounding section (β-verified round 1; text stable since `495a48e`);
- Amendment 3's gate as a standing requirement.

**Reject:** I1's measure (A2 self-report and its "yes, not maybe" bar); P as
a "known pass" and E1–E3-by-the-letter as its bar; the A3/A4 guess rule; the
widened F1 row; the claim that calibration discriminates; any use of HEAD to
score a README or a skill.

Owner decisions needed:

1. **Amendments.** Ratify, change or refuse each row of §3. δ: ratify G1,
   G3 (with C-1 and 3), C-1 (strengthened), C-3, C-4, Amendment 3; refuse G2;
   replace C-2.
2. **How "draws the visitor in" is measured.** Pick from the options in
   ε-1, or declare I1 owner-judged until a measure is validated.
3. **The reference opening.** Approve, rewrite or write P yourself; and say
   whether a reference that a panel cannot restate to the E1–E3 minimum is a
   fault of P, of the minimums, or of the panel.
4. **The clarity bar for I3.** Zero flags (as β last saw it) or the guess
   rule (round 5). This is a fidelity question on your highest-priority
   intent.
5. **Additions inside your intents.** Whether the A6 clause counts inside
   I1, and whether I5 (faithful) becomes an owner intent.
6. **Numbers.** 600 / 100 / 25 words and two of three.
7. **Next step.** Open a new cell from HEAD with a fresh round budget and β
   reviewing HEAD first, or stop here.

---

## 6. Protocol findings for ε

Faults in the protocol, not the matter. Each with the smallest fix.

**ε-1. Absolute self-report from same-model readers cannot measure pull.**
Evidence: §4 items 1–2. The cause is structural as well as empirical: a
reader with no competing demand on its attention pays nothing to say yes, and
"you have other things to do" is a sentence, not a constraint. Changing the
scale moved every answer together. The claim is shown for one model and two
wordings; it is not shown for other models or for people. Options, not a
decision:

| Option | What it measures | For | Against |
|---|---|---|---|
| A. Forced choice against fixed anchors: reader sees the candidate and an anchor in random order and must pick the one to keep reading; score is win rate against a ladder (inventory, kernel Statement, current README, P) | relative pull | No scale to hedge on. Calibration is built in: P must beat the inventory. Cheap, repeatable. | Relative only; needs owner-approved anchors. Order effects need counterbalancing. Still one model's taste, which may favour model-like prose. |
| B. Behavioural proxy: score what the reader asks or retains, not what it says it would do | content taken, curiosity about the subject | The only signal that moved in these runs (§4 item 8). | Measures content, not pull: jargon passed it 6 of 6. Overlaps I2. |
| C. Mixed-model panel (three or more model families) | agreement across models | Breaks the n = 1 correlation; automated. | Shared trained disposition to show interest may survive. Verdicts drift as models change, so the intent stops being a fixed yardstick. Cost. |
| D. Human readers (5–8 non-specialists; forced choice or continue/stop behaviour) | the construct itself | The only design with face validity for "visitor". | Slow, costly, noisy at small n, not repeatable per skill iteration; recruits are not real visitors. |
| E. D once, to validate A or C: humans rank about six anchor openings; keep the automated measure only if its ranking agrees | whether a proxy tracks people | Pays the human cost once; turns the proxy from asserted to checked. | Agreement on six anchors may not hold near the boundary where candidates sit. |
| F. Owner judges I1, blind forced choice among candidates | the owner's own intent | Correct by definition; zero build cost. | Not blind-testable by a fresh judge (breaks AC2); the owner is not a stranger to the idea. |

**ε-2. The calibration rule checks failure, not discrimination.** "Known
fail must fail" is met by a panel and judge that fail everything, which is
the pattern run 2 produced. Fix: one sentence in Amendment 2 C-1: "for each
reader-based clause, one fixture must pass and one must fail **on the same
answer field**, and the run is void unless they differ". Also require the
test to be executed in the round it is introduced: the reader-panel design
arrived in round 2 and first ran after round 4, with one round left.

**ε-3. Amendments and rounds have no rules.** (a) The orchestrator relaxed
acceptance criteria at the writer's request, mid-cell, without the owner.
Fix: "an amendment that relaxes a criterion or widens scope needs the
owner's sign-off before the next round; a tightening amendment may be
provisional". (b) A round is not defined; rounds 4 and 5 were spent on an
α ↔ calibration-judge loop with no β. Fix: "a round is one α commit and one
β verdict on it; a void calibration returns to α once without consuming a
round, and β reviews any change to a fixture, row or rule made after a void
run". (c) Contract findings (C-n) have no named dispositioner; γ was both
the amended party's arbiter and its author. Fix: C-n findings go to the
owner.

**ε-4. Evidence passes through the orchestrator.** γ ran the readers,
condensed their answers and handed the condensation to the judge. Fix: γ
writes one raw file per reader (prompt, model ID, settings, full output,
timestamp) and all fixture texts; the judge reads those; a summary is never
evidence.

**ε-5. Fitting to the test.** After a void run the writer changed fixtures,
rules and a row's stated answer from the run's own data, and one row was
widened until it held (R6). Fresh readers for run 2 was correct, but nothing
stops repeated revision until something passes. Fix: freeze each row's
"by this answer" before the run; widening a row needs β; cap calibration
runs per cell.

**ε-6. Independence from skills is stated but not enforced.** The seed was
drafted by the agent that knows the skill and carried its wording (R10); the
writer may read `skills/`. Fix: the owner supplies the seed in the owner's
own words (the four intents already are), and α's checkout excludes
`skills/`; α and β each state what they did not read.

**ε-7. The size cap is a proxy that was met by compression.** Fix: cap what
the reader bears (the sheet), not the key; or count words.

**ε-8. Review properties drift from the contract.** REVIEW-PROPERTIES was
never amended. Fix: an amendment edits both files in the same change.

**ε-9. Role attribution in git.** The seed is committed as "alpha". Fix:
commit author is the role that wrote the change.
