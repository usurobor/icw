# Protocol

How changes to this repository's public files are produced. Everything that
is not the product lives in `.cells/`.

## Layout

| Path | What |
|---|---|
| `intents/` | What the owner wants. Owner-ratified. |
| `skills/` | How to do a kind of work. Agent Skills format. |
| `runs/<date>-<name>/` | One cell run: contract, round files, log, receipt. |

Contracts, keys and fixtures live in the run that uses them. Promote one to its
own folder only when two runs share it.

## Cells

| Cell | Input | Output | Closes when |
|---|---|---|---|
| Planning | an intent | a contract: intent, acceptance spec, scope | β approves, calibration passes, owner ratifies |
| Working | a contract | the matter (e.g. the README) | β approves against the contract |
| Acceptance | a contract and the matter | PASS, FAIL or VOID, with evidence | β confirms the verdict followed the spec |

- **PASS**: the owner ships it. **FAIL**: back to Working, with the evidence.
  **VOID** (the test did not hold): back to Planning.
- An eval is an Acceptance run. Testing a skill means two Working runs, with
  and without it, through the same Acceptance cell.
- Acceptance shares no agent and no context with Working.

## Roles in a cell

- **α** produces. In Acceptance, α runs the spec and drafts the verdict;
  readers and judges are its instruments.
- **β** reviews α's output against the contract, adversarially, every
  property every round. β reports one verdict per property (pass, fail or
  void) with one line of evidence, and nothing else. In Acceptance, β audits
  how the verdict was reached.
- **Advisor** brings what the owner may be missing before the owner decides:
  two or three options for one decision, each with a one-line why and a
  one-line cost, plus anything the intent does not cover. Called at
  Planning, and when a verdict comes back void or with cause unknown. The
  advisor never writes matter and never reviews it. Its ideas reach the
  matter only through an owner decision recorded in the intent.
- **γ** dispatches, relays findings and keeps the log. γ does not edit matter.
- **δ** is a separate agent that validates the record against the contract
  and recommends to the owner. The owner decides.
- **ε** changes this file when a run exposes a fault in the protocol.

α and β are separate agents. β never sees α's reasoning, only its output
and dispositions. A final β on a different model is preferred.

## Rules

1. A round is one α commit and one β verdict. No round without β.
2. Every β finding gets an α disposition: fixed, or rejected with a reason β
   accepts.
3. Loosening a contract needs the owner's sign-off. γ may only record it.
4. Answers and transcripts are logged verbatim, by script, never summarised.
5. A test must show it can pass something and fail something before it is
   used. Calibration needs a known pass and a known fail on the same answer.
6. Do not measure "draws the visitor in" by same-model self-report.
7. Severity scales are incentives: form failures that a visitor would hit
   rank with accuracy failures.
8. A commit on `main` produced by a cell carries a trailer:
   `Cell-Run: .cells/runs/<id>`.

## History

- `runs/2026-11-12-front-door/`: produced the current README, `PRIOR-ART.md`
  and examples. Converged after 8 rounds; exposed rule 7.
- `runs/2026-11-12-readme-intent/`: planning run for the README intent. Did
  not converge; exposed rules 1, 3, 4, 5 and 6.
