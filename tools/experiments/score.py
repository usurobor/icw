"""Score the blind comparison against the frozen decision rule.

usage: score.py KEYFILE ORDER1_RESULTS ORDER2_RESULTS
"""
import json, re, sys
from statistics import mean

GROUP = {1:'P',4:'P',7:'P',10:'P', 3:'U',6:'U',8:'U',11:'U', 2:'N',5:'N',9:'N',12:'N'}
LINE = re.compile(r'^(\w+)\s*\|\s*1:\s*([\dn ]+)\|\s*2:\s*([\dn ]+)\|\s*choice:\s*([12])')

def load(path, key, order):
    rows = []
    for line in open(path, encoding='utf-8'):
        m = LINE.match(line.strip())
        if not m: continue
        pid, s1, s2, ch = m.groups()
        e = key[pid]
        c1, c2 = (e['first'], e['second']) if order == 1 else (e['second'], e['first'])
        sc = lambda s: [None if x == 'n' else int(x) for x in s.split()]
        rows.append(dict(pid=pid, q=e['q'], g=GROUP[e['q']], conds={c1: sc(s1), c2: sc(s2)},
                         winner=c1 if ch == '1' else c2, pair=''.join(sorted((c1, c2)))))
    return rows

def report(rows, label):
    def wins(x, y, groups):
        r = [w for w in rows if w['pair'] == ''.join(sorted((x, y))) and w['g'] in groups]
        return sum(w['winner'] == x for w in r), len(r)
    def item_mean(c, items, groups):
        v = [w['conds'][c][i] for w in rows if w['g'] in groups and c in w['conds']
             for i in items if w['conds'][c][i] is not None]
        return mean(v) if v else float('nan')
    print(f'== {label}: {len(rows)} judged pairs')
    for x, y in (('B','A'), ('B','C'), ('C','A')):
        for gs in ('PU', 'N'):
            k, n = wins(x, y, gs)
            print(f'  {x} beats {y} in {"P+U" if gs=="PU" else "N  "}: {k}/{n} = {k/n:.0%}')
    for c in 'ABC':
        print(f'  {c}: R1-3 mean P+U {item_mean(c,[0,1,2],"PU"):.2f}  R4 P+U {item_mean(c,[3],"PU"):.2f}'
              f'  | N: R4 {item_mean(c,[3],"N"):.2f} R5 {item_mean(c,[4],"N"):.2f}')
    return wins, item_mean

if __name__ == '__main__':
    key = json.load(open(sys.argv[1]))
    r1, r2 = load(sys.argv[2], key, 1), load(sys.argv[3], key, 2)
    allr = r1 + r2
    report(r1, 'order 1'); report(r2, 'order 2')
    wins, im = report(allr, 'both orders')
    bc_k, bc_n = wins('B','C','PU')
    d13 = im('B',[0,1,2],'PU') - im('C',[0,1,2],'PU')
    r4 = im('B',[3],'PU') - im('C',[3],'PU')
    helps = bc_k/bc_n >= 0.6 and d13 >= 0.3 and r4 >= 0
    ba_k, ba_n = wins('B','A','N')
    hurts = (ba_n - ba_k)/ba_n > 0.5 or im('B',[3],'N') < im('A',[3],'N') or im('B',[4],'N') < im('A',[4],'N')
    agree = sum(a['winner'] == b['winner'] for a, b in zip(sorted(r1, key=lambda w: w['pid']), sorted(r2, key=lambda w: w['pid'])))
    print(f'\nDecision rule: B beats C (P+U) {bc_k}/{bc_n}={bc_k/bc_n:.0%} (need >=60%); '
          f'R1-3 B-C {d13:+.2f} (need >=+0.30); R4 B-C {r4:+.2f} (need >=0)')
    print(f'  ICW helps: {helps}')
    print(f'  Controls: B loses to A in N {ba_n-ba_k}/{ba_n}; R4 B-A {im("B",[3],"N")-im("A",[3],"N"):+.2f}; '
          f'R5 B-A {im("B",[4],"N")-im("A",[4],"N"):+.2f}; ICW hurts on controls: {hurts}')
    print(f'  Agreement between orders on the winner: {agree}/{len(r1)} = {agree/len(r1):.0%} (need >=70%)')
