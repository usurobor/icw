# Intent key: README (judge only)

Judge only. The judge holds this, the reader sheet `intents/readme.md`, the
README under test and the kernel (`specs/ARTICULATION.md`). *In force*:
proposed by the writer, counted until the owner changes it. *Reported*:
scored, not counted. **Owner to approve**: to ratify; in force meanwhile.

## Readers and running

- **Reader** (*in force*): a fresh general-purpose language model instance, or
  an adult, new to this repository, with no tools, files or web, told only
  the reader sheet. Three of one kind per run; the judge records which.
- **Administration.** The judge gives each reader the sheet, the title and
  the opening (rule below); collects A1–A3; gives the whole README as
  written; collects A4–A6. Readers never see others' answers, key or kernel.
- **Scoring** (*in force*): each reader is scored alone, flags never pooled.
  A reader-based clause passes if it passes for two of three. Verdicts quote
  their evidence. An A3 or A4 flag is discarded if the reader's guess is the
  meaning the text intends (per the README and kernel), if it is on the
  name ICW alone, or if it is outside the text that answer covers.
- **Opening** (*in force*): split the source after the title into blocks at
  blank lines; skip headings, images, badges, HTML, code and tables. The first
  block left is the opening; if under 25 words, the next block left is joined
  to it, once. Readers see at most its first 100 words.
- **Words**: runs of Unicode letters or digits (`[^\W_]+`) in the source minus
  link targets (`](...)`, `<http...>`); image text, transcribed, counts.
- **Overall**: pass when I1–I4 pass, *in force* clauses counted; I5 is
  *reported*. Failing I1 or I3 ranks below every README passing both.

## Calibration (owner to approve; before every run)

Each fixture is a README: `# Identity in Changing Wholes`, a blank line, the
fixture text. Per fixture, three fresh readers of the run's kind, used for
nothing else, do Step 1 on it as on a README; on F4 they also do Step 2. The
judge scores only the fixture's row and logs every answer verbatim. The run
is void unless every row holds for two of three readers by the stated
answer; failing another way does not count. If void, change the reader kind
or revise fixtures.

| Fixture | Must | By this answer |
|---|---|---|
| P | pass I1 Step 1, I2, I3 Step 1 | A2 yes, quoting P; A1 meets E1–E3, no I2 fault; no A3 flag counts |
| F1 | fail I1 Step 1 | A2 maybe or no, or its question only asks what a word, name or the project means |
| F2 | fail I2 | A1 has the wave emerge from, steer, or outrank the water |
| F3 | fail I3 Step 1 | an A3 flag counts (no guess, or a wrong one) |
| F4 | fail I4 | A5 quotes a unit of its second paragraph |

- P: the reference opening below.
- F1 (plain, accurate, dull): "This repository holds the specification of
  Identity in Changing Wholes, with worked examples, notes and two checking
  scripts. Each sits in its own folder: specs, examples, notes, tools."
- F2 (plain, engaging, wrong): "A wave crosses the sea while the water under
  it only bobs in place. So what is the wave? ICW's answer: it is a higher
  thing that emerges from the water, steers it, and is more real than water."
- F3 (accurate, jargon): the kernel's Statement, its three quoted paragraphs
  joined as one, without the `>` marks.
- F4 (padded): P, a blank line, then "In short, ICW is about what stays the
  same when things change. Water and waves each stay the same in their own
  way. ICW does not pick one as the real thing. Its test is not finished."

## Intents

**I1 Draws the visitor in** (owner). For a reader: (Step 1) A2 is yes, not
maybe; its question is one the opening raises about the subject, not about
what a word, name or the project means; its quoted words are in the opening.
(Step 2, *in force*) A6 gives an answer that is in the README and does not
say a case has passed, say both ways are real or carried, rank one as real,
or claim a result the kernel does not state. "It cannot be answered yet,
because ..." passes when the README says so and the kernel agrees; "none"
fails. Honesty can pass; overclaiming cannot. Kernel part: to I5 if approved.

**I2 Top-down: the opening alone gives the idea** (owner). For a reader, A1
says at least the minimum of E1–E3 below, in any words, and none of: the two
are mere views or descriptions, nothing in the thing behind them (calling
them two ways of counting or criteria is fine); one makes, causes or emerges
from the other; one is the real one; a case has passed; an element's
opposite.

**I3 Clear to a non-specialist ("your grandma")** (owner). (a) For a reader:
nothing in A3 (Step 1) or A4 (Step 2). (b) The judge finds no technical term
in the opening, and every one elsewhere explained at or before first use.
*Technical term*: a term the kernel defines, in the kernel's sense (*a whole*
and *the changing* as nouns are; everyday *pattern*, *order* are not);
notation; a term of logic, mathematics or philosophy a newspaper would gloss;
a person or case the reader must already know to follow the unit (not one
named only as credit). Not terms: ICW; kernel IDs and link targets where the
unit reads whole without them. *Explained*: in everyday or already
explained words, or pinned by a picturable case; a link is not. (b) backs up
A3 and A4.

**I4 Succinct** (owner). At most 600 words (*in force*, owner to approve);
for a reader, nothing in A5 (calibrated by F4; a clean A5 is weak evidence).

**I5 Faithful to the kernel** (*reported*; guards against overpromising). The
judge lists every statement about what ICW says, shows, refuses or leaves
open, with its supporting kernel item; motivation, history and other
authors are out of scope. Pass: every statement is supported (a case the
kernel does not discuss is supported if the §6 checks, run on the case as
stated, give the README's verdict; a case only named is unsupported); none
contradicts a kernel item, asserts what an *Excludes* clause shuts out, or
uses an *Avoid* word for its concept except to deny it; *proposed* or
*declared* items are marked unsettled; the README says the last check cannot
yet be passed, carrying being undefined (D8, O2, §6).

## Reference answer: opening P, 95 words (owner to approve)

> When something keeps changing, what counts as one thing, and what keeps it
> the same one? Two ways of staying the same can come apart. At sea, the same
> water is passed by wave after wave, and the same wave moves on through new
> water: each stays the same while the other changes. ICW does not call
> either one the real thing. Its test asks whether the sea's own movement
> keeps both going, or one is just a way of sorting it. The test's last step
> is unfinished, so nothing has passed yet.

Least an A1 must say. E1: a question about what counts as one thing, or what
keeps a thing the same, while it changes (either half). E2: two ways of
staying the same, by the stuff and by the pattern (named or by a case), that
come apart both ways (two cases or "both ways"; one direction does not). E3:
neither way is the real one (or mere talk), and ICW asks whether the thing's
own change keeps both going ("whether both belong to the thing itself" does;
"which is right" does not). E4 (I5 only): the last step is unfinished.

## Grounding

Explanations of the same kind, putting an idea to a reader who did not ask
(checked November 2026). They ground the moves; 100 and 600 are the owner's.

- Turing, "Computing Machinery and Intelligence" (*Mind*, 1950): "I propose
  to consider the question, 'Can machines think?'", then swaps it for a game
  one can picture: a question the reader owns, then a test (I1, I2).
- Bostrom, "Are You Living in a Computer Simulation?" (*Phil. Quarterly*,
  2003): a ~100-word abstract gives thesis and consequence, not proof (I2, I5).
- Semantic Versioning 2.0.0 (semver.org): a 50-word summary precedes the
  introduction, rules and grammar (I2, I4).
- Goh, "Why Momentum Really Works" (*Distill*, 2017): starts from a picture
  readers hold (a man walking down a hill) that "isn't wrong, but it fails to
  explain" key behaviour (I1).
- Wikipedia, "Ship of Theseus", lead: one plain sentence states the puzzle:
  is an object with all its parts replaced the same object? (I3).
