# Round 2 — α

Commit: `f9fd515` (parent 8fcc0c7). Only `intents/readme.md` changed against
BASE. 119 lines.

## Design change

The file is now in two parts. **Part A** is a sheet for readers who are not
primed: they see only Part A and the README, first the title and opening,
then the whole, and they write A1–A6. **Part B** is for the judge only: the
running rules, intents, reference answer, elements and grounding. The judge
cuts the file at the Part B line. There are three readers, and a check
passes on two of three. I1–I4 are judged on what the readers wrote, so they
test effects rather than ingredients. The judge's own checks are mechanical
or anchored to the kernel: the opening rule, the word count, the
technical-term backstop, and I5. The in-file misreading list is gone; I5
points to the kernel's own *Excludes* clauses and its *Avoid* column, which
the judge holds.

Executable checks (script in /tmp/alpha/rules.py, not committed): on the
current README the opening rule gives the bold line joined to the next
paragraph (60 words), and the word rule gives 664 words. The reference answer
is 98 words by the same rule.

## Dispositions

| ID | Sev | Disposition | What changed |
|---|---|---|---|
| B1-1 | major | Fixed (design) | Readers see only Part A, never the reference answer, the elements or the rules. E1–E3 are matched against each reader's written A1, not against quotes from the opening. A README that copies the elements passes only if readers who were not primed restate them, and in that case the intent is met. Ideal fix needs a second file (gap G1). |
| B1-2 | major | Fixed | Opening rule, marked *proposed*: blocks split at blank lines; headings, images, badges, HTML, code and tables are skipped; a first block under 25 words is joined to the next one once; readers see at most 100 words. A script can implement it. A tagline is now read together with the paragraph after it, so the bold line alone no longer decides. |
| B1-3 | major | Fixed | (i) Words are regex matches of `[A-Za-z0-9]+` after link targets are removed; everything else counts. Compounds split, and `A < X > B` counts as three. (ii) A *unit* is a sentence, list item, table row or heading, defined in Part A. |
| B1-4 | major | Fixed | (a) I5: a verdict on a case the kernel does not discuss is supported if the §6 checks, run on that case, give the same verdict. (b) A technical term is any kernel-defined term used in the kernel's sense, with tie-breaks: *a whole* and *the changing* as nouns count; *pattern* and *order* in their everyday sense do not. (c) A name counts only if the reader must already know it to follow the unit, not when it is given as credit. (d) "Invite" is deleted, and misreadings now live only in I5. (e) Partial elements do not count; a question counts for E1 only. (f) "Promise" is replaced by A6: the README itself answers the reader's own question. (g) "Settle at a glance" is deleted. |
| B1-5 | major | Fixed (design) | The stake check I1(c) and I4's closed list are gone. I4 now flags redundancy through the readers (A5). I5 puts motivation outside its scope. No pair of checks contradicts. |
| B1-6 | major | Fixed | One home for each property. Term order is in I3(b) only. Misreadings, overpromising and proposed items are in I5 only. Plain words are tested in I3 only. Unfolding, I2(b), is removed: the owner defines top-down as "a reader who reads only the first paragraph gets the idea", and I2 tests exactly that. One defect can still fail two intents, such as jargon in the opening failing I2 and I3, but no two intents run the same check. |
| B1-7 | major | Fixed | I1 is now an effect test. The reader says whether they would read on and names the one question they want answered. The question must concern the subject and not ask what a word or the project means, the quoted trigger must be in the opening, and the README itself must answer it (A6). Your queue example fails if readers do not want the answer, or if the README does not answer it. The yes-bias of model readers remains (gap G3). |
| B1-8 | minor | Fixed via I1 | A6 means the README itself, not a link, must answer the question the opening raised. A 145-word stub that only points to the kernel fails I1. |
| B1-9 | major | Fixed | (i) The reference is 98 words, inside the cap, and is labelled a model opening. (ii) E1–E3 rewritten to say what the reference says; "not a viewer or a choice" is dropped. (iii) The reference separates two answers that disagree (the criteria) from whether the sea's own motion keeps both going (open, with the last step not yet worked out). (iv) "Laid over it as a mere sorting", "hold both up" and the bare "pair" are replaced by "a grouping the sea does nothing to keep up" and "no case has passed". (v) "Pattern travelling through the stuff" is replaced by "one wave keeps moving on into new water", as in examples/wave.md. Checked against READING 1–8. |
| B1-10 | major | Fixed (design) | The restated M1–M8 list is deleted, which removes the fidelity risk. I5 now uses the kernel's *Excludes* clauses, its *Avoid* column (level, part, state, real, view, emergence and so on), and a no-contradiction rule. That covers composition through D2 Excludes, carrying as a third term through D8 Type, and the R5 carve-out, since R5 itself says a cross-articulation causal claim "can be true". One rule now covers proposed items: if the only item that excludes a statement is *proposed*, the judge reports it instead of failing it. |
| B1-11 | minor | Fixed | (i) "Smart" is dropped, and the heading quotes the owner, "your grandma". (ii) The 100 and 600 limits and the opening rule are marked *proposed*. (iii) No proposed check sits inside an owner intent any more. (iv) Overall verdict: pass when I1–I4 pass; proposed checks are reported only; I1 and I3 decide the ranking. |
| B1-12 | minor | Partly fixed; partly rejected | (ii) Turing and Goh no longer fail I1, because I1 tests whether readers want to read on, not ingredients in paragraph one. Turing's first 100 words contain the question and the plan to replace it. (iii, iv) The file now says the exemplars ground the moves and that 100 and 600 are the owner's to set. (i) Rejected: AC3 allows "READMEs or explanations of the same kind". I did not find a theory-repository README I could verify as best-in-class, and I will not cite one I cannot verify. |
| B1-13 | minor | Fixed | I1(d) is deleted. Badges and images before the opening are skipped by the opening rule, so they are neither rewarded nor a style failure. |
| B1-14 | minor | Fixed, but no headroom | Deleting the M-list and the overlaps paid for Part A. The file is still 119 lines (gap G2). |

## Protocol gaps

- **G1, priming (B1-1): needs one change to the scope.** The seal in one file
  holds only if whoever spawns the readers cuts the file at the Part B line.
  If an agent is given the whole file it reads everything. Exact change:
  allow α to edit `intents/readme-key.md` as well, holding Part B's reference
  answer and E1–E4, and amend AC2 to "Readers hold only
  `intents/readme.md` and the README; the judge also holds
  `intents/readme-key.md` and the kernel."
- **G2, AC7 (120 lines) is binding.** A two-role protocol with mechanical rules
  fits only by compressing the rationale. Exact change: count AC7 over Part A
  plus Part B excluding Grounding, or raise the cap to 150 lines.
- **G3, AC2 says "a fresh reader-judge" in the singular.** This design uses
  three readers and one judge, all holding only the permitted materials.
  Exact change: AC2 to read "readers and a judge, holding only the intent
  file, the README and (judge only) the kernel". Model readers lean towards
  "yes" on A2. The owner may want a human reader for I1, or a calibration
  README known to be dull.
- The thresholds (opening rule, 25, 100 and 600 words, two of three readers)
  are α's choices, marked *proposed* where they bind, and the owner sets them.

## Round 2b (Amendment 1, G1)

Commit: `495a48e`. Part B (running rules, intents, reference
answer, elements, grounding) moved verbatim into `intents/readme-key.md`,
headed "judge only". `intents/readme.md` keeps the intro and Part A (the
reader sheet); the intro now names what each role receives: readers this
file and the README; the judge this file, `intents/readme-key.md`, the README
and the kernel. The cut line is removed. Nothing else changed. Sizes: 24 and
97 lines (Grounding included in the 97).
