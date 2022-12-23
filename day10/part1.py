#!/usr/bin/env python3

with open('input') as f:
    i, program, signal, v, x = 0, f.read().splitlines(), 0, None, 1

for c in range(1, 221):
    if c in (20, 60, 100, 140, 180, 220):
        signal += c * x

    if v:
        i, v, x = i + 1, None, x + v
    elif program[i][:4] == 'addx':
        v = int(program[i][5:])
    else:
        i += 1

print(signal)
