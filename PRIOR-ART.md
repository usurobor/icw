# Prior art

ICW is a contribution to a conversation about identity through change that is
about 2,500 years old. This file credits that conversation and states what ICW
inherits from it and what it adds. Terms are defined in the
[README](README.md#two-ways-of-counting). Parenthesised IDs point to the
kernel, [`specs/ARTICULATION.md`](specs/ARTICULATION.md), which governs.

## The conversation

- **Heraclitus** (fragment B12): on those who step into the same rivers,
  different waters flow.
- **Plutarch** (*Theseus* 23.1): the Athenians preserved Theseus's ship by
  replacing decayed timbers, and philosophers split over whether it remained
  the same ship.
- **Hobbes** (*De Corpore* II.11.7): rebuild a ship from the discarded
  planks, and there seem to be two ships numerically the same. His answer:
  sameness depends on what the name is given for (the matter, the form, or
  an aggregate of accidents). "Ship" signifies matter so shaped, so a ship
  is the same while its matter is.
- **Locke** (*Essay* II.xxvii.3, 7): atoms united in a mass are the same mass
  while they stay united, and add or remove one and it is another mass. Yet
  an oak stays the same oak through changes of matter. The idea of identity
  must suit the idea it is applied to.
- **Geach** (1962, 1967) and **Wiggins** (1980): every judgement of sameness
  answers *the same what?* Geach went further, to relative identity: a and b
  may be the same F but not the same G. Wiggins keeps the dependence on a
  kind and rejects relative identity.
- **Quine** (1950): "River stages are water stages, but rivers are not waters."
  You may bathe in the same river twice without the same water, and in the
  same water twice in two different rivers. One collection of stages, two
  groupings, coming apart in both directions: the structure ICW starts from.
- **Lewin** (1922) named *genidentity*, the relation between earlier and
  later stages of what develops one from the other. **Reichenbach** (1956)
  took it up.
- **Constitution.** A statue and its lump of clay coincide in place and
  matter. Gibbard (1975) made them come into being and perish together and
  argued that they are then identical, though only contingently: had the
  clay been squeezed into a ball, the lump would have survived and the statue
  not.
- **Causal persistence.** Russell (1948) let causal lines replace substance in
  what makes a thing the same over time. A mark criterion that Salmon (1984)
  takes from Reichenbach separates causal processes from pseudo-processes
  (Reichenbach's "unreal sequences", 1958, pp. 147–149), such as a moving spot
  of light, which cannot transmit a mark. On the immanent-causation view,
  discussed by Zimmerman (1997), a thing persists only where its earlier
  states cause its later ones.
- **Dennett** (1991): in the Game of Life nothing moves at what he calls the
  physical level, the cells and their rule, while at the design level one and
  the same glider moves. Every glider is calculable from the rule. He argues
  that such patterns are real.
- **Goodman** (1955) defined *grue*: green if examined before a fixed date,
  blue otherwise. It poses his new riddle of induction.
- **Lewis** (1983) separates an elite minority of natural properties from the
  abundant rest, which "carve reality at the joints — and everywhere else as
  well". He denies that grue is a universal: grueness "does not make for
  resemblance among all its instances".
- **Davidson** (1970): one event can fall under a mental and a physical
  description.
- **Gardner** (1970) described Conway's Game of Life in his *Scientific
  American* column.

## What ICW inherits and what it adds

Most of the structure is inherited. Quine already groups one collection of
stages two ways that come apart in both directions, and draws the consequence
for composition: a river is a summation of stages picked out by river kinship,
and each of its stages is a water stage, yet no river is a water. ICW's
composition result agrees with him and with Locke's oak (R4, proposed,
conditional on a pair passing): wherever `A < X > B`, "B consists of As", read
as fixing which B, refers only to B's footprint, never to B as it persists.
Dennett already follows one and the same glider over cells that never move,
and notes that it is calculable from the rule. ICW agrees that derivability
and a different criterion of identity are compatible (R2). Its additions are
narrower.

1. **A test that can refuse.** Checks 2 and 3 of the README's test use the
   ordinary refinement order on sameness relations: two are equal, one is
   finer, or neither is. The addition is to run the checks in order, in a
   named changing whole, with both directions witnessed, as stated grounds for
   refusing a pair. A pair in a whole that does not change, a coincident pair
   or a nested pair is refused, and the reason is named.
2. **The carrying question, placed.** Whether a way of tracing a thing is
   sustained by the world's changes is asked by the causal accounts of
   persistence listed above. Telling a natural sorting from a gerrymandered
   one is the problem Goodman's grue poses for induction, and the one Lewis's
   natural properties address. ICW's addition is the placement: carrying is
   the last check of an ordered test on a *pair* of criteria over one named
   changing, and it is left open (O2). As with Salmon's criterion, carrying is
   a property, here of a criterion, not a further relation among occurrences
   (D8). D8's first candidate, that the changing preserves a criterion's
   classes forward, sits close to these accounts.
3. **A consequence for causation, proposed and conditional on a pair
   passing** (R5). Where `A < X > B` there is one change. A causal claim
   across the two criteria can be true, but it is a claim about that change
   read through two criteria, never about a further process running between
   them. This is close to Davidson's (1970) one event under two descriptions.
   It differs in two ways. The two criteria pick out different things
   (cell-histories, gliders) in one change, rather than describing one item.
   And each must be carried (D9), which a description need not be.

## References

- Heraclitus, fragment DK 22 B12.
- Plutarch, *Life of Theseus* 23.1.
- Hobbes, *De Corpore* (1655), part II, ch. 11, §7.
- Locke, *An Essay Concerning Human Understanding*, 2nd ed. (1694), book
  II, ch. xxvii, §§3, 7.
- Lewin, K. (1922). *Der Begriff der Genese in Physik, Biologie und
  Entwicklungsgeschichte*. Berlin: Springer.
- Russell, B. (1948). *Human Knowledge: Its Scope and Limits*. New York:
  Simon and Schuster, pp. 333, 475–477.
- Quine, W. V. (1950). "Identity, Ostension, and Hypostasis." *Journal of
  Philosophy* 47(22): 621–633. Reprinted in *From a Logical Point of View*
  (1953).
- Goodman, N. (1955). *Fact, Fiction, and Forecast*, ch. III.
- Reichenbach, H. (1956). *The Direction of Time*. University of California
  Press.
- Reichenbach, H. (1958). *The Philosophy of Space and Time*. New York:
  Dover. Translation of *Philosophie der Raum-Zeit-Lehre* (1928).
- Geach, P. T. (1962). *Reference and Generality*. Cornell University Press.
- Geach, P. T. (1967). "Identity." *Review of Metaphysics* 21: 3–12.
- Davidson, D. (1970). "Mental Events." In Foster and Swanson (eds.),
  *Experience and Theory*.
- Gardner, M. (1970). "Mathematical Games." *Scientific American* 223(4),
  October.
- Gibbard, A. (1975). "Contingent Identity." *Journal of Philosophical Logic*
  4(2): 187–221.
- Wiggins, D. (1980). *Sameness and Substance*. Oxford: Blackwell.
- Lewis, D. (1983). "New Work for a Theory of Universals." *Australasian
  Journal of Philosophy* 61(4): 343–377.
- Salmon, W. C. (1984). *Scientific Explanation and the Causal Structure of
  the World*. Princeton University Press, pp. 141–148.
- Dennett, D. C. (1991). "Real Patterns." *Journal of Philosophy* 88(1):
  27–51.
- Zimmerman, D. W. (1997). "Immanent Causation." *Philosophical
  Perspectives* 11: 433–471.
