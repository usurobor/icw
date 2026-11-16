"""H2: does a candidate rule sort claims into articulation, production and none?

A claim names a cause and an effect as sets of occurrences (step, row, col) in
one history, with a label fixed by construction. See notes/runs/2026-11-16-h2.md.
"""
import re
import numpy as np
from life import GLIDER, BLOCK, N, board, run, frame_of
from cases import glider_at, track_glider, case_collision, case_indirect_splice, gliders_in

T = 200

GOSPER = ("24bo$22bobo$12b2o6b2o12b2o$11bo3bo4b2o12b2o$2o8bo5bo3b2o$"
          "2o8bo3bob2o4bobo$10bo5bo7bo$11bo3bo$12b2o!")


def rle(text):
    cells, r, c = [], 0, 0
    for n, ch in re.findall(r"(\d*)([bo$!])", text):
        k = int(n) if n else 1
        if ch == "b":
            c += k
        elif ch == "o":
            cells += [(r, c + i) for i in range(k)]
            c += k
        elif ch == "$":
            r, c = r + k, 0
    return cells


def occ(frames):
    """Occurrences from {step: frame}."""
    return frozenset((t, r, c) for t, f in frames.items() for r, c in f)


def dist(p, q):
    dr = abs(p[0] - q[0]) % N
    dc = abs(p[1] - q[1]) % N
    return max(min(dr, N - dr), min(dc, N - dc))


# --- candidates ---

def reach(H, cause, effect):
    if cause == effect:
        return "articulation"
    for te, re_, ce in effect:
        if not any(tc < te and dist((re_, ce), (rc, cc)) <= te - tc for tc, rc, cc in cause):
            return "none"
    return "production"


def intervention(H, cause, effect):
    if cause == effect:
        return "articulation"
    t0 = min(t for t, _, _ in cause)
    b = H[t0].copy()
    for t, r, c in cause:
        if t == t0:
            b[r, c] = False
    H2 = run(b, max(t for t, _, _ in effect) - t0)
    changed = any(not H2[t - t0][r, c] for t, r, c in effect)
    return "production" if changed else "none"


CANDIDATES = {"Reach": reach, "Intervention": intervention}


# --- claims ---

def claims():
    out = []

    H = run(board((GLIDER, (10, 10))), T)
    g, _ = track_glider(H, glider_at(10, 10), 0)
    span = occ({t: g[t] for t in range(0, 41)})
    out.append(("The glider's cells produce the glider", H, span, span, "articulation"))
    out.append(("Glider at step 0 produces glider at step 40", H,
                occ({0: g[0]}), occ({40: g[40]}), "production"))

    Hg = run(board((rle(GOSPER), (5, 5))), T)
    gun0 = occ({0: frame_of(Hg[0])})
    far = lambda f: min(r for r, _ in f) > 20 and min(c for _, c in f) > 45
    t_obs = 150
    stream = sorted((f for f in gliders_in(Hg[t_obs]) if far(f)),
                    key=lambda f: -min(r for r, _ in f))
    assert len(stream) >= 2, "gun stream too short"
    first, second = stream[0], stream[1]
    out.append(("A gun produces the first glider it emits", Hg, gun0,
                occ({t_obs: first}), "production"))
    later = gliders_in(Hg[t_obs + 30])
    nxt = min((f for f in later if far(f)),
              key=lambda f: min(abs(min(r for r, _ in f) - min(r for r, _ in second)), 99))
    out.append(("One glider from a gun produces the next one", Hg,
                occ({t_obs: first}), occ({t_obs + 30: nxt}), "none"))

    col = case_collision(debris=True)
    Hc, tr = col["H"], col["tracings"][0]
    last = max(tr)
    out.append(("A glider striking a block produces the debris", Hc,
                occ({0: tr[0]}), occ({last: tr[last]}), "production"))

    ind = case_indirect_splice()
    Hi, tr = ind["H"], ind["tracings"][0]
    last = max(tr)
    out.append(("Glider A produces glider B through a one-time turner", Hi,
                occ({0: tr[0]}), occ({last: tr[last]}), "production"))

    Hs = run(board((GLIDER, (10, 10)), (GLIDER, (10, 60))), T)
    a, _ = track_glider(Hs, glider_at(10, 10), 0)
    b, _ = track_glider(Hs, glider_at(10, 60), 0)
    out.append(("Glider A at step 0 produces distant glider B at step 20", Hs,
                occ({0: a[0]}), occ({20: b[20]}), "none"))
    out.append(("Glider A at step 0 produces distant glider B at step 100", Hs,
                occ({0: a[0]}), occ({100: b[100]}), "none"))
    order = [0, 1, 2, 4, 5, 6, 7, 3]  # file numbering: gun siblings last
    return [out[i] for i in order]


def main():
    names = list(CANDIDATES)
    rows = ["| # | Claim | Label | " + " | ".join(names) + " |",
            "|---|---|---|" + "---|" * len(names)]
    score = {n: 0 for n in names}
    cs = claims()
    for i, (name, H, cause, effect, label) in enumerate(cs, 1):
        cells = []
        for n in names:
            v = CANDIDATES[n](H, cause, effect)
            ok = v == label
            score[n] += ok
            cells.append(f"{'✓' if ok else '✗'} {v}")
        rows.append(f"| {i} | {name} | {label} | " + " | ".join(cells) + " |")
    rows.append("")
    rows.append("Score: " + ", ".join(f"{n} {score[n]}/{len(cs)}" for n in names))
    print("\n".join(rows))


if __name__ == "__main__":
    main()
