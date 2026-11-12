# Round 7 — β′ review

Commit reviewed: 1006cb949766629eea51d4ea420137c471db014e
Diffed against: 01f1e3b5a9cb3916fbf5a1bec1eed30343a2e695 (round 6). Base: 216a5d6.

Read this round: `log/round-7-alpha.md` only (plus BASE). HEAD matches; tree clean.

## Checks run

| Check | Result |
|---|---|
| `v_form.py` | pass (README 647/650, first screen 133/150, glider 490, limits 460, ship 472, wave 303) |
| `tools/lint.py` | 0 errors |
| Relative links and anchors | 24, all resolve |
| Scope vs base | README.md, PRIOR-ART.md, examples/*.md only |
| Round-7 diff | 5 files; limits.md untouched; no read-only file touched |

## B6 resolution

| ID | Status | Check |
|---|---|---|
| B6-1 | resolved | Both places now say "physical level" / "design level", Dennett's own terms (confirmed last round against the article). |
| B6-2 | resolved | ship.md credits Plutarch and Hobbes with the cases only; says the second witness holds under the stipulated through-repair criterion and that on Hobbes's answer the rebuilt ship is the same ship; says the plank/ship pair does not adjudicate between the two ship criteria. Consistent with Hobbes II.11.7 as verified last round. |
| B6-3 | resolved | wave.md fixes the criterion to one crest for as long as it lasts; witnesses use crests. The added fact (crests outrun the group, appear at its back, fade at its front) is correct for deep water. README hook no longer has a wave crossing the sea. |
| B6-4 | resolved | D7 now attached only to the cell/glider claim; arrangement step carries no kernel ID; "fixes which glider" gone. |
| B6-5 | resolved | Russell: "New York: Simon and Schuster" matches the SEP bibliography whose pagination the locators follow. Reichenbach 1958, *The Philosophy of Space and Time*, New York: Dover, pp. 147–149 on "unreal sequences": matches SEP "Causal Processes" (three citations). See B7-1 for a residual wording point. |
| B6-6 | resolved; Hirsch rejection accepted | Lewis verified in the article text: "an élite minority of special properties" called natural properties; "Properties carve reality at the joints — and everywhere else as well" (said of abundant properties); grue listed among non-universals, "Grueness does not make for resemblance among all its instances". AJP 61(4), December 1983, from p. 343. The Hirsch credit was optional and I had not verified its specific claim either; declining to cite what could not be checked is the right call. No README text added. |
| B6-7 | resolved | README: "what happens in its changing". glider.md: "Site labels do not privilege the cell criterion (A1, proposed)", which is what A1 says. |

## P1–P9 on the changed text

All pass. No new kernel claim; proposed markers intact (A1, R4, R5); no pair
said to hold; no ranking, agentive or carried-as-real phrasing introduced;
"nothing in the test ranks criteria (R3)" is within R3. The Lewis credit sits
in PRIOR-ART.md only, and addition 2 still claims placement alone. README
first screen unchanged in substance; first-time-reader line stands: "I want
to see the test, and find out why it cannot yet tell a glider from grue."

## New findings

No blocker. No major. Three minor.

**B7-1 — minor — P3 — PRIOR-ART.md, Causal persistence entry.**
"A mark criterion that Salmon (1984) takes from Reichenbach (1958, pp.
147–149, on 'unreal sequences')". The pages are where Reichenbach treats
unreal sequences; the source I could check does not place the mark criterion
itself there. The qualifier keeps it honest, but the parenthesis still reads
as the criterion's locator.
*Change:* move the locator to the pseudo-process clause: "pseudo-processes
(Reichenbach's 'unreal sequences', 1958, pp. 147–149)".

**B7-2 — minor — P3 — PRIOR-ART.md, Lewis entry.**
"natural properties, which carve at the joints" attaches to the natural
properties a phrase Lewis uses of the abundant ones ("at the joints — and
everywhere else as well"); and "does not count grue among them" is his
implication (grue is no universal, makes for no resemblance), not a
statement. Both are fair glosses, not quotations, and are not presented as
quotations.
*Change:* optional: "which alone carve only at the joints" and "treats grue
as no such property".

**B7-3 — minor — P8 — PRIOR-ART.md references; line wrapping.**
Lewis (1983) is listed after Salmon (1984) in an otherwise chronological
list. Several edited paragraphs are left ragged ("moves. Every" /
"different glider. If" / "ICW's addition is the"), and one README line
runs past the wrap width.
*Change:* reorder; rewrap.

## Contract findings

C-1 … C-7 from round 6 stand unchanged. One addition:

**C-8 — Round 7 exceeds "Maximum 6 rounds".** The cell continued past its
own cap without an amendment saying so. The outcome is better for it, which
is the point: the cap was the wrong rule (C-2), and it was set aside
informally by the party that validates.

## Verdict

Verdict: APPROVE

On the matter at 1006cb9: all seven B6 findings resolved, Hirsch rejection
accepted, no blocker or major, three new minor. AC9 passes on this commit.
Caveat unchanged: dispositions of findings from rounds 1–5 are outside what
I was allowed to read.
