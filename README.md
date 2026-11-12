# Identity in Changing Wholes

**What counts as one thing, when everything is changing?**

In Conway's Game of Life, no cell ever moves. Cells sit at fixed sites and
switch on and off. Yet a glider crosses the board. Something moves, and
nothing it is made of moves.

The usual answers pick a side. *Reduction*: there are only cells, and the
glider is a way of talking. *Emergence*: the glider is a new thing that arises
from the cells and acts back on them. Both take the cells as given and ask how
the glider relates to them.

ICW starts one step earlier. Before asking how two things relate, you have to
say what counts as one thing. A cell is one thing by one criterion: same site,
through any change of state. A glider is one thing by another: same
organization, through any change of site. Run both criteria over the same
history and you get two inventories. Neither is the substrate of the other.
Neither produces or constrains the other. They are two articulations of one
changing whole.

    cell < grid > glider

*The grid is articulated as cells and as gliders.*

## Why it matters

The same shape recurs wherever things persist through change. Is the wave the
water? Is the ship its planks? Is the flower just fields and light? Each
dispute assumes one criterion of identity is the real one, then argues over
whether the other's things exist.

ICW replaces that with a question that can be checked: do the two criteria
cross-cut, so that each holds where the other does not, and does the whole's
changing carry both? Causation, composition and reduction are asked afterwards,
within an articulation, once there is something to relate.

## It usually says no

A candidate pair goes through ordered checks and gets exactly one verdict.

| Pair | Verdict | Why |
|---|---|---|
| triangle, circle of a cone | **untyped** | nothing changes, so there is nothing to trace |
| charge, field | **coincident** | one criterion under two names |
| temperature, microstate | **nested** | one refines the other |
| colour, shape of parked cars | **uncarried** | cross-cuts, but carrying is not shown |
| cell, glider | **holds** | `cell < grid > glider` |

A theory that said yes to everything would say nothing.

## Examples

- [Glider](examples/glider.md): why "gliders emerge from cells" and "gliders
  are made of cells" both misfire, and why "the collision changed these cells"
  is still true.
- [Wave](examples/wave.md): the same structure in water.
- [Perception](examples/perception.md): "there is no red flower, only fields".
  Which half ICW refutes, and which it leaves open.
- [Limits](examples/limits.md): the four ways the test says no.

## What it does not claim

- That gliders are real and cells are not, or the reverse. No articulation
  ranks above another.
- That anything does the articulating, whether an observer or the whole
  itself. An articulation is a structure of the changing, not an act.
- That anything acts between articulations. There is one change, read twice.
- That passing the test makes something real.

## The open problem

Colour and shape across a car park cross-cut exactly as cell and glider do.
What makes one pair carried by the changing and the other merely laid across
it? The kernel names this condition and does not yet define it. It is the
theory's central open item (O2 in the spec), and the place to push.

## Layout

| Path | What |
|---|---|
| [`specs/ARTICULATION.md`](specs/ARTICULATION.md) | The kernel. Bottom-up: every term defined before use, every item with a stable ID. The only authoritative file. |
| [`specs/READING.md`](specs/READING.md) | Misreadings the kernel excludes, with probes. Read before writing about it. |
| [`examples/`](examples/) | Cases. An example may not conclude what the kernel does not contain. |
| [`notes/FINDINGS.md`](notes/FINDINGS.md) | Working notes. Not authoritative. |
| [`tools/`](tools/) | `python3 tools/lint.py` checks definition order, citations and rendering; `python3 tools/algebra.py` checks the relation's algebra. |
