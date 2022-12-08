#!/usr/bin/env python3

with open('input') as f:
    answer, priorities, rucksacks = 0, {}, f.read().splitlines()

for p, i in enumerate(tuple(range(97, 123)) + tuple(range(65, 91)), 1):
    priorities[chr(i)] = p

for i in range(0, len(rucksacks), 3):
    answer += priorities[set(rucksacks[i]).intersection(rucksacks[i + 1], rucksacks[i + 2]).pop()]

print(answer)
