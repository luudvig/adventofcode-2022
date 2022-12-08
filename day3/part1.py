#!/usr/bin/env python3

with open('input') as f:
    answer, priorities, rucksacks = 0, {}, f.read().splitlines()

for p, i in enumerate(tuple(range(97, 123)) + tuple(range(65, 91)), 1):
    priorities[chr(i)] = p

for r in rucksacks:
    answer += priorities[set(r[:len(r)//2]).intersection(r[len(r)//2:]).pop()]

print(answer)
