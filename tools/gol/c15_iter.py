"""C15, rule 5: noise in the Game of Life; rule 184 rings, with and without noise.
Declared in notes/runs/2026-11-18-c15.md. Rerun: python3 tools/gol/c15_iter.py"""
import copy
import sys

import numpy as np

import c13
import c15 as c14
import cases as C
import probes as PR
import run as R
from candidates import steps
from life import GLIDER, N, board

T = C.T


def noisy_life(eps, seed):
    rng = np.random.default_rng(seed)
    noise = rng.random((T + 1, N, N)) < eps
    noise[0] = False
    H = [board((GLIDER, (10, 10)), (GLIDER, (10, 60)))]
    for u in range(1, T + 1):
        H.append(c13.life_step_count(H[-1]) ^ noise[u])
    w = copy.copy(c14.LIFE_X)
    w.noise = noise
    return np.array(H), w


def verdict(H, tr, w):
    tr = R.trim(tr)
    fl = c14.c14(w)(H, tr)
    return c14.vword(fl), [k for (k, _), x in zip(steps(tr), fl) if x is not True][:5]


def life_noise():
    rows = ["| ε | seed | A tracked to | B tracked to | Glider | Splice | Union | Alternating |",
            "|---|---|---|---|---|---|---|---|"]
    tally = [0, 0]
    for eps in (1e-4, 1e-3):
        for seed in (0, 1, 2):
            H, w = noisy_life(eps, seed)
            a, _ = C.track_glider(H, C.glider_at(10, 10), 0)
            b, _ = C.track_glider(H, C.glider_at(10, 60), 0)
            both = min(max(a), max(b))
            s = min(100, both)
            cells = []
            for name, tr, want in (
                    ("glider", a, "holds"),
                    ("splice", {t: (a[t] if t < s else b[t]) for t in range(0, max(b) + 1)}, "uncarried"),
                    ("union", {t: a[t] | b[t] for t in range(both + 1)}, "uncarried"),
                    ("alt", {t: (a[t] if t % 2 == 0 else b[t]) for t in range(both + 1)}, "uncarried")):
                v, bad = verdict(H, tr, w)
                ok = v == want
                tally[0] += ok
                tally[1] += 1
                cells.append(f"{'✓' if ok else '✗'} {v} {bad}")
            rows.append(f"| {eps:g} | {seed} | {max(a)} | {max(b)} | " + " | ".join(cells) + " |")
    return rows, tally


def ring(density, seed, eps):
    L = PR.L
    rng = np.random.default_rng(seed)
    a = rng.random(L) < density
    noise = rng.random((T + 1, L)) < eps
    noise[0] = False
    H = [a]
    for u in range(1, T + 1):
        H.append(c13.r184_step(H[-1]) ^ noise[u])
    w = copy.copy(c14.R184)
    w.noise = noise
    return np.array(H), w


def cars(H):
    L = H.shape[1]
    out = []
    for p0 in np.nonzero(H[0])[0]:
        tr, p = {0: frozenset([int(p0)])}, int(p0)
        for t in range(T):
            p = (p + 1) % L if not H[t][(p + 1) % L] else p
            if not H[t + 1][p]:
                break
            tr[t + 1] = frozenset([p])
        out.append(tr)
    return out


def runs(H, t, m):
    return [r for r in PR.runs184(frozenset(np.nonzero(H[t])[0].tolist())) if len(r) >= m]


def jams(H):
    out = []
    for r0 in runs(H, 20, 4):
        tr, prev, event = {20: r0}, r0, False
        for t in range(21, T + 1):
            near = [r for r in runs(H, t, 3) if r & PR.near184(prev)]
            if not near:
                break
            if len(near) > 1:
                event = True
            src = [r for r in runs(H, t - 1, 3) if r & PR.near184(max(near, key=len))]
            if len(src) > 1:
                event = True
            prev = max(near, key=len)
            tr[t] = prev
        out.append((tr, event))
    return out


def moving():
    rows = ["| density | ε | cars carried | jams without merge or split: holds | with merge or split: holds / refused / unresolved |",
            "|---|---|---|---|---|"]
    tally = dict(cars=[0, 0], jams=[0, 0])
    for dens in (0.4, 0.55, 0.7):
        for eps in (0.0, 1e-3):
            cc = [0, 0]
            jq = [0, 0]
            ev = [0, 0, 0]
            for seed in (0, 1, 2):
                H, w = ring(dens, seed, eps)
                for tr in cars(H):
                    if len(tr) < 2:
                        continue
                    v, _ = verdict(H, tr, w)
                    cc[0] += v == "holds"
                    cc[1] += 1
                for tr, event in jams(H):
                    if len(tr) < 2:
                        continue
                    v, _ = verdict(H, tr, w)
                    if event:
                        ev[["holds", "uncarried", "unresolved"].index(v)] += 1
                    else:
                        jq[0] += v == "holds"
                        jq[1] += 1
            tally["cars"][0] += cc[0]
            tally["cars"][1] += cc[1]
            tally["jams"][0] += jq[0]
            tally["jams"][1] += jq[1]
            rows.append(f"| {dens} | {eps:g} | {cc[0]} of {cc[1]} | {jq[0]} of {jq[1]} | {ev[0]} / {ev[1]} / {ev[2]} |")
    return rows, tally


def main():
    out = ["### Noise in the Game of Life", ""]
    r, t = life_noise()
    out += r + ["", f"Matched: {t[0]} of {t[1]}.", "", "### Rule 184", ""]
    r, t = moving()
    out += r + ["", f"Cars carried: {t['cars'][0]} of {t['cars'][1]}; jams without an event: "
                    f"{t['jams'][0]} of {t['jams'][1]} hold."]
    print("\n".join(out))


if __name__ == "__main__":
    sys.exit(main())
