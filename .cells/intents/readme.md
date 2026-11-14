# Intent: README

**Status: draft for owner review.** *Owner* marks the owner's words or
decision, dated (records under Sources); *proposed* marks Claude's. The
Design section of `runs/2026-11-13-readme/contract.md` holds how (rule 9).

The README exists so that a stranger who reads it understands ICW's idea and
wants to read on. Each property is an outcome with a near-hit (✅), a
near-miss (❌) and what would show it; an *illustration* is one way to meet
it. Readers, judges, calibration and every "Pass" are *proposed*; the
planning cell settles them (rule 5). Priority (owner, 12 Nov): clarity is
"highest priority, with 1"; a README failing I1 or I2 ranks below every
README passing both. *Proposed:* then I3–I6 and I8; I7 always.

## The idea

One statement, used by I3, I5 and I7. Terms are the kernel's (D10); the
README says them in plain words (owner, 14 Nov).
1. What are called levels, such as squares and glider, can be two ways of
   saying what stays the same in one changing whole: *elemental*, sameness
   of what changes (a square); *pattern*, sameness of the change across what
   changes (the glider) (owner, 14 Nov; D10).
2. Each holds where the other does not: one square holds one glider, later
   another; one glider covers new squares at every step (D7).
3. ICW offers a test anyone, an LLM included, can run on a claimed pair
   (owner, 14 Nov). *Proposed*, for O2: it refuses a pair on stated grounds
   (no change; one criterion, two names; one inside the other) and cannot
   yet confirm one: its last check, whether the change keeps both going, is
   open (§6).

Supporting (owner, 14 Nov). A causal sentence across the two can be true:
it is the one change described at either level, and the README presents
this as proposed (R5). A description can be "sufficient, fixing every next
state, and still incomplete" (*proposed* reading, R1: it fixes all that
happens and leaves open what counts as one).

## I1. Draws the visitor in (owner, 12 Nov)

A stranger who reads the opening wants to read on (*proposed:* for its subject).
- ✅ *illustration*: the reader asks how the glider moves when no square does.
- ❌ the reader asks what "ICW" stands for.
- **Shown by:** the owner reads it and decides; no reader panel (owner,
  13 Nov; rule 6).

## I2. Plain words (owner, 12 and 13 Nov)

A non-specialist ("your grandma") reads it without help. Owner, 13 Nov: "no
lingo: plain words a grandma reads without help, wherever the README can
manage without a technical term." *Proposed:* explain a needed term at once.
- ✅ *illustration*: "a grid of squares that switch on and off by one rule".
- ❌ "a two-dimensional cellular automaton with a Moore-neighbourhood rule".
- **Shown by:** (a) a fresh non-specialist lists each phrase they guessed at,
  with the guess; a judge holding the kernel rules on each, and a flag counts
  only if the guess is missing or wrong (owner, 13 Nov). (b) A judge lists
  each technical term an everyday word could replace. Pass: both lists empty.

## I3. The first paragraph carries the idea (owner, 12 Nov)

"A reader who reads only the first paragraph gets the idea": parts 1–3.
- ✅ *illustration*: "No square ever moves, yet a glider crosses the grid,"
  then one sentence on each direction and one on the test.
- ❌ "In the Game of Life, gliders emerge from cells following simple rules."
- **Shown by:** a fresh reader reads the first paragraph, hands it back,
  restates it, and applies it to one case it did not name (*proposed*). A
  judge marks parts 1–3. Pass: all three, and the case handled.

## I4. Shows what it questions (*proposed; owner to confirm*)

The reader sees which familiar explanation ICW questions, and where it slips.
- ✅ *illustration*: "'Gliders emerge from the cells' starts out counting
  squares and ends up counting gliders."
- ❌ the README states the idea and names no explanation it differs from.
- **Shown by:** a fresh reader names the explanation, what it counts first
  and what last; a judge checks against the README and READING misreading 1.

## I5. Holds up wherever the reader stops (*proposed*; owner to confirm)

Claude's reading of "top-down": at every section's end the reader holds
parts 1–3, and nothing read so far contradicts them.
- ✅ *illustration*: section 1 ends with the glider worked through once.
- ❌ section 1 raises the question; the answer comes three sections later.
- **Shown by:** a fresh reader stopped at each section's end restates it; a
  judge marks parts 1–3 and flags contradictions. Pass: all three, no flag.

## I6. Succinct (owner, 12 Nov)

Every sentence carries something the reader would miss without it.
- ✅ *illustration*: a closing line pointing to the one next file to read.
- ❌ a closing paragraph restating the opening in other words.
- **Shown by:** a fresh reader marks each sentence they would not miss; a
  judge lists each sentence that serves no property. Pass: both lists empty.

## I7. True to the kernel (*proposed*: seed R6, 12 Nov; owner to confirm)

Every claim about ICW traces to `specs/ARTICULATION.md`, read with
`specs/READING.md`; open stays open and proposed stays proposed. Every claim
about a case is true of it; a case the kernel lacks is an application.
- ✅ "The test's last check is still open, so no pair has passed it."
- ❌ "ICW shows that the glider is as real as the squares."
- **Shown by:** a judge holding the kernel pairs each ICW claim with its
  item and checks each case claim (Life by running it). Pass: all hold.

## I8. Takes its place in an old conversation (owner, 12 and 14 Nov)

The reader sees that the question is old, who asked it before, and how ICW
relates to each, every credit accurate. No claim that ICW is first or new
until a novelty check on ICW has run (owner, 14 Nov).
- ✅ *illustration*: Heraclitus's river and Theseus's ship named as this
  question, ICW's test put to the ship, a link to `PRIOR-ART.md`.
- ❌ accurate names and dates with no word on how ICW relates to them.
- **Shown by:** a judge holding `PRIOR-ART.md` checks each credit against
  it, checks each name comes with a relation, and flags any first or new.

## Sources

12 Nov: `runs/2026-11-12-readme-intent/CONTRACT.md` (fixed intents); for I8,
`runs/2026-11-12-front-door/CONTRACT.md` ("millennia old, with full respect
to prior art"), owner to confirm as his wording. 13 Nov: commit `52d397d`.
14 Nov: commits `887d598`, `a0af299`, `2315eba`; after review round 1,
`runs/2026-11-14-readme-intent-review/LOG.md`.
