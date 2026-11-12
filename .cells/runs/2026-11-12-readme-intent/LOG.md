# Cell audit log: README intent

Contract: ../CONTRACT.md · Review: ../REVIEW-PROPERTIES.md
BASE (before seed): see BASE · Seed commit: see SEED (7e4f87e)
Roles: α writer, β reviewer (separate agents, β sees contract, matter and α's
dispositions only), γ orchestrator (relays, logs), δ separate validator agent
(recommends accept/reject), owner decides. ε only if δ finds protocol faults.

| Round | α commit | β verdict | Blocker | Major | Minor | Open |
|---|---|---|---|---|---|---|
| 1 | 8fcc0c7 | REQUEST CHANGES | 0 | 9 | 5 | 14 |

## Round 1
- α: 8fcc0c7. Iterated on the seed (round-1-alpha.md). Owner intents kept as
  I1–I4 with explicit priority (I1, I3 first); clarity strengthened; "read
  on 1–5" replaced by concrete checks; stake absorbed as proposed I5;
  reference answer split into required elements E1–E4 (seed's wording leaned
  toward "only a description"); misreadings summarised in-file; 5 exemplars
  verified. Thresholds 600/100 words are α's, not owner's. Gap: judge lacks
  READING.md — β to check the in-file summary.
- β (fable): REQUEST CHANGES on 8fcc0c7. Q1 owner fidelity pass; Q3
  grounding pass (5 exemplars fetched); Q2, Q4, Q5, Q6 fail. Majors: judge
  primed by reference answer in the same file (copying E1–E3 passes I2);
  "paragraph one" undecidable; no word-count rule; 7 unruled judgments;
  stake required by I1, cuttable by I4, unsupported by I5; overlapping
  checks; I1 tests ingredients not pull; reference answer breaks the file's
  own caps; M1 ambiguous. Blind run on current README: I1–I4 fail (stable),
  I5 undetermined.

## Round 2
- α: f9fd515. 13 fixed, B1-12 partly rejected (no verifiable theory-repo
  README exemplar). Redesign: reader sheet (Part A) vs judge key (Part B);
  3 readers, 2-of-3 rule; contradictory checks removed; I1 tests effect
  (reader's question answered in the README); scripted opening and word
  count. Gaps G1 (key needs its own file), G2 (no line headroom), G3 (AC2
  assumes one judge).
- γ: Contract Amendment 1 accepts G1–G3 (key file; caps exclude Grounding;
  readers + judge). β to review the amendment. α implements G1 before review.
| 2 | 495a48e | REQUEST CHANGES | 0 | 5 (+1 contract) | 3 (+3 contract) | 8 + 4 C |
- α 2b: 495a48e. Key moved verbatim to intents/readme-key.md (97 lines); readme.md is reader sheet (24 lines) naming each role's inputs.
- β: REQUEST CHANGES on 495a48e. All 14 B1 closed (13 resolved, B1-8
  accepted; B1-12(i) rejection accepted). Q1, Q3, Q4, Q6, Q7 pass; Q2, Q5
  fail. Majors: reader unspecified and no calibration (model readers always
  say "read on"); A1 completeness/misreading gap; 2-of-3 rule ambiguous;
  ASCII-only word regex; I1's "question answered" rewards overclaiming on the
  Theseus question. Contract: C-1 major (no calibration requirement), C-2..C-4
  minor (C-4: owner must ratify amendments).
- γ: Amendment 2 (calibration required; combined 150-line cap; wording;
  owner ratification at δ).
| 3 | 67a2515 | REQUEST CHANGES | 0 | 2 (+1 contract) | 3 | 5 + C-5 |

## Round 3
- α: 67a2515. B2-1..8 all fixed. A6: reader writes the README's answer to
  their own question; an honest "can't be answered yet, because …" passes,
  overclaims fail, counted inside I1 (proposed). Reader specified; calibration
  with P (reference opening, must pass) vs F (kernel Statement, must fail),
  3 fresh readers each, run void if indistinguishable. Per-reader scoring,
  2-of-3 (proposed). Unicode word regex. 29 + 130 lines (142 excl.
  Grounding). Gaps: calibration not yet run (α can't be a fresh reader);
  owner to approve F and the proposed numbers.
- β: REQUEST CHANGES on 67a2515. 7/8 B2 resolved, B2-1 carried as B3-2.
  Majors: "proposed = reported" would disable A6 and the word cap (need two
  labels: in force vs reported only); a yes-to-everything panel passes
  calibration because F fails on jargon, not pull — need a plain, accurate,
  dull known-fail for I1. A6 design judged sound. Contract C-5 (major):
  calibration must actually run before close.
- γ: Amendment 3 (logged calibration run before APPROVE; a known-fail per
  reader-based intent).
| 4 | 39049a9 | (calibration, then β) | | | | |
- α round 4: 39049a9. B3-1..5 fixed. Labels: in force / reported / owner to approve. Calibration procedure: 5 fixtures (P pass; F1 dull-plain fails I1; F2 misreading fails I2; F3 jargon fails I3; F4 repetition fails I4), 3 fresh readers each, void if any row fails for 2 of 3. 149 lines excl. Grounding.

## Calibration run 1 (Amendment 3) on 39049a9 — VOID
- Readers: 15 fresh Claude Sonnet instances, no tools, 3 per fixture, each
  used once. Step 2 administered only for F4 (the only Step-2 row); judged
  by the fresh judge as unable to change any verdict. Answers:
  calib/answers.md. Fresh judge (no log access): calib/judgement.md.
- P 0/3: A1 meets E1, E3 but not E2 (every reader reduced "both ways round"
  to "they can disagree"); A3 never empty (7–8 flags each, many contradicted
  by the reader's own correct A1). F1 0/3: all said yes ("weak yes") —
  though all fail I1 via the name-question clause, which "does not count".
  F2 3/3, F3 3/3, F4 3/3 hold.
- Judge's diagnosis: P/E2 = fixture wording ("both ways round" opaque; the
  same readers get E2 from plain "each can hold where the other does not");
  P/A3 = rule infeasible for this reader kind; F1 = rule too narrow ("A2 no"
  vs I1's own failure condition) plus yes-lean; A5 may flag any README's
  opening because readers saw it in Step 1. Also: all P readers wrote
  "two different ways of picking out", close to the "ways of looking"
  misreading.
| 5 | fb2b212 | not reviewed (cap reached; calibration run 2 void) | | | | |

## Round 5
- α: fb2b212. Fixes from run 1: P states both directions plainly; A3/A4
  flags count only with a missing or wrong guess; A2 adds "maybe", I1
  needs plain yes; F1 row covers all of I1 Step 1; A5 = repeats of an
  earlier unit; literal procedure; I2 "views" fault clarified.

## Calibration run 2 on fb2b212 — VOID
- 15 new fresh Claude Sonnet readers; Step 2 on F4 only (as now specified).
  Fresh judge: calib2/judgement.md.
- P 0/3: all three A2 "Maybe" (I1 needs yes); A1 misses E3 (P-1 "deciding
  which kind counts"), E3 placement (P-2), E2 (P-3, borderline); counted A3
  flags on "Its test". F1 3/3 (maybe + name-question), F2 3/3, F3 3/3 (some
  counts are kernel-meaning judgement calls: rhythm, cohering), F4 3/3.
- All 15 readers answered "Maybe": A2 no longer discriminates in either
  direction. Self-reported pull from same-model readers is not a usable
  signal (yes-bias in run 1, maybe-bias in run 2).
- Judge flagged a γ fault: answers.md condensed ("[list]", "same content"),
  F4-2/3 A5 described not quoted, F2–F4 fixture texts not stored in fx.json.
  The key requires verbatim logs. Readers not independent (one model).

## γ closure — NOT CONVERGED
- Round cap (5) reached. β's last review was round 3 (67a2515); rounds 4–5
  unreviewed. Amendment 3's calibration gate failed twice. The cell cannot
  close under its contract.
- What is settled: owner intents I1–I4 present and not weakened (β Q1 pass
  rounds 1–3); grounding verified; F2, F3, F4 discriminate reliably (3/3 in
  both runs); I2 elements and I4 repetition check work.
- What is not: a valid measure of I1 (pull) with model readers; P as a
  known pass; the A3 guess rule for openings that defer detail.
- Handing to δ.
