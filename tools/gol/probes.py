"""Integration probes: interacting gliders, glider and eater, rule-184 jam. Candidate C9."""
import numpy as np
from scipy import ndimage
from life import GLIDER, N, board, run, symmetries, frame_of
from cases import track_glider, follow, glider_at, T
from candidates import closure, integrated, local_next, c9_closure_integration, steps

EATER = [(0, 0), (0, 1), (1, 0), (1, 2), (2, 2), (3, 2), (3, 3)]
K5 = np.ones((5, 5))


def dist(f, g):
    return min(max(abs(a - c), abs(b - d)) for a, b in f for c, d in g)


def alone_track(cells, pos, steps_=T):
    H = run(board((cells, pos)), steps_)
    return [frame_of(h) for h in H]


def pieces(frame):
    """Groups of live cells within two cells of each other: groups that cannot interact."""
    cells = list(frame)
    parent = list(range(len(cells)))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    for i, (a, b) in enumerate(cells):
        for j in range(i):
            c, d = cells[j]
            if max(abs(a - c), abs(b - d)) <= 2:
                parent[find(i)] = find(j)
    groups = {}
    for i, p in enumerate(cells):
        groups.setdefault(find(i), set()).add(p)
    return [frozenset(g) for g in groups.values()]


def settled_from(H, t0, need_split=True):
    """First t >= t0 from which the actual board equals its pieces each run alone."""
    for t in range(t0, T + 1):
        ps = pieces(frame_of(H[t]))
        if need_split and len(ps) < 2:
            continue
        runs = [p for p in ps]
        ok = True
        for u in range(t, T + 1):
            if frozenset().union(*runs) != frame_of(H[u]):
                ok = False
                break
            runs = [local_next(p) for p in runs]
        if ok:
            return t
    return None


def flags(tr):
    return c9_closure_integration(None, tr)


def carried_on(tr, lo, hi):
    """C9 carries every step t -> t+1 with lo <= t < hi."""
    f = dict(zip([t for t, _ in steps(tr)], flags(tr)))
    return all(f[t] for t in range(lo, hi) if t in f), [t for t in sorted(f) if not f[t]]


def probe_gliders():
    a0 = (40, 40)
    for b_cells in symmetries(GLIDER):
        for d in range(10, 16):
            for off in range(-4, 5):
                b0 = (40 + d, 40 + d + off)
                H = run(board((GLIDER, a0), (list(b_cells), b0)), T)
                if not H[T].any():
                    continue
                A, B = alone_track(GLIDER, a0), alone_track(list(b_cells), b0)
                start = next((t for t in range(T) if dist(A[t], B[t]) <= 2), None)
                if start is None or start < 5 or start > 40:
                    continue
                end = settled_from(H, start)
                if end is None or end > T - 15:
                    continue
                return dict(H=H, A=A, B=B, start=start, end=end, b0=b0, b=b_cells)
    raise RuntimeError("no interacting pair found")


def probe_eater():
    g0 = (10, 10)
    G = alone_track(GLIDER, g0)
    for e in symmetries(EATER):
        for dr in range(-5, 6):
            for dc in range(-5, 6):
                e0 = (30 + dr, 30 + dc)
                eater = frozenset((e0[0] + r, e0[1] + c) for r, c in e)
                if dist(G[0], eater) <= 3:
                    continue
                H = run(board((GLIDER, g0), (list(e), e0)), T)
                if frame_of(H[T]) != eater:
                    continue
                start = next((t for t in range(T) if dist(G[t], eater) <= 2), None)
                if start is None:
                    continue
                end = next(t for t in range(start, T + 1)
                           if all(frame_of(H[u]) == eater for u in range(t, T + 1)))
                if end - start < 3:
                    continue
                return dict(H=H, G=G, eater=eater, start=start, end=end, e0=e0)
    raise RuntimeError("no eater placement found")


# --- rule 184 on a ring ---

L = 240


def step184(a):
    return (a & np.roll(a, -1)) | (np.roll(a, 1) & ~a)


def next184(frame):
    a = np.zeros(L, dtype=bool)
    for i in frame:
        a[i % L] = True
    return frozenset(np.nonzero(step184(a))[0].tolist())


def runs184(frame):
    out, cur = [], []
    for i in sorted(frame):
        if cur and i != cur[-1] + 1:
            out.append(frozenset(cur))
            cur = []
        cur.append(i)
    if cur:
        out.append(frozenset(cur))
    return out


def c9_184(tr):
    out = []
    for t, u in steps(tr):
        out.append(next184(tr[t]) == tr[u] and integrated(tr[t], next184, runs184))
    return out


def probe_jam():
    a = np.zeros(L, dtype=bool)
    a[0:120:2] = True             # inflow, density 1/2
    a[120:140] = True             # the jam
    a[141:L:2] = True             # outflow region, density 1/2
    H = [a]
    pos = list(np.nonzero(a)[0])  # car k at pos[k]
    cars = [list(pos)]
    for _ in range(T):
        cur = H[-1]
        moved = [(p + 1) % L if not cur[(p + 1) % L] else p for p in cars[-1]]
        cars.append(moved)
        H.append(step184(cur))
    jam = {}
    prev = frozenset(range(120, 140))
    for t in range(T + 1):
        rs = [r for r in runs184(frozenset(np.nonzero(H[t])[0].tolist())) if len(r) >= 3]
        near = [r for r in rs if min(min(abs(i - j) for j in prev) for i in r) <= 2]
        if not near:
            break
        prev = max(near, key=len)
        jam[t] = prev
    inside0 = {k for k, p in enumerate(cars[0]) if p in jam[0]}
    # cars that leave the jam come round the ring and re-enter it; compare at step 40
    insideT = {k for k, p in enumerate(cars[40]) if p in jam[40]}
    car = {t: frozenset([cars[t][min(inside0)]]) for t in range(T + 1)}
    return dict(jam=jam, car=car, turnover=not (inside0 & insideT),
                jam_len=(len(jam[0]), len(jam[max(jam)])), last=max(jam))


def main():
    out = []
    g = probe_gliders()
    s, e = g["start"], g["end"]
    trA, _ = track_glider(g["H"], g["A"][0], 0)
    trB, _ = track_glider(g["H"], g["B"][0], 0)
    okA, brA = carried_on(trA, 0, s - 1)
    okB, brB = carried_on(trB, 0, s - 1)
    union = {t: trA[t] | trB[t] for t in range(0, s)}
    u_ok = not all(flags(union))
    R = follow(g["H"], frame_of(g["H"][s]), s, T)
    okR, brR = carried_on(R, s, e)
    n_out = len(pieces(frame_of(g["H"][e])))
    out += [f"### Two gliders that interact (B placed at {g['b0']}; contact interval {s}–{e})", "",
            "| Part | Target | C9 | Detail |", "|---|---|---|---|",
            f"| Glider A before contact | carried | {'✓' if okA else '✗'} | breaks {brA[:6]} |",
            f"| Glider B before contact | carried | {'✓' if okB else '✗'} | breaks {brB[:6]} |",
            f"| A and B as one, before contact | uncarried | {'✓' if u_ok else '✗'} | |",
            f"| The interaction, {s}–{e} | carried | {'✓' if okR else '✗'} | breaks {[t for t in brR if s <= t < e][:8]} |",
            f"| After {e} | classify | — | {n_out} separate pieces; the interaction tracing breaks at {[t for t in brR if t >= e][:3]} |", ""]

    q = probe_eater()
    s, e = q["start"], q["end"]
    trG, stop = track_glider(q["H"], q["G"][0], 0)
    okG, brG = carried_on(trG, 0, s - 1)
    R = follow(q["H"], frame_of(q["H"][s]), s, T)
    okR, brR = carried_on(R, s, e)
    region = set()
    for r, c in q["eater"]:
        region |= {(r + i, c + j) for i in (-1, 0, 1) for j in (-1, 0, 1)}
    E = {t: frozenset(p for p in region if q["H"][t][p]) for t in range(T + 1)}
    okE, brE = carried_on(E, 0, T)
    E2 = {t: (q["eater"] if t < s or t >= e else frame_of(q["H"][t])) for t in range(T + 1)}
    okE2, brE2 = carried_on(E2, 0, T)
    out += [f"### Glider meets an eater (eater at {q['e0']}; contact interval {s}–{e}; glider tracker stops at {stop})", "",
            "| Part | Target | C9 | Detail |", "|---|---|---|---|",
            f"| Glider until contact | carried | {'✓' if okG else '✗'} | breaks {brG[:6]} |",
            f"| The interaction, {s}–{e} | carried | {'✓' if okR else '✗'} | breaks {[t for t in brR if s <= t < e][:8]} |",
            f"| Only the eater at the end | yes | ✓ | board at step {T} equals the eater |",
            f"| The eater persists: its region | carried | {'✓' if okE else '✗'} | breaks {brE[:8]} |",
            f"| The eater persists: eater, interaction, eater | carried | {'✓' if okE2 else '✗'} | breaks {brE2[:8]} |", ""]

    j = probe_jam()
    fj = c9_184(j["jam"])
    fc = c9_184(j["car"])
    out += [f"### Rule-184 jam (ring of {L}; jam {j['jam_len'][0]} cars long at step 0, {j['jam_len'][1]} at step {j['last']}; jam moves backward one cell a step; none of its cars at step 0 are in it at step 40: {j['turnover']})", "",
            "| Part | Target | C9 | Detail |", "|---|---|---|---|",
            f"| The jam holds | carried | {'✓' if all(fj) else '✗'} | carried on {sum(fj)} of {len(fj)} steps |",
            f"| A car that passes through the jam | carried | {'✓' if all(fc) else '✗'} | carried on {sum(fc)} of {len(fc)} steps |", ""]
    print("\n".join(out))


if __name__ == "__main__":
    main()
