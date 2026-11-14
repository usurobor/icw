# Identity in Changing Wholes

**When everything in a whole is changing, what counts as one thing?**

A wave runs across deep water while the water it passes through mostly circles
in place. A glider crawls across Conway's Game of Life while no cell ever
moves. The Athenians replaced the planks of Theseus's ship one by one. Was it
still the same ship?

Each time there are two ways of counting, and they come apart in both
directions: same wave, different water; same water, a different wave. Are
both sustained by the whole's own changing, or is one of them a sorting laid
across it? ICW (Identity in Changing Wholes) states a test. It refuses pairs
for three stated reasons. Its last check is an open problem, named but not
yet solved, and no pair has passed it.

## Two ways of counting

Parenthesised IDs point to the kernel,
[`specs/ARTICULATION.md`](specs/ARTICULATION.md), which governs.

- A whole's **occurrences** are what happens in its changing, ordered in
  time (P3, P4).
- A **continuity** is any sameness relation on those occurrences (D1): same
  cell, same glider, same colour. Each is a candidate *criterion of
  identity*, fixing what counts as one thing and what keeps it the same one.
  Whether the whole bears it is the carrying question below (D9).
- A **footprint** is a persisting thing at one instant. A frozen frame holds
  footprints, never the persisting thing (D3).
- A **refines** B when sameness by A guarantees sameness by B (D4). A and B
  **cross-cut** when neither refines the other, with witnesses in both
  directions (D7).
- A criterion is **carried** when the whole's changing sustains it, rather
  than having it laid across it. ICW names this and has not defined it: open
  item O2 (D8).
- If A and B cross-cut and both are carried, the whole X **is articulated as
  A and B**, written `A < X > B` (D9, D11). The brackets are a mnemonic,
  not arrows of cause, composition or order.

## The test

Two criteria in a named whole go through the checks in order; the first to
fail gives the verdict (§6).

| Check | Verdict if it fails | Case |
|---|---|---|
| 1. The whole changes | **untyped**: not false, not a claim | a cone's triangle and circle |
| 2. The criteria differ | **coincident** | Locke's same mass and same united atoms |
| 3. Neither refines the other | **nested** | a gas's temperature and microstate |
| 4. Both are carried | **uncarried**: undecided while O2 is open | Goodman's green and grue |
| All pass | **holds**: `A < X > B` | none yet |

Today every pair that cross-cuts stops at check 4, cell and glider as much
as green and grue. Intuition tells them apart; no definition does yet. That
gap is the place to push.

## Where this sits

The question is old: Heraclitus's river, the ship of Theseus, Locke's oak,
*the same what?*, Quine's river and its water, the statue and its clay,
causal theories of persistence, Dennett's real patterns, Craver and Bechtel's
levels without interlevel causes. ICW inherits most of its structure. What it
offers is narrow: an ordered test, run in a named
changing whole, that refuses pairs on stated grounds and ends in the carrying
question. Credits and comparisons are in [PRIOR-ART.md](PRIOR-ART.md).

## Examples

- [The glider](examples/glider.md): "gliders emerge from cells", examined.
- [The wave](examples/wave.md): the same structure in water.
- [The ship of Theseus](examples/ship.md): the test run on the oldest case.
- [Where the test stops](examples/limits.md): three refusals, and one pair it
  cannot refuse.

## What ICW does not claim

- That any pair is articulated.
- That *carried* means *real* (D8), or that a coarser or derivable criterion
  is less genuine (R2, R3).
- That identity depends on how the history is generated (R1).
- That anything performs an articulation, an observer or the whole itself
  (D9).
- That anything acts between articulations as a second cause (R5,
  proposed).

## Repository

[`specs/ARTICULATION.md`](specs/ARTICULATION.md) is the kernel and the only
authoritative file. [`specs/READING.md`](specs/READING.md) lists misreadings
it excludes, [`notes/FINDINGS.md`](notes/FINDINGS.md) holds working notes, and
[`tools/`](tools/) checks the kernel.
