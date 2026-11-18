"""Outside review, 18 Nov (notes/reviews/2026-11-18-simpler-o2.md).
Rerun: python3 tools/gol/s1.py conflicts | score
  conflicts  executable checks behind the target conflicts named in the review (T-1, T-2)
  score      candidate S-1 (tracks in the piece graph) on the register, hunter cases and rulings
"""
import sys

import numpy as np

import cases as C
import hunt13 as HU
import probes as PR
from life import GLIDER, BLOCK, N, board, run, frame_of, step

T = C.T


# ---------------------------------------------------------------- conflicts (checked before S-1 was written)

def plane_vs_torus(cells_at, steps_, big=1024):
    """First step at which the 128-torus history differs from the same start on a large plane, folded
    onto the torus. A difference means something came round the board and met something."""
    small = np.zeros((N, N), dtype=bool)
    plane = np.zeros((big, big), dtype=bool)
    off = big // 2 - N // 2
    for r, c in cells_at:
        small[r % N, c % N] = True
        plane[off + r, off + c] = True
    for t in range(1, steps_ + 1):
        small, plane = step(small), step(plane)
        fold = np.zeros((N, N), dtype=bool)
        rr, cc = np.nonzero(plane)
        fold[(rr - off) % N, (cc - off) % N] = True
        if (fold != small).any():
            return t
    return None


def conflicts():
    print("T-1. Things that separate on the plane meet again on the board the harness uses (128 torus).")
    gun = [(10 + r, 10 + c) for r, c in HU.GUN]
    print(f"  Gosper gun at (10, 10): torus and plane first differ at step {plane_vs_torus(gun, 1500)}")
    g = PR.probe_gliders()
    cells = list(frame_of(g["H"][0]))
    print(f"  registered interacting pair (products settle at {g['end']}): first differ at step "
          f"{plane_vs_torus(cells, 1500)}")
    u = C.case_union()
    print(f"  union of two distant gliders: first differ at step {plane_vs_torus(list(frame_of(u['H'][0])), 1500)}")
    print("T-2. Merger by size: the glider against a block.")
    print(f"  glider cells {len(GLIDER)}, block cells {len(BLOCK)}; at the first contact step the merged stage "
          f"is the two unchanged pieces, so overlap with each one-step evolution is "
          f"{len(GLIDER)}/{len(GLIDER) + len(BLOCK)} against {len(BLOCK)}/{len(GLIDER) + len(BLOCK)}")
    q = PR.probe_eater()
    print(f"  eater cells {len(q['eater'])}, glider {len(GLIDER)}: eater larger")



# ---------------------------------------------------------------- S-1 (declared in the review before this code ran)

import hashlib
from fractions import Fraction

import c11
import c12
import c13
import c15
import run as R
from candidates import steps


def jac(a, b):
    u = a | b
    return Fraction(len(a & b), len(u)) if u else Fraction(0)


class W:
    def __init__(self, ndim, stepf, pieces, near, alone, table):
        self.ndim, self.stepf, self.pieces, self.near, self.alone, self.table = ndim, stepf, pieces, near, alone, table

    def frame(self, a):
        return frame_of(a) if self.ndim == 2 else frozenset(np.nonzero(a)[0].tolist())

    def remove(self, a, cells):
        b = a.copy()
        for p in cells:
            b[p] = False
        return b


LIFE = W(2, step, c15.pieces_wrap, lambda f: C.dilate(f, 1), lambda f: c15.evolve_wrap(f), c11.LIFE.tab)
R184 = W(1, PR.step184, c15.runs184_wrap, PR.near184, PR.next184, c11.R184.tab)
_CACHE = {}


def graph(H, w):
    """Pieces, idle, links, groups (P-1 to P-4), tracks (P-5), dead ends and owners (P-6), for one history."""
    H = np.asarray(H)
    key = (w.ndim, H.shape, hashlib.sha1(H.tobytes()).hexdigest())
    if key in _CACHE:
        return _CACHE[key]
    Tn = len(H)
    ps, idle, inter = [], [], []
    for t in range(Tn):
        a = H[t]
        P = w.pieces(w.frame(a))
        ps.append(P)
        nxt = w.stepf(a)
        rem = [w.stepf(w.remove(a, p)) for p in P]
        idle.append([not (r ^ nxt).any() for r in rem])
        pairs = []
        for i in range(len(P)):
            n2 = w.near(w.near(P[i]))
            for j in range(i + 1, len(P)):
                if P[j] & n2:
                    both = w.stepf(w.remove(a, P[i] | P[j]))
                    if (nxt ^ rem[i] ^ rem[j] ^ both).any():
                        pairs.append((i, j))
        inter.append(pairs)
    kids = [[[] for _ in ps[t]] for t in range(Tn)]
    pars = [[[] for _ in ps[t]] for t in range(Tn)]
    for t in range(Tn - 1):
        for i, p in enumerate(ps[t]):
            if idle[t][i]:
                continue
            n1 = w.near(p)
            for j, q in enumerate(ps[t + 1]):
                if q & n1:
                    kids[t][i].append(j)
                    pars[t + 1][j].append(i)
    roots = [[None] * len(ps[t]) for t in range(Tn)]
    for t in range(Tn):
        for j in range(len(ps[t])):
            roots[t][j] = frozenset().union(*[roots[t - 1][i] for i in pars[t][j]]) if pars[t][j] else frozenset([(t, j)])
    sinks = [[None] * len(ps[t]) for t in range(Tn)]
    for t in reversed(range(Tn)):
        for i in range(len(ps[t])):
            sinks[t][i] = frozenset().union(*[sinks[t + 1][j] for j in kids[t][i]]) if kids[t][i] else frozenset([(t, i)])
    groups, gof = [], []
    for t in range(Tn):
        k = len(ps[t])
        par = list(range(k))

        def find(x):
            while par[x] != x:
                par[x] = par[par[x]]
                x = par[x]
            return x
        for i, j in inter[t]:
            par[find(i)] = find(j)
        for i in range(k):
            for j in range(i + 1, k):
                if roots[t][i] & roots[t][j] and sinks[t][i] & sinks[t][j]:
                    par[find(i)] = find(j)
        gs = {}
        for i in range(k):
            gs.setdefault(find(i), []).append(i)
        gl = list(gs.values())
        groups.append(gl)
        g = [0] * k
        for n, members in enumerate(gl):
            for i in members:
                g[i] = n
        gof.append(g)
    cells = [[frozenset().union(*[ps[t][i] for i in m]) for m in groups[t]] for t in range(Tn)]
    gk = [[set() for _ in groups[t]] for t in range(Tn)]
    gp = [[set() for _ in groups[t]] for t in range(Tn)]
    for t in range(Tn - 1):
        for i in range(len(ps[t])):
            for j in kids[t][i]:
                gk[t][gof[t][i]].add(gof[t + 1][j])
                gp[t + 1][gof[t + 1][j]].add(gof[t][i])
    cont = [[None] * len(groups[t]) for t in range(Tn)]   # cont[t][g] = group at t+1 it continues as
    for t in range(Tn - 1):
        alone = [w.alone(c) for c in cells[t]]
        sc = {}
        for g in range(len(groups[t])):
            for h in gk[t][g]:
                sc[(g, h)] = jac(cells[t + 1][h], alone[g])

        def ubest(opts, f):
            vals = [(f(o), o) for o in opts]
            if not vals:
                return None
            m = max(v for v, _ in vals)
            if m <= 0 or sum(v == m for v, _ in vals) > 1:
                return None
            return next(o for v, o in vals if v == m)
        for g in range(len(groups[t])):
            h = ubest(gk[t][g], lambda h: sc[(g, h)])
            if h is not None and ubest(gp[t + 1][h], lambda g2: sc[(g2, h)]) == g:
                cont[t][g] = h
    is_cont = [[False] * len(groups[t]) for t in range(Tn)]
    track = [[None] * len(groups[t]) for t in range(Tn)]
    nt = 0
    for t in range(Tn):
        for g in range(len(groups[t])):
            if track[t][g] is None:
                track[t][g] = nt
                nt += 1
            if t < Tn - 1 and cont[t][g] is not None:
                track[t + 1][cont[t][g]] = track[t][g]
                is_cont[t + 1][cont[t][g]] = True
    # P-6 dead ends
    dead = [[False] * len(groups[t]) for t in range(Tn)]
    for t in range(Tn):
        for g, m in enumerate(groups[t]):
            desc, front, ok = set((t, i) for i in m), [(t, i) for i in m], True
            while front and ok:
                s, i = front.pop()
                if s == Tn - 1:
                    ok = False
                    break
                for j in kids[s][i]:
                    if (s + 1, j) not in desc:
                        desc.add((s + 1, j))
                        front.append((s + 1, j))
            if ok:
                ok = all((s, j) in desc for s, i in desc for j in groups[s][gof[s][i]])
            dead[t][g] = ok
    first = {}
    for t in range(Tn):
        for g in range(len(groups[t])):
            first.setdefault(track[t][g], (t, g))
    owners = {}   # exhaust track -> tracks it belongs to
    for tid, (t, g) in sorted(first.items(), key=lambda x: x[1]):
        if is_cont[t][g] or not dead[t][g]:
            continue
        if gp[t][g]:
            own = set()
            for p in gp[t][g]:
                pt = track[t - 1][p]
                own |= owners.get(pt, {pt})
        else:
            n2 = w.near(w.near(cells[t][g]))
            own = {track[t][h] for h in range(len(groups[t])) if h != g and cells[t][h] & n2
                   and track[t][h] not in owners}
        owners[tid] = own
    G = dict(ps=ps, groups=groups, cells=cells, cont=cont, track=track, owners=owners, gof=gof,
             idle=idle, Tn=Tn)
    _CACHE[key] = G
    return G


def match(G, t, sl):
    """The track ids whose group at t, with that track's dead ends, makes up the slice exactly."""
    cs = G["cells"][t]
    hit = [g for g, c in enumerate(cs) if c & sl]
    if not hit or any(not cs[g] <= sl for g in hit) or frozenset().union(*[cs[g] for g in hit]) != sl:
        return {}
    out = {}
    for g in hit:
        tid = G["track"][t][g]
        if all(tid in G["owners"].get(G["track"][t][h], ()) for h in hit if h != g):
            out[tid] = g
    return out


def p_flags(H, tr, w):
    G = graph(H, w)
    fl = []
    for t, u in steps(tr):
        if u != t + 1:
            fl.append(False)
            continue
        a, b = match(G, t, tr[t]), match(G, u, tr[u])
        fl.append(any(G["cont"][t][g] == b.get(tid) for tid, g in a.items()))
    return fl


def holes(H):
    return np.asarray(H)[:, ::-1] ^ True


def e_flags(H, tr, w):
    if w.ndim == 1 and all(not np.asarray(H)[t][next(iter(f))] for t, f in tr.items()):
        L = np.asarray(H).shape[1]
        return c13.e_flags(holes(H), {t: frozenset(L - 1 - p for p in f) for t, f in tr.items()}, c15.R184)
    return c13.e_flags(H, tr, c15.R184 if w.ndim == 1 else c15.LIFE_X)


def s1(w=LIFE):
    def judge(H, tr):
        if all(len(f) == 1 for f in tr.values()):
            return e_flags(H, tr, w)
        return p_flags(H, tr, w)
    return judge


S1 = s1()


def w_of(rule):
    return R184 if rule is c11.R184 else LIFE



# ---------------------------------------------------------------- scoring

def vword(fl):
    return "holds" if all(x is True for x in fl) else "uncarried"


def bad(tr, fl):
    return [k for (k, _), x in zip(steps(tr), fl) if x is not True]


def rot(case):
    H = np.rot90(case["H"], 1, axes=(1, 2))
    trs = [{t: frozenset((N - 1 - c, r) for r, c in f) for t, f in tr.items()} for tr in case["tracings"]]
    return {**case, "H": H, "tracings": trs}


def hunter_cases():
    """(id, name, H, tracing, world, target, lo, hi). Targets from the 18 Nov rulings and principles."""
    import audit_c15 as AU
    out = []
    nc, _ = c13.new_cases()
    tg = {"N-1": "uncarried", "N-2": "uncarried", "N-3": "uncarried", "N-4": "uncarried", "N-5": "uncarried"}
    for name, Hn, trn, w in nc:
        out.append((name.split()[0], name, Hn, trn, R184 if w is c13.R184_W else LIFE, tg[name.split()[0]], None, None))
    gq = PR.probe_gliders()
    Hg, s, e = gq["H"], gq["start"], gq["end"]
    Rt = C.follow(Hg, frame_of(Hg[s]), s, T)
    out.append(("N-1b", "products as one, from contact, steps after the interval", Hg,
                {t: f for t, f in Rt.items() if t >= e - 1}, LIFE, "uncarried", None, None))
    Hb = run(board((HU.BLOCK, (40, 40)), (HU.BLOCK, (40, 43))), T)
    out.append(("H-3", "bi-block as one", Hb, HU.live(Hb), LIFE, "uncarried", None, None))
    Hp = run(board((HU.PULSAR, (40, 40))), T)
    out.append(("H-4", "pulsar", Hp, HU.live(Hp), LIFE, "none", None, None))
    Hgun = run(board((HU.GUN, (10, 10))), T)
    gun = frozenset((10 + r, 10 + c) for r, c in HU.GUN)
    out.append(("H-5", "Gosper gun, followed", Hgun, PR.follow_piece(Hgun, gun), LIFE, "conflict (T-1)", None, None))
    Hl = run(board((HU.LWSS, (60, 100))), T)
    out.append(("H-8", "lightweight spaceship, every live cell", Hl, HU.live(Hl), LIFE, "holds", None, None))
    out.append(("H-8b", "lightweight spaceship from step 1", Hl, {t: f for t, f in HU.live(Hl).items() if t >= 1},
                LIFE, "holds", None, None))
    trA, _ = C.track_glider(Hg, gq["A"][0], 0)
    out.append(("H-10a", "glider A into the reaction", Hg, {**{t: trA[t] for t in trA if t < s}, **Rt}, LIFE,
                "uncarried", None, None))
    kb = HU.kickback()
    if kb:
        b0, Hk = kb
        ta, _ = C.track_glider(Hk, C.glider_at(40, 40), 0)
        out.append(("H-10b", "kickback, A into the output glider", Hk,
                    {**ta, **C.follow(Hk, ta[max(ta)], max(ta), T)}, LIFE, "uncarried", None, None))
    sh = R.shifted(C.case_glider(), d=(100, 100))
    out.append(("H-11", "glider across the edge", sh["H"], sh["tracings"][0], LIFE, "holds", None, None))
    m = HU.merge184()
    if m:
        seed, t, Hh, srcs = m
        big, small = sorted(srcs, key=len, reverse=True)
        out.append(("H-13", f"larger jam ({len(big)}) through the merge at {t + 1}", Hh,
                    {**{t: big}, **HU.follow_jam(Hh, big, t)}, R184, "holds", None, None))
        out.append(("H-13", f"smaller jam ({len(small)}) into the merge", Hh,
                    {t: small, **{u: f for u, f in HU.follow_jam(Hh, big, t).items() if u > t}}, R184,
                    "uncarried", None, None))
    j = PR.probe_jam()
    Hj = np.array(j["H"])
    p = max(j["jam"][0])
    while Hj[0][p]:
        p += 1
    hole = {0: frozenset([p])}
    for t in range(T):
        p = (p - 1) % PR.L if Hj[t][(p - 1) % PR.L] and not Hj[t][p] else p
        hole[t + 1] = frozenset([p])
    out.append(("H-14", "rule 184 hole through the jam", Hj, hole, R184, "holds", None, None))
    tr = C.case_glider()["tracings"][0]
    box = {t: frozenset((r, c) for r in range(min(x for x, _ in f), max(x for x, _ in f) + 1)
                        for c in range(min(y for _, y in f), max(y for _, y in f) + 1)) for t, f in tr.items()}
    out.append(("H-15", "glider with its bounding box", C.case_glider()["H"], box, LIFE, "uncarried", None, None))
    H = run(board((GLIDER, (10, 10)), (AU.SOUP, (80, 70))), T)
    out.append(("H-21", "glider and a far dying soup, as one", H, HU.live(H), LIFE, "uncarried", None, None))
    H = run(board((GLIDER, (10, 10)), (AU.DIAG, (10, 50))), T)
    out.append(("H-22", "glider and a far 3-cell diagonal, as one", H, HU.live(H), LIFE, "uncarried", None, None))
    for t0 in (e, 105, 110):
        out.append(("H-23", f"products as one, from step {t0}", Hg, {t: f for t, f in Rt.items() if t >= t0}, LIFE,
                    "uncarried", None, None))
    trB, _ = C.track_glider(Hg, gq["B"][0], 0)
    for t1 in (s + 2, s + 10, e):
        ab = {**{t: trA[t] | trB[t] for t in range(0, s)}, **{t: f for t, f in Rt.items() if t <= t1}}
        out.append(("H-24", f"A and B as one, tracing to {t1}, judged before contact", Hg, ab, LIFE,
                    "uncarried", 0, s - 1))
    for nm, pat in (("MWSS", AU.MWSS), ("HWSS", AU.HWSS)):
        H = run(board((pat, (60, 100))), T)
        for t0 in (0, 1):
            out.append(("H-25", f"{nm} from step {t0}", H, {t: f for t, f in HU.live(H).items() if t >= t0}, LIFE,
                        "holds", None, None))
    return out


def noise_rows():
    import c15_iter as I
    rows, n, k = [], 0, 0
    for eps in (1e-4, 1e-3):
        for seed in (0, 1, 2):
            H, _ = I.noisy_life(eps, seed)
            a, _ = C.track_glider(H, C.glider_at(10, 10), 0)
            b, _ = C.track_glider(H, C.glider_at(10, 60), 0)
            both = min(max(a), max(b))
            s_ = min(100, both)
            cells = []
            for name, tr, want in (
                    ("glider", a, "holds"),
                    ("splice", {t: (a[t] if t < s_ else b[t]) for t in range(0, max(b) + 1)}, "uncarried"),
                    ("union", {t: a[t] | b[t] for t in range(both + 1)}, "uncarried"),
                    ("alt", {t: (a[t] if t % 2 == 0 else b[t]) for t in range(both + 1)}, "uncarried")):
                tr = R.trim(tr)
                fl = S1(H, tr)
                v = vword(fl)
                n += v == want
                k += 1
                cells.append(f"{'✓' if v == want else '✗'} {v} {bad(tr, fl)[:3]}")
            rows.append(f"| {eps:g} | {seed} | " + " | ".join(cells) + " |")
    return rows, n, k


def score():
    out = []
    cases = c12.all_grid_cases()
    rows = ["| Case | Target | S-1 | Detail |", "|---|---|---|---|"]
    m, sf = 0, []
    for case in cases:
        mk, det = R.score(case, "S-1", S1)
        m += mk == "✓"
        rows.append(f"| {case['name']} | {case['target']} | {mk} | {det} |")
        for name, c2 in (("shift 7,13", R.shifted(case, (7, 13))), ("shift 100,100", R.shifted(case, (100, 100))),
                         ("rotation", rot(case))):
            if R.score(c2, "S-1", S1)[0] != mk:
                sf.append((case["name"], name))
        H7 = np.concatenate([np.zeros((7, N, N), dtype=bool), case["H"]])
        for tr in case["tracings"]:
            tr = R.trim(tr)
            if S1(case["H"], tr) != S1(H7, {t + 7: f for t, f in tr.items()}):
                sf.append((case["name"], "time"))
    out += ["### Grid", ""] + rows + [f"| Rows matched | | {m} of {len(cases)} | |", "",
            "Shift (7, 13 and 100, 100), rotation and time-shift (7 steps) checks: " +
            ("every mark and flag unchanged." if not sf else f"changed: {sf}"), ""]
    print("grid done", file=sys.stderr, flush=True)

    head = ["| Board | Part | Target | S-1 | Steps not carried |", "|---|---|---|---|---|"]

    def parts_rows(parts):
        rows, n = [], 0
        for sec, name, target, H, tr, lo, hi, want, rule in parts:
            fl = s1(w_of(rule))(H, tr)
            ok, b = c13.part_ok(fl, tr, lo, hi, want)
            n += ok
            rows.append(f"| {sec.split(':')[0][:40]} | {name} | {target} | {'✓' if ok else '✗'} | {b[:6]} |")
        return rows, n
    pr, n = parts_rows(c12.probe_parts())
    out += ["### Registered probes", ""] + head + pr + ["", f"Parts matched: {n} of 10.", ""]
    g = C.case_glider()
    H, tr = g["H"], g["tracings"][0]
    sites = sorted(frozenset().union(*tr.values()))
    nc = sum(all(x is True for x in S1(H, {t: frozenset([p]) for t in range(len(H))})) for p in sites)
    out += [f"Elemental: {nc} of {len(sites)} crossed cells carried.", ""]
    print("probes done", file=sys.stderr, flush=True)

    parts = []
    for k, x in enumerate([x for _, x in zip(range(7), c13.gliders_configs())][4:7], 4):
        parts += c13.glider_parts(x, f"U-gliders {k}")
    for k, x in enumerate([x for _, x in zip(range(7), c13.eater_configs())][4:7], 4):
        parts += c13.eater_parts(x, f"U-eater {k}")
    pr, n = parts_rows(parts)
    crow = []
    for c in [c for c in c13.collision_configs(6) if c["placement"] != (37, 39)][3:6]:
        mk, det = R.score(c, "S-1", S1)
        n += mk == "✓"
        crow.append(f"| U-collision, block at {c['placement']} | glider | break at crash | {mk} | {det} |")
    out += ["### Unseen boards (C15's 4th to 6th)", ""] + head + pr + crow + \
        ["", f"Unseen parts matched: {n} of {len(parts) + 3}.", ""]
    print("unseen done", file=sys.stderr, flush=True)

    rows = ["| ID | Case | Target | S-1 | Steps not carried |", "|---|---|---|---|---|"]
    hit = tot = 0
    for i, name, Hn, trn, w, target, lo, hi in hunter_cases():
        trn = R.trim(trn)
        fl = s1(w)(Hn, trn)
        if lo is not None:
            ks = [k for k, _ in steps(trn)]
            fl_ = [x for k, x in zip(ks, fl) if lo <= k < hi]
            v = vword(fl_)
        else:
            v = vword(fl)
        mk = "" if target in ("none",) or target.startswith("conflict") else ("✓" if v == target else "✗")
        if mk:
            tot += 1
            hit += mk == "✓"
        rows.append(f"| {i} | {name} | {target} | {v} {mk} | {bad(trn, fl)[:8]} |")
    out += ["### Hunter and new cases", ""] + rows + ["", f"Matched: {hit} of {tot} with a target.", ""]
    print("hunter done", file=sys.stderr, flush=True)

    nr, n, k = noise_rows()
    out += ["### Noise in the Game of Life", "", "| ε | seed | Glider | Splice | Union | Alternating |",
            "|---|---|---|---|---|---|"] + nr + ["", f"Noise: {n} of {k}.", ""]
    print("\n".join(out))



def track_span(G, t, cell):
    """The track whose group at t holds the cell: (first step, last step, track id)."""
    g = next((g for g, c in enumerate(G["cells"][t]) if cell in c), None)
    if g is None:
        return None
    tid = G["track"][t][g]
    ts = [s for s in range(G["Tn"]) if tid in G["track"][s]]
    return ts[0], ts[-1], tid


def native():
    """S-6: what S-1 says at each event, with no hand-built tracing."""
    print("| Case | Question | S-1 |\n|---|---|---|")
    cols = [C.case_collision(False), C.case_collision(True)] + \
        [c for c in c13.collision_configs(6) if c["placement"] != (37, 39)][3:6]
    for c in cols:
        G = graph(c["H"], LIFE)
        f, l, _ = track_span(G, 0, (11, 12))
        print(f"| collision, block at {c['placement']} | glider's track ends (crash {c['crash']}) | {l} |")
    q = PR.probe_eater()
    G = graph(q["H"], LIFE)
    print(f"| eater | glider's track ends (contact {q['start']}) | {track_span(G, 0, (11, 12))[1]} |")
    print(f"| eater | eater's track spans | {track_span(G, 0, next(iter(q['eater'])))[:2]} |")
    g = PR.probe_gliders()
    G = graph(g["H"], LIFE)
    a = track_span(G, 0, next(iter(g["A"][0])))
    b = track_span(G, 0, next(iter(g["B"][0])))
    r = track_span(G, g["start"], next(iter(g["A"][g["start"]])))
    print(f"| two gliders | A's, B's track end (contact {g['start']}) | {a[1]}, {b[1]} |")
    print(f"| two gliders | track of the contact group spans (interval to {g['end']}) | {r[:2]} |")
    ins = C.case_indirect_splice()
    G = graph(ins["H"], LIFE)
    a = track_span(G, 0, (11, 12))
    bT = next(iter(ins["tracings"][0][T]))
    print(f"| indirect splice ({ins['reaction']}) | A's track ends (crash {ins['crash']}); B on A's track | "
          f"{a[1]}; {track_span(G, T, bT)[2] == a[2]} |")
    m = HU.merge184()
    if m:
        seed, t, Hh, srcs = m
        G = graph(Hh, R184)
        for s_ in sorted(srcs, key=len, reverse=True):
            sp = track_span(G, t, next(iter(s_)))
            print(f"| jam merge at {t + 1} | jam of {len(s_)} cars: track spans | {sp[:2]} |")
    Hg = run(board((HU.GUN, (10, 10))), T)
    G = graph(Hg, LIFE)
    print(f"| Gosper gun | gun's track spans | {track_span(G, 0, (15, 11))[:2]} |")
    Hl = run(board((HU.LWSS, (60, 100))), T)
    G = graph(Hl, LIFE)
    print(f"| LWSS | track spans | {track_span(G, 0, next(iter(frame_of(Hl[0]))))[:2]} |")


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "score"
    {"conflicts": conflicts, "score": score, "native": native}[mode]()
