# Blind comparison: results (pilot, 18 Nov)

Pre-registration: `2026-11-18-blind-comparison.md`. Answers: `answers/`.
Packets, keys and verbatim verdicts: `judging/`. Scoring: `tools/experiments/score.py`
(`judging/results/score-*.txt`). Keys were released only after all verdicts
on that family were logged; their sha256 hashes were committed first (dff3ace).

## Results under the frozen rule

| | GPT answers, Claude judges | Claude answers, GPT judges |
|---|---|---|
| Agreement between orders (need ≥ 70%) | 69%: **inconclusive** | 78% |
| B beats C, forced choice, P+U (need ≥ 60%) | 15/16 | 11/16 |
| R-1 to R-3, B − C (need ≥ +0.30) | +1.00 | +0.57 |
| R-4 overclaiming, B − C (need ≥ 0) | 0.00 | −0.19: **fails** |
| ICW helps | (inconclusive) | **no** |
| B loses to A on controls, forced choice | 1/8 | 2/8 |
| R-5 plainness on controls, B − A | −1.00 | −0.19 |
| ICW hurts on controls (frozen clause) | (inconclusive) | **yes** |

## Reading

- By the frozen rule, the pilot gives no support for "ICW helps". The one
  conclusive half fails on overclaiming and trips the controls clause on
  plainness.
- Most of B's advantage over no instruction is an effect of any instruction:
  the placebo beat no instruction in 14 of 16 pairs on Claude's answers.
- B's clear lead is on R-1 to R-3, the items closest to its own vocabulary.
- Design faults, for the next version: the forced choice came after the
  rubric, so the rubric primed it; R-4 sat at the ceiling for GPT's answers;
  twelve prompts, one run per condition; position effects were large between
  the two Claude judges (placebo against none: 7/8 in one order, 1/8 in the
  other).

## Next version

Forced choice first, then the rubric; a rubric without ICW vocabulary (or
judged only on correctness and overclaiming); at least 40 prompts written
outside the project; several runs per condition.
