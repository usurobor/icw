# Identity in Changing Wholes

## Emergence

A familiar picture of the world: living cells emerge from molecules, organisms
from cells, a mind from neurons. In each case, something more complex arises
from smaller, simpler things.

ICW examines that picture through a case where every step can be followed.

## One grid, two ways of staying the same

Conway's Game of Life is a grid of squares, each lit or dark. A fixed rule
takes the whole grid from one snapshot to the next; every square's next state
is calculated from that same snapshot.

Follow a square: it stays in place while it switches between lit and dark.

Follow a glider: a small pattern travels across the grid, changing shape as it
goes, and stays the same glider while passing over different squares.

Different gliders can pass over the same square. The same glider passes over
different squares. Neither way of staying the same guarantees the other.

One grid, one sequence of changes, two ways of staying the same.

## What "emerges" does

"How do squares make a glider?" can hold two questions.

How did a glider form here, where there was none before? The rule answers that
completely, snapshot by snapshot.

What makes it the same glider as its shape and its squares change? That needs
a criterion: which changes preserve its identity and which end it. Calculating
successive snapshots does not, by itself, specify that criterion. The rule can
then help test it.

ICW challenges using "emerges from" to bridge the two questions. In that use, a
difference in identity looks like one kind of thing producing another. Its
proposal is that the same changing grid sustains both kinds, with no further
process connecting them.

At any instant, a glider occupies a few lit squares. Later it can be the same
glider on none of them. Its motion is calculable from the squares and the rule,
while what makes it the same glider differs from what makes a square the same
square.

## Where else?

A living cell can replace molecules and stay the same cell. An organism can
replace cells and stay the same organism.

Still, how do molecules make a living cell? How do cells make an organism? How
do neurons make a mind?

These are mechanism questions. ICW asks how they relate to a different
question: what makes it the same cell, organism or mind through change?

It investigates whether some of these cases involve one changing whole
sustaining two kinds of identity, by its elements and by its patterns. Each
case has to be examined on its own.

## The research program

What separates a pattern the grid keeps going from a grouping laid over it? We
could group two unrelated gliders as one, or follow one glider and then switch
to another.

ICW calls a way of staying the same through change an *articulation* when the
whole's own changing sustains it. Making that precise is the open problem.

Candidate definitions are run against cases in the Game of Life, then
challenged with counterexamples. The [case register](notes/CASES.md) and
[working notes](notes/FINDINGS.md) record what passes, what fails, and what
changes next.

## Read next

- [The glider, step by step](examples/glider.md)
- [The question's history, from Heraclitus's river to the ship of
  Theseus](PRIOR-ART.md)
- [The definitions](specs/ARTICULATION.md)
