# Identity in Changing Wholes

**What counts as one thing, when everything is changing?**

## An old question

Heraclitus: upon those who step into the same river, different waters flow.
Plutarch: the Athenians kept Theseus's ship sailing by replacing its planks
one at a time. Was it still the same ship? Hobbes: and if someone reassembled
the old planks, which ship would be Theseus's?

Each puzzle has one structure. Two ways of counting come apart: same river,
different water; same ship, different planks; same planks, a different ship.

## What is already known

- **Locke**: identity depends on the kind of thing. Add one atom and a mass of
  matter is no longer the same mass; an oak stays the same oak through a
  lifetime of exchanged matter.
- **Geach, Wiggins**: "the same" always invites "the same *what*?"
- **Quine**: no entity without identity. You can bathe in the same river twice,
  though not in the same water.
- **Dennett**: the gliders of Conway's Game of Life are real patterns, though
  nothing but cells ever changes.

ICW starts from all of this. Identity depends on a criterion.

## What ICW adds

The tradition does not say when two criteria are two articulations of *one*
thing, rather than an arbitrary pair, or one criterion that merely refines the
other. ICW contributes:

1. **A test.** Two criteria articulate one changing whole when each holds where
   the other fails, checked in both directions, and the whole's changing
   carries both. Most pairs fail, in one of four named ways.
2. **A result on composition** *(proposed)*. "Made of" holds only within one
   criterion. The ship at an instant is made of planks; the ship that persists
   through repair is made of no particular planks.
3. **A result on causation** *(proposed)*. Between two articulations of one
   whole there is one change, read twice. Neither "the glider acts on the
   cells" (emergence) nor "only the cells act" (reduction) is the right
   picture.
4. **A separation.** Identity is independent of determination. The glider is
   fully calculable from the cell rule, and still not made of cells.

## The base case

In the Game of Life, no cell moves. Cells sit at fixed sites and switch on and
off. Yet a glider crosses the grid. A cell is one thing by one criterion (same
site, through any change of state); a glider by another (same organization,
through any change of site). Same cell, different gliders; same glider,
different cells.

    cell < grid > glider

*The grid is articulated as cells and as gliders.* The arrows point outward
from the whole and are a mnemonic only.

## It usually says no

| Pair | Verdict | Why |
|---|---|---|
| triangle, circle of a cone | **untyped** | nothing changes, so there is nothing to trace |
| charge, field in electrostatics | **coincident** | one criterion under two names |
| temperature, microstate | **nested** | one refines the other |
| cell, glider | cross-cuts | the paradigm case |
| colour, shape of parked cars | cross-cuts | passes the same checks as cell and glider |

The last two rows are the open problem. Cell and glider look carried by the
grid's changing; colour and shape look laid across the car park. The kernel
names that difference (*carrying*) and does not yet define it, so it cannot
yet tell the two rows apart. That is the place to push.

## Examples

- [Glider](examples/glider.md): why "gliders emerge from cells" and "gliders
  are made of cells" both misfire, and why "the collision changed these cells"
  is still true.
- [Wave](examples/wave.md): the same structure in water.
- [Ship of Theseus](examples/ship.md): what ICW says about the oldest case, and
  what it leaves open.
- [Limits](examples/limits.md): the ways the test says no.

## What it does not claim

- That one criterion is the real one. No articulation ranks above another.
- That anything does the articulating, whether an observer or the whole
  itself. An articulation is a structure of the changing, not an act.
- That anything acts between articulations. There is one change, read twice.
- That passing the test makes something real.

## Layout

| Path | What |
|---|---|
| [`specs/ARTICULATION.md`](specs/ARTICULATION.md) | The kernel. Every term defined before use, every item with a stable ID. The only authoritative file. |
| [`specs/READING.md`](specs/READING.md) | Misreadings the kernel excludes, with probes. |
| [`examples/`](examples/) | Cases. An example may not conclude what the kernel does not contain. |
| [`notes/FINDINGS.md`](notes/FINDINGS.md) | Working notes. Not authoritative. |
| [`tools/`](tools/) | `python3 tools/lint.py` checks definition order, citations and rendering; `python3 tools/algebra.py` checks the relation's algebra. |

## Prior art

Heraclitus, fragment B12. Plutarch, *Life of Theseus* 23. Hobbes, *De
Corpore* II.11. Locke, *Essay Concerning Human Understanding* II.xxvii. Geach,
*Reference and Generality* (1962). Wiggins, *Sameness and Substance* (1980).
Quine, "Identity, Ostension, and Hypostasis" (1950). Dennett, "Real Patterns"
(1991).
