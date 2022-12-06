#!/usr/bin/env python3

with open('input') as f:
    rounds, score = (r.split() for r in f.read().splitlines()), 0

for r in rounds:
    score += 1 if r[1] == 'X' else 2 if r[1] == 'Y' else 3

    if r[0] == 'A' and r[1] == 'X' or r[0] == 'B' and r[1] == 'Y' or r[0] == 'C' and r[1] == 'Z':
        score += 3
    elif r[0] == 'A' and r[1] == 'Y' or r[0] == 'B' and r[1] == 'Z' or r[0] == 'C' and r[1] == 'X':
        score += 6

print(score)
