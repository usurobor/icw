"""Transport and moving patterns in the elementary cellular automata.

Transport: flip one cell of a random board and follow the difference.
A rule transports when the difference ever stands 3 or more cells from the
flipped site (beyond the first step's reach).
Moving pattern: a finite seed on a quiescent 0 background that recurs
translated (period p <= 40, shift d != 0). Only rules with 000 -> 0 have
that background; the rest are reported as not searched.
"""
import random, sys

def step(cells, rule):
    n = len(cells)
    return [(rule >> (cells[i-1]*4 + cells[i]*2 + cells[(i+1) % n])) & 1 for i in range(n)]

def reflect(rule):
    out = 0
    for k in range(8):
        a, b, c = (k >> 2) & 1, (k >> 1) & 1, k & 1
        if (rule >> k) & 1: out |= 1 << (c*4 + b*2 + a)
    return out

def complement(rule):
    out = 0
    for k in range(8):
        if not (rule >> (7 - k)) & 1: out |= 1 << k
    return out

def classes():
    seen, reps = set(), []
    for r in range(256):
        if r in seen: continue
        orbit = {r, reflect(r), complement(r), reflect(complement(r))}
        seen |= orbit
        reps.append((min(orbit), sorted(orbit)))
    return reps

def transports(rule, trials=20, n=201, t=60, seed=0):
    rng = random.Random(seed)
    mid = n // 2
    for _ in range(trials):
        a = [rng.randint(0, 1) for _ in range(n)]
        b = a[:]; b[mid] ^= 1
        for _ in range(t):
            a, b = step(a, rule), step(b, rule)
            for i in range(n):
                if a[i] != b[i] and abs(i - mid) >= 3:
                    return True
    return False

def spaceship(rule, maxw=10, maxp=40):
    if rule & 1:  # 000 -> 1: no quiescent 0 background
        return None
    n = 2 * (maxw + 2 * maxp) + 20
    for w in range(1, maxw + 1):
        for body in range(2 ** (w - 2) if w > 1 else 1):
            bits = [1] + ([int(x) for x in format(body, f'0{w-2}b')] if w > 2 else []) + ([1] if w > 1 else [])
            cells = [0] * n
            off = n // 2 - w // 2
            for i, x in enumerate(bits): cells[off + i] = x
            start = cells[:]
            cur = cells
            for p in range(1, maxp + 1):
                cur = step(cur, rule)
                if not any(cur): break
                ones = [i for i, x in enumerate(cur) if x]
                if ones[-1] - ones[0] + 1 == w:
                    d = ones[0] - off
                    if d != 0 and cur[ones[0]:ones[0] + w] == bits:
                        return (bits, p, d)
    return False

if __name__ == '__main__':
    rows = []
    for rep, orbit in classes():
        # pick a member with 000 -> 0 for the background search, if any
        quiet = [r for r in orbit if not r & 1]
        s = spaceship(quiet[0]) if quiet else None
        rows.append((rep, transports(rep), s, quiet[0] if quiet else None))
    nt = sum(1 for r in rows if r[1])
    print(f"classes: {len(rows)}; transport: {nt}; no transport: {len(rows)-nt}")
    ships = [r for r in rows if r[2]]
    print("moving pattern found:", len(ships))
    bad = [r for r in ships if not r[1]]
    print("moving pattern without transport:", [r[0] for r in bad])
    nots = [r[0] for r in rows if not r[1]]
    print("no-transport classes:", nots)
    tr_noship = [r[0] for r in rows if r[1] and r[2] is False]
    print("transport, no moving pattern on 0 background:", tr_noship)
    print("not searched (no quiescent background):", [r[0] for r in rows if r[2] is None])
    print("examples:", [(r[0], r[3], r[2][1], r[2][2]) for r in ships][:40])
