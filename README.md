# Identity in Changing Wholes

## Emergence

A familiar picture of the world: living cells emerge from molecules, organisms
from cells, ant colonies from ants. In each case, something more complex arises
from smaller, simpler things.

ICW proposes another reading: one changing whole, told two ways, by elements
and by patterns.

## One grid, told two ways

Conway's Game of Life is a grid of squares, each lit or dark. A fixed rule
takes the whole grid from one snapshot to the next; every square's next state
is calculated from that same snapshot.

Follow a square: it stays in place while it switches between lit and dark.

Follow a glider: a small pattern travels across the grid, changing shape as it
goes, and stays the same glider while lighting different squares.

Different gliders can light the same square. The same glider lights different
squares.

One grid, one sequence of changes, told two ways.

## How do gliders emerge from squares?

Watch the squares and nothing travels: each square switches on or off according
to its neighbours. Yet a glider crosses the grid. The usual answer is that the
squares, interacting, somehow make up the glider.

Look at what happens. The rule takes the whole grid from one snapshot to the
next. Every fourth snapshot, the glider's five lit squares appear again in the
same arrangement, one square further along the diagonal. Eight snapshots on, it
lights none of the squares it started on.

Squares switching by their neighbours is the elemental telling of that change.
Following the glider as it recurs further along is the pattern telling. Both
tell the same snapshots.

Read as the squares producing the glider, "the glider emerges from the squares"
mixes the two tellings. It starts in the elemental one, ends in the pattern
one, and takes the switch between them for production. ICW proposes that
neither telling is more basic, and neither produces the other.

## Where else?

A living cell can replace molecules and stay the same cell. An organism can
replace cells and stay the same organism. A colony can replace ants and stay
the same colony.

Still, how do molecules make a living cell? How do cells make an organism? How
do ants make a colony?

These are mechanism questions. ICW asks how they relate to a different
question: what makes it the same cell, organism or colony through change?

It investigates whether some of these cases are one changing whole told two
ways, by elements and by patterns, and whether "emerges" mixes the two there as
well. Each case has to be examined on its own.

## How to examine a case

ICW offers a way for people and language models to examine an emergence claim:
name the changing whole first, then make both ways of staying the same
explicit. For the glider:

- **Whole:** the grid changing under one rule.
- **Element:** the same square, through changes between lit and dark.
- **Pattern:** the same glider, through changes of shape and place.
- **Claim:** what does "emerges from" assert between squares and gliders?
- **Open:** what distinguishes following the same glider from following one
  glider and then switching to another?

The labels make the claim explicit before anyone judges it.

## The research program

Running every step of the grid does not yet say what counts as the same glider.
Following one glider counts as following the same thing; following one glider
and then switching to another does not. What makes the difference is the
central open task: a test, grounded in how the whole changes, that separates a
way of staying the same the changing keeps going from a grouping laid over it.

Candidate definitions are tested first in the Game of Life, where every claim
can be checked by running it, then challenged with counterexamples. A
definition that survives is taken to other cases where a pattern is said to
emerge from elements: cells, organisms, colonies. Failures change the proposal.

The [case register](notes/CASES.md) and [working notes](notes/FINDINGS.md)
record the tests, failures and revisions.

## Read next

- [The glider, step by step](examples/glider.md)
- [The question's history, from Heraclitus's river to the ship of
  Theseus](PRIOR-ART.md)
- [The definitions](specs/ARTICULATION.md)
