"""C12: outflow share. Declared in notes/runs/2026-11-17-c12.md before this code ran.

For a step t -> t+1: receivers R are the cells at t+1 with an input in the
footprint F_t. Per receiver c, own_c = H(Y_c | S_c) as in C11 (same ensembles,
exact enumeration). out = sum own over R & F_{t+1} / sum own over R.
Rerun: python3 tools/gol/c12.py
"""
import sys

import numpy as np

import c11
import cases as C
import probes as PR
import run as R
from c11 import LIFE, R184, C_steps, score, fmt, mark
from life import N

# --- the score ---


def receivers(Ft, shape, rule):
    if len(shape) == 2:
        return frozenset(((r - o[0]) % shape[0], (c - o[1]) % shape[1])
                         for r, c in Ft for o in rule.offs)
    return frozenset((i - o) % shape[0] for i in Ft for o in rule.offs)


def out_share(Ht, Ft, Fu, rule, ens):
    """None when the previous stage sends no information."""
    if not Ft:
        return None
    Rt = receivers(Ft, Ht.shape, rule)
    den = c11.step_terms(Ht, Ft, Rt, rule, ens)[0]
    if den == 0:
        return None
    num = c11.step_terms(Ht, Ft, Rt & Fu, rule, ens)[0] if Rt & Fu else 0.0
    return num / den


def shares(H, tr, rule=LIFE, ens="knockout"):
    return [out_share(np.asarray(H[t]), tr[t], tr[u], rule, ens) for t, u in C_steps(tr)]


def candidate(theta, ens="knockout", rule=LIFE):
    def judge(H, tr):
        return [s is None or s > theta for s in shares(H, tr, rule, ens)]
    return judge


def anchors(ens, shares_fn=shares):
    g, s = C.case_glider(), C.case_splice()
    gs = score(shares_fn(g["H"], g["tracings"][0], ens=ens))
    ss = score(shares_fn(s["H"], s["tracings"][0], ens=ens))
    return gs, ss, (gs + ss) / 2


# Frozen after the anchor run, before any other case was scored. None until then.
THETA = {"knockout": 0.6304155159512824 / 2, "flip": 0.2818022981396315 / 2}


# --- generic reporting, shared with the combined run ---

class Measure:
    """A per-step judgement: shares_fn gives a number per step (or None); carried when > theta.
    For the combined run, flags_fn overrides."""

    def __init__(self, name, shares_fn, theta, ens, flags_fn=None):
        self.name, self.shares_fn, self.theta, self.ens = name, shares_fn, theta, ens
        self.flags_fn = flags_fn

    def sh(self, H, tr, rule=LIFE):
        return self.shares_fn(H, tr, rule=rule, ens=self.ens)

    def flags(self, H, tr, rule=LIFE, f=1.0):
        if self.flags_fn:
            return self.flags_fn(H, tr, rule, f)
        return [s is None or s > f * self.theta for s in self.sh(H, tr, rule)]

    def cand(self, f=1.0):
        def judge(H, tr):
            return self.flags(H, tr, LIFE, f)
        return judge


def grid(m, cases):
    rows, detail, shift_fail, verdicts = [], [], [], {}
    for case in cases:
        sc = [score(m.sh(case["H"], tr)) for tr in case["tracings"]]
        mk, v = R.score(case, m.name, m.cand())
        mlo, _ = R.score(case, m.name, m.cand(0.8))
        mhi, _ = R.score(case, m.name, m.cand(1.2))
        msh, _ = R.score(R.shifted(case), m.name, m.cand())
        H7 = np.concatenate([np.zeros((7,) + case["H"].shape[1:], dtype=bool), case["H"]])
        same_t = all(m.flags(case["H"], tr) == m.flags(H7, {t + 7: f for t, f in tr.items()})
                     for tr in case["tracings"])
        if msh != mk or not same_t:
            shift_fail.append(case["name"])
        verdicts[case["name"]] = (mk, v)
        rows.append(f"| {case['name']} | {', '.join(fmt(x) for x in sc)} | {v} | "
                    f"{case['target']} | {mk} | {mlo} | {mhi} |")
        for k, tr in enumerate(case["tracings"]):
            sh = m.sh(case["H"], tr)
            low = sorted(((s, i) for i, s in enumerate(sh) if s is not None))[:4]
            nj = sum(s is None for s in sh)
            detail.append(f"- {case['name']} [{k}]: lowest steps {[(i, round(s, 3)) for s, i in low]}; "
                          f"steps not judged {nj} of {len(sh)}")
    head = [f"| Case | Score | {m.name} verdict | Target | Match | at 0.8 θ | at 1.2 θ |",
            "|---|---|---|---|---|---|---|"]
    return head + rows, detail, shift_fail, verdicts


def carried_on(flags, keys, lo, hi):
    bad = [k for k, x in zip(keys, flags) if x is not True]
    return all(not (lo <= b < hi) for b in bad), bad


def probe_parts():
    """The registered probe parts, as in C11: (section, name, target, H, tracing, lo, hi, want, rule)."""
    parts = []
    g = PR.probe_gliders()
    H, s, e = g["H"], g["start"], g["end"]
    trA, _ = C.track_glider(H, g["A"][0], 0)
    trB, _ = C.track_glider(H, g["B"][0], 0)
    union = {t: trA[t] | trB[t] for t in range(0, s)}
    Rt = C.follow(H, c11.frame_of(H[s]), s, C.T)
    sec = f"Two gliders that interact (B at {g['b0']}; interval {s}–{e})"
    parts += [(sec, "Glider A before contact", "carried", H, trA, 0, s - 1, True, LIFE),
              (sec, "Glider B before contact", "carried", H, trB, 0, s - 1, True, LIFE),
              (sec, "A and B as one, before contact", "uncarried", H, union, 0, s - 1, False, LIFE),
              (sec, f"The interaction, {s}–{e}", "carried", H, Rt, s, e, True, LIFE)]
    q = PR.probe_eater()
    H, s, e = q["H"], q["start"], q["end"]
    trG, stop = C.track_glider(H, q["G"][0], 0)
    Rt = C.follow(H, c11.frame_of(H[s]), s, C.T)
    E3 = PR.follow_piece(H, q["eater"])
    G2 = {**{t: trG[t] for t in trG}, **{t: E3[t] for t in E3 if t > max(trG)}}
    sec = f"Glider meets an eater (eater at {q['e0']}; interval {s}–{e}; glider tracker stops at {stop})"
    parts += [(sec, "Glider until contact", "carried", H, trG, 0, s - 1, True, LIFE),
              (sec, "Glider continued into the merged piece", "uncarried", H, G2, 0, C.T, False, LIFE),
              (sec, f"The interaction, {s}–{e}", "carried", H, Rt, s, e, True, LIFE),
              (sec, "The eater persists (followed piece)", "carried", H, E3, 0, C.T, True, LIFE)]
    j = PR.probe_jam()
    Hj = np.array(j["H"])
    sec = f"Rule-184 jam (ring of {PR.L}; full turnover by step 40: {j['turnover']})"
    parts += [(sec, "The jam holds", "carried", Hj, j["jam"], 0, C.T, True, R184),
              (sec, "A car through the jam", "carried", Hj, j["car"], 0, C.T, True, R184)]
    return parts


def probe_report(m, parts):
    out, sec0, res = [], None, {}
    head = [f"| Part | Target | Score | {m.name} | at 0.8 θ | at 1.2 θ | Steps not carried |",
            "|---|---|---|---|---|---|---|"]
    for sec, name, target, H, tr, lo, hi, want, rule in parts:
        if sec != sec0:
            out += ([""] if sec0 else []) + [f"### {sec}", ""] + head
            sec0 = sec
        keys = [t for t, _ in C_steps(tr)]
        sh = m.sh(H, tr, rule)
        sel = [s for k, s in zip(keys, sh) if lo <= k < hi and s is not None]
        sc = min(sel) if sel else None
        marks = []
        for f in (1.0, 0.8, 1.2):
            ok, bad = carried_on(m.flags(H, tr, rule, f), keys, lo, hi)
            if not want:
                ok = not all(x is True for x in m.flags(H, tr, rule, f))
            marks.append(mark(ok == want) if want else mark(ok))
            if f == 1.0:
                bad0 = bad
        res[name] = (marks[0], sc, dict(zip(keys, sh)))
        out.append(f"| {name} | {target} | {fmt(sc)} | {marks[0]} | {marks[1]} | {marks[2]} | {bad0[:8]} |")
    return out + [""], res


def elemental(m):
    g = C.case_glider()
    H, tr = g["H"], g["tracings"][0]
    sites = sorted(frozenset().union(*tr.values()))
    scores, carried = [], 0
    for p in sites:
        site = {t: frozenset([p]) for t in range(len(H))}
        sh = m.sh(H, site)
        scores.append(score(sh))
        if all(x is True for x in m.flags(H, site)):
            carried += 1
    return len(sites), carried, scores


def extras(m):
    out = []
    g = C.case_glider()
    H = g["H"]
    allc = frozenset((r, c) for r in range(N) for c in range(N))
    wb = m.sh(H, {t: allc for t in range(len(H))})
    js = [s for s in wb if s is not None]
    out.append(f"Whole board scored directly: min {fmt(min(js) if js else None)}, steps not judged "
               f"{sum(s is None for s in wb)}. Check 3 refuses it (nested), as in C11.")
    Hi, trg, inc = c11.case_incar()
    out.append(f"Incar alone (steps {min(inc)}–{max(inc)}): score {fmt(score(m.sh(Hi, inc)))}; "
               f"same glider / same incar is nested at check 3.")
    u = C.case_union()
    out.append(f"Trout-turkey (union build, no target): score {fmt(score(m.sh(u['H'], u['tracings'][0])))}.")
    n, k, sc = elemental(m)
    js = [s for s in sc if s is not None]
    low = sum(s <= m.theta for s in js) if m.theta is not None else None
    out.append(f"Elemental: {n} crossed cells as single sites: {k} carried; judged {len(js)}; "
               f"scores min {fmt(min(js))}, median {fmt(sorted(js)[len(js) // 2])}, max {fmt(max(js))}; "
               f"at or below θ: {low}.")
    return out, dict(elemental=(n, k, js, low))


def all_grid_cases():
    return [C.case_glider(), c11.case_one_arrangement()] + C.all_cases()[1:]


def report(m, cases, parts):
    out = [f"## {m.name}, ensemble {m.ens}, θ = {fmt(m.theta)}", ""]
    rows, detail, sf, verdicts = grid(m, cases)
    out += rows
    out += ["", "Shift check (7 rows, 13 columns; 7 steps): " +
            ("every mark and flag unchanged." if not sf else f"changed: {sf}"), ""]
    ex, exd = extras(m)
    out += ex + [""]
    pr, res = probe_report(m, parts)
    out += pr
    out += ["Details:"] + detail + [""]
    return out, verdicts, res, exd


def main():
    if "--anchors" in sys.argv:
        for ens in ("knockout", "flip"):
            gs, ss, th = anchors(ens)
            print(f"{ens}: glider {gs}, splice {ss}, theta {th}")
        return 0
    cases, parts = all_grid_cases(), probe_parts()
    out = []
    for ens in ("knockout", "flip"):
        gs, ss, th = anchors(ens)
        assert THETA[ens] is not None and abs(th - THETA[ens]) < 1e-12, (ens, th, THETA[ens])
        out.append(f"Anchors ({ens}): glider score {fmt(gs)}, splice score {fmt(ss)}, θ = {th:.3f}.")
        m = Measure("C12", shares, th, ens)
        rep, verdicts, res, exd = report(m, cases, parts)
        out += [""] + rep
        if ens == "knockout":
            # prediction data
            sp = shares(C.case_splice()["H"], C.case_splice()["tracings"][0])
            si = C.case_step_indexed()
            si_sh = shares(si["H"], si["tracings"][0])
            al = C.case_alternating_splice()
            al_sh = shares(al["H"], al["tracings"][0])
            out.append(f"Prediction 1 data: splice out at 99 = {fmt(sp[99])}; step-indexed out at 99 = "
                       f"{fmt(si_sh[99])}; alternating max out {fmt(max(s for s in al_sh if s is not None))}.")
            car = score(list(res["A car through the jam"][2].values()))
            out.append(f"Prediction 7 data: car score {fmt(car)}.")
            for nm in ("Collision, annihilating (first build)", "Collision"):
                case = next(c for c in cases if c["name"] == nm)
                sh = shares(case["H"], case["tracings"][0])
                tc = case["crash"]
                out.append(f"Collision data, {nm}: crash {tc}; out at steps {tc - 3}..{tc + 3}: "
                           f"{[fmt(sh[i]) if i < len(sh) else '-' for i in range(tc - 3, tc + 4)]}.")
            out.append("")
    print("\n".join(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
