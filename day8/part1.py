#!/usr/bin/env python3

with open('input') as f:
    grid, visible = tuple(tuple(int(c) for c in r) for r in f.read().splitlines()), 0

def is_visible(y, x, y_range, x_range):
    for r in y_range:
        for c in x_range:
            if grid[r][c] >= grid[y][x]:
                return False
    return True

for y in range(len(grid)):
    for x in range(len(grid[y])):
        if any((is_visible(y, x, range(y - 1, -1, -1), range(x, x + 1)),
                is_visible(y, x, range(y, y + 1), range(x + 1, len(grid[y]))),
                is_visible(y, x, range(y + 1, len(grid)), range(x, x + 1)),
                is_visible(y, x, range(y, y + 1), range(x - 1, -1, -1)))):
            visible += 1

print(visible)
