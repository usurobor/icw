# β review properties: README intent

Review `intents/readme.md` at a named commit against CONTRACT.md. Be
adversarial. Check every property every round.

- **Q1 Owner fidelity (AC1).** Are all four owner intents present and at least
  as strong? Was anything weakened by rewording? Are added intents marked
  proposed and justified? Any violation is a **blocker**.
- **Q2 Blind testability (AC2).** Could a fresh judge, holding only this file,
  a README and the kernel, run each test and reach the same verdict as another
  judge? Flag tests that need judgment the file does not specify. Any test
  that refers to a skill is a **blocker**.
- **Q3 Grounding (AC3).** Verify every cited exemplar by web search. Does each
  really achieve what the file says? Are they the same kind of project? Is
  the set best-in-class, or merely available? A wrong or invented exemplar is
  a **blocker**.
- **Q4 Minimality (AC4).** Do any two intents overlap? Is any intent style
  rather than outcome?
- **Q5 Gameability (AC5).** For each pass condition, try to construct a README
  that passes while failing the intent. If you can, that is **major**.
- **Q6 Reference answer (AC6).** Check against specs/ARTICULATION.md and every
  misreading in specs/READING.md. Would a non-specialist understand it? Is it
  specific enough that a wrong restatement would fail to match?
- **Q7 Size and scope (AC7, scope).** Under 120 lines; only
  `intents/readme.md` changed against BASE.

The criterion "best for our repo" is judged through Q1–Q6, not as a separate
impression.

## Severity
- **blocker:** violates owner fidelity, refers to a skill, misattributes an
  exemplar, or contradicts the kernel.
- **major:** a test cannot be run blind, a pass condition can be gamed,
  intents overlap, or the reference answer is vague.
- **minor:** wording, ordering.

## Verdict
APPROVE only with no open blocker or major findings and every earlier finding
resolved or its rejection accepted by you. Otherwise REQUEST CHANGES.
