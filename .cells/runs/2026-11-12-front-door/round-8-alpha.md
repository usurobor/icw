# Round 8 — α

Commit: `b3a08345644e1d6e1327166f4fdcc048155a257c` (parent `1006cb9`). Diff:
PRIOR-ART.md, README.md, examples/glider.md and examples/ship.md.

- Content changes are confined to the PRIOR-ART causal-persistence entry,
  the Lewis entry, and the reference order.
- The README and examples are re-wrapped only. The words are unchanged
  (v_form counts are identical to round 7).

`python3 tools/lint.py`: 0 errors. 24 relative links, all resolving.

## v_form.py output

```
ok    README words 647 <= 650
ok    README first screen words 133 <= 150
ok    README has no reference list (credits live in PRIOR-ART.md)
ok    PRIOR-ART.md exists and README links to it
ok    glider.md words 490 <= 500
ok    limits.md words 460 <= 500
ok    ship.md words 472 <= 500
ok    wave.md words 303 <= 500
```

## Dispositions

| ID | Disposition | What was done |
|---|---|---|
| B7-1 | fixed | The locator moved to the pseudo-process clause: "A mark criterion that Salmon (1984) takes from Reichenbach separates causal processes from pseudo-processes (Reichenbach's "unreal sequences", 1958, pp. 147–149), such as a moving spot of light …". It no longer reads as the mark criterion's locator. |
| B7-2 | fixed | Both glosses are replaced by Lewis's own words, quoted exactly as verified in the article text, each under 15 words. The entry now reads: "separates an elite minority of natural properties from the abundant rest, which 'carve reality at the joints — and everywhere else as well'. He denies that grue is a universal: grueness 'does not make for resemblance among all its instances'." No gloss is presented as his words. |
| B7-3 | fixed | Lewis (1983) now comes before Salmon (1984) in References. Ragged and over-width paragraphs are re-wrapped at 78 columns with words unchanged: README first paragraph; PRIOR-ART causal-persistence, Dennett and Lewis entries, the "Most of the structure" paragraph, and additions #1 and #2; glider.md "made of cells" and "collision"; ship.md "made of planks". |

## New protocol gaps

None.

## Post-cap disposition

| B8-1 | accept-and-defer | β′ is right that Lewis's subject for "carve reality at the joints — and everywhere else as well" is properties in general, not only the abundant non-natural ones. The quote and the reported point are exact. Next edit to PRIOR-ART.md, fix the attachment using β′'s wording; the round cap bars any matter change now. |
