# Round 3 — α

Commit: `67a2515` (parent 495a48e). Changed against BASE: `intents/readme.md`
(29 lines) and `intents/readme-key.md` (130 lines, 113 excluding Grounding).
Together that is 142 lines excluding Grounding, under the 150 set by
Amendment 2.

## Design

The intents are unchanged. What changed is how readers are run and scored:

- **Reader and administration.** The key now says who a reader is: a fresh
  model instance with no tools, files or web access, or an adult new to the
  repository with no such access. Each reader is told nothing but the sheet.
  The run is staged: the judge shows the title and opening, collects A1–A3,
  then gives the whole README and collects A4–A6.
- **Calibration** (Amendment 2 C-1). Before scoring, six separate fresh
  readers do Step 1: three on P, the reference opening, which must pass I2
  and the Step 1 clauses of I1 and I3, and three on F, the kernel's Statement
  block, which must fail all three. If the panel cannot tell P from F, the run
  is void. F is accurate but abstract and full of jargon, so it tests whether
  readers will say "yes, I'd read on" to anything, and whether they will claim
  to understand jargon.
- **Simplifications.** A6 is now one open question instead of yes/no. Flags
  are scored per reader, never pooled.

## Dispositions

| ID | Sev | Disposition | What changed |
|---|---|---|---|
| B2-1 | major | Fixed | Key "Readers and running" now specifies the reader kind and the staged administration: who shows what, in which order, and what readers never see. It adds calibration on fixtures P (must pass) and F (must fail), using separate instances so the README's readers are not primed. If either fixture goes the wrong way, the run is void. A panel that says yes to anything fails on F, and that answers your queue example. |
| B2-2 | major | Fixed | (i) A1 now allows four sentences and asks the reader to "put down everything you took from it", which asks for completeness without leading. The key gives the least each element needs, with examples of what does and does not count. P must pass I2 in calibration, which shows the model opening meets its own test or voids the run. (ii) E1: either half suffices, and the key says so. (iii) I2 fails an A1 that treats the two as views or descriptions, has one make, cause or emerge from the other, ranks one as real, says a case has passed, or states the opposite of an element. This checks what the reader took away; I5 checks what the README states, so the two still test different things. |
| B2-3 | major | Fixed | One rule: each reader is scored alone, flags are never pooled, and a clause passes for at least two of three readers. Marked *proposed*, as is the 25-word join inside the *proposed* opening rule. |
| B2-4 | major | Fixed | Words are maximal runs of Unicode letters or digits (`[^\W_]+`). Checked: Cyrillic, accented and possessive forms count as 2, 1 and 2 as expected. Text inside images is transcribed by the judge and counted, and alt text counts. |
| B2-5 | major | Fixed (design) | A6 now asks what answer the README itself gave. An honest "cannot be answered yet, because …" passes when the README says so and the kernel agrees. An answer fails I1 if it says a case has passed, ranks one way as the real one, or contradicts a kernel item, and "none" fails. That check is counted inside I1 and does not wait on I5, so overclaiming cannot buy pull. The A6 clause is marked *proposed*. I2 also fails an opening that leads readers to say a case has passed. |
| B2-6 | minor | Fixed | The sheet says readers hand in A1–A3 before they see more, and that the whole README is then given to them. The key's administration says the same. A5 excludes headings. |
| B2-7 | minor | Fixed | The key's reader definition says readers have no tools, files or web access. The sheet names the key only to say readers never receive it. |
| B2-8 | minor | Fixed | A case that is only named, not stated, is unsupported. If the only excluding item is *proposed* or *declared* (for example D12 and "emergence"), I5 reports rather than fails. |

## Protocol gaps

- **Calibration not yet run.** Only the run itself shows whether P passes and
  F fails with a given reader kind. I am primed and cannot act as a fresh
  reader. The first real run should be a calibration-only run. If P fails, the
  owner revises P, which is already marked "owner to approve".
- **F is the owner's to ratify** as the "known fail", just as P is the known
  pass.
- The *proposed* numbers (25, 100 and 600 words, two of three readers) still
  wait on the owner.
