"""C16: window integration by part-dependence, with C10's closeness and C12's outflow.
Declared (and amended before any code) in notes/runs/2026-11-18-c16.md. Rerun: python3 tools/gol/c16.py
"""
import math
import sys
from collections import Counter
from functools import lru_cache

import numpy as np

import c11
import c12
import c13
import c14
import cases as C
import hunt13 as HU
import probes as PR
import run as R
from candidates import steps
from life import N, board, run, frame_of

T = C.T
WMAX = 60
THETA = 1.2469873517384964 / 2  # frozen after the anchor run (glider 1.247, union 0)
C12_THETA = c12.THETA["knockout"]


def _run_batch(H, t0, w, B0, step):
    """B0: (n, ...) start boards at t0; returns list of arrays per step u=t0+1..t0+w."""
    out, B = [], B0
    for _ in range(w):
        B = step(B)
        out.append(B)
    return out


def _gather(states, cells_by_u, ndim):
    cols = []
    for k, cells in enumerate(cells_by_u):
        S = states[k]
        for p in cells:
            cols.append(S[(slice(None),) + (p if ndim == 2 else (p,))])
    return np.stack(cols, axis=1) if cols else np.zeros((states[0].shape[0], 0), dtype=bool)


def _entropy(rows):
    c = Counter(map(bytes, np.packbits(rows, axis=1))) if rows.shape[1] else Counter({b"": len(rows)})
    n = len(rows)
    return -sum(v / n * math.log2(v / n) for v in c.values())


def integration_score(H, tr, world, rng_seed=0):
    """Minimum over splits of I(Y_P ; Y_Q); None when there is no split; also the split scores."""
    ts = sorted(tr)
    t0 = ts[0]
    W = [u for u in ts[1:WMAX + 1]]
    if not W:
        return None, []
    w = W[-1] - t0
    F0 = sorted(tr[t0], key=lambda p: p if isinstance(p, tuple) else (p,))
    live = [p for p in F0 if H[t0][p]]
    n = len(live)
    if n < 2:
        return None, []
    idx = {p: i for i, p in enumerate(live)}
    ps = world.pieces(frozenset(live))
    rng = np.random.default_rng(rng_seed)
    if len(ps) >= 2:
        k = len(ps)
        masks = list(range(1, 2 ** (k - 1)))
        if k > 6:
            masks = sorted(set(int(x) for x in rng.integers(1, 2 ** (k - 1), 31)))
        splits = [[i for m in range(k - 1) if mask >> m & 1 for i in (idx[p] for p in ps[m + 1])]
                  for mask in masks]
    else:
        splits = []
        for _ in range(8):
            cut = rng.random(n) < 0.5
            if cut.all() or not cut.any():
                cut[0] = not cut[0]
            splits.append([i for i in range(n) if cut[i]])
    cells_by_u = [sorted(tr[u], key=lambda p: p if isinstance(p, tuple) else (p,)) for u in W]
    stepu = [u - t0 for u in W]
    base = np.asarray(H[t0])

    def states_for(X):
        """X: (m, n) keep-bits; returns Y (m, cells) over the window."""
        m = X.shape[0]
        outs = []
        for a in range(0, m, 256):
            Xb = X[a:a + 256]
            B = np.repeat(base[None], len(Xb), axis=0)
            for j, p in enumerate(live):
                B[(slice(None),) + (p if world.ndim == 2 else (p,))] = Xb[:, j]
            seq = _run_batch(H, t0, w, B, world.step)
            outs.append(_gather([seq[s - 1] for s in stepu], cells_by_u, world.ndim))
        return np.concatenate(outs, axis=0)
    if n <= 12:
        X = ((np.arange(2 ** n)[:, None] >> np.arange(n)) & 1).astype(bool)
    else:
        X = rng.random((2048, n)) < 0.5
    Y = states_for(X)
    scores = []
    for Pi in splits:
        Qi = [i for i in range(n) if i not in Pi]
        regions = []
        for A_, B_ in ((Pi, Qi), (Qi, Pi)):
            reg = np.zeros(Y.shape[1], dtype=bool)
            for fixed in (True, False):
                if len(A_) <= 8:
                    XA = ((np.arange(2 ** len(A_))[:, None] >> np.arange(len(A_))) & 1).astype(bool)
                else:
                    XA = rng.random((256, len(A_))) < 0.5
                Xf = np.zeros((len(XA), n), dtype=bool)
                Xf[:, A_] = XA
                Xf[:, B_] = fixed
                Yf = states_for(Xf)
                reg |= (Yf != Yf[0]).any(axis=0)
            regions.append(reg)
        YP, YQ = Y[:, regions[0]], Y[:, regions[1]]
        mi = _entropy(YP) + _entropy(YQ) - _entropy(np.concatenate([YP, YQ], axis=1))
        scores.append(max(0.0, mi))
    return min(scores), scores


_cache = {}


def integrated(H, tr, world, theta):
    key = (id(H), tuple(sorted(tr)), hash(frozenset((t, f) for t, f in tr.items())))
    if key not in _cache:
        _cache[key] = integration_score(H, tr, world)[0]
    s = _cache[key]
    return True if s is None else s > theta


def c16(theta, world=c13.LIFE_W, rule=c11.LIFE, with_e=False):
    def judge(H, tr):
        if with_e and c13.elemental(tr):
            return c13.e_flags(H, tr, world)
        cl = c13.closeness(H, tr, world)
        out12 = c12.shares(H, tr, rule, "knockout")
        whole = integrated(H, tr, world, theta)
        return [bool(a is True and (b is None or b > C12_THETA) and whole) for a, b in zip(cl, out12)]
    return judge


def anchors():
    g, u = C.case_glider(), C.case_union()
    gs, gsc = integration_score(g["H"], g["tracings"][0], c13.LIFE_W)
    us, usc = integration_score(u["H"], u["tracings"][0], c13.LIFE_W)
    return gs, us, (gs + us) / 2, gsc, usc


def main():
    if "--anchors" in sys.argv:
        gs, us, th, gsc, usc = anchors()
        print(f"glider {gs} (cuts {[round(x, 3) for x in gsc]}), union {us}, theta {th}")
        return 0
    gs, us, th, _, _ = anchors()
    assert THETA is not None and abs(th - THETA) < 1e-9, (th, THETA)
    out = [f"Anchors: glider score {gs:.3f}, union score {us:.3f}, θ = {th:.3f}.", ""]
    cases = c12.all_grid_cases()
    out += ["### Grid", "", "| Case | Target | Integration score | Integration only | C16 | at 0.8 θ | at 1.2 θ | Verdict |",
            "|---|---|---|---|---|---|---|---|"]
    m = 0
    for case in cases:
        sc = [integration_score(case["H"], R.trim(tr), c13.LIFE_W)[0] for tr in case["tracings"]]
        intonly = all(s is None or s > th for s in sc)
        mk, det = R.score(case, "C16", c16(th))
        lo, _ = R.score(case, "C16", c16(0.8 * th))
        hi, _ = R.score(case, "C16", c16(1.2 * th))
        msh, _ = R.score(R.shifted(case), "C16", c16(th))
        m += mk == "✓"
        out.append(f"| {case['name']} | {case['target']} | {', '.join('—' if s is None else f'{s:.3f}' for s in sc)} | "
                   f"{'integrated' if intonly else 'split'} | {mk} | {lo} | {hi} | {det}{'' if msh == mk else ' (shift changes mark)'} |")
    out += [f"| Rows matched | | | | {m} | | | |", ""]
    out += ["### Registered probes", "", "| Part | Target | Integration score | C16 | C16 with E |", "|---|---|---|---|---|"]
    n1 = n2 = 0
    for sec, name, target, H, tr, lo_, hi_, want, rule in c12.probe_parts():
        w = c13.R184_W if rule is c11.R184 else c13.LIFE_W
        trr = R.trim(tr)
        if lo_ > min(trr) or hi_ < max(trr):
            trw = {t: f for t, f in trr.items() if lo_ <= t <= hi_}
        else:
            trw = trr
        s, _ = integration_score(H, trw, w)
        cells = []
        for e in (False, True):
            fl = c16(th, w, rule, e)(H, tr)
            ok, _ = c13.part_ok(fl, tr, lo_, hi_, want)
            cells.append(ok)
        n1 += cells[0]
        n2 += cells[1]
        out.append(f"| {name} | {target} | {'—' if s is None else f'{s:.3f}'} | {c13.mark(cells[0])} | {c13.mark(cells[1])} |")
    out += [f"| Parts matched | | | {n1} | {n2} |", ""]
    out += ["### Hunter and new cases (no target)", "", "| Case | Integration score | Integrated | C16 verdict |", "|---|---|---|---|"]
    hc = []
    nc_, _ = c13.new_cases()
    for name, Hn, trn, w in nc_[:3]:
        hc.append((name, Hn, trn))
    gq = PR.probe_gliders()
    Rt = C.follow(gq["H"], frame_of(gq["H"][gq["start"]]), gq["start"], T)
    hc.append(("N-1b products as one, from contact", gq["H"], Rt))
    Hb = run(board((HU.BLOCK, (40, 40)), (HU.BLOCK, (40, 43))), T)
    hc.append(("H-3 bi-block as one", Hb, HU.live(Hb)))
    Hp = run(board((HU.PULSAR, (40, 40))), T)
    hc.append(("H-4 pulsar", Hp, HU.live(Hp)))
    Hl = run(board((HU.LWSS, (60, 100))), T)
    hc.append(("H-8 lightweight spaceship", Hl, HU.live(Hl)))
    Hg = run(board((HU.GUN, (10, 10))), T)
    gun = frozenset((10 + r, 10 + c) for r, c in HU.GUN)
    hc.append(("H-5 Gosper gun, followed", Hg, PR.follow_piece(Hg, gun)))
    for name, Hn, trn in hc:
        trn = R.trim(trn)
        s, _ = integration_score(Hn, trn, c13.LIFE_W)
        fl = c16(th)(Hn, trn)
        bad = [k for (k, _), x in zip(steps(trn), fl) if x is not True]
        out.append(f"| {name} | {'—' if s is None else f'{s:.3f}'} | {s is None or s > th} | "
                   f"{'holds' if not bad else 'uncarried'} {bad[:5]} |")
    print("\n".join(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
