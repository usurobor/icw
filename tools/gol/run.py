"""Iteration 0: every candidate on every case. Prints a markdown report."""
import sys
import numpy as np
from life import N
from cases import all_cases, case_glider
from candidates import CANDIDATES


# --- checks 1-3 (kernel §6) on partitions of occurrences (step, row, col) ---

def cell_labels(H):
    T1 = len(H)
    return np.broadcast_to(np.arange(N * N).reshape(N, N), (T1, N, N)).ravel()


def tracing_labels(H, tracings):
    T1 = len(H)
    lab = np.arange(T1 * N * N, dtype=np.int64).reshape(T1, N, N) + len(tracings)
    for k, tr in enumerate(tracings):
        for t, f in tr.items():
            for r, c in f:
                lab[t, r, c] = k
    return lab.ravel()


def refines(P, Q):
    M = np.int64(Q.max() + 1)
    return len(np.unique(P.astype(np.int64) * M + Q)) == len(np.unique(P))


def checks_1_to_3(H, A, B):
    if not (H[1:] != H[:-1]).any():
        return "untyped"
    ab, ba = refines(A, B), refines(B, A)
    if ab and ba:
        return "coincident"
    if ab or ba:
        return "nested"
    return None


# --- candidates, scoring ---

def judge(cand, H, tr):
    v = cand(H, tr)
    return v if isinstance(v, list) else [v]


def trim(tr):
    live = [t for t in sorted(tr) if tr[t]]
    return {t: tr[t] for t in sorted(tr) if live and live[0] <= t <= live[-1]}


def verdict(case, cand):
    H = case["H"]
    case = {**case, "tracings": [trim(tr) for tr in case["tracings"]]}
    if not all(case["tracings"]):
        return "not a continuity", None
    pre = checks_1_to_3(H, cell_labels(H), tracing_labels(H, case["tracings"]))
    if pre:
        return pre, None
    flags = [judge(cand, H, tr) for tr in case["tracings"]]
    return ("holds" if all(all(f) for f in flags) else "uncarried"), flags


def score(case, name, cand):
    v, flags = verdict(case, cand)
    tgt = case["target"]
    if case["name"].startswith("Collision"):
        if getattr(cand, "whole", False):
            return "n/a", v
        f, tc = flags[0], case["crash"]
        before = all(f[:max(tc - 3, 0)])
        broke = not all(f[tc - 3:tc + 3])
        return ("✓" if before and broke else "✗"), f"break at {[i for i, x in enumerate(f) if not x][:4]}, crash {tc}"
    if tgt.startswith("pending"):
        return v, v
    want = tgt.split()[0]
    return ("✓" if v == want else "✗"), v


def shifted(case, d=(7, 13)):
    H = np.roll(case["H"], d, axis=(1, 2))
    trs = [{t: frozenset(((r + d[0]) % N, (c + d[1]) % N) for r, c in f)
            for t, f in tr.items()} for tr in case["tracings"]]
    return {**case, "H": H, "tracings": trs}


def main():
    cases = all_cases()
    names = list(CANDIDATES)
    rows, notes, shift_fail = [], [], []
    for case in cases:
        cells = []
        for n in names:
            mark, detail = score(case, n, CANDIDATES[n])
            mark2, _ = score(shifted(case), n, CANDIDATES[n])
            if mark2 != mark:
                shift_fail.append((case["name"], n))
            cells.append(mark)
            notes.append(f"- {case['name']} / {n}: {detail}")
        rows.append(f"| {case['name']} | {case['target']} | " + " | ".join(cells) + " |")

    g = case_glider()
    H = g["H"]
    whole = np.zeros(H.size, dtype=np.int64)
    ident = np.arange(H.size, dtype=np.int64)
    trivial = (checks_1_to_3(H, cell_labels(H), whole),
               checks_1_to_3(H, cell_labels(H), ident))

    out = ["| Case | Target | " + " | ".join(names) + " |",
           "|---|---|" + "---|" * len(names)] + rows
    out.append(f"| Trivial groupings | nested | whole board: {trivial[0]}; each occurrence alone: {trivial[1]} (check 3; candidates not reached) |" + " |" * (len(names) - 1))
    out += ["", "Shift check (board moved 7 rows, 13 columns): " +
            ("every mark unchanged." if not shift_fail else f"changed: {shift_fail}"), "",
            "Details:"] + notes
    extra = [c for c in cases if "reaction" in c or "placement" in c]
    for c in extra:
        out.append(f"- {c['name']} set-up: " + ", ".join(f"{k}={c[k]}" for k in ("reaction", "placement", "crash", "emerge") if k in c))
    print("\n".join(out))


if __name__ == "__main__":
    sys.exit(main())
