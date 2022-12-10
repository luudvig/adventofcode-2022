#!/usr/bin/env python3

with open('input') as f:
    (initial, procedure), stacks = (l.splitlines() for l in f.read().split('\n\n')), {}

for l in reversed(initial[:-1]):
    for i, c in enumerate(l):
        if c.isalpha():
            stacks.setdefault(initial[-1][i], []).append(c)

for q, f, t in ((d for d in p.split() if d.isdigit()) for p in procedure):
    for _ in range(int(q)):
        stacks[t].append(stacks[f].pop())

print(''.join(s[-1] for s in stacks.values()))
