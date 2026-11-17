"""C3: compression gain. Declared in notes/runs/2026-11-17-c3.md before this code ran.

gain = D(bit map) - (D(tracing description) + D(residual bit map)), D = lzma raw
LZMA2 preset 9 | extreme, in bits. A whole tracing is carried when gain > theta.
Rerun: python3 tools/gol/c3.py
"""
import lzma
import sys

import numpy as np

import c11
import c12
import cases as C
import run as R
from c11 import LIFE, R184, fmt, mark

FILTERS = [{"id": lzma.FILTER_LZMA2, "preset": 9 | lzma.PRESET_EXTREME}]


def D(b):
    return 8 * len(lzma.compress(b, format=lzma.FORMAT_RAW, filters=FILTERS))


def bitmap(H):
    return np.packbits(np.asarray(H, dtype=bool), axis=-1).tobytes()


def _cells(f, dims):
    return [p if dims == 2 else (p,) for p in f]


def describe(H, tr):
    H = np.asarray(H)
    dims, side = H.ndim - 1, H.shape[1]
    out, prev = bytearray(), None
    for t in sorted(tr):
        f = sorted(_cells(tr[t], dims))
        out += len(f).to_bytes(2, "big")
        if not f:
            continue
        corner = tuple(min(p[k] for p in f) for k in range(dims))
        for p in f:
            out += bytes((p[k] - corner[k]) % 256 for k in range(dims))
        move = corner if prev is None else tuple((corner[k] - prev[k]) % side for k in range(dims))
        out += bytes(m % 256 for m in move)
        prev = corner
        states = [bool(H[t][p if dims == 2 else p[0]]) for p in f]
        out += np.packbits(np.array(states, dtype=bool)).tobytes()
    return bytes(out)


def residual(H, tr):
    Hr = np.array(H, dtype=bool, copy=True)
    for t, f in tr.items():
        for p in f:
            Hr[t][p] = False
    return Hr


_raw_cache = {}


def gain(H, tr):
    key = id(H)
    if key not in _raw_cache or _raw_cache[key][0] is not H:
        _raw_cache[key] = (H, D(bitmap(H)))
    raw = _raw_cache[key][1]
    lt, lr = D(describe(H, tr)), D(bitmap(residual(H, tr)))
    return raw - lt - lr, raw, lt, lr


def anchors():
    g, s = C.case_glider(), C.case_splice()
    gg = gain(g["H"], g["tracings"][0])[0]
    sg = gain(s["H"], s["tracings"][0])[0]
    return gg, sg, (gg + sg) / 2


# Frozen after the anchor run, before any other case was scored. None until then.
THETA = (1192 + 296) / 2


def candidate(theta):
    def judge(H, tr):
        return gain(H, tr)[0] > theta
    judge.whole = True
    return judge


def time_shift(H, tr):
    H7 = np.concatenate([np.zeros((7,) + np.asarray(H).shape[1:], dtype=bool), H])
    return H7, {t + 7: f for t, f in tr.items()}


def main():
    if "--anchors" in sys.argv:
        g, s, th = anchors()
        print(f"glider gain {g}, splice gain {s}, theta {th}")
        gl, sp = C.case_glider(), C.case_splice()
        print("glider parts", gain(gl["H"], gl["tracings"][0]))
        print("splice parts", gain(sp["H"], sp["tracings"][0]))
        return 0
    g, s, th = anchors()
    assert THETA is not None and abs(th - THETA) < 1e-9
    out = [f"Anchors: glider gain {g} bits, splice gain {s} bits, θ = {th}.", ""]
    cases = c12.all_grid_cases()
    out += ["| Case | Gain (bits) | L_raw | L_trace | L_res | Verdict | Target | Match | at 0.8 θ | at 1.2 θ | at 0 | gain, space shift | gain, time shift |",
            "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    shift_fail = []
    for case in cases:
        gs = [gain(case["H"], tr) for tr in case["tracings"]]
        mk, v = R.score(case, "C3", candidate(th))
        lo, _ = R.score(case, "C3", candidate(0.8 * th))
        hi, _ = R.score(case, "C3", candidate(1.2 * th))
        z, _ = R.score(case, "C3", candidate(0))
        sc = R.shifted(case)
        msh, _ = R.score(sc, "C3", candidate(th))
        gsh = [gain(sc["H"], tr)[0] for tr in sc["tracings"]]
        gts = [gain(*time_shift(case["H"], tr))[0] for tr in case["tracings"]]
        Ht, _ = time_shift(case["H"], case["tracings"][0])
        ct = {**case, "H": Ht, "tracings": [time_shift(case["H"], tr)[1] for tr in case["tracings"]]}
        if "crash" in ct:
            ct["crash"] += 7
        mts, _ = R.score(ct, "C3", candidate(th))
        if msh != mk or mts != mk:
            shift_fail.append((case["name"], mk, msh, mts))
        j = lambda xs: ", ".join(str(x) for x in xs)
        out.append(f"| {case['name']} | {j(x[0] for x in gs)} | {j(x[1] for x in gs)} | {j(x[2] for x in gs)} | "
                   f"{j(x[3] for x in gs)} | {v} | {case['target']} | {mk} | {lo} | {hi} | {z} | {j(gsh)} | {j(gts)} |")
    out += ["", "Shift check (marks; space 7 rows, 13 columns; time 7 steps): " +
            ("every mark unchanged." if not shift_fail else f"changed (case, mark, space, time): {shift_fail}"), ""]

    # extras
    gl = C.case_glider()
    H = gl["H"]
    Hi, trg, inc = c11.case_incar()
    out.append(f"Incar alone: gain {gain(Hi, inc)[0]}; nested at check 3.")
    allc = frozenset((r, c) for r in range(H.shape[1]) for c in range(H.shape[2]))
    out.append(f"Whole board as one tracing: gain {gain(H, {t: allc for t in range(len(H))})[0]}; nested at check 3.")
    u = C.case_union()
    out.append(f"Trout-turkey (union build, no target): gain {gain(u['H'], u['tracings'][0])[0]}.")
    tr = gl["tracings"][0]
    sites = sorted(frozenset().union(*tr.values()))
    eg = [gain(H, {t: frozenset([p]) for t in range(len(H))})[0] for p in sites]
    out.append(f"Elemental: {len(sites)} crossed cells as single sites: gains min {min(eg)}, median "
               f"{sorted(eg)[len(eg) // 2]}, max {max(eg)}; above θ: {sum(x > th for x in eg)}; above 0: "
               f"{sum(x > 0 for x in eg)}.")
    out.append("")

    # probes
    out += ["| Part | Target | Gain | C3 | at 0.8 θ | at 1.2 θ | at 0 |", "|---|---|---|---|---|---|---|"]
    for sec, name, target, Hp, trp, lo_, hi_, want, rule in c12.probe_parts():
        sub = {t: f for t, f in trp.items() if lo_ <= t <= hi_} if want else trp
        gp = gain(np.asarray(Hp), sub)[0]
        marks = [mark((gp > f * th) == want) for f in (1.0, 0.8, 1.2)] + [mark((gp > 0) == want)]
        out.append(f"| {name} | {target} | {gp} | " + " | ".join(marks) + " |")
    print("\n".join(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
