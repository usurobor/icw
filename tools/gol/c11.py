"""C11: own-past share. Declared in notes/runs/2026-11-17-c11.md before this code ran.

For a step t -> t+1 of a tracing: Y is the next footprint's cells at t+1, O the
inputs that belong to the footprint at t, S the other inputs. Ensemble: each
varying input independently kept or toggled with probability 1/2 (knockout:
live inputs only, toggled to the quiescent 0; flip: every input). Per cell of Y,
own = H(Y_c | S_c), sur = H(Y_c | O_c), enumerated exactly.
share = sum own / sum (own + sur). Rerun: python3 tools/gol/c11.py
"""
import math
import sys
from collections import Counter
from functools import lru_cache

import numpy as np

import cases as C
import probes as PR
import run as R
from life import GLIDER, N, board, run, frame_of, step as life_step

# --- the rule, only through the transition function (rule 13) ---


class Rule:
    def __init__(self, name, offs, tab):
        self.name, self.offs, self.tab = name, offs, tab


def _life_rule():
    offs = [(i, j) for i in (-1, 0, 1) for j in (-1, 0, 1)]
    tab = []
    for idx in range(2 ** len(offs)):
        b = np.zeros((5, 5), dtype=bool)
        for k, (i, j) in enumerate(offs):
            if idx >> k & 1:
                b[2 + i, 2 + j] = True
        tab.append(int(life_step(b)[2, 2]))
    return Rule("life", offs, tuple(tab))


def _rule184():
    offs = [-1, 0, 1]
    tab = []
    for idx in range(8):
        a = np.zeros(5, dtype=bool)
        for k, o in enumerate(offs):
            if idx >> k & 1:
                a[2 + o] = True
        tab.append(int(PR.step184(a)[2]))
    return Rule("184", offs, tuple(tab))


LIFE, R184 = _life_rule(), _rule184()


def h2(p):
    return 0.0 if p <= 0 or p >= 1 else -(p * math.log2(p) + (1 - p) * math.log2(1 - p))


@lru_cache(maxsize=None)
def cell_terms(tab, nbits, pattern, own, vary):
    """(H(Y|S), H(Y|O)) for one target cell, exact over the ensemble."""
    ov = [k for k in range(nbits) if vary >> k & 1 and own >> k & 1]
    sv = [k for k in range(nbits) if vary >> k & 1 and not own >> k & 1]

    def mask(bits, a):
        m = 0
        for i, k in enumerate(bits):
            if a >> i & 1:
                m |= 1 << k
        return m
    om = [mask(ov, a) for a in range(2 ** len(ov))]
    sm = [mask(sv, a) for a in range(2 ** len(sv))]
    Y = [[tab[pattern ^ o ^ s] for s in sm] for o in om]
    no, ns = len(om), len(sm)
    h_given_s = sum(h2(sum(Y[i][j] for i in range(no)) / no) for j in range(ns)) / ns
    h_given_o = sum(h2(sum(Y[i]) / ns) for i in range(no))  / no
    return h_given_s, h_given_o


def step_terms(Ht, Ft, Fu, rule, ens):
    """Summed own and sur terms for the step whose footprints are Ft, Fu."""
    if not Fu:
        return 0.0, 0.0
    shape = Ht.shape
    ownb = np.zeros(shape, dtype=bool)
    if Ht.ndim == 2:
        for r, c in Ft:
            ownb[r % shape[0], c % shape[1]] = True
        tg = np.array(list(Fu))
    else:
        for i in Ft:
            ownb[i % shape[0]] = True
        tg = np.array(list(Fu))
    pat = np.zeros(len(tg), dtype=np.int64)
    own = np.zeros(len(tg), dtype=np.int64)
    for k, off in enumerate(rule.offs):
        if Ht.ndim == 2:
            idx = ((tg[:, 0] + off[0]) % shape[0], (tg[:, 1] + off[1]) % shape[1])
        else:
            idx = ((tg + off) % shape[0],)
        pat |= Ht[idx].astype(np.int64) << k
        own |= ownb[idx].astype(np.int64) << k
    nb = len(rule.offs)
    full = (1 << nb) - 1
    so = ss = 0.0
    for (p, o), n in Counter(zip(pat.tolist(), own.tolist())).items():
        vary = p if ens == "knockout" else full
        a, b = cell_terms(rule.tab, nb, p, o, vary)
        so += n * a
        ss += n * b
    return so, ss


def shares(H, tr, rule=LIFE, ens="knockout"):
    """Share per step (None: neither source carries information)."""
    out = []
    for t, u in C_steps(tr):
        so, ss = step_terms(np.asarray(H[t]), tr[t], tr[u], rule, ens)
        out.append(None if so + ss == 0 else so / (so + ss))
    return out


def C_steps(tr):
    ts = sorted(tr)
    return list(zip(ts[:-1], ts[1:]))


def score(sh):
    js = [s for s in sh if s is not None]
    return min(js) if js else None


def candidate(theta, ens="knockout", rule=LIFE):
    def judge(H, tr):
        return [s is None or s > theta for s in shares(H, tr, rule, ens)]
    return judge


# --- cases built for this run ---

def case_one_arrangement():
    """Glider B on glider A's lane, 20 cells behind: crosses A's sites 80 steps later."""
    H = run(board((GLIDER, (40, 40)), (GLIDER, (20, 20))), C.T)
    a, sa = C.track_glider(H, C.glider_at(40, 40), 0)
    b, sb = C.track_glider(H, C.glider_at(20, 20), 0)
    assert sa is None and sb is None and b[80] == a[0]
    return dict(name="Two gliders, one arrangement", H=H, tracings=[a, b], target="holds")


SQUARE = (20, 36)  # rows and columns [20, 36): the glider enters and leaves within the run


def case_incar():
    g = C.case_glider()
    tr = g["tracings"][0]
    lo, hi = SQUARE
    inside = {t: f for t, f in tr.items() if all(lo <= r < hi and lo <= c < hi for r, c in f)}
    ts = sorted(inside)
    assert ts and ts[-1] < max(tr) and ts == list(range(ts[0], ts[-1] + 1))
    return g["H"], tr, inside


# --- reporting ---

def fmt(x):
    return "—" if x is None else f"{x:.3f}"


def mark(ok):
    return "✓" if ok else "✗"


def anchors(ens):
    g, s = C.case_glider(), C.case_splice()
    gs = score(shares(g["H"], g["tracings"][0], ens=ens))
    ss = score(shares(s["H"], s["tracings"][0], ens=ens))
    return gs, ss, (gs + ss) / 2


# Frozen after the anchor run, before any other case was scored.
THETA = {"knockout": 0.5, "flip": 0.4474536500442652 / 2}


def grid(theta, ens, cases):
    rows, detail = [], []
    cand = candidate(theta, ens)
    lo_c, hi_c = candidate(0.8 * theta, ens), candidate(1.2 * theta, ens)
    shift_fail = []
    for case in cases:
        sc = [score(shares(case["H"], tr, ens=ens)) for tr in case["tracings"]]
        mk, v = R.score(case, "C11", cand)
        mlo, _ = R.score(case, "C11", lo_c)
        mhi, _ = R.score(case, "C11", hi_c)
        msh, _ = R.score(R.shifted(case), "C11", cand)
        # time shift: 7 empty frames before the history
        H7 = np.concatenate([np.zeros((7,) + case["H"].shape[1:], dtype=bool), case["H"]])
        same_t = all(shares(case["H"], tr, ens=ens) ==
                     shares(H7, {t + 7: f for t, f in tr.items()}, ens=ens)
                     for tr in case["tracings"])
        if msh != mk or not same_t:
            shift_fail.append(case["name"])
        rows.append(f"| {case['name']} | {', '.join(fmt(x) for x in sc)} | {v} | "
                    f"{case['target']} | {mk} | {mlo} | {mhi} |")
        for k, tr in enumerate(case["tracings"]):
            sh = shares(case["H"], tr, ens=ens)
            low = sorted(((s, i) for i, s in enumerate(sh) if s is not None))[:4]
            nj = sum(s is None for s in sh)
            detail.append(f"- {case['name']} [{k}]: lowest steps {[(i, round(s, 3)) for s, i in low]}; "
                          f"steps not judged {nj} of {len(sh)}")
    head = ["| Case | Score | C11 verdict | Target | Match | at 0.8 θ | at 1.2 θ |",
            "|---|---|---|---|---|---|---|"]
    return head + rows, detail, shift_fail


def interval_min(sh, lo, hi):
    v = [s for i, s in enumerate(sh) if lo <= i < hi and s is not None]
    return min(v) if v else None


def carried_on(sh, lo, hi, theta, keys):
    """Every step t -> t+1 with lo <= t < hi carried. keys[i] is the start step of step i."""
    bad = [keys[i] for i, s in enumerate(sh) if s is not None and s <= theta]
    return all(not (lo <= b < hi) for b in bad), bad


def probe_report(theta, ens):
    out = []
    head = ["| Part | Target | Score | C11 | Steps not carried |", "|---|---|---|---|---|"]

    def part(name, target, H, tr, lo, hi, want=True, rule=LIFE):
        keys = [t for t, _ in C_steps(tr)]
        sh = shares(H, tr, rule, ens)
        ok, bad = carried_on(sh, lo, hi, theta, keys)
        sel = [s for k, s in zip(keys, sh) if lo <= k < hi and s is not None]
        sc = min(sel) if sel else None
        return f"| {name} | {target} | {fmt(sc)} | {mark(ok == want)} | {bad[:8]} |", dict(zip(keys, sh))

    g = PR.probe_gliders()
    H, s, e = g["H"], g["start"], g["end"]
    trA, _ = C.track_glider(H, g["A"][0], 0)
    trB, _ = C.track_glider(H, g["B"][0], 0)
    union = {t: trA[t] | trB[t] for t in range(0, s)}
    Rt = C.follow(H, frame_of(H[s]), s, C.T)
    r1, _ = part("Glider A before contact", "carried", H, trA, 0, s - 1)
    r2, _ = part("Glider B before contact", "carried", H, trB, 0, s - 1)
    r3, _ = part("A and B as one, before contact", "uncarried", H, union, 0, s - 1, want=False)
    r4, shR = part(f"The interaction, {s}–{e}", "carried", H, Rt, s, e)
    inside = [v for k, v in shR.items() if s <= k < e and v is not None]
    after = [v for k, v in shR.items() if k >= e and v is not None]
    p6a = (min(inside) if inside else None, min(after) if after else None)
    out += [f"### Two gliders that interact (B at {g['b0']}; interval {s}–{e})", ""] + head + [r1, r2, r3, r4, ""]

    q = PR.probe_eater()
    H, s, e = q["H"], q["start"], q["end"]
    trG, stop = C.track_glider(H, q["G"][0], 0)
    Rt = C.follow(H, frame_of(H[s]), s, C.T)
    E3 = PR.follow_piece(H, q["eater"])
    G2 = {**{t: trG[t] for t in trG}, **{t: E3[t] for t in E3 if t > max(trG)}}
    r1, _ = part("Glider until contact", "carried", H, trG, 0, s - 1)
    r2, _ = part("Glider continued into the merged piece", "uncarried", H, G2, 0, C.T, want=False)
    r3, _ = part(f"The interaction, {s}–{e}", "carried", H, Rt, s, e)
    r4, shE = part("The eater persists (followed piece)", "carried", H, E3, 0, C.T)
    inside = [v for k, v in shE.items() if s <= k < e and v is not None]
    before = [v for k, v in shE.items() if k < s and v is not None]
    p6b = (min(inside) if inside else None, min(before) if before else None)
    out += [f"### Glider meets an eater (eater at {q['e0']}; interval {s}–{e}; glider tracker stops at {stop})", ""] + head + [r1, r2, r3, r4, ""]

    j = PR.probe_jam()
    Hj = np.array(j["H"])
    r1, shJ = part("The jam holds", "carried", Hj, j["jam"], 0, C.T, rule=R184)
    r2, shC = part("A car through the jam", "carried", Hj, j["car"], 0, C.T, rule=R184)
    jam_sc = score(list(shJ.values()))
    car_sc = score(list(shC.values()))
    out += [f"### Rule-184 jam (ring of {PR.L}; full turnover by step 40: {j['turnover']})", ""] + head + [r1, r2, ""]
    return out, dict(p6a=p6a, p6b=p6b, jam=jam_sc, car=car_sc)


def elemental(theta, ens):
    g = C.case_glider()
    H, tr = g["H"], g["tracings"][0]
    sites = sorted(frozenset().union(*tr.values()))
    scores, carried = [], 0
    for p in sites:
        sh = shares(H, {t: frozenset([p]) for t in range(len(H))}, ens=ens)
        sc = score(sh)
        scores.append(sc)
        if all(s is None or s > theta for s in sh):
            carried += 1
    return len(sites), carried, scores


def whole_board(ens):
    g = C.case_glider()
    H = g["H"]
    allc = frozenset((r, c) for r in range(N) for c in range(N))
    sh = shares(H, {t: allc for t in range(len(H))}, ens=ens)
    return score(sh), max(s for s in sh if s is not None), sum(s is None for s in sh)


def report(ens, theta, cases):
    out = [f"## Ensemble: {ens}, θ = {theta:.3f}", ""]
    rows, detail, sf = grid(theta, ens, cases)
    out += rows
    out += ["", "Shift check (7 rows, 13 columns; 7 steps): " +
            ("every mark and share unchanged." if not sf else f"changed: {sf}"), ""]
    H = cases[0]["H"]
    triv = (R.checks_1_to_3(H, R.cell_labels(H), np.zeros(H.size, dtype=np.int64)),
            R.checks_1_to_3(H, R.cell_labels(H), np.arange(H.size, dtype=np.int64)))
    wb = whole_board(ens)
    out.append(f"Trivial groupings: whole board {triv[0]}, each occurrence alone {triv[1]} "
               f"(check 3). C11 scored directly on the whole board: min share {fmt(wb[0])}, "
               f"max {fmt(wb[1])}, steps not judged {wb[2]}.")
    Hi, trg, inc = case_incar()
    chk = R.checks_1_to_3(Hi, R.tracing_labels(Hi, [trg]), R.tracing_labels(Hi, [inc]))
    out.append(f"Incars (steps {min(inc)}–{max(inc)} inside rows and columns {SQUARE}): "
               f"same glider / same incar is {chk} at checks 1–3; C11 score of the incar "
               f"tracing alone {fmt(score(shares(Hi, inc, ens=ens)))}.")
    u = C.case_union()
    out.append(f"Trout-turkey (union build, no target): score "
               f"{fmt(score(shares(u['H'], u['tracings'][0], ens=ens)))}.")
    n, k, sc = elemental(theta, ens)
    js = [s for s in sc if s is not None]
    out.append(f"Elemental: {n} cells the glider crosses, each traced as one site over the run: "
               f"{k} carried; scores min {fmt(min(js))}, median {fmt(sorted(js)[len(js) // 2])}, "
               f"max {fmt(max(js))}; at or below θ: {sum(s <= theta for s in js)}.")
    out.append("")
    pr, extra = probe_report(theta, ens)
    out += pr
    out.append(f"Prediction 6 data: interaction min inside {fmt(extra['p6a'][0])}, after "
               f"{fmt(extra['p6a'][1])}; eater piece min inside {fmt(extra['p6b'][0])}, before "
               f"{fmt(extra['p6b'][1])}. Jam score {fmt(extra['jam'])}, car score {fmt(extra['car'])}.")
    out += ["", "Details:"] + detail + [""]
    return out


def main():
    if "--anchors" in sys.argv:
        for ens in ("knockout", "flip"):
            gs, ss, th = anchors(ens)
            print(f"{ens}: glider {gs}, splice {ss}, theta {th}")
        return 0
    cases = [C.case_glider(), case_one_arrangement()] + C.all_cases()[1:]
    out = []
    for ens in ("knockout", "flip"):
        gs, ss, th = anchors(ens)
        if THETA[ens] is not None:
            assert abs(th - THETA[ens]) < 1e-12, (ens, th, THETA[ens])
        out.append(f"Anchors ({ens}): glider score {fmt(gs)}, splice score {fmt(ss)}, θ = {th:.3f}.")
        out += [""] + report(ens, th, cases)
    print("\n".join(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
