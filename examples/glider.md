# The glider

The computational case. Terms are in the [README](../README.md#two-ways-of-counting),
credits in [PRIOR-ART.md](../PRIOR-ART.md), and IDs point to
[`specs/ARTICULATION.md`](../specs/ARTICULATION.md).

## The case

Conway's Game of Life (Gardner 1970) is a grid of cells, each alive or dead.
A cell's next state is fixed by its own state and how many of its eight
neighbours are alive: a live cell with two or three live neighbours stays
alive, a dead cell with exactly three comes alive, and every other cell is
dead at the next step. Cells never move. A *glider* is a five-cell pattern
that recurs every four steps, shifted one cell diagonally.

## Two criteria

Both are Dennett's (1991): at what he calls the physical level, the cells and
their rule, nothing moves; at the design level one and the same glider moves.

- **Cell.** Same site, through any change of state.
- **Glider.** The same glider, followed from step to step, through any change
  of site, not sameness of arrangement.

Witnesses in both directions:

- *Same cell, different gliders.* A cell lies in one glider's path, then
  another's.
- *Same glider, different cells.* After sixteen steps a glider shares no cell
  with where it began.

The candidate is `cell < grid > glider`, where *the grid* is the running
grid, its whole history. Site labels do not privilege the cell criterion
(A1, proposed).

**Verdict.** The grid changes, the criteria differ, and they cross-cut (D7).
Whether its changing carries both is undecided (D8, O2): **uncarried**,
pending; check 3 is the furthest it passes.

## Three sentences

**"Gliders emerge from cells."** A glider can arise: at one step nothing fits
the glider criterion, later something does. That is a change in the one
history. Switching from counting cells to counting gliders changes what is
counted, not what occurs (D9). Neither is a process running from cells to
gliders.

**"Gliders are made of cells."** True of the glider's footprint: a frozen
frame shows five live cells, and no glider (D3). But cell-sameness is not what
makes it the same glider: the same glider has no fixed set of cells (D7). Nor
is cell-sameness with arrangement: a second glider crossing the same sites in
the same phase has the same cells in the same arrangement, yet is a different
glider. If the pair were articulated, "made of" in the identity-fixing sense
would refer only to footprints (R4, proposed).

**"The collision of two gliders made these cells switch."** This can be true:
without the collision, those cells would not have switched. If the pair were
articulated, it would be a claim about the grid's one change read through two
criteria, not a second cause running between them (R5, proposed). Compare
Davidson (1970); PRIOR-ART.md gives the differences.

## Derivable, and still a different sameness

Every glider is calculable from the rule, as Dennett notes, and derivability
is compatible with a different criterion of identity (R2). Dennett argues the
glider is a real pattern; ICW makes no claim about what is real.
