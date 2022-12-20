#!/usr/bin/env python3

with open('input') as f:
    head, tail = ({'y': 0, 'x': 0} for _ in range(2))
    motions, visited = f.read().splitlines(), {f"{tail['y']}:{tail['x']}"}

for m in (tuple((m[0], int(m[2:]))) for m in motions):
    key, sub = 'y' if m[0] in ('U', 'D') else 'x', False if m[0] in ('U', 'R') else True

    for _ in range(m[1]):
        head[key] += -1 if sub else 1

        if abs(head['y'] - tail['y']) < 2 and abs(head['x'] - tail['x']) < 2:
            continue

        tail['y' if key == 'x' else 'x'] = head['y' if key == 'x' else 'x']
        tail[key] += -1 if sub else 1

        visited.add(f"{tail['y']}:{tail['x']}")

print(len(visited))
