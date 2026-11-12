# Cell contract: ICW front door

## Goal

Make the public face of the Identity in Changing Wholes (ICW) repository —
`README.md` and `examples/*.md` — clear, accurate and compelling to a first-time
visitor, written as a contribution to a conversation about identity through
change that is millennia old, with full respect to prior art.

## Matter in scope (α may edit)

- `README.md`
- `examples/*.md` (may add, remove, rename, or merge example files)

## Read-only (α must not edit)

- `specs/ARTICULATION.md` — the kernel. The only authoritative file.
- `specs/READING.md` — misreadings the kernel excludes.
- `notes/FINDINGS.md` — working notes.
- `tools/*`

If α believes a read-only file is wrong, α records it as a **protocol gap** in
the round file. α does not edit it.

## Acceptance criteria

- **AC1 Hook.** The first screen of the README states the question ICW asks and
  pulls a non-specialist in.
- **AC2 Tradition.** ICW is presented as additive to a long conversation (e.g.
  Heraclitus, Theseus's ship, Locke, sortal/relative identity, Quine, Dennett,
  genidentity), with prior art credited accurately, and with ICW's novelty
  claims limited to what prior art does not already contain.
- **AC3 Canonical examples only.** Every example is a widely known
  philosophical, physical or computational case. No niche or invented cases.
- **AC4 Kernel fidelity.** No claim in README or examples goes beyond
  `specs/ARTICULATION.md`. Proposed results are marked as proposed. No pair is
  said to *hold* (co-articulate) while carrying (D8, O2) is undefined.
- **AC5 Misreadings.** Nothing in the matter commits any misreading listed in
  `specs/READING.md`, or reads *carried* as *real*.
- **AC6 Clarity and compression.** A careful non-specialist can follow it.
  Terms are defined before use. No filler.
- **AC7 Footprint.** As small as the goal allows. No mention of any
  predecessor project.
- **AC8 Mechanics.** `python3 tools/lint.py` reports 0 errors. Every relative
  link resolves. `A < X > B` is always written spaced or in code.

## Non-goals

- Changing the theory. Resolving O2. Adding new results.
- Styling beyond plain Markdown.

## Convergence

The cell closes when β returns **APPROVE** on a specific commit, with no open
blocker or major findings, and every finding from every round has an α
disposition (fixed, or rejected with a reason β accepted). Maximum 6 rounds.

---

## Amendment 1 (ε, after round 5)

*Why.* Rounds 1–5 converged on accuracy while the README grew from ~700 to
~2,000 words: every novelty or credit finding was answered by adding prior art,
and form defects could not block approval. This amendment makes form
mechanically checkable and gives credit a home outside the README.

- **Scope.** α may also create and edit `PRIOR-ART.md` at the repository root.
- **AC9 Form caps (mechanical).** `python3 /home/claude/icw-cell/v_form.py
  /home/claude/icw-cell/repo` passes: README ≤ 650 prose words; README text
  before the first `##` heading ≤ 150 words; no reference list in the README;
  `PRIOR-ART.md` exists and is linked from the README; each example ≤ 500
  words.
- **Credit lives in PRIOR-ART.md.** Full attributions, locators and the
  "what ICW adds relative to each" discussion go there. The README names the
  tradition briefly and links to it. Accuracy requirements (AC2, AC4, AC5)
  are unchanged and apply to PRIOR-ART.md too.
- **No accretion.** A finding about credit or novelty is resolved by changing
  or moving text, not by adding to the README past the caps.
- **Convergence** now also requires AC9 to pass on the approved commit.

## Amendment 2 (δ, during round 7)

- **Round cap** raised from 6 to 8 for this cell. Reason: Amendment 1 landed
  after round 5, leaving one round for a REQUEST CHANGES to converge (β′
  finding C-2). Recorded here in response to C-8, which noted the cap had
  been set aside only in the log.
