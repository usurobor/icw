---
name: readme
description: Writes and reviews the ICW front page (README and linked example pages) so that it pulls a stranger in and a smart non-specialist ("your grandma") understands the idea from the first paragraph. Use when writing, rewriting or reviewing README.md, PRIOR-ART.md or examples/ in this repository.
metadata:
  version: "1.0.2"
  author: usurobor
  artifact_class: skill
  kata_surface: embedded
  governing_question: "How do we write a front page that a stranger reads past the first paragraph and understands without being taught?"
  triggers: "writing or rewriting a README; reviewing a README before publishing; a README that reads like a spec, a literature review or a manifesto"
  scope: task-local
  composes_with: "cnos write, cnos document (not yet in this repo)"
---

# README

*Version 1.0.2. ICW-specific; generalize later. Unproven: no acceptance run yet.*

## Core Principle

A coherent README carries a stranger from something they already know to the
whole idea in one paragraph, then answers, section by section, the next
question that paragraph raises, in words they already own.

This skill teaches how to write the front page of a repository so a smart
non-specialist reads on and understands. It owns two axes only: **pull** (the
reader keeps going) and **plainness** (the reader understands without being
taught). Prose coherence belongs to `write`. Claims checked against their
source belong to `document`. Apply both alongside this one.

READMEs fail when understanding them requires already understanding the work.

## Algorithm

1. Define: name the reader, the one idea, why it matters, and the familiar
   thing it starts from.
2. Unfold: hook, idea, stakes, one worked example, status, map.
3. Rules: apply 3.1–3.12.
4. Verify: run the tests in §4 before publishing.

---

## 1. Define

### 1.1. Name the reader

The reader is a smart adult who knows nothing about the field and owes you
nothing. Call this reader *grandma*. Write for her, not for a peer.

- ❌ "Readers familiar with sortal relativity will recognise…"
- ✅ "When a wave crosses the sea, the water mostly stays where it is."

### 1.2. Name the one idea

State the idea in one sentence a stranger could repeat. If it takes two, there
are two ideas, and the README leads with one.

- ❌ "ICW is a framework for articulation, carrying and cross-cutting criteria."
- ✅ "Two honest ways of counting the same thing can disagree, and that is not a contradiction."

### 1.3. Name why it matters

Name the question people already argue about that the idea changes. That is
the stakes. Without stakes the reader has no reason to continue.

- ❌ The README explains the idea and never says what it is for.
- ✅ "Most arguments ask which count is the real one. ICW says that question is malformed."

### 1.4. Name the familiar starting point

Find the case the reader has already seen: a river, a ship, a wave, a game.
The idea enters through it.

- ❌ Start from your terminology.
- ✅ Start from the thing your terminology describes.

---

## 2. Unfold

Order sections so each answers the question the one before it raised. Broad
first, narrow later; stop when the stranger has what they came for.

1. **Hook**: a familiar case with a puzzle in it.
2. **Idea**: the answer, in one sentence.
3. **Stakes**: which argument it changes.
4. **One worked example**: the idea applied once, step by step.
5. **Status**: what already works, then what is open.
6. **Map**: where to go next, one line per destination.

The first paragraph holds 1–3. A reader who stops after it has the idea.

- ❌ Question → glossary → table → credits → examples.
- ✅ Hook → idea → stakes → example → status → map.

---

## 3. Rules

### 3.1. Put the whole idea in paragraph one

Hook, answer and stakes, in five sentences or fewer. Everything after is
optional for the reader.

- ❌ Paragraph one asks the question; the answer arrives in section three.
- ✅ Paragraph one asks it, answers it and says why it matters.

### 3.2. Show the familiar case before the general claim

Give the instance first, then the abstraction, adjacent to it.

- ❌ "Criteria of identity can cross-cut. For example, a wave…"
- ✅ "A wave crosses the sea while its water stays put. Two ways of counting disagree."

### 3.3. Use plain words, and keep precision

Use the word grandma uses. Bring in a technical term only when no plain word
is as precise. Define it in the same sentence and use it right away.

- ❌ "A continuity is an equivalence relation on occurrences (D1)."
- ✅ "Call each way of counting a *criterion*: a rule for when two moments show the same thing."

### 3.4. Keep notation, IDs and jargon off the first screen

Symbols, spec IDs and coined terms belong after the reader has the idea.

- ❌ `A < X > B` and "(D9)" in the opening paragraph.
- ✅ The notation appears once, in the worked example, already explained in words.

### 3.5. Write sentences a reader can check

Prefer a concrete claim to an impressive one.

- ❌ "A powerful new framework for identity."
- ✅ "It rejects a pair of counts for one of three named reasons."

### 3.6. Say what it is, not what it is not

Disclaimers go in the status section, briefly. Don't build a section of them.

- ❌ A section titled "What this does not claim."
- ✅ "It does not yet say which pairs pass; that is the open problem."

### 3.7. Lead status with what works

Put what the idea already does before what is open. Then state the limits
plainly.

- ❌ "No pair has passed the test." (first thing a reader learns)
- ✅ "The test already rejects bad pairs. Its final step is still open."

### 3.8. Give each stable fact one home

Credits, specs, proofs and details live in their own files. The README names
them and links to them.

- ❌ Nine prior-art bullets and a reference list in the README.
- ✅ "The question is 2,500 years old; see PRIOR-ART.md for who asked it."

### 3.9. Credit the tradition in one line, early enough

Name the lineage so experts trust you and newcomers see the context. Then
move on.

- ❌ No mention of prior work, or a literature review before the idea.
- ✅ One sentence after the stakes, with a link.

### 3.10. Make it as short as it can be, but no shorter

Cut whatever a stranger would not miss. Keep whatever they would.

- ❌ Compressing the example until it no longer shows anything.
- ✅ One example, worked fully. The rest go behind links.

### 3.11. End with one door

Close on the single next step for a curious reader.

- ❌ A list of every file.
- ✅ "Start with the glider example."

### 3.12. Keep it true

Pull never justifies a claim the source does not make. Run `document`'s check.

- ❌ "ICW solves the Ship of Theseus."
- ✅ "ICW shows why 'which ship is the real one?' is the wrong question, if both counts pass."

---

## 4. Verify

### 4.1. Grandma test

Read only paragraph one to someone outside the field, or have a fresh
reviewer read it in that role. Ask them to restate the idea and to say why it
matters. If they can only restate the question, rule 3.1 failed.

### 4.2. Stop-anywhere test

Stop after paragraph one, after the first section, and after the example. At
each stopping point the reader should hold a complete, smaller version of the
idea, not a fragment.

### 4.3. Mechanical checks

- The first paragraph contains no spec IDs, no notation and no undefined coined
  terms.
- The first screen is about 150 words or fewer; the whole README is as short as
  §3.10 allows.
- No reference list; credits are linked.
- Every coined term is defined in the sentence where it first appears.

### 4.4. Truth check

Run `document`: every claim traces to the source of truth.

---

## 5. Kata

- **Scenario:** a theory repository whose README opens with a question,
  follows it with a glossary of spec terms, and ends with "what this does not
  claim."
- **Task:** rewrite paragraph one so it carries hook, idea and stakes.
- **Governing skills:** readme, write, document.
- **Inputs:** the current README and the spec it summarises.
- **Expected artifact:** a first paragraph of at most five sentences, plus the
  section order from §2.
- **Verification:** the grandma test (4.1) passes with a fresh reader; the
  mechanical checks (4.3) pass; the truth check (4.4) passes.
- **Common failures:** the answer arrives late; a technical term goes
  undefined; the status leads with what is missing; stakes are absent.
- **Reflection:** which sentence did the fresh reader repeat back? If it
  wasn't the idea, rewrite that sentence first.
