"""C2: local statistical complexity filter (light-cone causal states, depth 1).
Declared in notes/runs/2026-11-17-c2.md before this code ran. Rerun: python3 tools/gol/c2.py
"""
import sys

import numpy as np
from scipy import ndimage
from scipy.stats import chi2_contingency

import c11
import c12
import cases as C
import probes as PR
import run as R
from c11 import LIFE, R184, C_steps, mark
from life import run as life_run

ALPHA, NMIN = 0.001, 50


# --- cone indices: the rule's neighbourhood, from the C11 rule objects ---

def cone_index(H, rule):
    """Index of the neighbourhood block around every cell of every frame."""
    H = np.asarray(H, dtype=np.int64)
    idx = np.zeros(H.shape, dtype=np.int64)
    for k, off in enumerate(rule.offs):
        if H.ndim == 3:
            idx |= np.roll(H, (-off[0], -off[1]), axis=(1, 2)) << k
        else:
            idx |= np.roll(H, -off, axis=1) << k
    return idx


def soups_life():
    rng = np.random.default_rng(0)
    for _ in range(16):
        b = rng.random((128, 128)) < 0.375
        yield life_run(b, 300)


def rings_184():
    rng = np.random.default_rng(0)
    for _ in range(64):
        a = rng.random(PR.L) < 0.5
        H = [a]
        for _ in range(300):
            H.append(PR.step184(H[-1]))
        yield np.array(H)


def joint_counts(histories, rule):
    nb = 2 ** len(rule.offs)
    M = np.zeros(nb * nb, dtype=np.int64)
    n = 0
    for H in histories:
        idx = cone_index(H, rule)
        past, fut = idx[:-2], idx[2:]          # past of cells at t = block at t-1; future = block at t+1
        M += np.bincount((past * nb + fut).ravel(), minlength=nb * nb)
        n += past.size
    return M.reshape(nb, nb), n


def same(a, b):
    cols = (a + b) > 0
    if cols.sum() <= 1:
        return True
    return chi2_contingency(np.stack([a[cols], b[cols]]))[1] > ALPHA


def causal_states(M):
    counts = M.sum(1)
    order = np.argsort(-counts, kind="stable")
    states, pools = {}, []
    for p in order:
        if counts[p] == 0:
            continue
        if counts[p] < NMIN:
            pools.append(M[p].copy())
            states[int(p)] = len(pools) - 1
            continue
        for s, pool in enumerate(pools):
            if pool.sum() >= NMIN and same(M[p], pool):
                pools[s] = pool + M[p]
                states[int(p)] = s
                break
        else:
            pools.append(M[p].copy())
            states[int(p)] = len(pools) - 1
    prob = np.array([pool.sum() for pool in pools], dtype=float) / counts.sum()
    nb = M.shape[0]
    cx = np.full(nb, np.inf)
    st = np.full(nb, -1)
    for p, s in states.items():
        cx[p] = -np.log2(prob[s])
        st[p] = s
    domain = int(np.argmax(prob))
    return dict(state=st, cx=cx, prob=prob, domain=domain, n_states=len(pools))


_model = {}


def model(rule):
    if rule.name not in _model:
        M, n = joint_counts(soups_life() if rule is LIFE else rings_184(), rule)
        cs = causal_states(M)
        cs["samples"] = n
        _model[rule.name] = cs
    return _model[rule.name]


_K = {}


def K_of(H, rule):
    """K[t]: cells not in the domain state; K[0] undefined (all False, never used)."""
    key = (id(H), rule.name)
    if key in _K and _K[key][0] is H:
        return _K[key][1]
    m = model(rule)
    idx = cone_index(H, rule)
    K = np.zeros(np.asarray(H).shape, dtype=bool)
    K[1:] = m["state"][idx[:-1]] != m["domain"]
    _K[key] = (H, K)
    return K


def near(f, shape, k=1):
    if len(shape) == 2:
        return {((r + i) % shape[0], (c + j) % shape[1]) for r, c in f
                for i in range(-k, k + 1) for j in range(-k, k + 1)}
    return {(i + d) % shape[0] for i in f for d in range(-k, k + 1)}


def parts(H, tr, rule=LIFE):
    """Per step: (filter, connection), or None when not judged (t = 0)."""
    K = K_of(H, rule)
    shape = K.shape[1:]
    out = []
    for t, u in C_steps(tr):
        if t == 0:
            out.append(None)
            continue
        Fu = tr[u]
        filt = sum(bool(K[u][p]) for p in Fu) * 2 >= len(Fu)
        st = np.stack([K[t], K[u]])
        lab, _ = ndimage.label(st, structure=np.ones((3,) * st.ndim))
        a = {lab[0][p] for p in near(tr[t], shape)} - {0}
        b = {lab[1][p] for p in near(Fu, shape)} - {0}
        out.append((filt, bool(a & b)))
    return out


def flags(H, tr, rule=LIFE, which="both"):
    out = []
    for x in parts(H, tr, rule):
        if x is None:
            out.append(True)
        elif which == "filter":
            out.append(x[0])
        elif which == "connection":
            out.append(x[1])
        else:
            out.append(x[0] and x[1])
    return out


def cand(which="both"):
    def judge(H, tr):
        return flags(H, tr, LIFE, which)
    return judge


def anchors():
    g, s = C.case_glider(), C.case_splice()
    return (R.score(g, "C2", cand())[0], R.score(s, "C2", cand())[0])


def d1_check():
    g = C.case_glider()
    H, tr = g["H"], g["tracings"][0]
    K = K_of(H, LIFE)
    ok_in, ok_near = True, True
    for t in range(1, len(H)):
        if not all(K[t][p] for p in tr[t]):
            ok_in = False
        nb = near(tr[t], K.shape[1:], 2)
        if any(p not in nb for p in zip(*map(lambda a: a.tolist(), np.nonzero(K[t])))):
            ok_near = False
    return ok_in, ok_near


def main():
    out = []
    for rule in (LIFE, R184):
        m = model(rule)
        cx = m["cx"][np.isfinite(m["cx"])]
        out.append(f"{rule.name}: {m['samples']} samples; {m['n_states']} causal states; domain probability "
                   f"{m['prob'][m['domain']]:.3f}; pasts in the domain "
                   f"{int((m['state'] == m['domain']).sum())} of {len(m['state'])}; unseen pasts "
                   f"{int((m['state'] < 0).sum())}; complexity range {cx.min():.2f}–{cx.max():.2f} bits.")
    a = anchors()
    out.append(f"Anchors under C2: glider {a[0]}, splice {a[1]}.")
    if "--anchors" in sys.argv:
        print("\n".join(out))
        return 0
    assert a == ("✓", "✓"), a
    d1 = d1_check()
    out.append(f"D-1 data: every live glider cell in K at t >= 1: {d1[0]}; every K cell within two cells "
               f"of the glider: {d1[1]}.")
    out += ["", "| Case | Target | C2 | at verdict | filter only | connection only | refused steps (filter, connection) |",
            "|---|---|---|---|---|---|---|"]
    shift_fail = []
    for case in c12.all_grid_cases():
        mk, v = R.score(case, "C2", cand())
        mf, _ = R.score(case, "C2f", cand("filter"))
        mc, _ = R.score(case, "C2c", cand("connection"))
        msh, _ = R.score(R.shifted(case), "C2", cand())
        H7 = np.concatenate([np.zeros((7,) + case["H"].shape[1:], dtype=bool), case["H"]])
        ct = {**case, "H": H7, "tracings": [{t + 7: f for t, f in tr.items()} for tr in case["tracings"]]}
        if "crash" in ct:
            ct["crash"] += 7
        mts, _ = R.score(ct, "C2", cand())
        if msh != mk or mts != mk:
            shift_fail.append((case["name"], mk, msh, mts))
        bad = []
        for tr in case["tracings"]:
            ps = parts(case["H"], tr)
            keys = [t for t, _ in C_steps(tr)]
            bad.append([(k, int(x[0]), int(x[1])) for k, x in zip(keys, ps) if x is not None and not (x[0] and x[1])][:6])
        out.append(f"| {case['name']} | {case['target']} | {mk} | {v} | {mf} | {mc} | {bad} |")
    out += ["", "Shift check (space 7 rows, 13 columns; time 7 steps): " +
            ("every mark unchanged." if not shift_fail else f"changed (case, mark, space, time): {shift_fail}"), ""]

    g = C.case_glider()
    H, tr = g["H"], g["tracings"][0]
    sites = sorted(frozenset().union(*tr.values()))
    carried = sum(all(flags(H, {t: frozenset([p]) for t in range(len(H))})) for p in sites)
    Hi, trg, inc = c11.case_incar()
    u = C.case_union()
    out.append(f"Elemental: {carried} of {len(sites)} crossed cells carried as single sites. Incar alone: "
               f"{'holds' if all(flags(Hi, inc)) else 'refused'}. Trout-turkey (union build): "
               f"{'holds' if all(flags(u['H'], u['tracings'][0])) else 'refused'}.")
    out += ["", "| Part | Target | C2 | filter only | connection only | steps not carried |", "|---|---|---|---|---|---|"]
    for sec, name, target, Hp, trp, lo, hi, want, rule in c12.probe_parts():
        keys = [t for t, _ in C_steps(trp)]
        row = []
        for which in ("both", "filter", "connection"):
            fl = flags(Hp, trp, rule, which)
            if want:
                ok, bad = c12.carried_on(fl, keys, lo, hi)
            else:
                ok = not all(fl)
                bad = [k for k, x in zip(keys, fl) if not x]
            row.append(mark(ok))
            if which == "both":
                bad0 = bad
        out.append(f"| {name} | {target} | " + " | ".join(row) + f" | {bad0[:8]} |")
    print("\n".join(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
