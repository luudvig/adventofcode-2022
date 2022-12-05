#!/usr/bin/env python3

with open('input') as f:
    calories = (sum(int(c) for c in e.splitlines()) for e in f.read().split('\n\n'))

print(max(calories))
