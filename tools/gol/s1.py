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


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "score"
    {"conflicts": conflicts}[mode]()
