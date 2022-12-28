#!/usr/bin/env python3

with open('input') as f:
    heightmap, end = [], None

    for y, l in enumerate(f):
        if 'E' in l:
            end = (y, l.index('E'))

        heightmap.append(l.rstrip().replace('S', 'a').replace('E', 'z'))

def get_steps(start, end):
    queue, steps, visited = [start], 0, set([start])

    while queue:
        for _ in range(len(queue)):
            square = queue.pop(0)

            if square == end:
                return steps

            for d in ((1, 0), (0, -1), (0, 1), (-1, 0)):
                y, x = square[0] + d[0], square[1] + d[1]

                if ((y, x) not in visited and 0 <= y < len(heightmap) and 0 <= x < len(heightmap[y]) and
                        ord(heightmap[y][x]) - ord(heightmap[square[0]][square[1]]) <= 1):
                    queue.append((y, x))
                    visited.add((y, x))

        steps += 1

startings = ((y, x) for y in range(len(heightmap)) for x in range(len(heightmap[y])) if heightmap[y][x] == 'a')
print(min(p for p in (get_steps(s, end) for s in startings) if p is not None))
