# Cases

The register O2 work runs against. A candidate definition of *carried* is
applied to every case; it becomes a candidate when it matches every expected
verdict. Then the hunter looks for cases it gets wrong.

## Rules

1. **Every case has a target verdict**, in the kernel's vocabulary (§6:
   holds, untyped, coincident, nested, uncarried), set by the owner before any
   candidate runs. A candidate succeeds when every verdict matches its target,
   never when every case reaches *holds*: a definition that refuses nothing
   is the emptiness O2 exists to remove.
2. **Roles.**
   - *anchor+* and *anchor−*: the owner's intuition is firm; candidates are
     fitted to these.
   - *probe*: contested. The candidate's verdict is recorded in the run before
     the owner rules. A revision that fixes a probe with a clause aimed at that
     case is flagged as a *patch*.
   - *regression*: refused before check 4, or a past error; every candidate
     must keep it.
   - *parked*: out of scope for now.
3. **A candidate and a target never change in the same round.** When they
   disagree, change one, log the reason in `notes/FINDINGS.md`, rerun all.
4. **Evaluator by kind of case.** *script*: a Game of Life (or other
   automaton) case; a program applies the candidate. *panel*: two or three
   independent models, of different families where possible, apply the
   candidate to the description without seeing the target or each other;
   disagreement means the candidate cannot be applied, which is a finding.
5. **Iteration 0 is the Game of Life.** A candidate that passes there must then
   pass a case that breaks a Game of Life assumption: elements that move, or
   noise.
6. **Hunter.** Knows the candidate; proposes cases it gets wrong. The owner
   sets each new target before seeing the candidate's verdict.
7. **Regression from history.** The determination/constitution slide
   (`notes/FINDINGS.md`): a candidate that makes *carried* imply that B cannot
   be calculated from A's rule fails, because R2 says the glider can be.
8. **Guards, reported every run:** the share of cases the test refuses (holds
   steady or rises); the candidate's length in words; the record of probe
   predictions, right and wrong.
9. **Stop rule.** If three successive revisions each fall to a new
   counterexample, test whether *carried* is graded or prototype-based before
   revising again.

10. **Labels are cheap to check.** Each target records who set it.
    - *owner*: a case that states ICW's own thesis (glider, two gliders in one
      arrangement, step-indexed grouping, wave, trivial groupings). Only the
      owner sets these; a model setting them would let the loop fit a
      definition to its own choice.
    - *literature*: a labeler model reports what the source concluded, with a
      citation and a one-line translation into §6 terms, e.g. "Korman: incars
      are not objects → no continuity the changing sustains → uncarried". The
      labeler is of a different family from the model proposing candidates. A
      second model audits the translations; the owner reads them once.
    Labels are frozen before a run and change only under rule 3.

## Seed list

Pairs use the kernel's notation where the repo has one. Targets are proposed
from the 14–16 Nov sessions and the literature; the owner confirms each,
probes first.

| Case | Pair | Kernel status | Target | Role | Evaluator | Breaks GoL | Source |
|---|---|---|---|---|---|---|---|
| Glider | `cell < grid > glider` | uncarried, pending; passes check 3 | holds | anchor+ | script | no | `examples/glider.md` |
| Two gliders, one arrangement | same sites and phase, different glider | — | holds | anchor+ | script | no | `examples/glider.md` |
| Step-indexed grouping | glider / "glider before t₀, block after" | — | uncarried | anchor− | script | no | new |
| Trivial groupings | same trajectory; whole board | — | nested (proposed) | regression | script | no | new |
| Incars (Hirsch) | car / car-matter inside a garage | — | uncarried ([Korman](https://philarchive.org/archive/KORSKF)) | anchor− | script: glider / its cells inside a region | no | literature |
| Trout-turkey (Lewis) | trout and turkey / front-and-rear fusion | — | uncarried ([Sanson](https://www.davidsanson.com/files/composition.pdf)) | anchor− | script: two non-interacting gliders | no | literature |
| Wave | `parcel < sea > wave` | uncarried, pending | holds | anchor+ | panel | moving elements | `examples/wave.md` |
| Traffic jam | cars / jam moving backward | — | holds ([Resnick](https://ccl.northwestern.edu/cm/models/traffic-basic/info.html)) | anchor+ | script: rule 184 | moving elements | literature |
| Grue, bleen | colour / grue-class over examinations | uncarried: undecided, not refused | uncarried (Goodman) | anchor− | panel | — | `examples/limits.md` |
| Reichenbach's spot | moving spot of light / the light's process | — | uncarried (pseudo-process) | anchor− | panel | no | `PRIOR-ART.md` |
| Ship | `plank < dockyard > ship` | stops at check 4 | ? | probe | panel | moving elements | `examples/ship.md` |
| Hobbes's ship | matter so shaped / ship through repair | — | ? | probe | panel | moving elements | `examples/ship.md` |
| Body | matter / living process | — | holds? | probe | panel | moving elements, noise | to write |
| River (Heraclitus, Quine) | water / river | — | holds? ([IEP](https://iep.utm.edu/page/heraclit)) | probe | panel | moving elements | `examples/wave.md` |
| Locke's oak | matter / one life | — | holds? (Locke) | probe | panel | moving elements | `PRIOR-ART.md` |
| Species (Boyd) | organisms / species | — | holds? ([Brigandt](https://sites.ualberta.ca/%7Ebrigandt/Natural_kinds_in_evolution_and_systematics.pdf)) | probe | panel | moving elements, noise | literature |
| Flame, whirlpool, Bénard cell | passing fluid / the structure | — | ? ([García-Valdecasas](https://philarchive.org/archive/GAROTN-4)) | probe | panel; script: structure fed by a glider stream | moving elements | literature |
| Neural attractor | `neuron < the brain's activity > attractor` | reaches check 3 | ? | probe | panel | noise | `examples/mind.md` |
| Running computer | `circuit < the running computer > variable` | uncarried, pending; nested if Chalmers and Piccinini are right | ? | probe | panel | moving elements | `examples/mind.md` |
| Statue and clay (Gibbard) | lump / statue | — | ? ([SEP](https://plato.stanford.edu/archives/win2018/entries/material-constitution/)) | probe (hard) | panel | — | `PRIOR-ART.md` |
| Tibbles and Tib | cat / cat minus tail | — | ? ([SEP](https://plato.stanford.edu/archives/win2018/entries/material-constitution/)) | probe | script: cut cells from a stable object | no | literature |
| Problem of the many | one cat / 1001 hair-sets | — | ? ([Lewis 1993](https://andrewmbailey.com/dkl/Many_Almost_One.pdf)) | probe | script: boundary cells | no | literature |
| Cone | `triangle < cone > circle` | refused, untyped | untyped | regression | control | — | `examples/limits.md` |
| Locke's mass | same mass / same united atoms | refused, coincident | coincident | regression | control | — | `examples/limits.md` |
| Temperature | microstate / temperature | refused, nested | nested | regression | control | — | `examples/limits.md` |
| Fission | "same ship" across a split | fails D1 | — | parked (O4) | panel | — | kernel O4 |
| Teletransporter (Parfit) | physical / psychological continuity | — | — | parked (with fission) | script: delete a glider, copy it | no | [LSE notes](https://personal.lse.ac.uk/robert49/teaching/ph103/lecture5.html) |
| Head-direction rings | ring attractors in different animals | — | — | parked (O5) | panel | noise | `examples/mind.md` |

## Candidates for carried

Tested before any new definition is invented. Iteration 0: C1, C2 and C7
against each other on the Game of Life rows; where they disagree is the
first finding.

| ID | Candidate | Source |
|---|---|---|
| C1 | The rule maps the grouping's classes onto classes: coarse-graining and running commute. Their blocks are fixed; a version that follows a moving pattern is C2's territory. | Israeli and Goldenfeld, PRL 92 (2004) |
| C2 | The grouping is the minimal one that predicts as well as the full state (causal states); applied locally, it picks out moving particles against filtered domains. Relative to a chosen measure of prediction. | Shalizi and Crutchfield (2001); Hanson and Crutchfield (1997); Shalizi et al., PRE 73 (2006) |
| C3 | The grouping compresses: some description using it is more efficient than the bit map. Compression is relative to a describer, which D9 excludes; may mark the laid-across side. | Dennett, "Real Patterns", J. Phil. 88 (1991) |
| C4 | The grouping is sustained by mechanisms that maintain its clustering (homeostatic property clusters). | Boyd (1991, 1999) |
| C5 | The grouping carves at the joints. Not operational; panel only. | Lewis (1983); Sider (2011) |
| C6 | Independent wholes converge on the grouping. | ICW, conjecture in O5 |
| C7 | The pattern maintains its own integrity: it has an intrinsic viability constraint. Reported to count still lifes too; ICW refuses those before check 4 (a block's pattern and cell criteria coincide). | Beer, McShaffrey and Gaul (2024) |
| C8 | The grouping makes the dynamics shortcuttable: its coarse rule predicts with less computation than running the cells. Expected to fail the splice, which is as predictable as the true trace. | Israeli and Goldenfeld (2004), as a hypothesis |

## Queued (16 Nov)

- **Splice and reach.** Splice (follow glider A, then an identical distant
  glider B), two simultaneous identical gliders, collision, shifted board or
  clock. Targets: owner. Decision pending on R1: carried read off the actual
  history (needs "next to") or off the rule's reach (qualifies R1).
- **Universality.** The Game of Life emulates any computable whole, so the
  running-computer probe can be built literally (Rendell's Turing machine), and
  the OTCA metapixel gives a stack (cells, metacells, meta-gliders) that tests
  R6 directly. Iteration 2: costly to run.
- **Undecidability.** Whether a pattern ever dies is undecidable in general.
  A candidate that quantifies over all future time makes check 4 undecidable
  for some patterns. Prefer candidates checked over a finite stretch; a
  continuity's verdict is then per stretch, which also fits the collision case.
  The verdicts may need *undecidable* as distinct from *undecided while O2 is
  open*.
- **Emulation.** A carried criterion should stay carried when its whole is
  emulated in the Game of Life (rule 184 traffic inside Life: the jam holds).
  A check on every candidate, and a candidate relation for O5. The emulation
  map is itself a commuting coarse-graining; check the cellular-automata
  "bulking" literature (Delorme, Mazoyer, Ollinger, Theyssier) before claiming
  anything.
- **Scope.** Computable wholes only. Bodies and seas stay with the panel.
