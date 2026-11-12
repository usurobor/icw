# Round 6 — β′ review (fresh reviewer, no earlier rounds read)

Commit reviewed: 01f1e3b5a9cb3916fbf5a1bec1eed30343a2e695
Base: 216a5d6b3b03a7c44655ad9ac3f3b4f00e95b9a2

HEAD is that commit; tree clean. I read CONTRACT.md, REVIEW-PROPERTIES.md,
the three read-only files and the matter. I opened nothing in `log/` except
BASE, so I cannot attest that earlier findings have dispositions (see C-2).

## Checks run

| Check | Result |
|---|---|
| `v_form.py` | pass, all 8 lines ok (README 647/650, first screen 133/150, glider 494/500, limits 460, ship 412, wave 264) |
| `tools/lint.py` | 0 errors |
| Relative links and anchors (24, incl. `#two-ways-of-counting`) | all resolve |
| `git diff --stat BASE 01f1e3b` | PRIOR-ART.md, README.md, examples/{glider,limits,ship,wave}.md only; no read-only file touched |
| `A < X > B` notation | always in code, spaced |
| Predecessor mentions in matter | none |
| Glider facts (simulated) | 5 cells, period 4, shift (1,1); disjoint from start at step 16 (already at 8 and 12) |

## P9 first-time-reader line

"I want to see the test, and find out why it cannot yet tell a glider from
grue: what would 'carried' have to mean?"

## Properties

| P | Result | Why |
|---|---|---|
| P1 Kernel fidelity | pass | IDs exist and say what is claimed; A1, R4, R5 marked proposed everywhere; no pair said to hold; verdict names match §6. Two minor wording points (B6-4, B6-7). |
| P2 Misreadings | pass | No production, ranking, agentive or carried-as-real phrasing; "level" appears only as Dennett's reported term. |
| P3 Prior-art accuracy | pass | Attributions, the Quine quotation and locators check out against sources (list below). Minor: one altered term (B6-1), one loose attribution (B6-2), one locator without edition (B6-5), one optional omission (B6-6). |
| P4 Novelty | pass | Additions limited to the ordered test, the placement of carrying, and a proposed conditional consequence; refinement order, both-directions structure, derivability and the carrying question are all credited as inherited. No "solves/dissolves". |
| P5 Examples | pass | Canonical cases; both directions witnessed in glider, wave, ship, grue; wholes named and plausible; technical facts correct. Minor: crest/group ambiguity (B6-3), ship witness depends on the stipulated criterion (B6-2). |
| P6 Clarity | pass | First screen states the question, shows three cases, states what the test does and that it is unfinished. Terms defined before the table uses them. |
| P7 Notation and mechanics | pass | Lint 0 errors, links resolve, notation correct. |
| P8 Footprint and scope | pass | Only in-scope files changed (reading P8 with Amendment 1; literally it would fail, see C-1). No predecessor mention. |
| P9 Form | pass | v_form passes; first screen earns the next; README shows the idea before the tradition; prior art in README is one sentence plus a link. |

## Prior-art verification

Confirmed against a fetched source:

- Quine 1950: exact sentence "River stages are water stages, but rivers are
  not waters." (10 words), "river kinship", "summation of momentary objects",
  bathing in the same river twice without the same water — text of essay IV
  of *From a Logical Point of View*.
- Dennett 1991: "at the physical level there is no motion", cells "defined
  by their fixed spatial location", "one and the same glider", perfect
  prediction from the single law (pp. 37–40 of the article).
- Hobbes, *De Corpore* II.11.7: three opinions (matter, form, aggregate of
  accidents), "two ships numerically the same, which is absurd", identity by
  the name, ship "partly the same, and partly not the same".
- Locke II.xxvii: mass of atoms and oak both in §3; "identity suited to the
  idea" in §7.
- Plutarch, *Theseus* 23.1: locator confirmed.
- Russell 1948: causal-line passages at pp. 333 and 475–7 (SEP "Causal
  Processes", Simon and Schuster pagination). Salmon 1984: pseudo-processes
  pp. 141–4, mark criterion p. 147, MT p. 148; mark criterion credited to
  Reichenbach.
- Geach 1967, *Review of Metaphysics* 21(1): 3–12; Wiggins 1980, Oxford:
  Blackwell; Gibbard 1975, *JPL* 4: 187–221 (SEP "Relative Identity").
  Geach 1962 as source of relative identity; a theorem following Wiggins
  denies Geach's thesis (SEP "Sortals").
- Lewin 1922, title and genidentity; Reichenbach took it up (year of
  Reichenbach's use not confirmed by the source fetched).
- Goodman: grue and bleen definitions, ch. III (via Norton's citation).
- Zimmerman 1997, *Philosophical Perspectives* 11: 433–471.

Not independently fetched (source blocked or not found); consistent with
standard citations as far as I know, but unverified this round: Heraclitus
B12 wording; Gardner 1970 volume/issue; Davidson 1970 venue; Lewin's
publisher; Quine's "same water twice in two different rivers" half-sentence;
Russell's "replace substance" paraphrase; Gibbard's squeezed-ball case.

## Matter findings

No blocker. No major. Seven minor.

**B6-1 — minor — P3 — PRIOR-ART.md l.47–48; examples/glider.md l.18–19.**
Dennett's contrast is between the "physical level" and the "design level".
The matter reports it as "the level of the rule" vs "the level of design",
changing one of his two terms while presenting it as his.
*Change:* write "physical level" (or drop "level of the rule" and say "at
the level of the cells and their rule, which he calls physical").

**B6-2 — minor — P3, P5 — examples/ship.md l.24–30, l.43–48.**
"Both directions are Plutarch's and Hobbes's ... the puzzle states both."
Hobbes supplies the scenario, not the verdict "different ships": on his own
answer (ship = matter so shaped) the rebuilt ship is the same ship, so
"same plank, different ships" is not a witness for him. The witness holds
only under the example's stipulated criterion "same vessel, through repair".
That stipulation also already answers "which ship is Theseus's?" within the
example, while l.46 says ICW "names no winner".
*Change:* say the cases are Plutarch's and Hobbes's and that the second
witness holds under the ship criterion as stipulated; say that Hobbes's
puzzle sets two candidate *ship* criteria against each other and that the
plank/ship pair does not adjudicate between them.

**B6-3 — minor — P5 — examples/wave.md l.8, l.16–24; README l.5.**
"The same wave" slides between a swell that crosses the sea and a single
crest. In deep water a crest travels at twice the group speed and dies at
the front of its group, so no crest crosses an ocean; the group does. The
witnesses use crests.
*Change:* fix one criterion (crest, over the stretch it lasts; or the swell
group) and word case and witnesses to match.

**B6-4 — minor — P1 — examples/glider.md l.50–53.**
"(D7)" is cited for "neither cell-sameness nor cell-sameness with
arrangement fixes which glider". D7 covers only the cell/glider pair; the
arrangement step is from READING §6 and FINDINGS, not the kernel. "Fixes
which glider" also sits near the determination/constitution slide FINDINGS
warns of, since cell states do determine the glider (R2).
*Change:* cite D7 for the first half only; phrase the second as "is not
what makes it the same glider".

**B6-5 — minor — P3 — PRIOR-ART.md l.107–108, l.33–35.**
Russell is cited to pages with no publisher or edition; the pages match the
Simon and Schuster printing only. "Reichenbach (1956) developed it" gives
the late work only and no locator; "takes from Reichenbach" (l.42–43) names
no work.
*Change:* add "New York: Simon and Schuster" to Russell; give Reichenbach a
locator or say "took it up".

**B6-6 — minor — P3 — PRIOR-ART.md addition 2 (l.79–88).**
The nearest neighbours of O2 as stated (which criteria of identity over
time are non-arbitrary) are in the persistence literature itself, e.g.
Hirsch, *The Concept of Identity* (1982), and Lewis on natural properties
(1983). Goodman and the causal accounts are credited; these are not. ICW
claims only the placement, so this is not needed for accuracy. Suggestion
from my own knowledge: I confirmed only that Hirsch 1982 is a standard
treatment of identity criteria; α should verify before citing.
*Change:* optional one-line credit in PRIOR-ART.md (no README text).

**B6-7 — minor — P1, P6 — README.md l.22; examples/glider.md l.33–34.**
(a) "occurrences are what make up its changing" is compositional wording
that P1's *Excludes* and the Nomenclature steer away from; the kernel says
occurrences are *in* the changing. (b) "Site labels do not make the cell
criterion the whole's own" reads as a carrying verdict on cell; A1 says
only that labels privilege no continuity.
*Change:* (a) "occurrences are what happens in its changing"; (b) "Site
labels do not privilege the cell criterion".

## Contract findings

**C-1 — Stale scope in the unamended text.** REVIEW-PROPERTIES header and
P8 ("Nothing outside README.md and examples/ was changed") and CONTRACT
"Matter in scope" contradict Amendment 1, which requires PRIOR-ART.md. Read
literally, P8 fails on every compliant commit. P5 also still lists Gauss's
law, which no example uses.

**C-2 — Round cap and fresh reviewer make the convergence clause
unattestable and pressure approval.** The amendment landed after round 5 of
a maximum 6, leaving one round for a restructure; a REQUEST CHANGES now
cannot converge under the contract. Separately, convergence requires every
earlier finding to have a disposition "β accepted", and the verdict rule
requires prior findings resolved "to you"; β′ is barred from the log and is
not defined in the contract. I cannot attest that clause, and nobody else
is assigned to.

**C-3 — AC4/P1 cannot be satisfied together with AC2.** "No claim goes
beyond `specs/ARTICULATION.md`" and "every substantive claim traces to an
item" — but the kernel contains no prior art and no novelty claims. Every
"ICW adds" sentence and every attribution is outside the kernel by
construction. AC4 needs scoping to claims *about ICW's content*; novelty
claims have no authoritative source at all and rest on the reviewer.

**C-4 — Form caps are proxies and are being written to.** README is 647 of
650, glider 494 of 500. `v_form.py` drops any line starting with four
spaces from the count, detects a reference list only by the literal heading
`## References`, treats "first screen" as text before the first `##`, and
passes the link check on a bare substring. PRIOR-ART.md has no cap and
examples can be multiplied, so accretion is relocated, not bounded. "Any
FAIL is a blocker" has no converse: a pass shows nothing about form. The
party that wrote the caps validates against them.

**C-5 — The first-time-reader test can hardly fail.** The instructions
have the reviewer read the kernel, READING and FINDINGS before the README,
so the reading is not naive; and the fail condition is the reviewer
volunteering "nothing". Run it with a reader who has seen only the first
screen, and ask for a restatement of the question as well as an appetite.

**C-6 — AC3 against the kernel's own cases.** "No niche or invented cases"
excludes the kernel's uncarried example (colour and shape over parked
cars), pushing the matter to build its own occurrence structure for grue
and a coincident pair for Locke. Those constructions are the writer's, sit
outside the kernel (C-3), and no property checks them beyond "widely
known".

**C-7 — "Brief naming" and "literature review" are undefined.** The P9
major for prior art in the README has no threshold; eight items in one
sentence passed here on judgement alone. With the 650 cap this is the main
remaining route for credit to be cut rather than moved, and "moving text
must not lose a credit" has no check (nothing diffs the credits before and
after the move).

None of these makes the matter impossible to judge.

## Verdict

Verdict: APPROVE

On the matter at 01f1e3b: no blocker or major findings; seven minor. AC9
passes on this commit. Caveat: the clause on dispositions of earlier
findings is outside what I was allowed to check (C-2).
