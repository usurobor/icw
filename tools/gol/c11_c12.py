"""C11 and C12 together at their frozen thresholds; comparison with closure, C9, C10.
Declared in notes/runs/2026-11-17-c11-c12.md. Rerun: python3 tools/gol/c11_c12.py
"""
import sys

import numpy as np

import c11
import c12
import cases as C
import probes as PR
import run as R
from c11 import LIFE, R184, C_steps
from candidates import CANDIDATES

TH11 = c11.THETA
TH12 = c12.THETA


def both(ens):
    def flags(H, tr, rule=LIFE, f=1.0):
        a = c11.shares(H, tr, rule, ens)
        b = c12.shares(H, tr, rule, ens)
        return [(x is None or x > f * TH11[ens]) and (y is None or y > f * TH12[ens])
                for x, y in zip(a, b)]
    return flags


def single(mod, ens):
    th = mod.THETA[ens]

    def flags(H, tr, rule=LIFE, f=1.0):
        return [x is None or x > f * th for x in mod.shares(H, tr, rule, ens)]
    return flags


def closure184(tr):
    return [PR.next184(tr[t]) == tr[u] for t, u in C_steps(tr)]


def old(name):
    def flags(H, tr, rule=LIFE, f=1.0):
        if rule is R184:
            return closure184(tr) if name == "Closure" else PR.flags184(tr, name, H)
        return CANDIDATES[name](H, tr)
    return flags


def as_cand(flags, f=1.0):
    def judge(H, tr):
        return flags(H, tr, LIFE, f)
    return judge


def refused(case, cand):
    v, fl = R.verdict(case, cand)
    return fl is not None and any(x is False for f in fl for x in f)


def main():
    ens_list = ("knockout", "flip")
    cases = c12.all_grid_cases()
    parts = c12.probe_parts()
    out = []
    for ens in ens_list:
        methods = ([("Closure", old("Closure")), ("C9", old("C9")), ("C10", old("C10"))]
                   if ens == "knockout" else [])
        methods += [("C11", single(c11, ens)), ("C12", single(c12, ens)), ("C11 ∧ C12", both(ens))]
        names = [n for n, _ in methods]
        out += [f"## Ensemble {ens}", "",
                "| Case | Target | " + " | ".join(names) + " | ∧ at 0.8 | ∧ at 1.2 | ∧ verdict |",
                "|---|---|" + "---|" * (len(names) + 3)]
        nref = {n: 0 for n in names}
        nmatch = {n: 0 for n in names}
        shift_fail = []
        for case in cases:
            cells = []
            for n, fl in methods:
                mk, v = R.score(case, n, as_cand(fl))
                cells.append(mk)
                nmatch[n] += mk == "✓"
                nref[n] += refused(case, as_cand(fl))
                if n == "C11 ∧ C12":
                    vb = v
                    msh, _ = R.score(R.shifted(case), n, as_cand(fl))
                    H7 = np.concatenate([np.zeros((7,) + case["H"].shape[1:], dtype=bool), case["H"]])
                    same_t = all(fl(case["H"], tr) == fl(H7, {t + 7: f for t, f in tr.items()})
                                 for tr in case["tracings"])
                    if msh != mk or not same_t:
                        shift_fail.append(case["name"])
            fb = both(ens)
            lo, _ = R.score(case, "∧", as_cand(fb, 0.8))
            hi, _ = R.score(case, "∧", as_cand(fb, 1.2))
            out.append(f"| {case['name']} | {case['target']} | " + " | ".join(cells) +
                       f" | {lo} | {hi} | {vb} |")
        out.append("| Rows matched (of 11) | | " + " | ".join(str(nmatch[n]) for n in names) + " | | | |")
        out.append("| Rows refused (of 11) | | " + " | ".join(str(nref[n]) for n in names) + " | | | |")
        out += ["", "Shift check on the conjunction (7 rows, 13 columns; 7 steps): " +
                ("every mark and flag unchanged." if not shift_fail else f"changed: {shift_fail}"), ""]

        out += ["### Probes", "",
                "| Part | Target | " + " | ".join(names) + " | ∧ at 0.8 | ∧ at 1.2 |",
                "|---|---|" + "---|" * (len(names) + 2)]
        pm = {n: 0 for n in names}
        for sec, name, target, H, tr, lo_, hi_, want, rule in parts:
            keys = [t for t, _ in C_steps(tr)]
            cells = []
            for n, fl in methods + [("lo", lambda H, tr, rule, f=0.8: both(ens)(H, tr, rule, 0.8)),
                                    ("hi", lambda H, tr, rule, f=1.2: both(ens)(H, tr, rule, 1.2))]:
                fl_ = fl(H, tr, rule)
                if want:
                    ok, _ = c12.carried_on(fl_, keys, lo_, hi_)
                    good = ok
                else:
                    good = not all(x is True for x in fl_)
                cells.append(c11.mark(good))
                if n in pm:
                    pm[n] += good
            out.append(f"| {name} | {target} | " + " | ".join(cells) + " |")
        out.append("| Parts matched (of 10) | | " + " | ".join(str(pm[n]) for n in names) + " | | |")
        out.append("")
    print("\n".join(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
