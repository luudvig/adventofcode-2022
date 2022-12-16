#!/usr/bin/env python3

with open('input') as f:
    grid, highest = tuple(tuple(int(c) for c in r) for r in f.read().splitlines()), 0

def get_view(y, x, sequence, vertical=True):
    for n in sequence:
        if (grid[n][x] if vertical else grid[y][n]) >= grid[y][x] or n == sequence.stop - sequence.step:
            return abs((y if vertical else x) - n)
    return 0

for y in range(len(grid)):
    for x in range(len(grid[y])):
        score = (get_view(y, x, range(y - 1, -1, -1)) *
                 get_view(y, x, range(x - 1, -1, -1), False) *
                 get_view(y, x, range(x + 1, len(grid[y])), False) *
                 get_view(y, x, range(y + 1, len(grid))))

        if score > highest:
            highest = score

print(highest)
