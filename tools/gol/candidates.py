"""Candidate definitions of *carried*. Each judges every step t -> t+1 of a tracing."""
from collections import Counter
import numpy as np
from scipy import ndimage
from life import isolated_next, dilate, shape


def steps(tr):
    ts = sorted(tr)
    return list(zip(ts[:-1], ts[1:]))


def closure(H, tr):
    return [isolated_next(tr[t]) == tr[u] for t, u in steps(tr)]


def c7_viability(H, tr):
    out = []
    for t, u in steps(tr):
        iso = isolated_next(tr[t])
        region = dilate(tr[t], 1)
        actual = frozenset(p for p in region if H[u][p])
        out.append(iso == tr[u] and actual == (iso & region))
    return out


def c1_film_map(H, tr):
    moves = []
    for t, u in steps(tr):
        s0, o0 = shape(tr[t])
        s1, o1 = shape(tr[u])
        moves.append((s0, (s1, (o1[0] - o0[0], o1[1] - o0[1]))))
    by_key = {}
    for k, v in moves:
        by_key.setdefault(k, Counter())[v] += 1
    out = []
    for k, v in moves:
        ranked = by_key[k].most_common()
        top = ranked[0][1]
        winners = {x for x, n in ranked if n == top}
        out.append(winners == {v})
    return out


def _active(H, t):
    a = np.zeros_like(H[t])
    if t > 0:
        a |= H[t] != H[t - 1]
    if t + 1 < len(H):
        a |= H[t] != H[t + 1]
    return a


def c2_activity(H, tr):
    out = []
    for t, u in steps(tr):
        st = np.stack([_active(H, t), _active(H, u)])
        lab, _ = ndimage.label(st, structure=np.ones((3, 3, 3)))
        start = {lab[0][p] for p in dilate(tr[t], 1)} - {0}
        end = {lab[1][p] for p in dilate(tr[u], 1)} - {0}
        out.append(bool(start & end))
    return out


def segments(frames):
    """Fewest periodic runs (same shape every p <= 8 steps, fixed shift), greedy."""
    def shifted(f, d):
        return frozenset((r + d[0], c + d[1]) for r, c in f)
    i, count = 0, 0
    while i < len(frames):
        count += 1
        best = i + 1
        for p in range(1, 9):
            if i + p >= len(frames):
                break
            s0, o0 = shape(frames[i])
            s1, o1 = shape(frames[i + p])
            if s0 != s1:
                continue
            d = (o1[0] - o0[0], o1[1] - o0[1])
            j = i
            while j + p < len(frames) and frames[j + p] == shifted(frames[j], d):
                j += 1
            best = max(best, j + p)
        i = best
    return count


def c8_shortcut(K):
    def judge(H, tr):
        return segments([tr[t] for t in sorted(tr)]) <= K
    judge.whole = True
    return judge


CANDIDATES = {
    "Closure": closure,
    "C1": c1_film_map,
    "C2": c2_activity,
    "C7": c7_viability,
    "C8, K=1": c8_shortcut(1),
    "C8, K=2": c8_shortcut(2),
}
