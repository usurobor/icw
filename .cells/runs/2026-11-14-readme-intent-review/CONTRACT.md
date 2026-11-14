# Contract: review of the README intent

- **Matter:** `.cells/intents/readme.md` at the commit in `BASE`.
- **Owner's words:** the intent's "Owner decisions" sections (13 Nov, 14 Nov) and the four fixed intents in `runs/2026-11-12-readme-intent/CONTRACT.md`.
- **Kernel:** `specs/ARTICULATION.md`, `specs/READING.md`.
- **Producer skill:** none.

## Properties

| ID | Property | Shown by | Severity if failed |
|---|---|---|---|
| P1 | Owner fidelity: every owner decision and fixed intent is present and no weaker; anything Claude added is marked proposed. | Line-by-line comparison against the owner's words. | blocker |
| P2 | Purpose only: the intent states outcomes; how the README gets there belongs to the planning cell (the intent's own header). | List every line that prescribes method, order or wording. | major |
| P3 | Blind testability: each property's "shown by" can be run by a fresh judge holding only this file, a README and the kernel, and two judges reach the same verdict. | For each, state what the judge does and where judgment is unspecified. | major |
| P4 | Minimality: no two properties overlap; none is style rather than outcome. | Pairwise check. | major |
| P5 | Gameability: no test can be passed by a README that misses the property's purpose. | Construct a passing-but-failing README per property. | major |
| P6 | Truth: every claim about ICW agrees with the kernel, including the 14 Nov snapshot and sequence criteria. | Check each against `specs/ARTICULATION.md` and `specs/READING.md`. | blocker |
| P7 | Internal consistency: no two sections contradict each other. | Cross-check sections, including the 13 Nov and 14 Nov decisions. | major |
| P8 | Size: at most 120 lines (the bar set by the 12 Nov intent run). | `wc -l`. | major |
