# Cases

The register O2 work runs against. A candidate definition of *carried* is
applied to every case; it becomes a candidate when it matches every expected
verdict. Then the hunter looks for cases it gets wrong.

## Rules

1. **Expected verdicts are the owner's**, set before any candidate is applied.
2. **A candidate and an expected verdict never change in the same round.**
   When they disagree, change one, log the reason in `notes/FINDINGS.md`, and
   rerun everything.
3. **Evaluator by kind of case:**
   - *script*: a Game of Life case; a program applies the candidate.
   - *panel*: a described case; two or three independent models, of
     different families where possible, apply the candidate to the
     description without seeing the expected verdict or each other.
     Disagreement means the candidate cannot be applied; that is a finding.
   - *control*: refused before check 4; any candidate must leave it refused.
4. **Open cases** have no expected verdict. They score nothing; the
   candidate's verdict on them is its prediction.
5. **Iteration 0 is the Game of Life.** A candidate that passes there must
   then pass a case that breaks a Game of Life assumption: elements that
   move, or noise.
6. **Hunter:** knows the candidate; proposes cases it gets wrong. The owner
   labels each new case before seeing the candidate's verdict.
7. **Stop rule:** if three successive revisions each fall to a new
   counterexample, test whether *carried* is graded or prototype-based before
   revising again.

## Register

| Case | Pair | Expected | Evaluator | Breaks GoL | Source |
|---|---|---|---|---|---|
| Glider | squares / glider | carried | script | no | `examples/glider.md` |
| Step-indexed grouping | a grouping that switches at step T / the squares | not carried | script | no | new |
| Trivial groupings | each state alone; all states together | flagged trivial | script | no | new |
| Grue | green / grue | not carried | panel | — | `examples/limits.md` |
| Wave | water parcels / wave | carried | panel | moving elements | `examples/wave.md` |
| Body | matter / living process | carried | panel | moving elements, noise | to write |
| Computer | memory contents / running program, one machine | open | panel | no | to write |
| Ship | planks / repaired ship | open | panel | — | `examples/ship.md` |
| Mind | brain / mind | open | panel | noise | `examples/mind.md` |
| Cone | triangle / circle | refused, untyped | control | — | `examples/limits.md` |
| Locke's mass | mass / matter | refused, coincident | control | — | `examples/limits.md` |
| Temperature | microstate / temperature | refused, nested | control | — | `examples/limits.md` |
| Fission | ship split and completed twice | stress test for D1 (O4) | panel | — | kernel O4 |

Expected verdicts above are proposed from the 14–16 Nov sessions; the owner
confirms each before the first candidate runs.
