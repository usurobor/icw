# Round 1 — β

Commit reviewed: `9ec0b37fb7778a6e2dab7a5d7943f7eec82a46b8`
Base: `216a5d6b3b03a7c44655ad9ac3f3b4f00e95b9a2`

Working tree clean, HEAD = 9ec0b37 (branch `icw-fresh`).

## Mechanical checks run

- `python3 tools/lint.py`: `0 error(s)`.
- Relative links: all 18 in README.md and examples/*.md resolve. The anchor
  `#icws-terms` matches the heading "ICW's terms".
- `git diff --stat 216a5d6 9ec0b37`: only README.md and examples/{glider,limits,ship,wave}.md.
- `A < X > B` forms: all spaced and in code (README 72, 87, 115, 119; each example).
- Executable checks (script outside the repo, imports `tools/algebra.py`):
  - Glider (B3/S23, standard glider): period 4, shift (1,1); no live cell in
    common with step 0 at step 16 (and from step 8 on). Matter is correct here.
  - Life rule: a dead cell with 2 live neighbours stays dead, a live one stays
    alive. Neighbours alone do not fix the next state (B1-2).
  - Share of distinct partition pairs that cross-cut: n=4 57%, n=5 77%,
    n=6 89%, n=7 95%. Cross-cutting is the generic case (B1-3).

## Properties

| Property | Result | Why |
|---|---|---|
| P1 Kernel fidelity | fail | limits.md treats "not holds" as "refused" (B1-3); one wrong ID citation (B1-15). Verdict names, proposed markers and "no pair holds" are otherwise correct. |
| P2 Misreadings | fail | ship.md puts the ship itself in a frozen frame, against D3 and READING #3 (B1-4). glider.md's "otherwise arranged" argument slides into determination (B1-10). |
| P3 Prior-art accuracy | fail | Gibbard is cited for the opposite of his claim (B1-1). Hobbes and Locke paraphrases are slightly lossy (B1-11, B1-12). Other locators verified. |
| P4 Novelty claims | fail | Additions #2, #3 and #4, and ship.md's addition, are already in prior art that is credited or omitted (B1-5 to B1-8). "Stated exactly" overclaims (B1-13). |
| P5 Examples | fail | The Life rule is stated falsely (B1-2). Grue and Locke's mass have no named changing whole (B1-9). Wave, glider and ship give both directions and a plausible whole. |
| P6 Clarity | fail (minor only) | The first screen works. Problems: "occurrence" undefined, an opaque genidentity gloss, small wording faults (B1-14, B1-17 to B1-20). |
| P7 Notation and mechanics | pass | Lint shows 0 errors, links resolve, and notation is spaced and in code. |
| P8 Footprint and scope | pass | Only matter files changed. No predecessor project is named in the matter (see gap 6). |

## Verification of prior art (web)

Verified: Heraclitus B12 (SEP *Heraclitus*). Plutarch *Theseus* 23.1
(Perrin). Hobbes *De Corpore* II.11.7, including "by what name anything is
called" and "a ship, which signifies matter so figured" (Pomona handout of
the Molesworth text). Locke II.xxvii.3, 7, including the §7 heading "Idea of
identity suited to the idea it is applied to" (CUHK text). Quine 1950, *JPhil*
47: 621–633: "River stages are water stages, but rivers are not waters", plus
the same-river/different-water and same-water/different-river cases (FLPV
text). Geach 1967, *Rev. Metaphysics* 21: 3–12. Wiggins rejects relative
identity but holds D (NDPR review of *S&S Renewed*). Dennett 1991, *JPhil*
88(1): 27–51, p. 39: "at the physical level there is no motion", and "one and
the same glider". Life's rules (LifeWiki).

Not verified, and not claimed by the matter: a section number or wave example
for Reichenbach's material/functional genidentity. That the distinction is in
*The Direction of Time* is supported by secondary notes. I accept α's
book-level citation.

Found wrong: Gibbard 1975 (B1-1). In SEP *Material Constitution* and the
Oberlin summary, the statue and lump in Gibbard's case are made and destroyed
together. The squeezing is counterfactual, and Gibbard concludes they are
contingently identical.

## Findings

### Blockers

**B1-1** · blocker · P3 · README.md, "A conversation 2,500 years old",
"Constitution" bullet (lines 44–46).
*Problem.* "squeeze the clay into a ball and the lump survives while the
statue does not (Gibbard 1975)". Gibbard built his case so this does not
happen. Goliath and Lumpl begin and end together, and the squeezing appears
only as a counterfactual. His thesis is that they are **identical**
(contingently), with persistence relative to the kind each name is given
under. The matter cites him for the non-identity argument he rejects.
*Change.* Choose one:
(a) Credit the actual-squeeze non-identity argument to Wiggins, "On Being in
the Same Place at the Same Time", *Phil. Review* 77 (1968): 90–95, and add it
to References.
(b) Keep Gibbard and state his claim correctly. The two are made and
destroyed together and differ only in what would happen. Gibbard concludes
they are contingently identical, each name carrying its kind's persistence
conditions.
Whichever you choose, the bullet must not attribute to Gibbard a conclusion
he denies.

**B1-2** · blocker · P5 · examples/glider.md, "The case" (line 9).
*Problem.* "each cell's next state is fixed by its eight neighbours" is false.
The next state depends on the cell's own state and the count of live
neighbours (B3/S23). With exactly two live neighbours, a dead cell stays dead
and a live cell stays alive.
*Change.* Write "each cell's next state is fixed by its own state and how many
of its eight neighbours are alive", or give B3/S23 in words.

**B1-3** · blocker · P1 · examples/limits.md, opening paragraph (line 3), page
title, and README "Examples" (lines 130–131).
*Problem.* "Most pairs put to the test are refused" is false, and it reads a
§6 verdict wrongly. Cross-cutting pairs are not refused. They get
**uncarried**, which the kernel calls "undecided while O2 is open", and O2
says co-articulation "cannot be refused for arbitrariness". Cross-cutting is
also the generic case: 57–95% of distinct partition pairs for 4–7
occurrences. README itself says "Cross-cutting is cheap". FINDINGS' "most
cases will not return *holds*" is a different claim from "most are refused".
The title "Where the test says no", and README's list putting grue under it,
repeat the error, because the test does not say no to grue.
*Change.* Replace the opening claim with something like: "The test refuses a
pair for type, coincidence or nesting. A cross-cutting pair, the common case,
it cannot yet refuse (O2)." Retitle the page (e.g. "Where the test stops"),
or give grue a heading that says the test cannot refuse it. Update README
lines 130–131 to match.

**B1-4** · blocker · P2 (READING #3; D3) · examples/ship.md, "What ICW adds to
Hobbes", second paragraph (lines 46–47).
*Problem.* "True of its footprint: freeze the dockyard and the ship is some
planks (D3)." The sentence after the colon says the frozen frame holds *the
ship*. D3's *Why* says "A frozen frame holds footprints only, never a
persistence", and READING #3 says "A frame holds neither, only a footprint."
*Change.* Write "freeze the dockyard and the ship's footprint is some planks".
For consistency, rewrite wave.md line 36–37 the same way: "at an instant, the
wave's footprint is some water".

### Majors

**B1-5** · major · P4, P3 · README.md, opening (lines 12–15, "asks the next
question") and "What ICW adds" #2 (lines 106–110).
*Problem.* The hook and #2 imply that the tradition has not asked whether a
criterion of persistence is sustained by the world's changing or laid across
it. That question has direct prior art the matter omits:
- Reichenbach's mark criterion, which separates causal processes from
  pseudo-processes ("unreal sequences", e.g. a moving spot of light).
- Salmon, *Scientific Explanation and the Causal Structure of the World*
  (1984), on causal processes and pseudo-processes.
- Russell's causal lines as what constitutes identity over time.
- Immanent causation as a condition of persistence (Zimmerman, "Immanent
  Causation", *Phil. Perspectives* 11, 1997).
- Hirsch, *The Concept of Identity* (1982), on unified versus gerrymandered
  persistence conditions.

D8's first candidate, "the changing preserves the continuity's classes
forward", sits very close to mark transmission and immanent causation.
*Change.* Credit at least the pseudo-process line (Reichenbach / Salmon 1984)
and the immanent-causation line (Zimmerman 1997), and consider Hirsch 1982.
Verify each locator before citing. Reword #2 so the addition is only what
these do not contain. Candidates: making carrying the last check of an ordered
test on a *pair* of criteria over one changing; and D8's type constraint, that
carrying is a predicate on relations, not a further relation. If α finds the
type constraint in the cited works, drop it too. Change "asks the next
question" so it does not suggest the question is new.

**B1-6** · major · P4, P3 · README.md "What ICW adds" #3 (lines 111–113);
examples/glider.md "Two criteria" and final paragraph (lines 66–68).
*Problem.* Dennett (1991, p. 39) already states both Life criteria. At the
physical level nothing moves and cells are fixed locations. At the design
level "one and the same glider" moves. He also says the patterns are fully
calculable from the rule. So README #3's illustration ("A glider is
calculable from the cell rule, and glider-sameness and cell-sameness still
cross-cut") is Dennett's point. glider.md's "ICW asks a different question,
what counts as one" misdescribes Dennett, who does say what counts as one
glider.
*Change.*
- glider.md: credit Dennett in "Two criteria" for both criteria. Rewrite the
  last paragraph: Dennett argues the pattern is real; ICW asks whether the
  grid's changing carries both criteria, and stops at uncarried.
- README #3: credit Dennett for derivability versus pattern, and name what R1–R3
  add beyond him, or drop #3 from the additions.

**B1-7** · major · P4 · README.md "What ICW adds" #4 (lines 114–121).
*Problem.*
- R4's content is older. A persisting thing is made of no particular matter,
  and composition is true of it only at a time. ship.md already concedes this
  ("Locke's oak … makes the older form of this point"), and the constitution
  debate has time-indexed parthood. #4 still lists composition as an ICW
  addition without credit.
- R5 ("one change … read through two criteria … never … a further process") is
  close to Davidson's one event under two descriptions. Davidson is cited only
  in glider.md and in README's References, never in README's body.
- "Against the constitution debate, the addition is a scope" is opaque to a
  non-specialist.

*Change.*
- Credit Locke's oak (and, if used, time-relative parthood, with verified
  locators) at R4. Credit Davidson 1970 at R5.
- For each, name the precise addition as "makes precise …", or withdraw it.
  Example for R4: the identity-fixing reading fails across a cross-cutting pair
  because neither criterion refines the other.
- For R5, say how two *criteria of identity* differ from Davidson's two
  *descriptions*. D9 excludes reading articulations as descriptions; apply
  the same caution to glider.md line 57.
- Rewrite the constitution sentence in plain terms tied to the statue-and-clay
  bullet.

**B1-8** · major · P4 · examples/ship.md "What ICW adds to Hobbes", first
paragraph (lines 40–42).
*Problem.* "What it adds is checkable: the pair cross-cuts in both directions."
The two directions are Plutarch's and Hobbes's own. Lines 22–23 of the same
file say "the case is stated in them". This is claimed as an addition.
*Change.* Credit both directions to Plutarch and Hobbes. State ICW's addition
only as running the ordered test (the pair passes checks 1–3 and stops at 4,
uncarried) and naming the open carrying question for this case.

**B1-9** · major · P5, P1 (D11) · examples/limits.md, "Coincident" and
"Uncarried" sections. README.md test table rows 2 and 4 and lines 89–92.
*Problem.* D11 requires X, and README line 78 says "in a named whole". Neither
Locke's mass nor green/grue has a named whole. For grue, the only implied
whole is "the gems" (README 92; limits 47 "their changing"). The gems do not
change in any respect either criterion tracks, so check 1 would make the case
**untyped**, like the cone, not **uncarried**. The witnesses compare
different gems, not occurrences in one changing.
Also, a reader given README's definition of a criterion of identity ("fixes
what counts as one thing, what keeps it the same one …") will not see colour
as one. The matter never says that D1 admits any equivalence on occurrences
as a candidate, which is what makes grue relevant.
*Change.*
- Name X for each case and show it changes. For grue, e.g. X = a run of
  examinations of gems spanning t, with the examinations as occurrences.
  Colour-sameness and grue-sameness are then both equivalences on those
  occurrences, and the witnesses are stated as pairs of occurrences.
- For Locke, e.g. X = a mass gaining and losing atoms over time.
- Add one sentence saying that any sameness relation on occurrences is a
  candidate criterion (D1), which is why a sorting such as colour qualifies.
- Or replace grue with a canonical uncarried case that has a changing whole.

**B1-10** · major · P2 (READING #5; FINDINGS "determination/constitution
slide", "Refinement is by arrangement too") · examples/glider.md, "Gliders
are made of cells." (lines 46–48).
*Problem.* "the same cells otherwise arranged give no glider". Here cells are
sites (lines 9–10, 15) and never move, so "the same cells otherwise arranged"
does not make sense. Read as "same sites, different states", it shows only
that cell states determine whether a glider is present. That is
determination, which nobody disputes. It does not touch the composition claim,
which is that cell-sameness *together with arrangement* fixes glider-sameness.
This is the slide FINDINGS says to check every time.
*Change.* Replace that clause with sameness-level witnesses:
- the same glider has no fixed set of cells (after 16 steps it shares none
  with its start);
- two gliders can share an arrangement and be different gliders.

So neither cell-sameness nor cell-sameness plus arrangement fixes which
glider. Keep "(D7)".

### Minors

**B1-11** · minor · P3 · README.md Hobbes bullet (lines 26–28); ship.md "The
case" (lines 14–15) and "What ICW adds to Hobbes" (lines 38–41).
*Problem.* Hobbes did apply his rule. "Ship" signifies "matter so figured",
so it is the same while the matter is, and partly the same if partly changed.
ship.md's "Hobbes already answered that it depends on the criterion … ICW
names no winner" suggests Hobbes named none. He also lists a third candidate
(aggregate of accidents).
*Change.* Add Hobbes's application to "ship" in ship.md, or at least do not
imply he left it open.

**B1-12** · minor · P3 · examples/limits.md "Coincident" (lines 18–20).
*Problem.* Locke's condition is that the atoms are "joined together into the
same mass" and stay united. Without it, "same atoms" outlasts "same mass"
when the atoms disperse, and coincidence fails.
*Change.* Write "while the same atoms stay united".

**B1-13** · minor · P4 · README.md line 16–17.
*Problem.* "an open problem, stated exactly" overclaims. D8 is *declared* with
"Content. None yet", and O2 is one line.
*Change.* "an open problem (O2), named but not yet solved".

**B1-14** · minor · P6 · README.md "ICW's terms".
*Problem.* "occurrence" is used in the definitions of continuity and
cross-cut but never defined. "O2" is never said to be the kernel's open item
on carrying.
*Change.* Add one clause defining occurrences as what makes up the whole's
changing (P3), and write "open item O2" at first use.

**B1-15** · minor · P1 · README.md line 136–137.
*Problem.* "That *carried* means *real*" is cited to (R2, R3). Neither says
so. The kernel says it in D8's nomenclature row ("Avoid: real").
*Change.* Cite D8 for the first clause, and keep R2 and R3 for the second.

**B1-16** · minor · P5 · examples/ship.md lines 22–23.
*Problem.* "neither has to be imagined" is inaccurate, because Hobbes's
rebuild is his hypothetical ("if some man had kept the old planks").
*Change.* "neither has to be invented: the puzzle states both".

**B1-17** · minor · P6 · README.md "What ICW adds" #1 (line 104).
*Problem.* "A pair that is static". The whole is static, not the pair.
*Change.* "A pair in a whole that does not change, a coincident pair, or a
nested pair is refused …".

**B1-18** · minor · P6 · README.md Reichenbach clause (lines 42–43).
*Problem.* "distinguished material from functional genidentity" carries no
information for a non-specialist.
*Change.* Gloss it in a few words from a verified source, or reduce it to
"also developed genidentity".

**B1-19** · minor · P6 · README.md line 7–8.
*Problem.* "and kept the ship" assumes the sameness that Plutarch reports as
disputed.
*Change.* "…one by one. Was it still the same ship?"

**B1-20** · minor · P6 · examples/*.md.
*Problem.* The examples cite (Gardner 1970), (Davidson 1970), Goodman (1955)
and Dennett (1991) with no pointer to where the full references are.
*Change.* Add a link to `../README.md#references` in each example's header
line.

## On α's protocol gaps

1. **"Cross-cuts" vs §6.** Agreed that P1 is internally inconsistent. I judge
   by the kernel: verdicts must be §6 names, and "cross-cuts" may only name
   the furthest check passed, never a verdict. The matter does this
   consistently (README 89–94, glider 34). No finding. I will judge every
   round the same way.
2. **D9 presupposes carrying.** Agreed as a kernel and READING issue. The
   matter uses "articulated" only conditionally or in negations. No finding.
3. **R4/R5 read as unconditional in READING and FINDINGS.** Agreed. Outside
   the matter. The matter conditionalises correctly.
4. **Gauss's law in P5.** I read it as an example of facts to check if
   present, not a required example. I agree electrostatics fails check 1.
   Removing it is fine.
5. **READING's `colour < cars > shape`.** Agreed it is invented. Outside the
   matter.
6. **FINDINGS names a predecessor project.** Confirmed: "Carrying cannot be
   another relation", Source paragraph. The matter is clean. The README's
   link exposes the name to visitors. That is for the orchestrator, not α.
7. **Reichenbach locator.** Agreed. I could not verify a section or a wave
   example either, and a book-level citation is acceptable. See B1-18 for
   the gloss.

## Counts

Blocker 4 · Major 6 · Minor 10

Verdict: REQUEST CHANGES
