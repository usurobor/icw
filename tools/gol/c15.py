"""C15: C14 with one notion of interacting (history joins interaction components); ring seam.
Declared in notes/runs/2026-11-18-c15.md before this code ran. Rerun: python3 tools/gol/c15.py
"""
import sys

import numpy as np
from scipy import ndimage

import c11
import c12
import c13
import cases as C
import hunt13 as HU
import probes as PR
import run as R
from candidates import steps, jaccard
from c13 import rerun, _box, _boxes_close, e_flags, elemental, unique_best
from life import N, board, run, frame_of, isolated_next

T = C.T


# ---------------------------------------------------------------- wrap-aware Life

def pieces_wrap(frame, n=N):
    if not frame:
        return []
    b = np.zeros((n, n), dtype=bool)
    for r, c in frame:
        b[r % n, c % n] = True
    lab, k = ndimage.label(b, structure=np.ones((3, 3)))
    parent = list(range(k + 1))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    for i in range(n):
        for d in (-1, 0, 1):
            j = (i + d) % n
            for a, b_ in ((lab[0, i], lab[n - 1, j]), (lab[i, 0], lab[j, n - 1])):
                if a and b_:
                    parent[find(a)] = find(b_)
    a, b_ = lab[0, 0], lab[n - 1, n - 1]
    if a and b_:
        parent[find(a)] = find(b_)
    a, b_ = lab[0, n - 1], lab[n - 1, 0]
    if a and b_:
        parent[find(a)] = find(b_)
    groups = {}
    for r, c in zip(*np.nonzero(lab)):
        groups.setdefault(find(lab[r, c]), set()).add((int(r), int(c)))
    return [frozenset(g) for g in groups.values()]


def evolve_wrap(frame):
    return isolated_next(frame)


LIFE_X = c13.World("life", 2, c13.life_step_count, evolve_wrap, pieces_wrap, C.dilate, c11.LIFE.tab)
LIFE_XT = c13.World("life", 2, c13.life_step_table,
                    lambda f: frame_of(c13.life_step_table(np.pad(np.zeros((N, N), bool), 0) | _tb(f))),
                    pieces_wrap, C.dilate, c11.LIFE.tab)


def _tb(f):
    b = np.zeros((N, N), dtype=bool)
    for r, c in f:
        b[r % N, c % N] = True
    return b


def runs184_wrap(frame, L=PR.L):
    rs = PR.runs184(frame)
    if len(rs) > 1 and 0 in rs[0] and (L - 1) in rs[-1]:
        rs = [rs[0] | rs[-1]] + rs[1:-1]
    return rs


R184 = c13.World("184", 1, c13.r184_step, PR.next184, runs184_wrap, PR.near184, c11.R184.tab)


# ---------------------------------------------------------------- per-step facts

def facts(H, tr, world):
    """One pass in time order: descent joins, then integration, whose components join too."""
    ts = sorted(tr)
    Tend = len(H) - 1
    t1 = ts[-1]
    parent = {}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    out = {}
    prev_ps = None
    for t in ts:
        ps = world.pieces(tr[t])
        for i in range(len(ps)):
            parent[(t, i)] = (t, i)
        produced = [False] * len(ps)
        if prev_ps is not None and prev_ps and ps:
            dels = rerun(H, t - 1, t, prev_ps + [tr[t - 1]], world)[:, -1]
            actual = np.asarray(H[t])
            for i in range(len(prev_ps)):
                ch = world.frame(actual ^ dels[i])
                for j, q in enumerate(ps):
                    if ch & q:
                        parent[find((t - 1, i))] = find((t, j))
            ch_all = world.frame(actual ^ dels[-1])
            produced = [bool(ch_all & q) for q in ps]
        roots = [find((t, i)) for i in range(len(ps))]
        f = dict(ps=ps, produced=produced, roots=roots, idle=[False] * len(ps), int=True)
        out[t] = f
        prev_ps = ps
        if len(ps) < 2 or t == Tend:
            continue
        Hw = np.asarray(H[t:Tend + 1])
        single = rerun(H, t, Tend, ps, world)
        D = Hw[None] ^ single
        f["idle"] = [not D[i, 1:].any() for i in range(len(ps))]
        if t == t1:
            continue
        f["int"], comps = _integration(H, t, t1, Tend, ps, roots, Hw, single, D, world)
        for comp in comps:
            for i in comp[1:]:
                parent[find((t, i))] = find((t, comp[0]))
    return out


def _integration(H, t, t1, Tend, ps, roots, Hw, single, D, world):
    k = len(ps)
    short = t1 - t  # index of the tracing window's end in the run arrays
    hc = {}
    for i, r in enumerate(roots):
        hc.setdefault(r, []).append(i)
    same_h = {(i, j): roots[i] == roots[j] for i in range(k) for j in range(k)}
    parent = list(range(k))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    boxes = [[_box(D[i, w]) for w in range(D.shape[1])] for i in range(k)]
    pairs = []
    for i in range(k):
        for j in range(i + 1, k):
            end = D.shape[1] - 1 if same_h[(i, j)] else short
            if any(_boxes_close(boxes[i][w], boxes[j][w]) for w in range(end)):
                pairs.append((i, j, end))
    if pairs:
        dbl = rerun(H, t, Tend, [ps[i] | ps[j] for i, j, _ in pairs], world)
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
    none = rerun(H, t, Tend, [allp], world)[0]
    c = len(comps)
    unresolved = False
    for mask in range(1, 2 ** (c - 1)):
        Pi = [i for m in range(c - 1) if mask >> m & 1 for i in comps[m + 1]]
        Qi = [i for i in range(k) if i not in Pi]
        joined = any(same_h[(i, j)] for i in Pi for j in Qi)
        end = Tend - t if joined else short
        P = frozenset().union(*[ps[i] for i in Pi])
        Q = frozenset().union(*[ps[i] for i in Qi])
        rp, rq = rerun(H, t, Tend, [P, Q], world)
        if (Hw[1:end + 1] ^ rp[1:end + 1] ^ rq[1:end + 1] ^ none[1:end + 1]).any():
            continue
        if not (Hw[end] ^ rp[end]).any() or not (Hw[end] ^ rq[end]).any():
            continue  # a group without lasting effects does not split the stage
        if not joined:
            return False, comps
        unresolved = True
    return (None if unresolved else True), comps


# ---------------------------------------------------------------- the candidate

def core(f):
    ex = [p for p, pr, idl in zip(f["ps"], f["produced"], f["idle"]) if pr and idl]
    if not ex or len(ex) == len(f["ps"]):
        return None
    return frozenset().union(*[p for p in f["ps"] if p not in ex])


def p_flags(H, tr, world):
    fa = facts(H, tr, world)
    out = []
    for t, u in steps(tr):
        F, X = tr[t], tr[u]
        cF, cX = core(fa[t]), core(fa[u])
        isoF = world.evolve(F)
        bt, bu = world.frame(H[t]), world.frame(H[u])
        conts = [X] + [p for p in world.pieces(bu) if p & world.near(F)] + [frozenset()]
        fwd = unique_best([jaccard(c, isoF) for c in conts], [c != X and c != cX for c in conts])
        preds = [F] + [p for p in world.pieces(bt) if p & world.near(X)] + [frozenset()]
        bwd = unique_best([jaccard(X, world.evolve(p)) for p in preds], [p != F and p != cF for p in preds])
        if not (fwd is True and bwd is True):
            out.append(False)
            continue
        out.append(fa[t]["int"])
    return out


def c14(world=LIFE_X):  # C15
    def judge(H, tr):
        if elemental(tr):
            return e_flags(H, tr, world)
        return p_flags(H, tr, world)
    return judge


C14 = c14()  # the C15 candidate (name kept so the report code is shared)


def world_of(rule):
    return R184 if rule is c11.R184 else LIFE_X


# ---------------------------------------------------------------- report

def mark(ok):
    return "✓" if ok else "✗"


def vword(fl):
    if any(x is not True and x is not None for x in fl):
        return "uncarried"
    return "unresolved" if any(x is None for x in fl) else "holds"


def part_rows(parts):
    rows, n = [], 0
    for sec, name, target, H, tr, lo, hi, want, rule in parts:
        fl = c14(world_of(rule))(H, tr)
        ok, bad = c13.part_ok(fl, tr, lo, hi, want)
        n += ok
        rows.append(f"| {sec.split(':')[0][:40]} | {name} | {target} | {mark(ok)} | {bad[:6]} |")
    return rows, n


def main():
    out = []
    cases = c12.all_grid_cases()
    print("grid", file=sys.stderr)
    rows = ["| Case | Target | C15 | Verdict |", "|---|---|---|---|"]
    m = ref = 0
    sf, rf = [], []
    for case in cases:
        mk, det = R.score(case, "C14", C14)
        _, fl = R.verdict(case, C14)
        ref += fl is not None and any(x is not True for f in fl for x in f)
        m += mk == "✓"
        rows.append(f"| {case['name']} | {case['target']} | {mk} | {det} |")
        for d in ((7, 13), (100, 100)):
            if R.score(R.shifted(case, d), "C14", C14)[0] != mk:
                sf.append((case["name"], d))
        H7 = np.concatenate([np.zeros((7, N, N), dtype=bool), case["H"]])
        for tr in case["tracings"]:
            tr = R.trim(tr)
            a = C14(case["H"], tr)
            if a != C14(H7, {t + 7: f for t, f in tr.items()}):
                sf.append((case["name"], "time"))
            if a != c14(LIFE_XT)(case["H"], tr):
                rf.append(case["name"])
    out += ["### Grid", ""] + rows + [f"| Rows matched | | {m} | |", f"| Rows refused | | {ref} | |", "",
            "Shift check (7 rows and 13 columns; 100 rows and 100 columns; 7 steps): " +
            ("every mark and flag unchanged." if not sf else f"changed: {sf}"),
            "Representation check (lookup table): " + ("every flag unchanged." if not rf else f"changed: {rf}"), ""]

    print("probes", file=sys.stderr)
    head = ["| Board | Part | Target | C15 | Steps not carried |", "|---|---|---|---|---|"]
    pr, n = part_rows(c12.probe_parts())
    out += ["### Registered probes", ""] + head + pr + ["", f"Parts matched: {n} of 10.", ""]

    g = C.case_glider()
    H, tr = g["H"], g["tracings"][0]
    sites = sorted(frozenset().union(*tr.values()))
    nc = sum(all(x is True for x in C14(H, {t: frozenset([p]) for t in range(len(H))})) for p in sites)
    out += [f"Elemental: {nc} of {len(sites)} crossed cells carried.", ""]

    print("unseen", file=sys.stderr)
    parts = []
    gl = [x for _, x in zip(range(7), c13.gliders_configs())][4:7]
    ea = [x for _, x in zip(range(7), c13.eater_configs())][4:7]
    for k, x in enumerate(gl, 4):
        parts += c13.glider_parts(x, f"U-gliders {k}")
    for k, x in enumerate(ea, 4):
        parts += c13.eater_parts(x, f"U-eater {k}")
    pr, n = part_rows(parts)
    cols = [c for c in c13.collision_configs(6) if c["placement"] != (37, 39)][3:6]
    crow = []
    for c in cols:
        mk, det = R.score(c, "C14", C14)
        n += mk == "✓"
        crow.append(f"| U-collision, block at {c['placement']} | glider | break at crash | {mk} | {det} |")
    out += ["### Unseen boards (4th to 6th)", ""] + head + pr + crow + \
        ["", f"Unseen parts matched: {n} of {len(parts) + len(cols)}.", ""]

    print("hunter", file=sys.stderr)
    hc = []
    nc_, _ = c13.new_cases()
    for name, Hn, trn, w in nc_:
        hc.append((name, Hn, trn, LIFE_X if w is c13.LIFE_W else w))
    gq = PR.probe_gliders()
    Rt = C.follow(gq["H"], frame_of(gq["H"][gq["start"]]), gq["start"], T)
    hc.append(("N-1b products as one, from contact (steps after the interval)", gq["H"],
               {t: f for t, f in Rt.items() if t >= gq["end"] - 1}, LIFE_X))
    Hb = run(board((HU.BLOCK, (40, 40)), (HU.BLOCK, (40, 43))), T)
    hc.append(("H-3 bi-block as one", Hb, HU.live(Hb), LIFE_X))
    Hp = run(board((HU.PULSAR, (40, 40))), T)
    hc.append(("H-4 pulsar", Hp, HU.live(Hp), LIFE_X))
    Hg = run(board((HU.GUN, (10, 10))), T)
    gun = frozenset((10 + r, 10 + c) for r, c in HU.GUN)
    hc.append(("H-5 Gosper gun, followed", Hg, PR.follow_piece(Hg, gun), LIFE_X))
    Hl = run(board((HU.LWSS, (60, 100))), T)
    hc.append(("H-8 lightweight spaceship", Hl, HU.live(Hl), LIFE_X))
    trA, _ = C.track_glider(gq["H"], gq["A"][0], 0)
    hc.append(("H-10a glider A into the reaction", gq["H"],
               {**{t: trA[t] for t in trA if t < gq["start"]}, **Rt}, LIFE_X))
    kb = HU.kickback()
    if kb:
        b0, Hk = kb
        ta, _ = C.track_glider(Hk, C.glider_at(40, 40), 0)
        hc.append(("H-10b kickback, A into the output glider", Hk,
                   {**ta, **C.follow(Hk, ta[max(ta)], max(ta), T)}, LIFE_X))
    sh = R.shifted(C.case_glider(), d=(100, 100))
    hc.append(("H-11 glider across the edge", sh["H"], sh["tracings"][0], LIFE_X))
    box = {t: frozenset((r, c) for r in range(min(x for x, _ in f), max(x for x, _ in f) + 1)
                        for c in range(min(y for _, y in f), max(y for _, y in f) + 1))
           for t, f in C.case_glider()["tracings"][0].items()}
    hc.append(("H-15 glider with its bounding box", C.case_glider()["H"], box, LIFE_X))
    rows = ["| Case | C15 | Steps not carried or unresolved |", "|---|---|---|"]
    for name, Hn, trn, w in hc:
        trn = R.trim(trn)
        fl = c14(w)(Hn, trn)
        rows.append(f"| {name} | {vword(fl)} | {[k for (k, _), x in zip(steps(trn), fl) if x is not True][:8]} |")
    out += ["### Hunter and new cases (no target)", ""] + rows
    print("\n".join(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
