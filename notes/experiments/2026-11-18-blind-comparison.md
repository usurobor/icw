# Blind comparison: does ICW improve reasoning?

Pre-registration, frozen before any answer is collected. Owner decision
(18 Nov): freeze candidate runs and test whether ICW improves reasoning. The
result informs the pending purpose decision in `notes/CASES.md`.

## Question

Does an ICW instruction make a model's answers to questions about
persistence, emergence and the reality of patterns better, by criteria fixed
here, than no instruction and than a length-matched instruction to reason
carefully?

## Conditions

- **A, none.** The prompt alone.
- **B, ICW.** The prompt plus the instruction below.
- **C, placebo.** The prompt plus a length-matched instruction to reason
  carefully, check assumptions and consider alternatives. C controls for the
  effect of any instruction at all.

### Instruction B (frozen)

> Before answering, describe the thing in question twice: once by its
> elements (what it is made of at an instant) and once as a pattern (what
> stays the same while the elements change). Say whether the two descriptions
> pick out different things, with an example in each direction if they do.
> "Made of" holds for a snapshot; say whether the question is about a snapshot
> or about something that persists. If an argument concludes that a pattern is
> unreal because it is absent among the elements, say so, and say that this
> exposes a weak argument without showing that the pattern persists. Where
> neither description changes the answer, say that, and answer plainly.

### Instruction C (frozen)

> Before answering, reason carefully. State your assumptions, check each one,
> consider at least one alternative view and what would decide between them,
> and avoid claims stronger than your reasons support. Where the question is
> simple, say so, and answer plainly.

## Prompts (frozen, 12)

Three groups. Group N contains controls where the right answer is plain
composition and ICW should add nothing.

- **P (persistence and patterns)**
  - P-1. Is a traffic jam a thing, or just cars?
  - P-2. If every plank of a ship is replaced, is it the same ship?
  - P-3. Is a glider in Conway's Game of Life real, or just cells switching?
  - P-4. Is a river the same river from one year to the next?
- **U (arguments that a pattern is unreal)**
  - U-1. Money is just paper we agree to believe in. Is that right?
  - U-2. Search for the self among body, thoughts and sensations, and you find
    no self. So there is no self. Is that sound?
  - U-3. A character in a video game cannot find the graphics card, so the
    game world is less real than the hardware. Agree?
  - U-4. Temperature is just molecules moving, so temperature is not real.
    Is that right?
- **N (controls)**
  - N-1. Is a pile of bricks anything more than the bricks?
  - N-2. Is a car engine made of its parts?
  - N-3. Is a block in the Game of Life (a still life) more than its four
    cells?
  - N-4. Is a sentence made of words?

## Answerers

At least two model families. Each answers every prompt under A, B and C in a
fresh conversation: 12 × 3 × 2 = 72 answers. Answers are logged verbatim by
script (cells protocol rule 4), with model, version and date.

## Judging

- Judges see a prompt and two answers from the same answerer, in random
  order, with the instruction stripped and no condition labels. Pairs: B
  against A, B against C, C against A.
- Judges come from a family other than the answerer's, and from two families
  in total where possible. Each pair is judged twice with the order swapped.
- Rubric, scored for each answer 0–2 on each item:
  - R-1. Identifies whether the question is about a snapshot or about
    something that persists.
  - R-2. Gives a correct witness where the element and pattern descriptions
    come apart, or correctly says they do not (group N).
  - R-3. Flags a weak inference from "absent among the elements" to
    "unreal", without claiming this proves the pattern persists (group U).
  - R-4. Makes no claim stronger than its reasons (overclaiming scores 0).
  - R-5. Plain and short enough to follow.
- Plus a forced choice: which answer would you rather rely on?

## Decision rule (frozen)

- **ICW helps** if, summed over groups P and U, B beats C in the forced choice
  in at least 60% of judged pairs, B's mean on R-1 to R-3 exceeds C's by at
  least 0.3, and B does not lose to C on R-4.
- **ICW hurts on controls** if, in group N, B loses to A in the forced choice
  in more than 50% of pairs or scores lower on R-4 or R-5. Either outcome is
  reported, whatever happens in P and U.
- **No effect** otherwise. Report effect sizes and every judged pair.
- Agreement between judges is reported. Below 70% agreement on the forced
  choice, the result is inconclusive.

## Known limits

- Twelve prompts are a pilot. A positive result calls for a larger set
  written by someone outside the project.
- Prompts U-1 to U-3 come from debates in which ICW was used, so they may
  favour B. Group N is there to catch an instruction that rewards its own
  vocabulary.
- R-1 to R-3 are close to the vocabulary of instruction B, so R-4, R-5 and
  the forced choice carry the weight against that bias.
