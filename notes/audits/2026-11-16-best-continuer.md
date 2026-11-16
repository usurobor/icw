# Audit of candidate C10 against the closest-continuer literature, 2026-11-16

Auditor check of C10 and C10s (best continuer, two-way, Jaccard closeness, plus integration) against Nozick, Philosophical Explanations (1981), ch. 1, and the objections to it. "Verified" means I opened a page that states it. Page numbers marked (2nd-hand) come from a secondary source and were not checked against the book.

| Q | Finding | Citation verified? | Consequence for C10 |
|---|---|---|---|
| 1 Attribution | Nozick's term is "closest continuer", not "best continuer". Ch. 1 ("The Identity of the Self"). Two conditions: the continuer is causally dependent on x, and no rival is at least as close. | Chapter: yes. Pages p. 35 (conditions) and p. 62 (ties; "Ties and Caring" begins there): p. 62 twice, p. 35 once (2nd-hand). | Say "closest continuer (Nozick)"; "best" is the register's word. Cite ch. 1, pp. 35 and 62 (2nd-hand). |
| 2a Only x and y | Noonan names it and attributes it to Williams, not Wiggins. Nozick rejects it knowingly. | Noonan §1.11 p. 13: yes. Wiggins: not found. | Applies fully: C10's A->B verdict changes with a rival in reach. Declare it; do not claim the principle holds. |
| 2b Parfit and others | Parfit: a "no branching" clause makes identity extrinsic; identity is not what matters. A sharp cutoff on a spectrum is arbitrary. Fost: Nozick leaves the metric open. | Parfit via Noonan pp. 19-21, WILP-7 §2, Cooper: yes (secondary). Parfit's own pages: not checked. | Arbitrariness applies to C10s (0.5) and to "unique best" (flips on one cell). Fixing a metric is the register's choice, not Nozick's. |
| 2c Ties | Nozick: equal closeness, neither is x. Wiggins 1967 has the amoeba case, same verdict. Fost: a tie is indeterminate, not false. | IEP, Barrette p. 62 (2nd-hand), Wiggins Pt 2 §2.1 pp. 37-38 (tool-read): yes. | C10 matches Nozick. Log "tie" apart from "uncarried" so a tie does not read as a refusal by the rule. |
| 3 Jaccard | One dimension of Nozick's multi-dimensional closeness, and the causal-dependence side (what F alone yields). Defensible as a special case, not as "Nozick's closeness". | Nozick's open metric: Fost p. 113 (2nd-hand quote of Nozick 2003). | Claim "a rule-relative closeness in the spirit of", never "Nozick's measure". |
| 4 Prior art | Two-way best match exists as "mutual NN" cross-check in feature matching. Tracking tools I opened use one-to-one assignment or forward-only linking. Nothing found in CA literature. Wiggins's "dominant claimant" is the one-way philosophical ancestor. | Image-matching survey §4.2: yes. SimpleTracker, two PTV papers: yes (no mutual rule). Computational mechanics: searched, not opened. | Prior art is for the operation, not for identity. Report "not found" for CA and persistence. |
| 5 Overreach | See below: C10s is ambiguous; comparison set is a parameter; integration is the C9 patch plus a horizon; R1 tension with D8's wording. | n/a | Six changes listed in the last line block. |

## Q1. Attribution

The term is Nozick's, from ch. 1 of Philosophical Explanations. A Cambridge chapter note says he gives "most, but not all, of the first chapter" to personal identity. Barrette (2008) cites p. 35 for the condition that a continuer arise from x's properties. Gordon's letter in the NYRB (1982) puts "Ties and Caring" at p. 62; Barrette also puts ties at p. 62. Cooper cites p. 67 for the "Platonic glasses" remark. The IEP and Cooper describe "closeness" as weighted dimensions, not one score. "Best continuer" does not appear in the sources I opened; Nozick's "best instantiated relation" (Barrette, pp. 53-54, 2nd-hand) is a neighbouring term. A "close enough" clause appears in Nozick's closeness schema (Barrette, p. 85, 2nd-hand), so a threshold variant like C10s stays inside the family, but no source gives a number. specs/ARTICULATION.md line 280 ("Parfit and Nozick on fission") has no locator; add one.

## Q2. Objections

**(a) Only x and y.** Noonan §1.11 p. 13 defines it as: no facts about any other individual can be relevant. He attributes it to Williams, and uses it against Nozick (split brain: survival depends on a rival's non-existence). Wiggins (1967) does not state it in the text I opened. Applies: C10 breaks it by design, and says so only if the register says so. The comparison set (connected pieces within reach) makes the dependence bounded: a rival beyond reach changes nothing. Nozick accepts the dependence (core.ac.uk, a Spanish summary of the ch. 1 theory).

**(b) Parfit and others.** Parfit's fission argument (Noonan pp. 19-21): identity is not what matters. A "no branches" clause makes identity extrinsic (WILP-7, §2). Cooper reports Parfit's objection that a cutoff on a spectrum is arbitrary. Fost objects that the metric is unspecified and that ties give indeterminacy. Applies to the 0.5 of C10s and to exact-uniqueness in C10.

**(c) Ties.** IEP: if two continuers are equally close, neither is identical to the original. Wiggins Pt 2 §2.1: "neither of them can be identical with it" (amoeba). Applies: C10 follows Nozick. With floating-point Jaccard, ties become rare accidents; compare exact fractions.

## Q3. Jaccard against isolated evolution

Jaccard of X against what F alone yields in one step is a counterfactual comparison under the rule. That matches Nozick's causal condition (the continuer grows out of x) and gives a resemblance score on the cells that result. It drops the other dimensions Nozick lists, and his weighting by what the self cares about; Fost quotes Nozick as refusing fixed details. So it narrows the concept to rule-relative resemblance. Defensible when called that. Two cautions: one step looks only at the next stage, and Jaccard on the empty stage is 0/0, which needs a stated value.

## Q4. Two-way matching

Verified: the image-matching survey (§4.2) calls the cross-check "mutual NN" and keeps a match only if found in both directions. SimpleTracker (GitHub README) links frames by Hungarian assignment minimising total distance, one-to-one but not mutual-best. The arXiv a-contrario tracker and the 4-frame PTV paper (§3.3) use global trajectory extraction and forward nearest-neighbour. The local-information-transfer paper for CAs computes particles from observed statistics, and describes no matching criterion in the part I read. Not found: a persistence criterion in CA or philosophy that is best-successor AND best-predecessor. Nozick treats fusion as well as fission (Noonan §1.11 p. 13), the nearest philosophical relative.

## Q5. Overreach

1. C10s says "share" but Jaccard is not normalised. Two rivals can both exceed 0.5, so both would be carried, which is the fission verdict Nozick denies. State raw or normalised.
2. Carrying depends on the board partition. C9 failed because connectivity flickered (probes, finding 2); the comparison set repeats that risk. Declare connectedness, reach and the empty stage as part of the candidate.
3. "Integration over the remainder of the run" is the C9 patch the owner called a patch, and it makes a verdict at step t depend on a horizon.
4. D8 says the changing sustains the continuity. C10 lets a rival elsewhere remove it. Say in D8 that carrying is relative to a comparison set, as R1's exception allows.
5. Tie counts and refusal share belong in the run's guards.
6. Claim Nozick as a parallel only.

URLs opened: https://eclass-b.uoa.gr/modules/document/file.php/PHS688/Metaphysics_Bibliography/Noonan%20Personal%20Identity.pdf ; https://core.ac.uk/download/39056278.pdf ; https://iep.utm.edu/nozick ; https://www.lorenzopena.es/Sorites/Issue_20/cooper.htm ; https://philarchive.org/archive/WILP-7 ; https://www.nybooks.com/articles/1982/05/27/the-identity-of-nozick/ ; https://era.library.ualberta.ca/items/e1900112-d8d3-4ef5-9ab4-694391019679/download/3381dd7b-38c1-4ece-9653-e684cb70c075 ; https://philarchive.org/archive/FOSTES ; https://cambridge.org/core/books/robert-nozick/metaphysics-i-personal-identity/8F259B385A27D71DFD00F2C1993DE715 ; https://www.informationphilosopher.com/solutions/philosophers/wiggins/identity.pdf ; https://arxiv.org/pdf/2003.01587 ; https://www.github.com/tinevez/simpletracker ; https://arxiv.org/pdf/1507.06266 ; https://arxiv.org/pdf/1712.07506 ; https://ar5iv.arxiv.org/html/0809.3275 ; https://cambridge.org/core/services/aop-cambridge-core/content/view/FD14040991C63AF8F9D15EFF8C305856/S0034412500021570a.pdf/reincarnation-closest-continuers-and-the-three-card-trick-a-reply-to-noonan-and-daniels1.pdf (no use made). Blocked or not opened: PMC2747604 (captcha), pdcnet (login), SEP (not on allowlist).

AUDIT: CHANGES
1. Write "closest continuer (Nozick, PE ch. 1)"; "best" is the register's term; add a locator to ARTICULATION.md line 280.
2. Cite the only-x-and-y principle to Williams via Noonan §1.11 p. 13, not Wiggins; state that C10 violates it by design.
3. Define C10s: raw Jaccard threshold or normalised share, and what happens when two candidates both pass.
4. Declare the comparison set (connectedness, reach, empty stage, value of Jaccard on empty) as part of C10 before the run; use exact fractions for ties.
5. Name integration over the remainder of the run as the C9 patch with a horizon; do not count it as the candidate's principled part.
6. Log ties apart from "uncarried"; claim Nozick only as a parallel.
