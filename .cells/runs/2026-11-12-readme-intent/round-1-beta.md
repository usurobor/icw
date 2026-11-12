# Round 1 — β

Commit reviewed: `8fcc0c7fca68735cbb423a4bcb46fd2b28243fb5` (HEAD, clean tree).
Diff against BASE `2b155ac`: `intents/readme.md` only, 119 lines.
Not read: `skills/`, α's reasoning.

## Properties

| Q | Result | One line |
|---|---|---|
| Q1 Owner fidelity | pass | All four present, none weaker; I3/I4 stricter. Minors: "smart", unmarked α thresholds (B1-11). |
| Q2 Blind testability | **fail** | Judge is primed by the file itself; "paragraph one", "sentence" and "word" are underdefined; several verdicts hinge on unspecified judgment (B1-1 to B1-4). No skill is referred to. |
| Q3 Grounding | pass | All five exemplars exist and say what the file reports. Minors: none is a README; two fail the test they are cited for (B1-12). |
| Q4 Minimality | **fail** | One defect fails two or three intents; I1(c), I4(b) and I5 contradict each other (B1-5, B1-6). I1(d) is style (B1-13). |
| Q5 Gameability | **fail** | I1 passes on ingredients with no pull; I2 passes by copying E1–E3; a 145-word stub clears nearly everything (B1-1, B1-7, B1-8). |
| Q6 Reference answer | **fail** | No kernel contradiction, but it breaks the file's own cap and clarity rule, omits half of E3, and one sentence reads as settled what the last sentence denies (B1-9). In-file misreadings lose a READING carve-out (B1-10). |
| Q7 Size and scope | pass | 119 < 120; one file changed. No headroom (B1-14). |

## Blind run on the current README.md

Paragraph one, by the file's rule, is the 12-word bold line (README.md:3).

| Intent | Verdict | Rests on | Judgment the file does not specify |
|---|---|---|---|
| I1 | FAIL | (a) no case in the bold line; (c) no stake in it. (d) holds. | (b) "cannot settle at a glance"; whether "a whole" is everyday; (e) what a question "promises" and whether a test with no passing pair "delivers" it. |
| I2 | FAIL | Only E1 is in the bold line, and only half of it. (b) "carrying" used at :27 before :33. | Whether half of E1 counts. Read with the two paragraphs under it, E1 and E2 are conveyed and E3 is posed as a question: the paragraph-one rule alone decides. |
| I3 | FAIL | glider, witnesses, grue, Locke's atoms, microstate, Dennett's real patterns, all unexplained. | Whether "whole" is technical (decides the paragraph-one clause). Whether names in a credits list are "used to make a point". Whether table cells and bullets are sentences. |
| I4 | FAIL | Over 600 words on every count. | I get 620, 624 or 654 depending on tokens; α reports 652. Whether the Repository lines (READING, FINDINGS, tools) "point to the kernel, examples or credits". |
| I5 | **undetermined** | — | "Locke's same mass and united atoms" as coincident, "green and grue" as uncarried, the ship: none is in the kernel. Supported (the judge applies §6) or unsupported (no kernel item)? Pass or fail turns on it. |

Four verdicts are stable, though the evidence lists would differ between
judges. I5 is not stable.

## Findings

**B1-1 — major — Q2, Q5 — Ground rules "Reading order"; I2(a); I3(b).**
The reading order holds back the kernel so that "kernel knowledge cannot fill
gaps", but the judge has already read this file's reference answer, E1–E4 and
M1–M8, which are the kernel's idea in plain words. The restatement in I2(a) is
therefore written by a primed reader, and the match is made against quotes
from paragraph one, not against the restatement. Result: I2 tests whether the
elements are present, not whether a reader gets the idea. Constructed pass:
a paragraph one that copies E1–E3 nearly word for word (96 words, below)
passes I2, including the sentence "What decides is the whole's own changing,
not a viewer or a choice", which no newcomer could restate. The same priming
lets the judge paraphrase any sentence in I3(b).
*Required:* extend the reading order to this file: a first part the judge
reads (rules, what to write down), a marked stop, and the reference answer,
elements and misreadings below it, opened only after the paragraph-one answers
are written. Match E1–E3 against the judge's written restatement; quotes are
evidence, not the match.

**B1-2 — major — Q2 — Ground rules "Paragraph one".**
"First block of text after the title, whatever its form" is not decidable for
a heading, a list, a table, a blockquote of several paragraphs or raw HTML.
On semver.org, one of the file's own exemplars, the first block is either the
heading "Summary" or the line ending "increment the:". The rule also decides
I1 and I2 alone on the current README (see the run above). The owner's word
is "paragraph"; treating a tagline as the paragraph is α's choice and is not
marked as such.
*Required:* define it decidably (say what happens with headings, lists,
blockquotes; either a short line before the first prose paragraph is read
together with it, or it is not allowed) and mark the definition *proposed*.

**B1-3 — major — Q2, Q5 — Ground rules "Words"; I3(b); I4.**
(i) No token rule. Is `A < X > B` one word or five, `specs/ARTICULATION.md`
one or more, a list number a word, "(R5, proposed)" removed or kept? Three
defensible counts of the current README give 620, 624 and 654. A README near
600 gets opposite verdicts, and "same-wave/different-water" compounds hide
words from a whitespace count. (ii) I3(b) and I4(b) work on "every sentence",
but READMEs carry tables, bullets, headings and fragments, and the file does
not say whether they are sentences.
*Required:* one counting rule a script could implement; one definition of the
unit for I3(b) and I4(b).

**B1-4 — major — Q2 — I1, I2, I3, I5, Ground rules "Technical term".**
Verdict-deciding judgments with no rule:
(a) I5: verdicts on cases absent from the kernel (see the run). State whether
the judge applies §6 or fails them.
(b) Technical terms: the "always" list omits kernel words *whole, changing,
instant, coincide, elemental, pattern, cohering, rhythm*. "Whole" decides
I3's paragraph-one clause for the current README.
(c) "A named case or author used to make a point": does a credits list
qualify? If so, I3 and the I4 allowance for "earlier work" collide.
(d) I2(a): "assert or invite" a misreading. "Invite" has no test.
(e) I2(a): a partly conveyed element, or one conveyed as a question.
(f) I1(e): what counts as a promise, and whether a link delivers it.
(g) I1(b): "cannot settle at a glance".
*Required:* a rule or a worked tie-break for each, or delete the clause.

**B1-5 — major — Q4, Q2 — I1(c) against I4(b) and I5.**
I1(c) requires a stake in paragraph one. I4(b)'s closed list of what a
sentence may do has no entry for it, so the stake sentence is marked and I4
fails. The kernel states no stake, so under I5 it is either an unsupported
statement about ICW or out of scope and unchecked. A README cannot satisfy
all three as written; my own constructed README trips on it.
*Required:* add the stake to I4(b)'s list and say how I5 treats it (what a
stake may claim without a kernel item).

**B1-6 — major — Q4 — I1(b), I1(e), I2(b), I3, I5.**
Same defect, several intents: a term used before it is explained fails I2(b)
and I3(b) ("terms explained above it"); a misreading fails I2(a), I2(b) and
I5; an overpromise fails I1(e), I2(b) ("impression a later sentence must
correct") and I5; "everyday words" is tested in I1(b) and again in I3. AC4
says no two intents test the same thing.
*Required:* one home for each: term order in I3 only; misreadings and
overpromising in I5 only; I2(b) keeps only what is specific to unfolding, or
goes.

**B1-7 — major — Q5 — I1.**
The owner's intent is an effect (the visitor is drawn in). The test checks
ingredients. Passing example that draws nobody: "A post-office queue keeps
its place while the people in it are replaced. Is it the same queue? How
statements about queues are typed turns on the answer." (a) and (b) need not
concern the same thing, or ICW; (c) only requires that the judge can name
something that turns on it, not that a reader would care.
*Required:* tie the case to the question; require the stake quoted and of a
kind a non-specialist has reason to care about; add one reader-effect check
that survives the B1-1 seal (for example, the unprimed judge writes the
question they now want answered, and it must be the README's).

**B1-9 — major — Q6 — Reference answer, lines 85–99.**
(i) 123 words; 109 without the E4 sentence. The file's model of what
paragraph one conveys cannot fit the file's 100-word cap. (ii) E3 requires
"not a viewer or a choice"; the reference never says it. Reference and
elements disagree about what must be matched. (iii) "Two answers can hold at
once" reads as settled; the last sentence says no pair has passed the test
for having both. A non-specialist will see a contradiction, and I5's own rule
on declared items would flag it. (iv) "laid over it as a mere sorting", "hold
both up" and "pair" (no antecedent) would fail I3(b) as this file states it.
(v) "pattern travelling through the stuff" casts the stuff as the medium of
the pattern, the reading D2 excludes ("the material of another's") and M2
names; "travelling" is also wave-specific.
*Required:* make reference and E1–E3 say the same things; bring it within the
cap or state that it is not a model paragraph; separate "two ways of counting
exist" from "the whole has both" (open); replace the opaque phrases.
Not a kernel contradiction: the kernel Statement uses the same construction.

**B1-10 — major — Q2, Q6 — Ground rules "Misreadings" (α's protocol gap).**
Restating READING inside the file is the right resolution of the gap: it is
the only one consistent with AC2. M2, M3, M4, M5, M6 and M8 are faithful.
Faults:
(i) M1: "as a second cause" can be read as qualifying only "acts on". READING
1 says a sentence such as *the collision made these cells change state* can
be true, and that a glider can arise in time. A judge without READING can
fail true sentences.
(ii) M1 fails a README on R5 (*proposed*) and D12 (*declared*), while M6 is
report-only for being under review, and I5 forbids presenting proposed items
as settled. One rule for proposed items is needed.
(iii) Omitted: composition across the two ways ("a wave is made of water";
READING 1, R4); in M7, "X is greater than both" and carrying as a third term
behind the relation; the levels frame READING opens with.
*Required:* fix (i) and (ii); for (iii) either add them or point I5 at the
kernel's Nomenclature "Avoid" column, which the judge holds and which covers
level, part, state, real, view, emergence in one line.

**B1-8 — minor — Q5 — whole file.**
No floor on content. A 145-word README (the 96-word paragraph below plus
three sentences: ICW gives a test; its last check cannot yet be passed
because it is undefined; see the kernel) clears I2, I3 and I5 and fails I4
only through B1-5. Nothing requires the README to state the test or give a
next step. Not one of the owner's four intents, so not major; the owner
should decide whether to add a *proposed* intent or sharpen I1(e) to "in the
README itself".

> A wave crosses the sea, yet the water under it only bobs in place. So what
> counts as one thing in something that keeps changing, and what keeps it the
> same one? There is the same stuff (the water) and the same pattern through
> it (the wave): one wave passes through new water, and one patch of water is
> passed by wave after wave. Neither is ranked the real one. What decides is
> the whole's own changing, not a viewer or a choice. Whether a queue, a firm
> or you outlast your parts turns on this.

**B1-11 — minor — Q1 — I3 heading; "(owner)" labels; I1 pass; priority.**
(i) "smart non-specialist": the owner said "non-specialist". The pass
condition does not use the word, so not a blocker; delete it. (ii) I2 and I4
are labelled "(owner)" but the 100- and 600-word limits and the paragraph-one
rule are α's (α's log says so; the file does not). Mark them *proposed*.
(iii) Proposed check I1(c) sits inside the pass condition of an owner intent
at top priority; make it separable. (iv) The priority rule ranks, but no
overall verdict is defined.

**B1-12 — minor — Q3 — Grounding.**
Verified by search and fetch on 2026-11-12: Turing's opening sentence and the
replacement by the imitation game; Bostrom's abstract (101 words, three
propositions, "It follows that…"; *Phil. Quarterly* 53, 2003); semver.org
(50-word Summary, then Introduction, Specification, BNF grammar); Goh
(Distill, April 2017, both quoted phrases); Wikipedia lead. None invented or
misdescribed. But: (i) the set has no README of a theory or research
repository; (ii) Turing describes the game in paragraph two and Goh states
the stake in paragraph two, so both fail I1 as tested here ("title and
paragraph one only"), and Turing's first paragraph exceeds 100 words; (iii)
the semver.org page runs far past 600 words, so it does not support I4's
limit; (iv) no exemplar supports 100, 600 or I1(d). Either loosen the tests
to what the exemplars do, or say the tests are deliberately stricter.

**B1-13 — minor — Q4 — I1(d).** "No badge, image or banner" is style, and no
exemplar supports it. Drop it or state the outcome it protects.

**B1-14 — minor — Q7.** 119 of 120 lines. The changes above need room; the
overlap cuts in B1-6 and a shorter M list (B1-10 iii) would supply it.

## Counts

Blocker 0 · Major 9 (B1-1, B1-2, B1-3, B1-4, B1-5, B1-6, B1-7, B1-9, B1-10) ·
Minor 5 (B1-8, B1-11, B1-12, B1-13, B1-14).

## Verdict

**REQUEST CHANGES** on `8fcc0c7fca68735cbb423a4bcb46fd2b28243fb5`.
