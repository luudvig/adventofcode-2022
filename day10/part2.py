#!/usr/bin/env python3

with open('input') as f:
    i, program, v, x = 0, f.read().splitlines(), None, 1

for _ in range(6):
    for p in range(40):
        print('#' if p in (x - 1, x, x + 1) else '.', end='' if p < 39 else '\n')

        if v:
            i, v, x = i + 1, None, x + v
        elif program[i][:4] == 'addx':
            v = int(program[i][5:])
        else:
            i += 1
