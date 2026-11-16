"""Iteration-0 cases. Each case: a history H, tracings (dict step -> frame), a target."""
import numpy as np
from scipy import ndimage
from life import (GLIDER, BLOCK, STILL_LIFES, N, board, run, frame_of, dilate,
                  is_glider, symmetries, shape)

T = 120


def cells_at(H, t, near):
    return frozenset(p for p in near if H[t][p])


def track_glider(H, frame, t0, t1=T):
    """Follow a glider forward while it is glider-shaped. Returns frames, stop step."""
    frames = {t0: frame}
    for t in range(t0, t1):
        nxt = cells_at(H, t + 1, dilate(frames[t], 1))
        if not is_glider(nxt):
            return frames, t + 1
        frames[t + 1] = nxt
    return frames, None


def follow(H, frame, t0, t1, k=1):
    """Follow whatever is alive near the previous frame."""
    frames = {t0: frame}
    for t in range(t0, t1):
        frames[t + 1] = cells_at(H, t + 1, dilate(frames[t], k))
    return frames


def glider_at(r, c):
    return frozenset((r + dr, c + dc) for dr, dc in GLIDER)


def case_glider():
    H = run(board((GLIDER, (10, 10))), T)
    tr, stop = track_glider(H, glider_at(10, 10), 0)
    assert stop is None
    return dict(name="Glider", H=H, tracings=[tr], target="holds")


def case_two_gliders():
    H = run(board((GLIDER, (10, 10)), (GLIDER, (10, 60))), T)
    a, _ = track_glider(H, glider_at(10, 10), 0)
    b, _ = track_glider(H, glider_at(10, 60), 0)
    assert len(a) == len(b) == T + 1
    return dict(name="Two identical gliders", H=H, tracings=[a, b], target="holds")


def case_splice():
    H = run(board((GLIDER, (10, 10)), (GLIDER, (10, 60))), T)
    a, _ = track_glider(H, glider_at(10, 10), 0)
    b, _ = track_glider(H, glider_at(10, 60), 0)
    tr = {t: (a[t] if t < 100 else b[t]) for t in range(T + 1)}
    return dict(name="Splice", H=H, tracings=[tr], target="uncarried")


def case_step_indexed():
    H = run(board((GLIDER, (10, 10)), (BLOCK, (80, 20))), T)
    a, _ = track_glider(H, glider_at(10, 10), 0)
    blk = frozenset((80 + dr, 20 + dc) for dr, dc in BLOCK)
    tr = {t: (a[t] if t < 100 else blk) for t in range(T + 1)}
    return dict(name="Step-indexed", H=H, tracings=[tr], target="uncarried")


def case_periodic_splice():
    placed = [(GLIDER, (10, 10 + 8 * k)) for k in range(8)]
    H = run(board(*placed), T)
    tracks = [track_glider(H, glider_at(10, 10 + 8 * k), 0)[0] for k in range(8)]
    assert all(len(x) == T + 1 for x in tracks)
    tr = {t: tracks[t % 8][t] for t in range(T + 1)}
    return dict(name="Cyclic splice, 8 gliders (first build)", H=H, tracings=[tr],
                target="uncarried (proposed; owner pending)")


def case_alternating_splice():
    """A, B, A, B: every jump is the same rule-like move for each phase."""
    H = run(board((GLIDER, (10, 10)), (GLIDER, (10, 60))), T)
    a, _ = track_glider(H, glider_at(10, 10), 0)
    b, _ = track_glider(H, glider_at(10, 60), 0)
    tr = {t: (a[t] if t % 2 == 0 else b[t]) for t in range(T + 1)}
    return dict(name="Alternating splice", H=H, tracings=[tr],
                target="uncarried (proposed; owner pending)")


def case_collision(debris=True):
    """Glider into a block. debris=True: a placement that leaves a remnant to follow."""
    for dr in range(-3, 4):
        for dc in range(-3, 4):
            H = run(board((GLIDER, (10, 10)), (BLOCK, (40 + dr, 40 + dc))), T)
            a, tc = track_glider(H, glider_at(10, 10), 0)
            if tc is None or tc > 100:
                continue
            last = max(a)
            tail = follow(H, a[last], last, T)
            tr = {**a, **tail}
            if debris and not all(tr[t] for t in tr):
                continue
            name = "Collision" if debris else "Collision, annihilating (first build)"
            return dict(name=name, H=H, tracings=[tr], target="break at crash",
                        crash=tc, placement=(40 + dr, 40 + dc))
    raise RuntimeError("no collision found")


def gliders_in(b):
    """Glider-shaped connected components of a board."""
    lab, n = ndimage.label(b, structure=np.ones((3, 3)))
    out = []
    for i in range(1, n + 1):
        f = frame_of(lab == i)
        if is_glider(f):
            out.append(f)
    return out


def case_indirect_splice():
    """Search small collisions for a one-time turner: glider A in, a different glider B out."""
    for name, cells in STILL_LIFES.items():
        for sym in symmetries(cells):
            for dr in range(-4, 5):
                for dc in range(-4, 5):
                    pos = (30 + dr, 30 + dc)
                    H = run(board((GLIDER, (10, 10)), (list(sym), pos)), T)
                    a, tc = track_glider(H, glider_at(10, 10), 0)
                    if tc is None or tc > 60:
                        continue
                    outs = gliders_in(H[T])
                    if len(outs) != 1:
                        continue
                    # B: tracked back from the end while glider-shaped
                    b = {T: outs[0]}
                    t = T
                    while t > 0:
                        prev = cells_at(H, t - 1, dilate(b[t], 1))
                        if not is_glider(prev):
                            break
                        b[t - 1] = prev
                        t -= 1
                    tb = t
                    if tb <= tc + 2 or T - tb < 20:
                        continue
                    # B must move: glider shape 4 steps on, shifted diagonally
                    s0, o0 = shape(b[T - 4])
                    s1, o1 = shape(b[T])
                    if s0 != s1 or abs(o1[0] - o0[0]) != 1 or abs(o1[1] - o0[1]) != 1:
                        continue
                    last = max(a)
                    mid = follow(H, a[last], last, tb - 1, k=2)
                    tr = {**a, **mid, **{s: b[s] for s in b if s >= tb}}
                    if sorted(tr) != list(range(T + 1)):
                        continue
                    return dict(name="Indirect splice", H=H, tracings=[tr],
                                target="uncarried", crash=tc, emerge=tb,
                                reaction=(name, pos))
    raise RuntimeError("no one-time turner found")


def all_cases():
    return [case_glider(), case_two_gliders(), case_splice(), case_indirect_splice(),
            case_collision(debris=False), case_collision(), case_step_indexed(),
            case_periodic_splice(), case_alternating_splice()]
