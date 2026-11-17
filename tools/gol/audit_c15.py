"""Audit of C15 (notes/audits/2026-11-18-c15-audit.md). C15 itself is not modified.
Rerun: python3 tools/gol/audit_c15.py hunt | ablate | checks
  hunt    the auditor's hunter cases H-21 to H-25 (numbered after the C13 hunter round)
  ablate  C15 with one clause switched off at a time, on the registered probes and the six unseen boards
  checks  unseen boards as translates of the registered board; noise near the tracked gliders;
          C14's candidate with C15's ring-aware jam builder
"""
import sys

import numpy as np

import c11
import c12
import c13
import c14
import c15
import cases as C
import probes as PR
import run as R
from candidates import steps
from life import GLIDER, board, run, frame_of

T = C.T
W = c15.LIFE_X

# A 13-cell soup found by random search (5 x 5, seed 1): it lives 97 steps and leaves nothing.
SOUP = [(0, 1), (0, 3), (1, 0), (1, 2), (1, 3), (1, 4), (2, 0), (2, 2), (2, 4), (3, 1), (4, 1), (4, 3), (4, 4)]
DIAG = [(0, 0), (1, 1), (2, 2)]  # dies in two steps: 3 cells, 1 cell, none
MWSS = [(0, 3), (1, 1), (1, 5), (2, 0), (3, 0), (3, 5), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]
HWSS = [(0, 3), (0, 4), (1, 1), (1, 6), (2, 0), (3, 0), (3, 6), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5)]


def live(H):
    return {t: frame_of(H[t]) for t in range(len(H))}


def flags(H, tr, world=W):
    tr = R.trim(tr)
    return tr, c15.c14(world)(H, tr)


def report(name, H, tr, world=W, lo=None, hi=None):
    tr, fl = flags(H, tr, world)
    keys = [t for t, _ in steps(tr)]
    bad = [(k, x) for k, x in zip(keys, fl) if x is not True]
    sel = [x for k, x in zip(keys, fl) if (lo is None or lo <= k < hi)]
    v = c15.vword(sel)
    rng = "" if lo is None else f" (steps {lo}–{hi - 1})"
    print(f"| {name} | {v}{rng} | {[k for k, _ in bad][:8]} | {[str(x) for _, x in bad][:8]} |", flush=True)


def hunt():
    print("| Case | C15 verdict | Steps not carried | Flags there |\n|---|---|---|---|")
    # H-21: a glider and a far soup that dies by itself, traced as one (every live cell)
    H = run(board((GLIDER, (10, 10)), (SOUP, (80, 70))), T)
    death = next(t for t in range(T + 1) if not frame_of(H[t]) - frame_of(run(board((GLIDER, (10, 10))), T)[t]))
    print(f"<!-- H-21 soup gone from step {death} -->")
    report("H-21 glider and a far soup that dies at step %d, as one" % death, H, live(H))
    # H-22: as N-2, with a three-cell far junk that dies in two steps
    H = run(board((GLIDER, (10, 10)), (DIAG, (10, 50))), T)
    report("H-22 glider and a far 3-cell diagonal (dies in 2 steps), as one", H, live(H))
    # H-23: an interaction's products as one, traced from contact and from step 110 (registered pair)
    g = PR.probe_gliders()
    Hg, s, e = g["H"], g["start"], g["end"]
    Rt = C.follow(Hg, frame_of(Hg[s]), s, T)
    for t0 in (e, 105, 110):
        report(f"H-23 products as one, traced from step {t0}", Hg, {t: f for t, f in Rt.items() if t >= t0})
    # H-24: A and B as one from step 0, continued into the reaction; judged before contact
    trA, _ = C.track_glider(Hg, g["A"][0], 0)
    trB, _ = C.track_glider(Hg, g["B"][0], 0)
    ab = {**{t: trA[t] | trB[t] for t in range(0, s)}, **{t: f for t, f in Rt.items() if t <= e}}
    report("H-24 A and B as one, continued into the reaction", Hg, ab, lo=0, hi=s - 1)
    for t1 in (s + 2, s + 10, e):
        ab = {**{t: trA[t] | trB[t] for t in range(0, s)}, **{t: f for t, f in Rt.items() if t <= t1}}
        report(f"H-24 same, tracing ending at {t1}", Hg, ab, lo=0, hi=s - 1)
    report("H-24 control: registered part, A and B as one to step %d" % (s - 1), Hg,
           {t: trA[t] | trB[t] for t in range(0, s)})
    # H-25: the other two catalogue spaceships, every live cell, from step 0 and from step 1
    for nm, pat in (("MWSS", MWSS), ("HWSS", HWSS)):
        H = run(board((pat, (60, 100))), T)
        tr = live(H)
        report(f"H-25 {nm} from step 0", H, tr)
        report(f"H-25 {nm} from step 1", H, {t: f for t, f in tr.items() if t >= 1})


# ---------------------------------------------------------------- ablations

_orig_core, _orig_int = c15.core, c15._integration


def _int_no_lasting(H, t, t1, Tend, ps, roots, Hw, single, D, world):
    """C15's _integration with the lasting-effects exemption removed (any zero-contrast split counts)."""
    k = len(ps)
    short = t1 - t
    same_h = {(i, j): roots[i] == roots[j] for i in range(k) for j in range(k)}
    parent = list(range(k))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    boxes = [[c13._box(D[i, w]) for w in range(D.shape[1])] for i in range(k)]
    pairs = []
    for i in range(k):
        for j in range(i + 1, k):
            end = D.shape[1] - 1 if same_h[(i, j)] else short
            if any(c13._boxes_close(boxes[i][w], boxes[j][w]) for w in range(end)):
                pairs.append((i, j, end))
    if pairs:
        dbl = c13.rerun(H, t, Tend, [ps[i] | ps[j] for i, j, _ in pairs], world)
        for n, (i, j, end) in enumerate(pairs):
            if (Hw[1:end + 1] ^ single[i, 1:end + 1] ^ single[j, 1:end + 1] ^ dbl[n, 1:end + 1]).any():
                parent[find(i)] = find(j)
    comps = {}
    for i in range(k):
        comps.setdefault(find(i), []).append(i)
    comps = list(comps.values())
    if len(comps) == 1:
        return True, comps
    allp = frozenset().union(*ps)
    none = c13.rerun(H, t, Tend, [allp], world)[0]
    c = len(comps)
    unresolved = False
    for mask in range(1, 2 ** (c - 1)):
        Pi = [i for m in range(c - 1) if mask >> m & 1 for i in comps[m + 1]]
        Qi = [i for i in range(k) if i not in Pi]
        joined = any(same_h[(i, j)] for i in Pi for j in Qi)
        end = Tend - t if joined else short
        P = frozenset().union(*[ps[i] for i in Pi])
        Q = frozenset().union(*[ps[i] for i in Qi])
        rp, rq = c13.rerun(H, t, Tend, [P, Q], world)
        if (Hw[1:end + 1] ^ rp[1:end + 1] ^ rq[1:end + 1] ^ none[1:end + 1]).any():
            continue
        if not joined:
            return False, comps
        unresolved = True
    return (None if unresolved else True), comps


def set_variant(v):
    c15.core, c15._integration = _orig_core, _orig_int
    if v == "no-idle":
        c15.core = lambda f: None
    elif v == "no-lasting":
        c15._integration = _int_no_lasting
    elif v == "no-idle-no-lasting":
        c15.core = lambda f: None
        c15._integration = _int_no_lasting


def all_parts():
    parts = [("registered",) + p for p in c12.probe_parts()]
    gl = [x for _, x in zip(range(7), c13.gliders_configs())][4:7]
    ea = [x for _, x in zip(range(7), c13.eater_configs())][4:7]
    for k, x in enumerate(gl, 4):
        parts += [("unseen",) + p for p in c13.glider_parts(x, f"U-gliders {k}")]
    for k, x in enumerate(ea, 4):
        parts += [("unseen",) + p for p in c13.eater_parts(x, f"U-eater {k}")]
    return parts


def ablate():
    parts = all_parts()
    cols = [c for c in c13.collision_configs(6) if c["placement"] != (37, 39)][3:6]
    variants = ["C15", "no-idle", "no-lasting", "no-idle-no-lasting", "C14"]
    print("| Set | Board | Part | Target | " + " | ".join(variants) + " |")
    print("|---|---|---|---|" + "---|" * len(variants))
    for kind, sec, name, target, H, tr, lo, hi, want, rule in parts:
        cells = []
        for v in variants:
            if v == "C14":
                fl = c14.c14(c14.world_of(rule))(H, tr)
            else:
                set_variant(v)
                fl = c15.c14(c15.world_of(rule))(H, tr)
            ok, bad = c13.part_ok(fl, tr, lo, hi, want)
            cells.append(("✓" if ok else "✗") + f" {[b for b in bad if lo <= b < hi][:4] if want else ''}")
        print(f"| {kind} | {sec.split(':')[0][:28]} | {name} | {target} | " + " | ".join(cells) + " |", flush=True)
    for c in cols:
        cells = []
        for v in variants:
            if v == "C14":
                mk, det = R.score(c, "C14", c14.C14)
            else:
                set_variant(v)
                mk, det = R.score(c, "C15", c15.c14(W))
            cells.append(f"{mk} {det}")
        print(f"| unseen | U-collision {c['placement']} | glider | break at crash | " + " | ".join(cells) + " |",
              flush=True)
    set_variant("C15")


# ---------------------------------------------------------------- checks

def translate_of(Ha, Hb, max_dt=40):
    """Is Hb a space-time translate of Ha after some step? Returns (dt, dr, dc) or None."""
    for dt in range(0, max_dt + 1):
        a, b = Ha[60], Hb[60 + dt] if 60 + dt < len(Hb) else None
        if b is None:
            break
        fa, fb = frame_of(a), frame_of(b)
        if len(fa) != len(fb) or not fa:
            continue
        ra, ca = min(fa)
        rb, cb = min(fb)
        dr, dc = rb - ra, cb - ca
        if all(np.array_equal(np.roll(Ha[u], (dr, dc), axis=(0, 1)), Hb[u + dt])
               for u in range(0, len(Ha) - dt)):
            return dt, dr, dc
    return None


def checks():
    reg_e, reg_g = PR.probe_eater(), PR.probe_gliders()
    ea = [x for _, x in zip(range(7), c13.eater_configs())]
    gl = [x for _, x in zip(range(7), c13.gliders_configs())]
    print("Translates of the registered boards (dt, dr, dc):")
    for k, x in enumerate(ea):
        print(f"  eater board {k} (eater at {x['e0']}): {translate_of(reg_e['H'], x['H'])}")
    for k, x in enumerate(gl):
        prev = [translate_of(gl[j]['H'], x['H']) for j in range(k)]
        print(f"  glider board {k} (B at {x['b0']}): of registered {translate_of(reg_g['H'], x['H'])}; "
              f"of earlier boards {prev}")
    print("Noise flips within two cells of a tracked glider, during its tracked span:")
    import c15_iter as I
    for eps in (1e-4, 1e-3):
        for seed in (0, 1, 2):
            H, w = I.noisy_life(eps, seed)
            out = []
            for g0 in ((10, 10), (10, 60)):
                tr, _ = C.track_glider(H, C.glider_at(*g0), 0)
                n = 0
                for t in sorted(tr)[1:]:
                    near = C.dilate(tr[t - 1], 2)
                    n += sum(1 for p in near if w.noise[t][p])
                out.append((max(tr), n))
            print(f"  eps {eps:g} seed {seed}: (tracked to, flips near) A {out[0]}, B {out[1]}")
    print("C14's candidate with C15's ring-aware jam builder:")
    import c14_iter as J
    J.runs = I.runs
    r, t = J.moving()
    print("\n".join(r))
    print(f"  jams without an event: {t['jams'][0]} of {t['jams'][1]}")


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "hunt"
    {"hunt": hunt, "ablate": ablate, "checks": checks}[mode]()
