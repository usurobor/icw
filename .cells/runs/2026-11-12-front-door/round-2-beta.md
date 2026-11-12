# Round 2 — β

Commit reviewed: `8db7422e1433aab9cfbd2c34923cf3e2b19a9b12`
Base: `216a5d6b3b03a7c44655ad9ac3f3b4f00e95b9a2`

Working tree clean, HEAD = 8db7422 (branch `icw-fresh`).

## Mechanical checks run

- `python3 tools/lint.py`: `0 error(s)`.
- Relative links: 22, all resolve, including the new `../README.md#references`
  anchors.
- `git diff --stat 216a5d6 8db7422`: only README.md and examples/{glider,limits,ship,wave}.md.
- `A < X > B` forms: all spaced and in code. No predecessor project named.

## Properties

| Property | Result | Why |
|---|---|---|
| P1 Kernel fidelity | fail | "Cross-cutting is the common case" is not in the kernel (B2-1). The terms entry blurs continuity with criterion of identity (B2-5). Verdict names, proposed markers and "no pair holds" are correct. |
| P2 Misreadings | pass | Frames hold footprints only. No levels or second-cause reading, no observer or whole as agent, carried ≠ real stated. Determination is kept apart from identity in glider.md. |
| P3 Prior-art accuracy | fail (minor only) | New credits verified (below). The mark criterion is attributed to Reichenbach with no reference to the work that contains it (B2-3). |
| P4 Novelty claims | fail | Addition #2 claims D8's type as new, but Salmon's credited criterion already has that type (B2-2). Additions #1 and #3 are now correctly credited and narrowed. |
| P5 Examples | fail (minor only) | Facts correct, wholes named, both directions witnessed in every cross-cutting case. glider.md's "with arrangement" conclusion lacks its witness (B2-4). |
| P6 Clarity | pass | The first screen states the question and earns the next. Terms are defined before use and IDs explained. B2-5 is counted under P1. |
| P7 Notation and mechanics | pass | Lint shows 0 errors, links resolve, notation is correct. |
| P8 Footprint and scope | pass | Only matter files changed, no predecessor mention, every section has a job. |

## Verification of new or changed prior art (web)

- **Russell 1948.** SEP *Causal Processes* quotes *Human Knowledge* p. 333
  (definition of "causal line") and pp. 475–477 ("A causal line may always be
  regarded as a persistence of something…"; "When 'substance' is abandoned,
  the identity … of a thing"). "Let causal lines replace substance" is
  faithful, and the locators are correct.
- **Salmon 1984.** SEP gives pp. 141–144 for pseudo-processes (spot of light,
  shadows), p. 147 for the mark criterion ("a process is causal if it is
  capable of transmitting a local modification in structure"), and p. 148 for
  marks. pp. 141–148 is correct.
- **Reichenbach and the mark criterion.** The attribution is correct in
  substance: Reichenbach's mark method appears in the *Axiomatik* (1924) and
  *Philosophie der Raum-Zeit-Lehre* (1928, Eng. 1958). SEP cites 1958
  pp. 147–149 for "unreal sequences". It is not in the only Reichenbach work
  in References, 1956 (B2-3).
- **Zimmerman 1997.** "Immanent Causation", *Noûs* 31 Suppl. (=
  *Phil. Perspectives* 11): 433–471 (Rutgers record). "Discussed by" is
  accurate. Zimmerman in fact defends the view, so the wording is
  conservative, not wrong.
- **Davidson 1970.** One event under two descriptions (token identity of the
  mental and physical) is a faithful summary, and the two stated differences
  are fair.
- **Gibbard 1975.** Statue and lump are made and destroyed together, he
  concludes contingent identity, and the squeezing is a counterfactual (SEP
  *Material Constitution*; Oberlin summary). The bullet is now correct.
- **Hobbes II.11.7.** "A ship, which signifies matter so figured, will be the
  same as long as the matter remains the same", and the three candidates. The
  README and ship.md paraphrases are now faithful.
- **Dennett 1991, p. 39.** "The only individuals, cells, are defined by their
  fixed spatial location", "one and the same glider", and Laplacean
  predictability at p. 38. Crediting both criteria and derivability to him is
  correct.

## Findings

### Majors

**B2-1** · major · P1 (AC4) · README.md "The test" (lines 107–108: "and
cross-cutting is the common case"); examples/limits.md opening (lines 3–4: "A
pair that cross-cuts, the common case, …").
*Problem.* No kernel item says cross-cutting is the common case. It rests on
my round-1 arithmetic: share of distinct pairs of partitions of a small
finite set. That is a fact about counting partitions uniformly. It says
nothing about the pairs anyone proposes, or about infinite occurrence sets,
where "common" needs a measure the kernel does not supply. AC4 bars claims
beyond the kernel.
I introduced the phrase in B1-3's suggested wording. I withdraw that part of
B1-3: the kernel-faithful content of B1-3 is only that cross-cutting pairs are
not refused (O2). This finding corrects my own suggestion; α did nothing
wrong in adopting it.
*Change.* Delete the clause in both places.
- README: "Today the test stops at check 4 for every pair that cross-cuts."
- limits.md: "A pair that cross-cuts it cannot yet refuse (O2)."

If α wants a reason the gap matters, use the kernel's own: O2, "cannot be
refused for arbitrariness", with green/grue as the case.

**B2-2** · major · P4 · README.md "What ICW adds" #2 (lines 131–135).
*Problem.* The addition claims that "the kernel also fixes its type: carrying
is a property of a criterion, not a further relation among occurrences (D8)".
It contrasts this with causal lines and immanent causation as "relations
between earlier and later states". Salmon's mark criterion, credited two
sentences earlier, already has that type. "A process is causal if it is
*capable of transmitting* a mark" is a predicate on a process, and a process
is "anything that displays consistency of structure over time", i.e. a
candidate persistence. It is not a further relation among events. The
contrast is also doubtful for Russell: a causal line is a *series* of events
picked out by a property (inferability), not a relation added to the series.
So the type is not something the credited prior art lacks.
*Change.* Either:
(a) Move the type statement out of the additions and credit it, e.g. "As with
Salmon's criterion, carrying is a property of a criterion, not a further
relation among occurrences (D8)."
or
(b) Narrow the addition to something α can show is absent from Salmon,
Russell and Zimmerman, and name it precisely. A candidate is that carrying is
relative to a named whole's one changing and must hold for *both* members of
a cross-cutting pair. Verify before claiming.

Either way, drop the sentence contrasting D8 with causal lines and immanent
causation, or limit it to immanent causation, which does make persistence
consist partly in a causal relation among stages.

### Minors

**B2-3** · minor · P3 · README.md "Causal persistence" bullet (line 55) and
References.
*Problem.* "Reichenbach's mark criterion" has no reference to the work that
contains it. The only Reichenbach entry is *The Direction of Time* (1956),
cited for genidentity, so a reader will take it as the source.
*Change.* Add Reichenbach, *The Philosophy of Space and Time* (1928; Eng.
1958), pp. 147–149 for the "unreal sequences" passage (as cited in SEP
*Causal Processes*), and cite it at the mark-criterion clause. Alternatively
reword to "a mark criterion Salmon (1984) takes from Reichenbach", with no
separate Reichenbach claim.

**B2-4** · minor · P5 · examples/glider.md "Gliders are made of cells."
(lines 53–56).
*Problem.* The conclusion "neither cell-sameness nor cell-sameness with
arrangement fixes which glider" needs a witness with the same cells *and* the
same arrangement but different gliders. The two given do not supply it:
- "no fixed set of cells" shows cell-sameness is not necessary;
- "two gliders share an arrangement" involves different sites, so different
  cells.

*Change.* Add the missing witness, e.g. "and a second glider that later
crosses the same sites in the same phase has the same cells in the same
arrangement, yet is a different glider."

**B2-5** · minor · P1 (D1, D9) · README.md "ICW's terms", second bullet
(lines 72–77).
*Problem.* The bullet first says a criterion of identity "ICW calls … a
*continuity*", then that any sameness relation is a continuity and only "a
candidate". The kernel separates the two. A continuity is any equivalence on
occurrences (D1). A criterion of identity that the whole bears is a *carried*
continuity, an articulation (D9, *Why the word*). As written, a reader can
conclude that colour is a criterion of identity.
*Change.* Reorder, e.g.:
"ICW calls any sameness relation on a whole's occurrences a *continuity*
(D1). Any continuity is a candidate criterion of identity, a mere sorting
such as by colour included. Whether the whole bears it as one is the
carrying question below (D9)."

## Round-1 findings: status in the matter at 8db7422

| ID | Status | Evidence |
|---|---|---|
| B1-1 | resolved | README 49–53: Gibbard's case, contingent identity, squeeze as counterfactual. |
| B1-2 | resolved | glider.md 10–13: B3/S23 in words. |
| B1-3 | resolved | limits.md retitled "Where the test stops"; grue under "Not refused, uncarried"; README 157–158 updated. The "common case" phrase I suggested is withdrawn (B2-1). |
| B1-4 | resolved | ship.md 52, wave.md 38: "footprint is some …"; README 79–80 adds the frame rule. |
| B1-5 | partly resolved | Omitted prior art now credited and locators verified, and the hook no longer says "the next question". The residual type-novelty claim is carried as B2-2. |
| B1-6 | resolved | glider.md 18–19, 71, 76–78; README 116–120; the "Separations" addition is removed. |
| B1-7 | resolved | README 137–148: Locke's oak, statue/clay, Davidson credited, differences named; opaque sentence removed. glider.md 65–67 has the same caution. |
| B1-8 | resolved | ship.md 25–31, 36–49: directions credited; addition limited to running the test and naming O2. |
| B1-9 | resolved | Wholes named for Locke (limits 19), gas (27), grue (43–48), with witnesses as pairs of examinations; README table names each whole; README 75–77 says sortings qualify. |
| B1-10 | resolved | "Otherwise arranged" removed; sameness-level witnesses given. A remaining witness gap is minor (B2-4). |
| B1-11 | resolved | README 31–33, ship.md 15–18, 44–45. |
| B1-12 | resolved | README 34–35, limits.md 20–22, table row 2. |
| B1-13 | resolved | README 19. |
| B1-14 | resolved | README 68, 70–71, 88. |
| B1-15 | resolved | README 163: (D8). |
| B1-16 | resolved | ship.md 25–26. |
| B1-17 | resolved | README 124–125. |
| B1-18 | resolved | README 47–48. |
| B1-19 | resolved | README 7–8. |
| B1-20 | resolved | Each example header links `../README.md#references`. |

## On α's new protocol gaps

1. **"Refused" for untyped.** I agree the kernel is not quite consistent
   with itself: §6 says untyped is "not false, not a claim", while O2 counts
   type among the grounds of refusal. The matter follows O2 and keeps §6's
   gloss beside it (limits.md 10–15, README table). I accept this and will
   judge the same way in later rounds. A kernel wording fix is for the owner.
2. **Cross-cutting share.** I agree it is arithmetic, not theory, and that is
   why it should go from the matter (B2-1). The fault was in my round-1
   wording, not in α's disposition.

## Counts

Blocker 0 · Major 2 · Minor 3

Verdict: REQUEST CHANGES
