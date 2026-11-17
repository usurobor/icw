# Cases

The register O2 work runs against. A candidate definition of *carried* is
applied to every case; it becomes a candidate when it matches every expected
verdict. Then the hunter looks for cases it gets wrong.

The hypotheses these cases serve are in [HYPOTHESES.md](HYPOTHESES.md).

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
9. **Shift check.** Every candidate gives the same verdict on a board shifted
   in space or time. The rule is the same everywhere and always, so a grouping
   that needs an outside clock (step-indexed, splice) fails.
10. **Stop rule.** If three successive revisions each fall to a new
   counterexample, test whether *carried* is graded or prototype-based before
   revising again.

11. **Labels are cheap to check.** Each target records who set it.
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
12. **Carrying is read off the rule** (R1, owner, 16 Nov). Reach is necessary;
    closure is the proposed addition.
13. **Representation-invariance.** Equivalent expressions of the same
    transition function give the same verdicts (owner, 16 Nov). Present scope:
    candidates that only call the transition function (C9, C10) pass by
    construction. Rule 184's flow fixes each car's move (audited 16 Nov);
    identity adds an order-preserving convention, and holds for flows in
    {0, 1} only.
14. **Closeness in context** (owner, 16 Nov). The car in the jam and the
    eater's persistence stay open under this heading; C10 unchanged, its misses
    kept. A context-aware closeness must separate F's contribution from what
    its surroundings supply: running the whole board only reproduces the next
    frame and would pass any tracing. It need not give every later occurrence
    one source: conservation may give a strong flow-based witness as a special
    case, while the Game of Life needs joint, many-to-many dependence. A
    by-product rule is judged only on boards it has not seen.

## Seed list

Pairs use the kernel's notation where the repo has one. Targets are proposed
from the 14–16 Nov sessions and the literature; the owner confirms each,
probes first.

| Case | Pair | Kernel status | Target | Role | Evaluator | Breaks GoL | Source |
|---|---|---|---|---|---|---|---|
| Glider | `cell < grid > glider` | uncarried, pending; passes check 3 | holds | anchor+ | script | no | `examples/glider.md` |
| Two gliders, one arrangement | same sites and phase, different glider | — | holds | anchor+ | script | no | `examples/glider.md` |
| Two identical gliders at once | two classes of `same glider` | — | holds, owner: two classes of one continuity, told apart by separate reach | anchor+ | script | no | 16 Nov |
| Splice | glider A to step 100, then identical distant glider B | — | uncarried, owner | anchor− | script | no | 16 Nov |
| Indirect splice | as splice, A fires a signal that triggers B | — | uncarried, owner; tests closure | anchor− | script | no | 16 Nov |
| Alternating splice | A, B, A, B, one glider per step | — | uncarried, owner 16 Nov: derived from Splice and R1; a history that looks like a glider does not make the trace carried | anchor− | script | no | iteration 0 |
| Union of two distant gliders | two gliders traced as one persistence | — | uncarried, a bundle (owner, 16 Nov, before the integration run). Not a ruling on Lewis's trout-turkey, which stays no clean translation | anchor− | script | no | review of iteration 0 |
| Two gliders that interact | glider A, glider B, their interaction | — | owner, 16 Nov: two glider continuities before contact; one integrated interaction continuity while they affect each other; then classify what persists from the actual output. Not a claim that they fuse into one enduring glider. Interval fixed from trajectories before the run | probe | script | no | 16 Nov |
| Glider meets an eater | glider, eater, their interaction | — | owner, 16 Nov: the glider continuity ends at contact; the eater persists; eater plus glider is integrated for the interval; afterwards only the eater remains. Interval fixed from trajectories before the run | probe | script | no | 16 Nov |
| Rule-184 jam, integration | same car / same jam | — | holds and integrated (owner, 16 Nov): the update couples a car's motion to occupancy ahead, and the jam persists as cars pass through it | probe | script: rule 184 | moving elements | 16 Nov |
| Collision | glider until it hits a block | — | holds up to the collision, ends there, owner | anchor+ | script | no | 16 Nov |
| Step-indexed grouping | glider / "glider before t₀, block after" | — | uncarried | anchor− | script | no | new |
| Trivial groupings | same trajectory; whole board | — | nested (proposed) | regression | script | no | new |
| Incars (Hirsch) | same car / same incar (one garage-bound episode) | — | nested, labeler: "same incar implies same car; the car continues outside" (Hirsch 1982, pp. 32–33; Korman 2015) | regression | script: glider / glider inside a region | no | literature, audited 16 Nov |
| Trout-turkey (Lewis) | same animal / same fusion | — | no clean translation, labeler: Lewis (1991, §3.5) and Korman dispute existence, not persistence. closure was predicted to refuse it and does not: the Game of Life union of two distant gliders holds under every candidate (iteration 0); owner to set | probe | script: two non-interacting gliders | no | literature, audited 16 Nov |
| Wave | `parcel < sea > wave` | uncarried, pending | holds | anchor+ | panel | moving elements | `examples/wave.md` |
| Traffic jam | same car / same jam | — | holds, labeler: "one jam persists through different cars; one car passes through different jams" (Resnick 1994; Nagel and Schreckenberg 1992, §3; rule 184 in Israeli and Goldenfeld 2006, §IV.B.3) | anchor+ | script: rule 184 | moving elements | literature, audited 16 Nov |
| Grue, bleen | colour / grue-class over examinations | uncarried: undecided, not refused | uncarried (medium), labeler: Goodman (1955) concerns projection, not persistence; Lewis (1983) denies grue naturalness. Covered in the Game of Life by the step-indexed grouping | source | panel | — | `examples/limits.md`, audited 16 Nov |
| Reichenbach's spot | same wall patch / same sweeping spot | — | no clean translation in plain sense, labeler: Salmon (1984, pp. 141–147) shows the spot transmits no mark; that yields uncarried only once carrying is causal (R1, 16 Nov). Under closure: the spot's next stage depends on the lamp, not on the spot | anchor− (given R1) | panel | no | `PRIOR-ART.md`, audited 16 Nov |
| Ship | `plank < dockyard > ship` | stops at check 4 | ? | probe | panel | moving elements | `examples/ship.md` |
| Hobbes's ship | matter so shaped / ship through repair | — | ? | probe | panel | moving elements | `examples/ship.md` |
| Body | matter / living process | — | holds? | probe | panel | moving elements, noise | to write |
| River (Heraclitus, Quine) | water / river | — | holds? ([IEP](https://iep.utm.edu/page/heraclit)) | probe | panel | moving elements | `examples/wave.md` |
| Locke's oak | matter / one life | — | holds? (Locke) | probe | panel | moving elements | `PRIOR-ART.md` |
| Species (Boyd) | organisms / species | — | holds? ([Brigandt](https://sites.ualberta.ca/%7Ebrigandt/Natural_kinds_in_evolution_and_systematics.pdf)) | probe | panel | moving elements, noise | literature |
| Money | `note < economy > currency` | uncarried, pending; passes check 3 | holds? (owner, 17 Nov: carried by the observable practice of settlement) | probe | panel | moving elements; reflexive elements (holders' expectations track the pattern) | `examples/money.md` |
| Flame, whirlpool, Bénard cell | passing fluid / the structure | — | ? ([García-Valdecasas](https://philarchive.org/archive/GAROTN-4)) | probe | panel; script: structure fed by a glider stream | moving elements | literature |
| Neural attractor | `neuron < the brain's activity > attractor` | reaches check 3 | ? | probe | panel | noise | `examples/mind.md` |
| Running computer | `circuit < the running computer > variable` | uncarried, pending; nested if Chalmers and Piccinini are right | ? | probe | panel | moving elements | `examples/mind.md` |
| Statue and clay (Gibbard) | lump / statue | — | ? ([SEP](https://plato.stanford.edu/archives/win2018/entries/material-constitution/)) | probe (hard) | panel | — | `PRIOR-ART.md` |
| Tibbles and Tib | cat / cat minus tail | — | ? ([SEP](https://plato.stanford.edu/archives/win2018/entries/material-constitution/)) | probe | script: cut cells from a stable object | no | literature |
| Problem of the many | one cat / 1001 hair-sets | — | ? ([Lewis 1993](https://andrewmbailey.com/dkl/Many_Almost_One.pdf)) | probe | script: boundary cells | no | literature |
| Cone | `triangle < cone > circle` | refused, untyped | untyped | regression | control | — | `examples/limits.md` |
| Locke's mass | same mass / same united atoms | refused, coincident | coincident | regression | control | — | `examples/limits.md` |
| Temperature | microstate / temperature | refused, nested | nested | regression | control | — | `examples/limits.md` |
| Fission | "same ship" across a split | fails D1 | — | probe (O4) | panel; script: a collision that yields two gliders | — | kernel O4 |
| Bell pair under local evolution | each qubit / the pair's correlation | — | — | parked | panel; quantum CA later | non-separable state | `notes/ENTANGLEMENT.md` |
| Teleportation | particle / quantum state | — | — | parked | panel | non-separable state | `notes/ENTANGLEMENT.md` |
| Teletransporter (Parfit) | physical / psychological continuity | — | — | parked (with fission) | script: delete a glider, copy it | no | [LSE notes](https://personal.lse.ac.uk/robert49/teaching/ph103/lecture5.html) |
| Head-direction rings | ring attractors in different animals | — | — | parked (O5) | panel | noise | `examples/mind.md` |

## Candidates for carried

Tested before any new definition is invented. Iteration 0: C1, C2 and C7
against each other on the Game of Life rows; where they disagree is the
first finding. Every candidate, from the literature or invented here, is
listed in this table with its status and run.

| ID | Candidate | Source | Status |
|---|---|---|---|
| C1 | The rule maps the grouping's classes onto classes: coarse-graining and running commute. Their blocks are fixed; a version that follows a moving pattern is C2's territory. | Israeli and Goldenfeld, PRL 92 (2004) | Run, iteration 0 (as a film map). Accepts the alternating splice: judged on history only. Out. |
| C2 | The grouping is the minimal one that predicts as well as the full state (causal states); applied locally, it picks out moving particles against filtered domains. Relative to a chosen measure of prediction. | Shalizi and Crutchfield (2001); Hanson and Crutchfield (1997); Shalizi et al., PRE 73 (2006) | Run, iteration 0 (activity filter, a stand-in for causal states). Accepts the indirect splice. The full causal-state version is unrun. |
| C3 | The grouping compresses: some description using it is more efficient than the bit map. Compression is relative to a describer, which D9 excludes; may mark the laid-across side. | Dennett, "Real Patterns", J. Phil. 88 (1991) | Not run. |
| C4 | The grouping is sustained by mechanisms that maintain its clustering (homeostatic property clusters). | Boyd (1991, 1999) | Not run; panel only. |
| C5 | The grouping carves at the joints. Not operational; panel only. | Lewis (1983); Sider (2011) | Not run; panel only. |
| C6 | Independent wholes converge on the grouping. | ICW, conjecture in O5 | Not run; needs a relation across wholes (O5). |
| C7 | The pattern maintains its own integrity: it has an intrinsic viability constraint. Reported to count still lifes too; ICW refuses those before check 4 (a block's pattern and cell criteria coincide). | Beer, McShaffrey and Gaul (2024) | Run, iteration 0 (stand-in: closure plus the actual surroundings). Matches every iteration-0 target; holds the union of two distant gliders like every candidate before C9. |
| C8 | The grouping makes the dynamics shortcuttable: its coarse rule predicts with less computation than running the cells. Expected to fail the splice, which is as predictable as the true trace. | Israeli and Goldenfeld (2004), as a hypothesis | Run, iteration 0. The verdict turns on a free bound K (K = 2 accepts the splice). Out until K is fixed in advance. |
| C9 | Closure plus integration: each stage depends on the previous stage of the same continuity, and does not split into parts that each evolve as they would apart. | ICW, owner candidate (D8), 16 Nov | Run, 16 Nov (`notes/runs/2026-11-16-probes.md`). Refuses the union; fails both interaction probes (integration judged per step flickers), breaks the eater, refuses the jam and the car. Not O2; integration as computed is a patch. |
| C10 | Closest continuer with integration over the interaction's interval; C10s, its share variant (closeness above 0.5 both ways). | ICW, after C9 (Nozick's closest continuer as a parallel), 16 Nov | Run, 16 Nov (`notes/runs/2026-11-16-c10.md`). Passes everything frozen except the interaction probes, the eater's persistence and the car. Not O2; two owner questions open (by-products; the rule's presentation). |
| C11 | A stage gets more of its information from the persistence's own past than from its surroundings (temporal integrity, by information decomposition). Graded: separates driven forms (whirlpool, flame) from organismal ones. A measure for the *mainly* in closure and for rule 14's closeness in context. The source makes individuality relative to an observer's lens; D9 needs it read off the rule. Run: `notes/runs/2026-11-17-c11.md`. | Krakauer, Bertschinger, Olbrich, Flack and Ay, *Theory in Biosciences* 139 (2020) | Run, 17 Nov. Gets the eater's two sides right; holds the union, the collisions and the indirect splice; refuses the car; sorts elements (fed by surroundings) from patterns (fed by their own past). Not O2. |

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

## Queued (17 Nov)

- **Self-maintenance as a further distinction.** Montévil and Mossio (2015):
  living organisation is a closure of constraints, constraints that depend on
  and maintain one another. A flame may be carried (C11's driven form) without
  closure of constraints; a body has both. Proposed: self-maintenance sits on
  top of carrying, and the flame and body rows test it. Owner to rule.
- **Name clash.** Their *closure* is mutual dependence among constraints; this
  register's *closure* is a stage depending on its own previous stage. Rename
  ours or define the difference where the term first appears.
