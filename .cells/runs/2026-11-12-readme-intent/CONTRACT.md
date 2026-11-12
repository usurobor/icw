# Cell contract: README intent

## Goal

Produce `intents/readme.md`: the owner's definition of what the ICW README
must achieve, written so that a judge who has never seen any skill can test a
README against it. It will be used to evaluate README-writing skills, so it
must not be derived from any skill.

## Seed

`intents/readme.md` at the commit in log/BASE + 1 (also at
/home/claude/intent-cell/SEED-intent.md). Drafted by the orchestrator. α may
converge on it as is, or iterate.

## Owner's stated intents (fixed)

The owner stated four intents. They may be sharpened, given better tests, or
split, but not dropped, weakened or replaced:

1. Draw the visitor in.
2. Top-down unfolding: a reader who reads only the first paragraph gets the
   idea.
3. Clarity, even for a non-specialist ("your grandma"). Highest priority,
   with 1.
4. Succinct.

## Scope

α may edit only `intents/readme.md` in /home/claude/intent-cell/repo.
Read-only: everything else, including specs/ARTICULATION.md (the kernel),
specs/READING.md, README.md, skills/.

## Acceptance criteria

- **AC1 Owner fidelity.** All four stated intents are present, at least as
  strong as stated. Added intents are marked *proposed* with a one-line
  reason.
- **AC2 Testable blind.** Each intent has a test a fresh reader-judge can run
  with only the intent file, the README under test and the kernel. Each has an
  explicit pass condition. No test refers to a skill.
- **AC3 Benchmarked.** The intents are justified against at least three
  best-in-class READMEs or explanations of the same kind (theory, research or
  idea-first projects), each verified by web search, with one line on what
  each achieves that an intent encodes. Put these in a short "Grounding"
  section.
- **AC4 Minimal.** No two intents test the same thing. Nothing that is mere
  style.
- **AC5 Not gameable.** No pass condition can be met trivially (for example by
  hiding words from a counter, or by a reference answer vague enough to match
  anything).
- **AC6 Reference answer.** The R2 reference answer is faithful to the kernel
  (no misreading in specs/READING.md), plain enough for a non-specialist, and
  marked "owner to approve".
- **AC7 Small.** The file stays under 120 lines.

## Convergence

The cell closes when β returns APPROVE on a named commit, with no open
blocker or major findings, and every finding has an α disposition. At most 5
rounds. The δ agent then validates the record against this contract and
recommends accept or reject to the owner, who decides.

---

## Amendment 1 (after round 2; requested by α as protocol gaps G1–G3)

- **G1 Scope.** α may also create `intents/readme-key.md`, the judge-only
  answer key (rules, reference answer, elements). Readers receive only
  `intents/readme.md` and the README; the separation must be structural, not
  a cut line inside one file.
- **G2 Size.** AC7 becomes: each file under 120 lines, excluding the
  Grounding section.
- **G3 Judges.** AC2 is read as: tests may use several fresh readers plus one
  judge, provided each role's inputs are specified and none of them sees a
  skill.
- β reviews this amendment for consistency alongside the matter.

## Amendment 2 (after β round 2, contract findings C-1 to C-4)

- **C-1 Calibration.** Any test that uses readers must specify the reader
  (who or what, and what they are told), who shows them what and in which
  order, and must include a calibration step: before scoring, the panel is
  given one opening known to pass and one known to fail, and the run is void
  if it does not tell them apart.
- **C-2 Size.** Combined, the two files stay under 150 lines excluding
  Grounding (replaces Amendment 1's per-file 120).
- **C-3 Wording.** Where the Goal, AC2 and Q2 speak of "a reader-judge", read
  "the roles specified in the files". AC6's "R2" means the top-down intent,
  whatever its ID.
- **C-4 Ratification.** Amendments 1 and 2 relax or change acceptance
  criteria. They are provisional until the owner ratifies them at δ; δ must
  list them for the owner.

## Amendment 3 (after β round 3, contract finding C-5)

- **C-5 Calibration must run.** Before β may APPROVE, γ runs one logged,
  calibration-only run with fresh readers who have not seen either intent
  file's key, and a fresh judge, exactly as the key specifies. Its result is
  matter for β. If the known-pass opening does not pass, or a known-fail does
  not fail for its stated reason, the cell cannot close.
- **Known fails per intent.** Each reader-based intent has its own known-fail
  opening, failing for that intent's reason.
- **Q7 wording.** Read "only the files in scope under the amendments changed".
