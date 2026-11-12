# Glider

The base case. IDs refer to `specs/ARTICULATION.md`.

## Two criteria, one history

In Conway's Game of Life, cells sit at fixed sites and switch on and off. Run
the rule, and a five-cell shape reappears every four steps, one site over
diagonally. That shape is a glider.

Two ways of counting one thing:

- **Cell.** Same site, through any change of state. A cell never moves.
- **Glider.** Same organization, through any change of site. A glider never
  stays.

Each holds where the other does not. One cell is occupied by a glider, then by
nothing, then by a different glider: same cell, different gliders. One glider
occupies different cells at every step: same glider, different cells. The two
criteria cross-cut (D7), over one history.

    cell < grid > glider

Read: *the grid is articulated as cells and as gliders.* The arrows point
outward from the whole and are mnemonic; they are not causation, composition or
order (D11).

*The grid* here is the running grid, its whole history of changes, not the
lattice of sites. The lattice is how occurrences are labelled, and a label is
not a criterion of identity (A1). Otherwise the cell side would quietly become
the whole.

## Three sentences, three verdicts

**"Gliders emerge from cells."** Two different things are easily confused. A
glider can *arise* in time: at one step nothing on the board fits the glider
criterion, at a later step something does. That is a change. Switching from
counting cells to counting gliders is not a change at all; nothing in the
board corresponds to it. Neither is a new level coming into being, and neither
is a process running from cells to gliders.

**"Gliders are made of cells."** True of the glider's footprint at an instant:
a frozen frame shows five live cells. False of the glider as a persisting
thing, which has no fixed set of cells. Replace every cell and the same glider
goes on; take the same cells otherwise arranged and there is no glider.
"Consists of" works within one criterion, never across two (R4).

**"The collision of two gliders made these cells change."** True. Had the
gliders not collided, those cells would not have changed. It picks out its
subject by one criterion and its object by the other, and that is fine. What
it cannot mean is a second cause acting between the two inventories alongside
the cell rule. There is one change, read twice (R5).

## Derivable is not the same as constituted

Given the rule and the starting states, every glider is calculable. ICW does
not deny this. Derivability and a different criterion of identity are
compatible facts (R2): the cell description determines the history, and the
glider is still not built out of cells.
