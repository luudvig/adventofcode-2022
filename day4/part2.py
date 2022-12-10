#!/usr/bin/env python3

with open('input') as f:
    overlap, pairs = 0, (tuple(p.split('-') for p in l.split(',')) for l in f.read().splitlines())

for p in pairs:
    if range(max(int(p[0][0]), int(p[1][0])), min(int(p[0][1]), int(p[1][1])) + 1):
        overlap += 1

print(overlap)
