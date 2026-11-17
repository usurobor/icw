# Transport and moving patterns in the elementary rules

Owner conjecture (18 Nov): where the dynamics moves state across elements, a
pattern articulation exists; where it does not, none does. Rerun:
`python3 tools/eca/transport.py` (about 15 seconds).

## Definitions

- **Classes.** The 256 elementary rules, grouped under reflection and
  complement: 88 classes.
- **Transport.** Flip one cell of a random board (201 cells, ring) and run
  both boards 60 steps. The rule transports when the difference ever stands 3
  or more cells from the flipped site. 20 random boards per rule.
- **Moving pattern.** A seed of width 1 to 10 on a quiescent 0 background that
  recurs shifted (period up to 40, shift not 0). Searched only in rules where
  000 gives 0. A pattern that recurs in place coincides with its cells and does
  not cross-cut them.

## Results

| | Classes |
|---|---|
| No transport | 15: 0, 1, 4, 5, 8, 12, 19, 29, 36, 51, 72, 76, 128, 200, 204 |
| Transport | 73 |
| Moving pattern found | 20, every one of them in a transporting class |
| Moving pattern without transport | none |
| Transport, no moving pattern on the 0 background | 34, among them 30, 54, 90, 110, 150 |

## What this shows

1. **The negative direction holds, and it is close to analytic.** A pattern
   that cross-cuts its elements stands at different elements at different
   times, so state has moved relative to them. No transport leaves only
   patterns that coincide with their cells or are nested in them (rule 51:
   every cell flips, nothing travels). The run finds no exception.
2. **The positive direction fails for lasting patterns.** Transport is
   necessary and far from sufficient. Of 73 transporting classes, 20 show a
   moving pattern on the 0 background. Chaotic rules (30, 90, 150) spread
   every difference and keep no particle; transport there yields only
   short-lived structure.
3. **Search limit.** Rules 54 and 110 have known particles on a periodic
   background (ether), which this search does not try. The count of 20 is a
   floor.

So transport is the condition for any cross-cutting pattern, and carrying is
what sorts the lasting ones from the transient. That places O2 between the
two: among transporting rules, what keeps transported state together?
