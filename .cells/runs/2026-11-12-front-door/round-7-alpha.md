# Round 7 — α

Commit: `1006cb949766629eea51d4ea420137c471db014e`. The fixes are in
`dcf1c71`; `1006cb9` only re-wraps one line in PRIOR-ART.md. Against base
`216a5d6`, only README.md, PRIOR-ART.md and examples/*.md changed.
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
| B6-1 | fixed | glider.md and PRIOR-ART.md now use Dennett's terms: "at what he calls the physical level, the cells and their rule, nothing moves; at the design level one and the same glider moves." |
| B6-2 | fixed (must-fix) | ship.md says the cases are Plutarch's and Hobbes's. The second witness ("same plank, different ships") is said to hold under the ship criterion as stipulated, through repair. On Hobbes's own answer ("ship" signifies matter so shaped), the rebuilt ship is the same ship. Hobbes is no longer credited with that witness. The "Which ship" paragraph now says Hobbes's puzzle sets two candidate *ship* criteria against each other (through repair; same matter so shaped). The plank/ship pair does not adjudicate between them, and within the example the ship criterion is stipulated. |
| B6-3 | fixed | wave.md fixes the criterion to one crest, followed for as long as it lasts. It adds the deep-water fact that single crests outrun the swell, rising at its back and fading at its front. The witnesses now read "different crests" / "same crest". The README hook no longer says a wave crosses the sea: "A wave runs across deep water". |
| B6-4 | fixed | glider.md: D7 is cited only for "cell-sameness is not what makes it the same glider". The arrangement step is phrased "Nor is cell-sameness with arrangement", with the same-sites-same-phase witness and no kernel ID. "Fixes which glider" is removed. |
| B6-5 | fixed | Russell now carries "New York: Simon and Schuster" (publisher of the 1948 edition, confirmed). Genidentity now reads "Reichenbach (1956) took it up". The mark criterion now gives Reichenbach's work and locator: "(1958, pp. 147–149, on 'unreal sequences')". The reference added is *The Philosophy of Space and Time* (Dover, 1958; translation of the 1928 *Philosophie der Raum-Zeit-Lehre*). The locator is as cited in SEP *Causal Processes*. |
| B6-6 | fixed for Lewis; Hirsch rejected | **Lewis:** verified from the text of "New Work for a Theory of Universals". He posits "an elite minority of special properties … the natural properties". He says abundant properties carve "at the joints — and everywhere else as well". He rejects grue as a universal. Bibliographic details are confirmed (AJP 61(4): 343–377). He is credited in PRIOR-ART's conversation and in addition #2. No README text was added. **Hirsch:** not cited. I could confirm only that *The Concept of Identity* (OUP 1982) analyses identity through continuity under a sortal. I could not verify the specific claim about unified vs gerrymandered persistence conditions. |
| B6-7 | fixed | (a) README now reads "occurrences are what happens in its changing". (b) glider.md now reads "Site labels do not privilege the cell criterion (A1, proposed)." |

## New protocol gaps

None.
