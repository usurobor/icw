# Intent: README

**Status: draft for owner review.** Purpose only. How the README gets there
belongs to the planning cell.

The README exists so that a stranger who reads it understands ICW's idea and
wants to read on. Each property below is stated as an outcome, pinned by a
near-hit (✅) and a near-miss (❌), with what would show it. Examples marked
*illustration* show what meeting a property looks like; the working cell may
meet it another way.

Priority: **I1 and I2 first.** A README that fails either ranks below every
README that passes both. Then I3–I6 and I8. I7 always.

## I1. Draws the visitor in

A stranger who reads the opening wants to read on, because of a question
about the subject itself.

- ✅ *illustration*: the opening leaves the reader asking how the glider can
  move when no square does.
- ❌ the opening leaves the reader asking what "ICW" stands for.
- **Shown by:** the owner reads it and decides.

## I2. Plain words

A non-specialist reads it without help. Technical terms appear only where no
everyday word does the job, and each is explained where it first appears.

- ✅ *illustration*: "a grid of squares that switch on and off by one simple
  rule".
- ❌ "a two-dimensional cellular automaton with a Moore-neighbourhood update
  rule".
- **Shown by:** a fresh reader's list of phrases they had to guess at. A flag
  counts only when their guess is missing or wrong.

## I3. The first paragraph carries the idea

A reader who stops after the first paragraph can say, in their own words:
there can be two honest ways to say what stays the same while something
changes; they can disagree in both directions; and ICW asks whether the
changing thing itself keeps both going, instead of choosing one.

- ✅ *illustration*: "No square on the grid ever moves, yet a glider crosses
  it. The same square holds one glider, then another; the same glider covers
  new squares at every step."
- ❌ "In the Game of Life, gliders emerge from cells following simple rules."
  Readers come away with the usual story, and with ICW's idea missing.
- **Shown by:** a fresh reader restates the first paragraph; the restatement
  contains all three parts.

## I4. Shows what it questions (*proposed by Claude; owner to confirm*)

The reader sees which familiar explanation ICW questions, and where it slips.

- ✅ *illustration*: "'Gliders emerge from the cells' starts out counting
  squares and ends up counting gliders."
- ❌ the README explains ICW's idea and leaves the reader unaware of any
  explanation it differs from.
- **Shown by:** a fresh reader can name the explanation and the slip.

## I5. Holds up wherever the reader stops (*Claude's reading of the owner's "top-down unfolding"; owner to confirm*)

After the first paragraph, after the first section and after the first worked
example, the reader holds a complete, smaller version of the idea.

- ✅ the first section ends with the glider worked through once, both
  directions shown.
- ❌ the first paragraph asks the question and the answer arrives three
  sections later.
- **Shown by:** a fresh reader stopped at each point restates what they have.

## I6. Succinct

Every sentence adds something the reader would miss without it.

- ✅ a closing line that points to the one next file to read.
- ❌ a closing paragraph that restates the opening in other words.
- **Shown by:** a fresh reader's list of sentences that repeat an earlier one.

## I7. True to the kernel

Every claim about what ICW says or shows traces to `specs/ARTICULATION.md`.
What is open is stated as open.

- ✅ "The test's last step is still unfinished, so no case has passed it."
- ❌ "ICW shows that the glider is as real as the squares." The kernel's test
  for that is unfinished.
- **Shown by:** a judge holding the kernel checks each claim.

## I8. Takes its place in an old conversation

The reader sees that the question is old, who asked it before, and what ICW
adds, with every credit accurate. (Owner, 12 Nov: "additive to the
conversation going on for millennia, with respect to prior art.")

- ✅ *illustration*: one sentence naming Heraclitus's river and Theseus's
  ship, linking to `PRIOR-ART.md` for the full credits.
- ❌ the README presents the glider puzzle as ICW's discovery.
- **Shown by:** a judge checks each credit against its source and each
  "ICW adds" claim against the credited work.

## Owner decisions (13 Nov 2026)

- I1 is judged by the owner. No reader panel scores it.
- I2 uses the lenient bar above, and no jargon.
- Hint for planning (the planning cell decides whether it becomes a
  requirement): concrete cases first, then the general idea. The glider and the "emerges from" explanation as the lead;
  molecules flowing through a cell as a second case.

## Owner decisions (14 Nov 2026, advisor session)

Each line is the owner's decision; the advisor proposed, the owner chose.

- **The one idea.** Levels of organization (glider and squares, program and
  hardware, body and organs) can be different ways of counting one changing
  process, with no causation between them. Supporting claim: a description
  can be sufficient, fixing every next state, and still incomplete.
- **Two kinds of criteria**, defined over snapshots with no observer:
  - *Snapshot criterion*: one snapshot settles sameness, by fixed address.
  - *Sequence criterion*: sameness is settled only across a sequence of
    snapshots, by continuity.
  - ✅ One snapshot settles every square and its state. One snapshot can hold
    a glider-shaped group and cannot show it is a glider; that takes five
    consecutive snapshots, one period of four generations.
  - ❌ "One snapshot plus the rules defines the squares but not the glider."
    The rules generate the whole sequence; the glider is a fact about it.
  - Line for the README: *Squares can be counted in one snapshot. A glider
    needs five.*
- **Every example pairs one snapshot criterion with one sequence criterion.**
- **Examples climb: glider, computer, body.** This replaces the 13 Nov hint
  (molecules flowing through a cell as the second case); molecules move to
  "read next".
  - Computer: physics fixes every voltage; "the same program running on two
    machines" exists only in the other count.
  - Body: ✅ the living body, followed across a sequence through its
    turnover. ❌ the body as the organs it contains, compared through
    transplants: both sides are snapshot criteria.
- **Theseus's ship sits beside the body, in the section on where ICW stands.**
  The repaired ship persists through an unbroken sequence; a ship rebuilt
  from the old planks starts a new sequence at its assembly; Hobbes's matter
  verdict holds within its own criterion. Ship and body both persist through
  turnover; the ship is repaired by others and the body repairs itself.
  Whether that difference is what "carried" means is the open question (O2).
  Fission is logged as O4.
- **Outline for 1.0.0**, one line per section on what the reader then holds:
  0. Title and one-sentence claim.
  1. The glider: two ways of counting one process.
  2. The computer: sufficient yet incomplete is ordinary.
  3. What ICW is: the idea, then the four checks in plain words.
  4. The body: the question of causation between levels becomes a question
     of identity; mind and brain in one line (Kim).
  5. Where it stands: "carried" is open; ship beside body.
  6. Read next: examples, kernel, pairs still to examine.
  7. Prior art: a few lines on what ICW adds (Putnam and Fodor credited;
     Kim and Searle named); full credits in `PRIOR-ART.md`.
