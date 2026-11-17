"""Hunter round on C13a. Declared in notes/runs/2026-11-18-c13-hunt.md before this code ran.
Rerun: python3 tools/gol/hunt13.py"""
import sys

import numpy as np

import c13
import cases as C
import probes as PR
import run as R
from candidates import steps
from life import GLIDER, BLOCK, STILL_LIFES, N, board, run, frame_of, symmetries, is_glider

T = C.T
A = c13.c13("a")
GUN = [(5, 1), (5, 2), (6, 1), (6, 2), (3, 13), (3, 14), (4, 12), (4, 16), (5, 11), (5, 17),
       (6, 11), (6, 15), (6, 17), (6, 18), (7, 11), (7, 17), (8, 12), (8, 16), (9, 13), (9, 14),
       (1, 25), (2, 23), (2, 25), (3, 21), (3, 22), (4, 21), (4, 22), (5, 21), (5, 22), (6, 23),
       (6, 25), (7, 25), (3, 35), (3, 36), (4, 35), (4, 36)]
LWSS = [(0, 1), (0, 4), (1, 0), (2, 0), (2, 4), (3, 0), (3, 1), (3, 2), (3, 3)]
PULSAR = sorted({p for r in (0, 5, 7, 12) for c in (2, 3, 4, 8, 9, 10) for p in ((r, c), (c, r))})
BLINKER = [(0, 0), (0, 1), (0, 2)]


def verdict(H, tr, world=c13.LIFE_W):
    fl = c13.c13("a", world)(H, R.trim(tr))
    bad = [k for (k, _), x in zip(steps(R.trim(tr)), fl) if x is not True]
    return ("holds" if not bad else "uncarried"), bad[:6]


def live(H):
    return {t: frame_of(H[t]) for t in range(len(H))}


def h1():
    """Glider and a small object; the board ends as one glider and the glider's path changed."""
    objs = list(STILL_LIFES.items()) + [("blinker", BLINKER)]
    G0 = run(board((GLIDER, (10, 10))), T)
    for name, cells in objs:
        for sym in symmetries(cells):
            for dr in range(-4, 5):
                for dc in range(-4, 5):
                    pos = (30 + dr, 30 + dc)
                    H = run(board((GLIDER, (10, 10)), (list(sym), pos)), T)
                    fT = frame_of(H[T])
                    if not is_glider(fT) or fT == frame_of(G0[T]):
                        continue
                    if not any(H[t].sum() > 5 for t in range(T)):
                        continue
                    tr = PR.follow_piece(H, C.glider_at(10, 10))
                    return name, pos, H, tr
    return None


def kickback():
    a0 = (40, 40)
    for b_cells in symmetries(GLIDER):
        for d in range(8, 16):
            for off in range(-5, 6):
                b0 = (40 + d, 40 + d + off)
                H = run(board((GLIDER, a0), (list(b_cells), b0)), T)
                fT = frame_of(H[T])
                if is_glider(fT) and H[T].sum() == 5 and H[0].sum() == 10:
                    return b0, H
    return None


def merge184(seeds=range(40)):
    L = PR.L
    for seed in seeds:
        rng = np.random.default_rng(seed)
        a = rng.random(L) < 0.55
        Hh = [a]
        for _ in range(T):
            Hh.append(c13.r184_step(Hh[-1]))
        Hh = np.array(Hh)
        for t in range(20, T - 10):
            now = [r for r in PR.runs184(frozenset(np.nonzero(Hh[t])[0].tolist())) if len(r) >= 3]
            nxt = [r for r in PR.runs184(frozenset(np.nonzero(Hh[t + 1])[0].tolist())) if len(r) >= 3]
            for m in nxt:
                srcs = [r for r in now if r & PR.near184(m)]
                if len(srcs) == 2 and len(srcs[0]) != len(srcs[1]):
                    return seed, t, Hh, srcs
    return None


def follow_jam(Hh, start, t0):
    tr, prev = {t0: start}, start
    for t in range(t0 + 1, T + 1):
        rs = [r for r in PR.runs184(frozenset(np.nonzero(Hh[t])[0].tolist())) if len(r) >= 3]
        near = [r for r in rs if r & PR.near184(prev)]
        if not near:
            break
        prev = max(near, key=len)
        tr[t] = prev
    return tr


def main():
    out = ["| ID | Case | C13a verdict | Steps not carried | Prediction | |", "|---|---|---|---|---|---|"]

    def row(i, name, v, pred):
        out.append(f"| {i} | {name} | {v[0]} | {v[1]} | {pred} | {'right' if v[0] == pred else 'wrong'} |")

    r = h1()
    if r:
        name, pos, H, tr = r
        row("H-1", f"glider through a {name} at {pos}, followed", verdict(H, tr), "uncarried")
        row("H-1", f"glider through a {name} at {pos}, F2", verdict(H, c13.by_product_trim(H, C.glider_at(10, 10), 0)), "holds")
    else:
        out.append("| H-1 | no board found in the search | | | | |")
    H = run(board((BLOCK, (40, 40)), (BLOCK, (40, 43))), T)
    row("H-3", "bi-block as one", verdict(H, live(H)), "uncarried")
    H = run(board((PULSAR, (40, 40))), T)
    row("H-4", "pulsar", verdict(H, live(H)), "holds")
    H = run(board((GUN, (10, 10))), T)
    gun = frozenset((10 + r, 10 + c) for r, c in GUN)
    row("H-5", "Gosper gun, followed", verdict(H, PR.follow_piece(H, gun)), "uncarried")
    row("H-5", "Gosper gun, F2", verdict(H, c13.by_product_trim(H, gun, 0)), "holds")
    H = run(board((LWSS, (60, 100))), T)
    row("H-8", "lightweight spaceship", verdict(H, live(H)), "holds")
    g = PR.probe_gliders()
    Hg, s = g["H"], g["start"]
    trA, stop = C.track_glider(Hg, g["A"][0], 0)
    Rt = C.follow(Hg, frame_of(Hg[s]), s, T)
    contA = {**{t: trA[t] for t in trA if t < s}, **Rt}
    row("H-10a", "glider A into the reaction (registered pair)", verdict(Hg, contA), "uncarried")
    kb = kickback()
    if kb:
        b0, Hk = kb
        ta, _ = C.track_glider(Hk, C.glider_at(40, 40), 0)
        rest = C.follow(Hk, ta[max(ta)], max(ta), T)
        row("H-10b", f"kickback (B at {b0}): A into the output glider", verdict(Hk, {**ta, **rest}), "uncarried")
    else:
        out.append("| H-10b | no kickback found in the search | | | | |")
    case = C.case_glider()
    sh = R.shifted(case, d=(100, 100))
    row("H-11", "glider across the board's edge", verdict(sh["H"], sh["tracings"][0]), "uncarried")
    m = merge184()
    if m:
        seed, t, Hh, srcs = m
        big, small = sorted(srcs, key=len, reverse=True)
        tb = {**{t: big}, **follow_jam(Hh, big, t)}
        ts = {t: small, **{u: f for u, f in follow_jam(Hh, big, t).items() if u > t}}
        row("H-13", f"rule 184 seed {seed}, larger jam ({len(big)}) into the merge at {t + 1}", verdict(Hh, tb, c13.R184_W), "holds")
        row("H-13", f"rule 184 seed {seed}, smaller jam ({len(small)}) into the merge", verdict(Hh, ts, c13.R184_W), "uncarried")
    else:
        out.append("| H-13 | no merge found | | | | |")
    j = PR.probe_jam()
    Hj = np.array(j["H"])
    p = max(j["jam"][0])
    while Hj[0][p]:
        p += 1  # the first hole in front of the jam
    hole = {0: frozenset([p])}
    for t in range(T):
        p = (p - 1) % PR.L if Hj[t][(p - 1) % PR.L] and not Hj[t][p] else p
        hole[t + 1] = frozenset([p])
    assert all(not Hj[t][list(hole[t])[0]] for t in hole)
    row("H-14", "rule 184 hole through the jam", verdict(Hj, hole, c13.R184_W), "uncarried")
    case = C.case_glider()
    tr = case["tracings"][0]
    box = {t: frozenset((r, c) for r in range(min(x for x, _ in f), max(x for x, _ in f) + 1)
                        for c in range(min(y for _, y in f), max(y for _, y in f) + 1))
           for t, f in tr.items()}
    row("H-15", "glider with its bounding box", verdict(case["H"], box), "uncarried")
    print("\n".join(out))


if __name__ == "__main__":
    sys.exit(main())
