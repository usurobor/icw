"""Build blind judging packets for the ICW blind comparison.

Reads notes/experiments/answers/{family}-{A,B,C}.md, splits per question,
strips framing outside the per-question answers, and writes packets of
unlabelled answer pairs. The key (pair id -> conditions and sides) is written
outside the repo until judging is done.
"""
import json, random, re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
ANS = ROOT / 'notes/experiments/answers'
OUT = ROOT / 'notes/experiments/judging'
KEYDIR = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else OUT

QUESTIONS = {
 1: "Is a glider in Conway's Game of Life real, or just cells switching?",
 2: "Is a car engine made of its parts?",
 3: "Money is just paper we agree to believe in. Is that right?",
 4: "Is a traffic jam a thing, or just cars?",
 5: "Is a sentence made of words?",
 6: "A character in a video game cannot find the graphics card, so the game world is less real than the hardware. Agree?",
 7: "Is a river the same river from one year to the next?",
 8: "Search for the self among body, thoughts and sensations, and you find no self. So there is no self. Is that sound?",
 9: "Is a pile of bricks anything more than the bricks?",
 10: "If every plank of a ship is replaced, is it the same ship?",
 11: "Temperature is just molecules moving, so temperature is not real. Is that right?",
 12: "Is a block in the Game of Life (a still life) more than its four cells?",
}
HEAD = re.compile(r'^\**Q-(\d+)\**\.?\s*(.*)$')

def norm(s): return re.sub(r"[^a-z]", "", s.lower().replace('’', "'"))

def parse(path):
    text = path.read_text(encoding='utf-8')
    text = text.split('\n---\n', 1)[1]          # drop the log header
    text = text.split('What the twelve questions reveal')[0]   # GPT-A's added summary
    out, cur, buf = {}, None, []
    for line in text.splitlines():
        m = HEAD.match(line.strip())
        if m and 1 <= int(m.group(1)) <= 12:
            if cur: out[cur] = '\n'.join(buf).strip()
            cur, buf = int(m.group(1)), []
            rest = m.group(2).strip()
            if rest and norm(rest)[:25] != norm(QUESTIONS[cur])[:25]:
                buf.append(rest)
        elif cur:
            buf.append(line)
    if cur: out[cur] = '\n'.join(buf).strip()
    assert sorted(out) == list(range(1, 13)), (path, sorted(out))
    return out

RUBRIC = """For each pair, score each answer 0, 1 or 2 on these items (n/a where an item does not apply):
- R-1. Says whether the question is about the thing at one moment or about something that persists over time.
- R-2. Says correctly whether the thing's make-up at a moment and its identity over time come apart, with a correct example if they do; or correctly says they do not.
- R-3. Where the question argues that something is unreal because it cannot be found among its parts: flags that inference as weak, without claiming this proves the thing persists. Otherwise n/a.
- R-4. Makes no claim stronger than its reasons support (any overclaim scores 0).
- R-5. Plain and short enough to follow.
Then choose: which answer would you rather rely on, 1 or 2?

Reply with one line per pair, exactly in this form:
PAIR-ID | 1: R1 R2 R3 R4 R5 | 2: R1 R2 R3 R4 R5 | choice: 1 or 2
Use n for n/a. Add nothing else."""

def build(family, seed):
    ans = {c: parse(ANS / f'{family}-{c}.md') for c in 'ABC'}
    rng = random.Random(seed)
    pairs, key = [], {}
    for q in range(1, 13):
        for x, y in (('B', 'A'), ('B', 'C'), ('C', 'A')):
            pid = f'{family[0].upper()}{rng.randrange(10**5):05d}'
            while pid in key: pid = f'{family[0].upper()}{rng.randrange(10**5):05d}'
            first, second = (x, y) if rng.random() < 0.5 else (y, x)
            key[pid] = {'q': q, 'first': first, 'second': second}
            pairs.append(pid)
    rng.shuffle(pairs)
    for order in (1, 2):
        chunks = [pairs[i:i + 12] for i in range(0, 36, 12)]
        for k, chunk in enumerate(chunks, 1):
            lines = [f'# Judging packet {family}-o{order}-p{k}', '',
                     'You are judging answers to philosophy questions. Each pair shows one question and two answers. '
                     'The answers come from the same source under different, hidden conditions. Judge only what is written.', '',
                     RUBRIC, '']
            for pid in chunk:
                e = key[pid]
                a1, a2 = (e['first'], e['second']) if order == 1 else (e['second'], e['first'])
                lines += [f'## {pid}', '', f'**Question:** {QUESTIONS[e["q"]]}', '',
                          '**Answer 1:**', '', ans[a1][e['q']], '', '**Answer 2:**', '', ans[a2][e['q']], '']
            (OUT / f'{family}-o{order}-p{k}.md').write_text('\n'.join(lines), encoding='utf-8')
    (KEYDIR / f'key-{family}.json').write_text(json.dumps(key, indent=1), encoding='utf-8')

if __name__ == '__main__':
    build('gpt', 20261118)
    build('claude', 20261119)
    print('ok')
