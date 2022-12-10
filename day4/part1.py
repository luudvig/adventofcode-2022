#!/usr/bin/env python3

with open('input') as f:
    contain, pairs = 0, (tuple(p.split('-') for p in l.split(',')) for l in f.read().splitlines())

for p in pairs:
    p1_start, p1_stop, p2_start, p2_stop = int(p[0][0]), int(p[0][1]), int(p[1][0]), int(p[1][1])
    if p1_start >= p2_start and p1_stop <= p2_stop or p2_start >= p1_start and p2_stop <= p1_stop:
        contain += 1

print(contain)
