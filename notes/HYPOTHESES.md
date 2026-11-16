# Hypotheses

What the ICW research programme hopes to establish, and how each claim could
fail. Drafted 16 Nov by the owner with Claude and GPT. This file changes only
when evidence arrives: a run, a review, or an owner ruling.

**Status** is one of: *untested*; *supported* or *contradicted*, each within a
stated scope; *inconclusive*. A failed search defeats the candidates or the
programme searched, never the unrestricted claim.

**Three ambitions, kept apart.** Clarifying existing explanations (H4–H8),
discovering continuities nobody supplied (H9), and improving decisions (H10).
Success at one is no evidence for another. H1–H3 are the formal ground; HM is
about the method itself.

## The three questions

"Cells produce a glider" can mean any of three questions, so its words alone
show no confusion.

| | Question | Answering it requires |
|---|---|---|
| Q1 | Which configurations develop into a glider? | an account of the dynamics |
| Q2 | What makes successive footprints the same glider? | a persistence criterion, and evidence the dynamics sustain it |
| Q3 | What further process turns cell activity into a separate glider process? | first, a reason to think there is such a process |

ICW's strongest possible contribution concerns Q3. It must leave Q1 and Q2
intact.

## Formal ground

**H1 — Game of Life calibration** (formal obligation). For registered glider
histories, formation under the cell rule (Q1) and persistence under an
explicit tracking criterion (Q2) can be described separately, and computing
the histories needs no dynamics beyond the rule.
- *Check:* executable accounts agree with the simulator on the registered cases.
- *Limit:* the rule is complete by stipulation. H1 fixes no unique tracking
  criterion and settles nothing about O2.
- *Status:* untested. Iteration 0 exercises Q2 on placed gliders; formation is
  not yet scripted.

**H2 — Articulation versus production** (formal hypothesis). Registered
computational cases can be sorted into a change of description and a causal
transition by a frozen candidate rule. First candidate:
> A causal claim is about production when its cause and effect are different
> occurrences linked by reach, whichever criteria describe them. The suspect
> move is a claim whose cause and effect are the same occurrences read under
> two criteria.

This keeps R5: "the collision made these cells switch" relates earlier
occurrences to later ones, read at either level. Competing candidates, such as
"the two can be manipulated separately", are registered beside it and the
cases decide.
- *Test:* cell and glider, guns, collisions, splices, each with the exact
  occurrences and transitions every claim concerns.
- *Against:* independently established causal transitions repeatedly sorted as
  articulation, or verdicts that turn on arbitrary choices of description.
  Shared occurrences alone decide nothing.
- *Status:* the first candidate (reach) is contradicted within eight
  registered claims: it calls a distant glider and a gun's next glider
  products of the cause. Dependence (different occurrences, and deleting the
  cause changes the effect) is supported within the same eight. Untested:
  overdetermination, preemption, partly overlapping cause and effect
  (`notes/runs/2026-11-16-h2.md`).

**H3 — Carrying generalises** (bounded conjecture, O2). A criterion grounded in
the dynamics separates the intended carried continuities from stipulated
splices, admits structures fed by their surroundings, treats integration as a
separate property, and covers both sides of `A < X > B`, the elemental one
included.
- *Test:* freeze candidate and anchors, then run unfamiliar cases: fed
  structures, moving elements, perturbation.
- *Against:* every candidate in the declared programme fails these
  requirements, or passes only through case-specific exceptions.
- *Status:* inconclusive. Iteration 0: Closure and C7 match every target, the
  union of two distant gliders holds under every candidate, and Closure's
  isolation test may refuse fed structures by construction
  (`notes/runs/2026-11-16-iteration-0.md`; review `2616eef`).

## Clarifying explanations

**H4 — Reliable interpretation** (comparative). An ICW-guided procedure
identifies which of Q1–Q3 a passage asks more accurately than an equally
structured control, without dismissing legitimate causal questions more often.
- *Test:* unseen passages, about half of them legitimate production;
  independent judges; mixed and ambiguous questions allowed.
- *Against:* the prespecified improvement ruled out, or more false dismissals.
- *Status:* untested.

**H5 — Better explanations** (comparative). The three-question method improves
how explanations separate mechanism, persistence and added assumptions, and
keeps their scientific content.
- *Test:* blind assessment against an equally structured generic checklist;
  factual preservation scored apart from clarity.
- *Against:* no meaningful advantage, or clarity bought by deleting content.
- *Status:* untested.

**H6 — A false gap exists** (bounded existence). In a specified corpus, at
least one explanation demands an extra mechanism because of an unjustified
move between identity criteria, and removing the move keeps every legitimate
target of explanation.
- *Evidence:* one documented case survives independent domain and
  philosophical criticism. A manual case needs no validated instrument; an
  automated survey needs H4.
- *Against a case:* the author made no such move, or a legitimate target was
  discarded.
- *Status:* untested.

**H7 — False gaps recur** (distribution). The move in H6 occurs in
independently developed explanations in at least two fields.
- *Test:* independently sampled material and independent diagnoses. A borrowed
  example appearing twice counts once. Prevalence is a separate estimate.
- *Status:* untested; needs H6.

**H8 — Mind** (speculative, argument-specific). In at least one specified
mind–brain argument, ICW identifies an unneeded demand for an extra mechanism
without removing what the argument seeks to explain.
- *Bridge required:* a reason to treat neural and experiential descriptions as
  articulations of one changing whole. That cannot be assumed.
- *Against:* the problem survives the reformulation, or disappears only because
  experience was left out. Success elsewhere is no evidence here.
- *Status:* untested; held until H4–H7 have results.

## Discovery and use

**H9 — Discovering continuities** (constructive). Given unfamiliar
computational dynamics with no catalogue of objects, an ICW-guided procedure
finds defensible persistence criteria nobody supplied, better than existing
discovery tools at equal compute: apgsearch's census of soups, and the
particle filters of Hanson and Crutchfield (C2).
- *Test:* explicit tracking rules, independent verification, unseen histories.
- *Against:* it only recognises familiar patterns, produces unsupported
  groupings, or matches the baseline.
- *Status:* untested.

**H10 — Operational value** (practical). An ICW-derived distinction improves a
specified prediction, intervention or engineering decision.
- *Test:* task, outcome and useful improvement fixed in advance; compared with
  equally resourced conventional methods. Software identity bugs and neural
  steering are separate studies.
- *Against:* new vocabulary with no useful improvement, or costs above the gain.
- *Status:* untested. Software identity bugs parked 16 Nov (problem judged
  diffuse; owner).

## The method

**HM — Automated criticism pays** (method). The adversarial loop (register,
scripts, model panel, predictions frozen before runs) finds defects in the
theory at lower cost in owner attention than unaided dialogue.
- *Evidence:* git history records who or what found each defect, and at what
  cost.
- *Log:* 16 Nov, the harness refuted the verbal prediction that Closure refuses
  the union of two distant gliders. 16 Nov, the panel caught an unchecked
  attribution (Krakauer et al. 2020 cast as an indecomposability criterion).
- *Status:* untested as a comparison; two entries logged.

## Dependencies

H1, H2 and H3 are formal and run in parallel with H4 and H5. H6 by hand needs
nothing; H6 by survey needs H4. H7 needs H6. H9 needs only a specified evaluator. H8 needs its own bridge whatever the others show.
