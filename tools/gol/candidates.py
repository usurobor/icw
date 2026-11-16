"""Candidate definitions of *carried*. Each judges every step t -> t+1 of a tracing."""
from collections import Counter
import numpy as np
from scipy import ndimage
from life import isolated_next, dilate, shape


K3 = np.ones((3, 3))
K3[1, 1] = 0


def local_next(frame):
    """One step of the frame alone, computed on a small padded array."""
    if not frame:
        return frozenset()
    rs = [r for r, _ in frame]
    cs = [c for _, c in frame]
    r0, c0 = min(rs) - 2, min(cs) - 2
    a = np.zeros((max(rs) - r0 + 3, max(cs) - c0 + 3), dtype=bool)
    for r, c in frame:
        a[r - r0, c - c0] = True
    n = ndimage.convolve(a.astype(int), K3, mode="constant")
    b = (n == 3) | (a & (n == 2))
    return frozenset((int(r) + r0, int(c) + c0) for r, c in zip(*np.nonzero(b)))


def blobs(frame):
    """8-connected pieces of a frame."""
    if not frame:
        return []
    rs = [r for r, _ in frame]
    cs = [c for _, c in frame]
    r0, c0 = min(rs), min(cs)
    a = np.zeros((max(rs) - r0 + 1, max(cs) - c0 + 1), dtype=bool)
    for r, c in frame:
        a[r - r0, c - c0] = True
    lab, n = ndimage.label(a, structure=np.ones((3, 3)))
    return [frozenset((int(r) + r0, int(c) + c0) for r, c in zip(*np.nonzero(lab == i)))
            for i in range(1, n + 1)]


def integrated(frame, evolve=local_next, pieces=blobs):
    """True unless the stage splits into two groups that, run apart, give what the whole gives."""
    bs = pieces(frame)
    if len(bs) <= 1:
        return True
    whole = evolve(frame)
    n = len(bs)
    for mask in range(1, 2 ** (n - 1)):
        P = frozenset().union(*[bs[i + 1] for i in range(n - 1) if mask >> i & 1])
        Q = frame - P
        if evolve(P) | evolve(Q) == whole:
            return False
    return True


def steps(tr):
    ts = sorted(tr)
    return list(zip(ts[:-1], ts[1:]))


def closure(H, tr):
    return [isolated_next(tr[t]) == tr[u] for t, u in steps(tr)]


def c9_closure_integration(H, tr):
    return [c and integrated(tr[t]) for c, (t, u) in zip(closure(H, tr), steps(tr))]


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
    "C9": c9_closure_integration,
}


# --- C10: best continuer, integration over the interval (declared in notes/runs/2026-11-16-c10.md) ---

from fractions import Fraction


def jaccard(a, b):
    """Exact overlap, so ties are real ties."""
    u = a | b
    return Fraction(len(a & b), len(u)) if u else Fraction(0)


def near2d(frame):
    return dilate(frame, 1)


def far2d(p, q):
    if not p or not q:
        return True
    return min(max(abs(a - c), abs(b - d)) for a, b in p for c, d in q) >= 3


def window_integrated(tr, t, evolve, pieces, far):
    """True: one whole. False: splits into parts that run apart to the end and finish apart.
    None: they run apart to the end but finish within two cells (unresolved)."""
    F = tr[t]
    bs = pieces(F)
    if len(bs) <= 1:
        return True
    later = [u for u in sorted(tr) if u > t]
    n, unresolved = len(bs), False
    for mask in range(1, 2 ** (n - 1)):
        p = frozenset().union(*[bs[i + 1] for i in range(n - 1) if mask >> i & 1])
        q = F - p
        ok = True
        for u in later:
            p, q = evolve(p), evolve(q)
            if p | q != tr[u]:
                ok = False
                break
        if ok:
            if far(p, q):
                return False
            unresolved = True
    return None if unresolved else True


def unique_best(scores, rivals_differ):
    """scores[0] is the proposal; rivals_differ[i] says rival i is a different stage.
    Returns True, False, or "tie" (a different stage equally close)."""
    s0 = scores[0]
    if s0 <= 0:
        return False
    rivals = [s for s, d in zip(scores[1:], rivals_differ[1:]) if d]
    if any(s > s0 for s in rivals):
        return False
    return "tie" if any(s == s0 for s in rivals) else True


def c10_flags(tr, board_at, evolve=local_next, pieces=blobs, near=near2d, far=far2d, share=None):
    out = []
    for t, u in steps(tr):
        F, X = tr[t], tr[u]
        isoF = evolve(F)
        if share is not None:
            ok = jaccard(X, isoF) > share
        else:
            conts = [X] + [p for p in pieces(board_at(u)) if p & near(F)] + [frozenset()]
            fwd = unique_best([jaccard(c, isoF) for c in conts], [c != X for c in conts])
            preds = [F] + [p for p in pieces(board_at(t)) if p & near(X)] + [frozenset()]
            bwd = unique_best([jaccard(X, evolve(p)) for p in preds], [p != F for p in preds])
            ok = True if (fwd is True and bwd is True) else \
                ("tie" if "tie" in (fwd, bwd) and False not in (fwd, bwd) else False)
        if ok is not True:
            out.append(ok)
            continue
        out.append(window_integrated(tr, t, evolve, pieces, far))
    return out


def _c10(share=None):
    def judge(H, tr):
        return c10_flags(tr, lambda t: frame_of(H[t]), share=share)
    return judge


from life import frame_of  # noqa: E402

CANDIDATES["C10"] = _c10()
CANDIDATES["C10s"] = _c10(share=0.5)
