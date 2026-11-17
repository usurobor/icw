"""C13: closest continuer, integration in context, elemental clause.
Declared in notes/runs/2026-11-18-c13.md before this code ran.

Variants a, b, c differ only in when a stage counts as split. Clause E judges
tracings whose every footprint is one site; clause P (C10's closeness plus
integration in context) judges the rest. Rerun: python3 tools/gol/c13.py
"""
import itertools
import sys
from fractions import Fraction

import numpy as np

import c11
import c12
import cases as C
import probes as PR
import run as R
from candidates import blobs, local_next, steps, jaccard, CANDIDATES
from life import GLIDER, N, board, run, frame_of, symmetries
from probes import EATER

T = C.T


# ---------------------------------------------------------------- worlds

def _roll_sum2(B):
    return sum(np.roll(np.roll(B, i, -2), j, -1)
               for i in (-1, 0, 1) for j in (-1, 0, 1) if (i, j) != (0, 0))


def life_step_count(B):
    """The rule as a neighbour count (life.py's expression), for stacks."""
    n = _roll_sum2(B)
    return (n == 3) | (B & (n == 2))


_LTAB = np.array(c11.LIFE.tab, dtype=bool)
_LOFF = c11.LIFE.offs


def life_step_table(B):
    """The same rule as a 512-entry lookup table (rule 13 check)."""
    idx = np.zeros(B.shape, dtype=np.int64)
    for k, (i, j) in enumerate(_LOFF):
        idx |= np.roll(np.roll(B, -i, -2), -j, -1).astype(np.int64) << k
    return _LTAB[idx]


def r184_step(B):
    return (B & np.roll(B, -1, -1)) | (np.roll(B, 1, -1) & ~B)


def local_next_table(frame):
    """Isolated one-step evolution through the lookup table."""
    if not frame:
        return frozenset()
    rs = [r for r, _ in frame]
    cs = [c for _, c in frame]
    r0, c0 = min(rs) - 2, min(cs) - 2
    a = np.zeros((max(rs) - r0 + 3, max(cs) - c0 + 3), dtype=bool)
    for r, c in frame:
        a[r - r0, c - c0] = True
    a = np.pad(a, 1)
    b = life_step_table(a)[1:-1, 1:-1]
    return frozenset((int(r) + r0, int(c) + c0) for r, c in zip(*np.nonzero(b)))


class World:
    def __init__(self, name, ndim, step, evolve, pieces, near, table):
        self.name, self.ndim, self.step, self.evolve = name, ndim, step, evolve
        self.pieces, self.near, self.table = pieces, near, table

    def mask(self, frame, shape):
        m = np.zeros(shape, dtype=bool)
        for p in frame:
            m[p] = True
        return m

    def frame(self, m):
        if self.ndim == 2:
            return frozenset(zip(*map(lambda a: a.tolist(), np.nonzero(m))))
        return frozenset(np.nonzero(m)[0].tolist())


LIFE_W = World("life", 2, life_step_count, local_next, blobs, C.dilate, c11.LIFE.tab)
LIFE_T = World("life", 2, life_step_table, local_next_table, blobs, C.dilate, c11.LIFE.tab)
R184_W = World("184", 1, r184_step, PR.next184, PR.runs184, PR.near184, c11.R184.tab)


# ---------------------------------------------------------------- clause E

def flow_of(tab):
    """phi on adjacent pairs with f(x-1,x0,x1) = x0 + phi(x-1,x0) - phi(x0,x1), phi(0,0)=0.
    Neighbourhood index: bit k for offset (-1, 0, 1)[k]. None if no such phi (not conserving)."""
    if len(tab) != 8:
        return None
    sols = []
    for vals in itertools.product((-1, 0, 1), repeat=3):
        phi = {(0, 0): 0, (0, 1): vals[0], (1, 0): vals[1], (1, 1): vals[2]}
        ok = True
        for idx in range(8):
            xm, x0, xp = idx & 1, idx >> 1 & 1, idx >> 2 & 1
            if tab[idx] != x0 + phi[(xm, x0)] - phi[(x0, xp)]:
                ok = False
                break
        if ok:
            sols.append(phi)
    return sols[0] if len(sols) == 1 else None


def e_flags(H, tr, world):
    """Clause E per step: same site, or (conserving rule) the flow's move of a live token."""
    phi = flow_of(world.table) if world.ndim == 1 else None
    out = []
    for t, u in steps(tr):
        (p,), (q,) = tuple(tr[t]), tuple(tr[u])
        if p == q:
            out.append(True)
            continue
        if phi is None:
            out.append(False)
            continue
        a, L = H[t], len(H[t])
        if not (a[p] and H[u][q]):
            out.append(False)
            continue
        if phi[(int(a[p]), int(a[(p + 1) % L]))] == 1:
            dest = (p + 1) % L
        elif phi[(int(a[(p - 1) % L]), int(a[p]))] == -1:
            dest = (p - 1) % L
        else:
            dest = p
        out.append(bool(q == dest))
    return out


def elemental(tr):
    return all(len(f) == 1 for f in tr.values())


# ---------------------------------------------------------------- clause P: closeness

def unique_best(scores, differ):
    s0 = scores[0]
    if s0 <= 0:
        return False
    rivals = [s for s, d in zip(scores[1:], differ[1:]) if d]
    if any(s > s0 for s in rivals):
        return False
    return "tie" if any(s == s0 for s in rivals) else True


def closeness(H, tr, world):
    out = []
    for t, u in steps(tr):
        F, X = tr[t], tr[u]
        isoF = world.evolve(F)
        bt, bu = world.frame(H[t]), world.frame(H[u])
        conts = [X] + [p for p in world.pieces(bu) if p & world.near(F)] + [frozenset()]
        fwd = unique_best([jaccard(c, isoF) for c in conts], [c != X for c in conts])
        preds = [F] + [p for p in world.pieces(bt) if p & world.near(X)] + [frozenset()]
        bwd = unique_best([jaccard(X, world.evolve(p)) for p in preds], [p != F for p in preds])
        if fwd is True and bwd is True:
            out.append(True)
        elif False in (fwd, bwd):
            out.append(False)
        else:
            out.append("tie")
    return out


# ---------------------------------------------------------------- clause P: integration in context

def rerun(H, t, t1, dels, world):
    """Runs from step t to t1 with each deletion set's cells set to 0 at t. Shape (len, t1-t+1, ...)."""
    B = np.repeat(np.asarray(H[t])[None], len(dels), axis=0).copy()
    for k, d in enumerate(dels):
        for p in d:
            B[(k,) + (p if world.ndim == 2 else (p,))] = False
    out = [B]
    noise = getattr(world, "noise", None)
    for s in range(t1 - t):
        B = world.step(B)
        if noise is not None:
            B = B ^ noise[t + s + 1]
        out.append(B)
    return np.stack(out, axis=1)


def _box(m):
    """Bounding box of a boolean array (per step), or None."""
    idx = np.nonzero(m)
    if len(idx[0]) == 0:
        return None
    return [(int(a.min()), int(a.max())) for a in idx]


def _boxes_close(b1, b2, d=2):
    if b1 is None or b2 is None:
        return False
    return all(lo1 - d <= hi2 and lo2 - d <= hi1 for (lo1, hi1), (lo2, hi2) in zip(b1, b2))


def _min_dist(m1, m2, world):
    a, b = np.argwhere(m1), np.argwhere(m2)
    if len(a) == 0 or len(b) == 0:
        return None
    best = None
    for x in a:
        d = np.abs(b - x)
        L = np.array(m1.shape)
        d = np.minimum(d, L - d)
        v = int(d.max(axis=1).min())
        best = v if best is None else min(best, v)
    return best


def far(m1, m2, world):
    d = _min_dist(m1, m2, world)
    return d is None or d >= 3


def integration_ab(H, tr, t, world, variant, cache):
    """True: one whole; False: split; None: unresolved (split parts finish within two cells)."""
    F = tr[t]
    t1 = max(tr)
    ps = world.pieces(F)
    k = len(ps)
    if k <= 1:
        return True
    Hw = np.asarray(H[t:t1 + 1])
    single = rerun(H, t, t1, ps, world)
    D = Hw[None] ^ single  # dependents, (k, W, ...)
    boxes = [[_box(D[i, w]) for w in range(D.shape[1])] for i in range(k)]
    parent = list(range(k))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    close_pairs = [(i, j) for i in range(k) for j in range(i + 1, k)
                   if any(_boxes_close(boxes[i][w], boxes[j][w]) for w in range(D.shape[1] - 1))]
    if close_pairs:
        dbl = rerun(H, t, t1, [ps[i] | ps[j] for i, j in close_pairs], world)
        for n, (i, j) in enumerate(close_pairs):
            con = Hw[1:] ^ single[i, 1:] ^ single[j, 1:] ^ dbl[n, 1:]
            if con.any():
                parent[find(i)] = find(j)
    comps = {}
    for i in range(k):
        comps.setdefault(find(i), []).append(i)
    comps = list(comps.values())
    if len(comps) == 1:
        cache["graph"] = cache.get("graph", 0) + 1
        return True
    allp = frozenset().union(*ps)
    none = rerun(H, t, t1, [allp], world)[0]
    unresolved = False
    c = len(comps)
    for mask in range(1, 2 ** (c - 1)):
        P = frozenset().union(*[ps[i] for m in range(c - 1) if mask >> m & 1 for i in comps[m + 1]])
        Q = allp - P
        rp, rq = rerun(H, t, t1, [P, Q], world)
        con = Hw[1:] ^ rp[1:] ^ rq[1:] ^ none[1:]
        if con.any():
            continue  # higher-order interaction: not a split
        dP, dQ = Hw[-1] ^ rp[-1], Hw[-1] ^ rq[-1]
        if variant == "b" and (not dP.any() or not dQ.any()):
            continue  # a group whose effects die inside the window does not split the stage
        if far(dP, dQ, world):
            return False
        unresolved = True
    return None if unresolved else True


def history_connected(H, tr, world):
    """C13c: pieces over the window joined by one-step dependence form one graph."""
    ts = sorted(tr)
    nodes = {t: world.pieces(tr[t]) for t in ts}
    ids = {(t, i): n for n, (t, i) in enumerate((t, i) for t in ts for i in range(len(nodes[t])))}
    if not ids:
        return False
    parent = list(range(len(ids)))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    for t, u in zip(ts[:-1], ts[1:]):
        if not nodes[t] or not nodes[u]:
            continue
        nxt = rerun(H, t, u, nodes[t], world)[:, -1]
        actual = np.asarray(H[u])
        for i in range(len(nodes[t])):
            changed = world.frame(actual ^ nxt[i])
            for j, q in enumerate(nodes[u]):
                if changed & q:
                    parent[find(ids[(t, i)])] = find(ids[(u, j)])
    return len({find(n) for n in range(len(ids))}) == 1


def p_flags(H, tr, world, variant):
    cl = closeness(H, tr, world)
    if variant == "c":
        whole = history_connected(H, tr, world)
        return [x if x is not True else whole for x in cl]
    cache = {}
    out = []
    for (t, u), x in zip(steps(tr), cl):
        if x is not True:
            out.append(x if x is False else False)  # a tie carries nothing
            continue
        out.append(integration_ab(H, tr, t, world, variant, cache))
    return out


def c13(variant, world=LIFE_W):
    def judge(H, tr):
        if elemental(tr):
            return e_flags(H, tr, world)
        return p_flags(H, tr, world, variant)
    return judge


VARIANTS = ("a", "b", "c")


# ---------------------------------------------------------------- unseen boards

def gliders_configs():
    """probes.probe_gliders as a generator, same criteria and order."""
    a0 = (40, 40)
    for b_cells in symmetries(GLIDER):
        for d in range(10, 16):
            for off in range(-4, 5):
                b0 = (40 + d, 40 + d + off)
                H = run(board((GLIDER, a0), (list(b_cells), b0)), T)
                if not H[T].any():
                    continue
                A, B = PR.alone_track(GLIDER, a0), PR.alone_track(list(b_cells), b0)
                start = next((t for t in range(T) if PR.dist(A[t], B[t]) <= 2), None)
                if start is None or start < 5 or start > 40:
                    continue
                end = PR.settled_from(H, start)
                if end is None or end > T - 15:
                    continue
                yield dict(H=H, A=A, B=B, start=start, end=end, b0=b0, b=b_cells)


def eater_configs():
    g0 = (10, 10)
    G = PR.alone_track(GLIDER, g0)
    for e in symmetries(EATER):
        for dr in range(-5, 6):
            for dc in range(-5, 6):
                e0 = (30 + dr, 30 + dc)
                eater = frozenset((e0[0] + r, e0[1] + c) for r, c in e)
                if PR.dist(G[0], eater) <= 3:
                    continue
                H = run(board((GLIDER, g0), (list(e), e0)), T)
                if frame_of(H[T]) != eater:
                    continue
                start = next((t for t in range(T) if PR.dist(G[t], eater) <= 2), None)
                if start is None:
                    continue
                end = next(t for t in range(start, T + 1)
                           if all(frame_of(H[u]) == eater for u in range(t, T + 1)))
                if end - start < 3:
                    continue
                yield dict(H=H, G=G, eater=eater, start=start, end=end, e0=e0)


def collision_configs(span=3):
    """case_collision's search as a generator; span 3 is the registered range."""
    from life import BLOCK
    for dr in range(-span, span + 1):
        for dc in range(-span, span + 1):
            H = run(board((GLIDER, (10, 10)), (BLOCK, (40 + dr, 40 + dc))), T)
            a, tc = C.track_glider(H, C.glider_at(10, 10), 0)
            if tc is None or tc > 100:
                continue
            last = max(a)
            tail = C.follow(H, a[last], last, T)
            tr = {**a, **tail}
            if not all(tr[t] for t in tr):
                continue
            yield dict(name="Collision", H=H, tracings=[tr], target="break at crash",
                       crash=tc, placement=(40 + dr, 40 + dc))


def glider_parts(g, tag):
    H, s, e = g["H"], g["start"], g["end"]
    trA, _ = C.track_glider(H, g["A"][0], 0)
    trB, _ = C.track_glider(H, g["B"][0], 0)
    union = {t: trA[t] | trB[t] for t in range(0, s)}
    Rt = C.follow(H, frame_of(H[s]), s, T)
    sec = f"{tag}: two gliders that interact (B at {g['b0']}; interval {s}–{e})"
    return [(sec, "Glider A before contact", "carried", H, trA, 0, s - 1, True, c11.LIFE),
            (sec, "Glider B before contact", "carried", H, trB, 0, s - 1, True, c11.LIFE),
            (sec, "A and B as one, before contact", "uncarried", H, union, 0, s - 1, False, c11.LIFE),
            (sec, f"The interaction, {s}–{e}", "carried", H, Rt, s, e, True, c11.LIFE)]


def eater_parts(q, tag):
    H, s, e = q["H"], q["start"], q["end"]
    trG, stop = C.track_glider(H, q["G"][0], 0)
    Rt = C.follow(H, frame_of(H[s]), s, T)
    E3 = PR.follow_piece(H, q["eater"])
    G2 = {**{t: trG[t] for t in trG}, **{t: E3[t] for t in E3 if t > max(trG)}}
    sec = f"{tag}: glider meets an eater (eater at {q['e0']}; interval {s}–{e})"
    return [(sec, "Glider until contact", "carried", H, trG, 0, s - 1, True, c11.LIFE),
            (sec, "Glider continued into the merged piece", "uncarried", H, G2, 0, T, False, c11.LIFE),
            (sec, f"The interaction, {s}–{e}", "carried", H, Rt, s, e, True, c11.LIFE),
            (sec, "The eater persists (followed piece)", "carried", H, E3, 0, T, True, c11.LIFE)]


def by_product_trim(H, start, t0, world=LIFE_W):
    """Fork F2 (by-product ruling): follow from the start stage; at each step, when the stage's
    pieces fall into groups that do not interact over the rest of the run (pairwise contrast
    components), keep the unique closest group to the previous kept stage's one-step evolution
    and drop the rest; a tie ends the tracing."""
    tr = {t0: start}
    for t in range(t0 + 1, T + 1):
        S = frozenset(p for p in world.near(tr[t - 1]) if H[t][p])
        if not S:
            break
        ps = world.pieces(S)
        if len(ps) > 1:
            comps = contrast_components(H, t, T, ps, world)
            if len(comps) > 1:
                iso = world.evolve(tr[t - 1])
                sc = [jaccard(g, iso) for g in comps]
                best = max(sc)
                if sc.count(best) > 1 or best == 0:
                    break
                S = comps[sc.index(best)]
        tr[t] = S
    return tr


def contrast_components(H, t, t1, ps, world):
    """Groups of pieces joined by nonzero pairwise contrast over (t, t1]."""
    k = len(ps)
    if t1 <= t:
        return [frozenset().union(*ps)]
    Hw = np.asarray(H[t:t1 + 1])
    single = rerun(H, t, t1, ps, world)
    D = Hw[None] ^ single
    boxes = [[_box(D[i, w]) for w in range(D.shape[1])] for i in range(k)]
    parent = list(range(k))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    pairs = [(i, j) for i in range(k) for j in range(i + 1, k)
             if any(_boxes_close(boxes[i][w], boxes[j][w]) for w in range(D.shape[1] - 1))]
    if pairs:
        dbl = rerun(H, t, t1, [ps[i] | ps[j] for i, j in pairs], world)
        for n, (i, j) in enumerate(pairs):
            if (Hw[1:] ^ single[i, 1:] ^ single[j, 1:] ^ dbl[n, 1:]).any():
                parent[find(i)] = find(j)
    groups = {}
    for i in range(k):
        groups.setdefault(find(i), set()).update(ps[i])
    return [frozenset(g) for g in groups.values()]


def unseen(gen, n=3):
    it = gen()
    next(it)  # the registered board
    return [x for _, x in zip(range(n), it)]


# ---------------------------------------------------------------- new cases (no target)

def ring_cars():
    """The jam probe's ring with every car followed by the motion rule (rule 184 cars)."""
    j = PR.probe_jam()
    a = np.array(j["H"])
    pos0 = list(np.nonzero(a[0])[0])
    cars = [pos0]
    for t in range(T):
        cur = a[t]
        cars.append([(p + 1) % PR.L if not cur[(p + 1) % PR.L] else p for p in cars[-1]])
    return a, cars, j


def new_cases():
    out = []
    g = PR.probe_gliders()
    H, e = g["H"], g["end"]
    out.append(("N-1 fission bundle (products as one, from the interval's end)", H,
                C.follow(H, frame_of(H[e]), e, T), LIFE_W))
    Hs = run(board((GLIDER, (10, 10)), ([(0, 0), (0, 1)], (10, 50))), T)
    gl, _ = C.track_glider(Hs, C.glider_at(10, 10), 0)
    sp = {**gl, 0: gl[0] | frozenset([(10, 50), (10, 51)])}
    out.append(("N-2 glider with a dying spark, as one", Hs, sp, LIFE_W))
    q = PR.probe_eater()
    e0, ecells = q["e0"], q["eater"]
    sym = next(s for s in symmetries(EATER)
               if frozenset((e0[0] + r, e0[1] + c) for r, c in s) == ecells)
    H2 = run(board((GLIDER, (10, 10)), (list(sym), e0), (GLIDER, (10, 60)),
                   (list(sym), (e0[0], e0[1] + 50))), T)
    eat2 = frozenset((r, c + 50) for r, c in ecells)
    t1, t2 = PR.follow_piece(H2, ecells), PR.follow_piece(H2, eat2)
    out.append(("N-3 fed bundle (two eaters, each eating its glider, as one)", H2,
                {t: t1[t] | t2[t] for t in t1}, LIFE_W))
    a, cars, j = ring_cars()
    k0 = pos0_index = min(k for k, p in enumerate(cars[0]) if p in j["jam"][0])
    ahead = min((k for k in range(len(cars[0])) if (cars[60][k] - cars[60][k0]) % PR.L >= 30),
                key=lambda k: (cars[60][k] - cars[60][k0]) % PR.L)
    spl = {t: frozenset([cars[t][k0] if t < 60 else cars[t][ahead]]) for t in range(T + 1)}
    out.append(("N-4 car splice (car to step 60, then the car 30 sites ahead)", a, spl, R184_W))
    adv, p = {0: frozenset([cars[0][k0]])}, cars[0][k0]
    phi = flow_of(R184_W.table)
    for t in range(T):
        nxt = (p + 1) % PR.L
        if a[t + 1][nxt]:
            p = nxt
        else:
            p = (p + 1) % PR.L if phi[(int(a[t][p]), int(a[t][(p + 1) % PR.L]))] == 1 else p
        adv[t + 1] = frozenset([p])
    out.append(("N-5 car by the advance convention", a, adv, R184_W))
    return out, (j, cars, k0)


# ---------------------------------------------------------------- reporting

def mark(ok):
    return "✓" if ok else "✗"


def world_of(rule):
    return R184_W if rule is c11.R184 else LIFE_W


def part_ok(flags, tr, lo, hi, want):
    keys = [t for t, _ in steps(tr)]
    if want:
        bad = [k for k, x in zip(keys, flags) if x is not True]
        return all(not (lo <= b < hi) for b in bad), bad
    return (not all(x is True for x in flags)), [k for k, x in zip(keys, flags) if x is not True]


def grid_report(cases, world=LIFE_W):
    names = [f"C13{v}" for v in VARIANTS]
    cands = {v: c13(v, world) for v in VARIANTS}
    rows, refused, matched, shift_fail, verd = [], {v: 0 for v in VARIANTS}, {v: 0 for v in VARIANTS}, [], {}
    for case in cases:
        cells, vs = [], []
        for v in VARIANTS:
            mk, det = R.score(case, "C13" + v, cands[v])
            cells.append(mk)
            vs.append(str(det))
            matched[v] += mk == "✓"
            _, fl = R.verdict(case, cands[v])
            refused[v] += fl is not None and any(x is not True for f in fl for x in f)
            msh, _ = R.score(R.shifted(case), "C13" + v, cands[v])
            H7 = np.concatenate([np.zeros((7,) + case["H"].shape[1:], dtype=bool), case["H"]])
            same_t = all(cands[v](case["H"], R.trim(tr)) ==
                         cands[v](H7, {t + 7: f for t, f in R.trim(tr).items()})
                         for tr in case["tracings"])
            if msh != mk or not same_t:
                shift_fail.append((case["name"], v))
            verd[(case["name"], v)] = (mk, det)
        rows.append(f"| {case['name']} | {case['target']} | " + " | ".join(cells) +
                    " | " + "; ".join(vs) + " |")
    head = ["| Case | Target | " + " | ".join(names) + " | Verdicts (a; b; c) |",
            "|---|---|" + "---|" * len(names) + "---|"]
    tail = ["| Rows matched | | " + " | ".join(str(matched[v]) for v in VARIANTS) + " | |",
            "| Rows refused | | " + " | ".join(str(refused[v]) for v in VARIANTS) + " | |"]
    return head + rows + tail, shift_fail, verd


def parts_report(parts):
    out, sec0, score = [], None, {v: 0 for v in VARIANTS}
    head = ["| Part | Target | " + " | ".join(f"C13{v}" for v in VARIANTS) + " | Steps not carried (a; b; c) |",
            "|---|---|" + "---|" * len(VARIANTS) + "---|"]
    for sec, name, target, H, tr, lo, hi, want, rule in parts:
        if sec != sec0:
            out += ([""] if sec0 else []) + [f"#### {sec}", ""] + head
            sec0 = sec
        w = world_of(rule)
        cells, bads = [], []
        for v in VARIANTS:
            fl = c13(v, w)(H, tr)
            ok, bad = part_ok(fl, tr, lo, hi, want)
            score[v] += ok
            cells.append(mark(ok))
            bads.append(str(bad[:6]))
        out.append(f"| {name} | {target} | " + " | ".join(cells) + " | " + "; ".join(bads) + " |")
    return out + [""], score


def main():
    out = []
    cases = c12.all_grid_cases()
    print("grid...", file=sys.stderr)
    rows, sf, verd = grid_report(cases)
    out += ["### Grid", ""] + rows + ["",
            "Shift check (7 rows, 13 columns; 7 steps): " +
            ("every mark and flag unchanged." if not sf else f"changed: {sf}"), ""]

    print("representation...", file=sys.stderr)
    rep_fail = []
    for case in cases:
        for v in VARIANTS:
            for tr in case["tracings"]:
                tr = R.trim(tr)
                if tr and c13(v, LIFE_W)(case["H"], tr) != c13(v, LIFE_T)(case["H"], tr):
                    rep_fail.append((case["name"], v))
    out += ["Representation check (rule as lookup table): " +
            ("every flag unchanged." if not rep_fail else f"changed: {rep_fail}"), ""]

    print("probes...", file=sys.stderr)
    pr, sc = parts_report(c12.probe_parts())
    out += ["### Registered probes", ""] + pr + \
        ["Parts matched (of 10): " + ", ".join(f"C13{v} {sc[v]}" for v in VARIANTS), ""]

    print("elemental...", file=sys.stderr)
    g = C.case_glider()
    H, tr = g["H"], g["tracings"][0]
    sites = sorted(frozenset().union(*tr.values()))
    nc = sum(all(x is True for x in c13("a")(H, {t: frozenset([p]) for t in range(len(H))}))
             for p in sites)
    out += [f"Elemental: {nc} of {len(sites)} crossed cells carried (clause E, site).",
            f"Rule 184 flow derived from the table: {flow_of(c11.R184.tab)}; Life conserving: "
            f"{flow_of(c11.LIFE.tab) is not None}.", ""]

    print("unseen...", file=sys.stderr)
    out += ["### Unseen boards", ""]
    usc = {v: [0, 0] for v in VARIANTS}
    for n, gcfg in enumerate(unseen(gliders_configs), 1):
        p, s = parts_report(glider_parts(gcfg, f"U-gliders {n}"))
        out += p
        for v in VARIANTS:
            usc[v][0] += s[v]
            usc[v][1] += 4
    for n, qcfg in enumerate(unseen(eater_configs), 1):
        p, s = parts_report(eater_parts(qcfg, f"U-eater {n}"))
        out += p
        for v in VARIANTS:
            usc[v][0] += s[v]
            usc[v][1] += 4
    crow = ["| Board | Target | " + " | ".join(f"C13{v}" for v in VARIANTS) + " | Detail (a; b; c) |",
            "|---|---|---|---|---|---|"]
    reg = (37, 39)
    ucol = [c for c in collision_configs(6) if c["placement"] != reg][:3]
    out.append(f"Debris boards in the registered search range: "
               f"{[c['placement'] for c in collision_configs(3)]}; widened to offsets −6..6 (amendment).")
    for n, case in enumerate(ucol, 1):
        cells, dets = [], []
        for v in VARIANTS:
            mk, det = R.score(case, "C13" + v, c13(v))
            cells.append(mk)
            dets.append(det)
            usc[v][0] += mk == "✓"
            usc[v][1] += 1
        crow.append(f"| U-collision {n}, block at {case['placement']} | break at crash | " +
                    " | ".join(cells) + " | " + "; ".join(dets) + " |")
    out += ["#### U-collision", ""] + crow + ["",
            "Unseen parts matched: " + ", ".join(f"C13{v} {usc[v][0]} of {usc[v][1]}" for v in VARIANTS), ""]

    print("by-product fork...", file=sys.stderr)
    out += ["### Fork F2: tracings with by-products removed", "",
            "| Board | Part | Target | Kept steps | C13a | C13b | C13c | Steps not carried (a; b; c) |",
            "|---|---|---|---|---|---|---|---|"]
    fsc = {v: [0, 0] for v in VARIANTS}
    gl = [("registered", PR.probe_gliders())] + [(f"U-gliders {n}", x) for n, x in enumerate(unseen(gliders_configs), 1)]
    ea = [("registered", PR.probe_eater())] + [(f"U-eater {n}", x) for n, x in enumerate(unseen(eater_configs), 1)]
    rows = []
    for tag, g_ in gl:
        H, s_, e_ = g_["H"], g_["start"], g_["end"]
        rows.append((tag, f"The interaction, {s_}–{e_}", H, by_product_trim(H, frame_of(H[s_]), s_), s_, e_))
    for tag, q_ in ea:
        H, s_, e_ = q_["H"], q_["start"], q_["end"]
        rows.append((tag, f"The interaction, {s_}–{e_}", H, by_product_trim(H, frame_of(H[s_]), s_), s_, e_))
        rows.append((tag, "The eater persists", H, by_product_trim(H, q_["eater"], 0), 0, T))
    for tag, name, H, tr, lo, hi in rows:
        cells, bads = [], []
        reach = max(tr) >= hi - 1 if hi < T else max(tr) == T
        for v in VARIANTS:
            fl = c13(v)(H, tr)
            ok, bad = part_ok(fl, tr, lo, hi, True)
            ok = ok and reach
            cells.append(mark(ok))
            bads.append(str(bad[:6]))
            if tag != "registered":
                fsc[v][0] += ok
                fsc[v][1] += 1
        out.append(f"| {tag} | {name} | carried | {min(tr)}–{max(tr)} | " + " | ".join(cells) +
                   " | " + "; ".join(bads) + " |")
    out += ["", "Unseen F2 parts matched: " + ", ".join(f"C13{v} {fsc[v][0]} of {fsc[v][1]}" for v in VARIANTS), ""]
    g_ = PR.probe_gliders()
    H, s_, e_ = g_["H"], g_["start"], g_["end"]
    Rt = C.follow(H, frame_of(H[s_]), s_, T)
    tail = []
    for v in VARIANTS:
        fl = c13(v)(H, Rt)
        tail.append(all(x is True for (k, _), x in zip(steps(Rt), fl) if k >= e_))
    out += [f"N-1b (amendment): the registered interaction tracing after its interval, steps {e_}–{T}, "
            f"the products traced as one from contact: " +
            ", ".join(f"C13{v} {'holds' if x else 'uncarried'}" for v, x in zip(VARIANTS, tail)), ""]

    print("new cases...", file=sys.stderr)
    nc_, _ = new_cases()
    out += ["### New cases (no target)", "",
            "| Case | C13a | C13b | C13c | C10 | Steps not carried (a; b; c) |", "|---|---|---|---|---|---|"]
    for name, Hn, trn, w in nc_:
        cells, bads = [], []
        for v in VARIANTS:
            fl = c13(v, w)(Hn, trn)
            cells.append("holds" if all(x is True for x in fl) else "uncarried")
            bads.append(str([k for (k, _), x in zip(steps(trn), fl) if x is not True][:5]))
        if w is LIFE_W:
            fl10 = CANDIDATES["C10"](Hn, trn)
        else:
            fl10 = PR.flags184(trn, "C10", Hn)
        c10v = "holds" if all(x is True for x in fl10) else "uncarried"
        out.append(f"| {name} | " + " | ".join(cells) + f" | {c10v} | " + "; ".join(bads) + " |")
    print("\n".join(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
