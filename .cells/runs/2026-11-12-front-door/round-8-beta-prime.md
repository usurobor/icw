# Round 8 — β′ review

Commit reviewed: b3a08345644e1d6e1327166f4fdcc048155a257c
Diffed against: 1006cb949766629eea51d4ea420137c471db014e (round 7). Base: 216a5d6.

Read this round: `log/round-8-alpha.md` only. HEAD matches; tree clean.

## Checks run

| Check | Result |
|---|---|
| `v_form.py` | pass (README 647/650, first screen 133/150, glider 490, limits 460, ship 472, wave 303) |
| `tools/lint.py` | 0 errors |
| Relative links and anchors | 24, all resolve |
| Scope vs base | README.md, PRIOR-ART.md, examples/*.md only |
| Re-wraps | README.md, glider.md, ship.md (and untouched wave.md, limits.md): whitespace-normalised text identical between 1006cb9 and b3a0834. Word-diff shows word changes in PRIOR-ART.md only, confined to the causal-persistence entry, the Lewis entry and the Lewis/Salmon reference order. |

## B7 resolution

| ID | Status | Check |
|---|---|---|
| B7-1 | resolved | Locator now sits on the pseudo-process clause: `pseudo-processes (Reichenbach's "unreal sequences", 1958, pp. 147–149)`. Matches SEP "Causal Processes". No longer reads as the mark criterion's locator. |
| B7-2 | resolved | Both quotations verbatim against the article text. "carve reality at the joints — and everywhere else as well": 10 words; source sentence "Properties carve reality at the joints -- and everywhere else as well." "does not make for resemblance among all its instances": 9 words; source sentence (5) "Grueness does not make for resemblance among all its instances.", which Lewis says is true. "He denies that grue is a universal" is supported by "A universal of grueness would be anathema". See B8-1 for a residual point on the first quotation's subject. |
| B7-3 | resolved | Lewis (1983) precedes Salmon (1984). Ragged paragraphs re-wrapped with no word changed. Remaining lines over 80 columns are table rows and link lines only. |

## P1–P9 on the changed text

All pass. The only content change is two PRIOR-ART.md entries; no kernel
claim, novelty claim, example or README sentence changed. Quotations exact
and under 15 words (P3). First-time-reader line unchanged: "I want to see
the test, and find out why it cannot yet tell a glider from grue."

## New findings

No blocker. No major. One minor.

**B8-1 — minor — P3 — PRIOR-ART.md, Lewis entry.**
"separates an elite minority of natural properties from the abundant rest,
which 'carve reality at the joints — and everywhere else as well'". In
Lewis the subject of "carve" is "Properties": all properties on the abundant
conception, natural ones included, which is why they carve at the joints
*and* everywhere else. The matter attaches the quotation to "the abundant
rest". The quotation is exact and the point Lewis draws from it (abundance
does not discriminate; the natural minority does) is what the entry reports.
*Change:* optional: "Properties in general, he says, 'carve reality at the
joints — and everywhere else as well'; he separates out an elite minority of
natural properties."

## Contract findings

C-1 … C-8 stand. Nothing new.

## Verdict

Verdict: APPROVE

On the matter at b3a0834: B7-1 … B7-3 resolved; no blocker or major; one new
minor (B8-1, optional). AC9 passes on this commit. Caveat unchanged:
dispositions of findings from rounds 1–5 are outside what I was allowed to
read.
