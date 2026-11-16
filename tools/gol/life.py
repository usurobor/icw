"""Game of Life on a wrapping board, and helpers for frames (sets of live cells)."""
import numpy as np

N = 128  # board side

GLIDER = [(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)]  # moves (+1, +1) every 4 steps
BLOCK = [(0, 0), (0, 1), (1, 0), (1, 1)]
STILL_LIFES = {
    "block": BLOCK,
    "beehive": [(0, 1), (0, 2), (1, 0), (1, 3), (2, 1), (2, 2)],
    "boat": [(0, 0), (0, 1), (1, 0), (1, 2), (2, 1)],
    "loaf": [(0, 1), (0, 2), (1, 0), (1, 3), (2, 1), (2, 3), (3, 2)],
    "tub": [(0, 1), (1, 0), (1, 2), (2, 1)],
    "ship": [(0, 0), (0, 1), (1, 0), (1, 2), (2, 1), (2, 2)],
}


def step(b):
    n = sum(np.roll(np.roll(b, i, 0), j, 1)
            for i in (-1, 0, 1) for j in (-1, 0, 1) if (i, j) != (0, 0))
    return (n == 3) | (b & (n == 2))


def run(b, steps):
    h = [b]
    for _ in range(steps):
        h.append(step(h[-1]))
    return np.array(h)


def board(*placed, n=N):
    b = np.zeros((n, n), dtype=bool)
    for cells, (r, c) in placed:
        for dr, dc in cells:
            b[(r + dr) % n, (c + dc) % n] = True
    return b


def frame_of(b):
    return frozenset(zip(*map(lambda a: a.tolist(), np.nonzero(b))))


def to_board(frame, n=N):
    b = np.zeros((n, n), dtype=bool)
    for r, c in frame:
        b[r % n, c % n] = True
    return b


def isolated_next(frame, n=N):
    """The frame alone on an empty board, one step on."""
    return frame_of(step(to_board(frame, n)))


def dilate(frame, k=1, n=N):
    return frozenset(((r + i) % n, (c + j) % n) for r, c in frame
                     for i in range(-k, k + 1) for j in range(-k, k + 1))


def shape(frame):
    """Shape and offset of a frame. Frames never straddle the board edge here."""
    if not frame:
        return frozenset(), (0, 0)
    r0 = min(r for r, _ in frame)
    c0 = min(c for _, c in frame)
    return frozenset((r - r0, c - c0) for r, c in frame), (r0, c0)


def symmetries(cells):
    out = []
    for flip in (False, True):
        for rot in range(4):
            pts = [(c, r) if flip else (r, c) for r, c in cells]
            for _ in range(rot):
                pts = [(c, -r) for r, c in pts]
            out.append(shape(frozenset(pts))[0])
    return list(dict.fromkeys(out))


def _glider_shapes():
    shapes = set()
    for g in symmetries(GLIDER):
        f = frozenset((r + 10, c + 10) for r, c in g)
        for _ in range(4):
            shapes.add(shape(f)[0])
            f = isolated_next(f)
    return frozenset(shapes)


GLIDER_SHAPES = _glider_shapes()


def is_glider(frame):
    return shape(frame)[0] in GLIDER_SHAPES
