# Cases

The register O2 work runs against. A candidate definition of *carried* is
applied to every case; it becomes a candidate when it matches every expected
verdict. Then the hunter looks for cases it gets wrong.

## Rules

1. **Target labels are the owner's**, set before any candidate is applied, and
   may cite the literature. A target label says what a correct definition of
   *carried* should return. The kernel status column says what the test
   returns today; O2 is scored on the target, progress on the status.
2. **A candidate and an target label never change in the same round.**
   When they disagree, change one, log the reason in `notes/FINDINGS.md`, and
   rerun everything.
3. **Evaluator by kind of case:**
   - *script*: a Game of Life case; a program applies the candidate.
   - *panel*: a described case; two or three independent models, of
     different families where possible, apply the candidate to the
     description without seeing the target label or each other.
     Disagreement means the candidate cannot be applied; that is a finding.
   - *control*: refused before check 4; any candidate must leave it refused.
4. **Open cases** have no target label. They score nothing; the
   candidate's verdict on them is its prediction.
5. **Iteration 0 is the Game of Life.** A candidate that passes there must
   then pass a case that breaks a Game of Life assumption: elements that
   move, or noise.
6. **Hunter:** knows the candidate; proposes cases it gets wrong. The owner
   labels each new case before seeing the candidate's verdict.
7. **Stop rule:** if three successive revisions each fall to a new
   counterexample, test whether *carried* is graded or prototype-based before
   revising again.

## Seed list

Pairs use the kernel's notation `A < X > B`. Kernel status is quoted from the
source. Target labels are proposed; the owner confirms each before the first
candidate runs.

| Case | Pair | Kernel status | Target | Evaluator | Breaks GoL | Source |
|---|---|---|---|---|---|---|
| Glider | `cell < grid > glider` | uncarried, pending; passes check 3 | carried | script | no | `examples/glider.md` |
| Two gliders, one arrangement | same sites and phase, different glider | — | carried (the glider criterion separates them) | script | no | `examples/glider.md` |
| Step-indexed grouping | a GoL grouping that switches at step T | — | uncarried | script | no | new |
| Trivial groupings | each state alone; all states together | — | uncarried | script | no | new |
| Wave | `parcel < sea > wave` | uncarried, pending | carried | panel | moving elements | `examples/wave.md` |
| Quine's river | water stages / river stages | — | carried | panel | moving elements | `examples/wave.md` |
| Grue, bleen | colour / grue-class over examinations | uncarried: undecided, not refused | uncarried (Goodman) | panel | — | `examples/limits.md` |
| Reichenbach's spot | a moving spot of light / the light's process | — | uncarried (a pseudo-process) | panel | no | `PRIOR-ART.md` |
| Ship | `plank < dockyard > ship` | stops at check 4 | open | panel | moving elements | `examples/ship.md` |
| Hobbes's ship | ship as matter so shaped / ship through repair | — | open | panel | moving elements | `examples/ship.md` |
| Locke's oak | matter / organization of one life | — | carried (Locke) | panel | moving elements | `PRIOR-ART.md` |
| Neural attractor | `neuron < the brain's activity > attractor` | reaches check 3 | open | panel | noise | `examples/mind.md` |
| Running computer | `circuit < the running computer > variable` | uncarried, pending; nested if Chalmers and Piccinini are right | open | panel | moving elements | `examples/mind.md` |
| Body | matter / living process | — | carried | panel | moving elements, noise | to write |
| Statue and clay | lump / statue | — | open: coincident or nested, unverified | panel | — | `PRIOR-ART.md` |
| Cone | `triangle < cone > circle` | refused, untyped | refused, untyped | control | — | `examples/limits.md` |
| Locke's mass | same mass / same united atoms | refused, coincident | refused, coincident | control | — | `examples/limits.md` |
| Temperature | microstate / temperature | refused, nested | refused, nested | control | — | `examples/limits.md` |
| Fission | "same ship" across a split | fails D1; never reaches checks 2–4 | stress test (O4) | panel | — | kernel O4 |
| Head-direction rings | ring attractors in different animals | — | stress test (O5, across wholes) | panel | noise | `examples/mind.md` |
