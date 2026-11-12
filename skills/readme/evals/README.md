# Evals for `readme`

Not yet run. Each scenario is run twice, with and without the skill, by a
writer who has not seen the other run. A fresh reader, blind to which is
which, scores both.

## Scenarios

1. **ICW front page.** Input: `specs/ARTICULATION.md` and the current
   `README.md`. Task: rewrite the README.
2. **One example page.** Input: the kernel and `examples/glider.md`. Task:
   rewrite the example for a non-specialist.
3. **Paragraph one only.** Input: the kernel. Task: write the README's first
   paragraph, at most five sentences.

## Scoring (per output)

- **Grandma test (4.1):** from paragraph one alone, can the reader restate the
  idea, and why it matters? 0 / 1 / 2.
- **Stop-anywhere (4.2):** after paragraph one, the first section and the
  example, does the reader hold a complete smaller version? 0–3.
- **Mechanical (4.3):** no IDs or notation in paragraph one; first screen
  ≤ 150 words; no reference list; terms defined where first used. Pass/fail.
- **Truth (4.4):** every claim traces to the kernel. Pass/fail.

The skill earns its version only if the with-skill runs beat the baseline on
the grandma test across all three scenarios.
