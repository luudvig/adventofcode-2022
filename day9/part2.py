#!/usr/bin/env python3

with open('input') as f:
    rope = [{'y': 0, 'x': 0} for _ in range(10)]
    motions, visited = f.read().splitlines(), {f"{rope[-1]['y']}:{rope[-1]['x']}"}

for m in (tuple((m[0], int(m[2:]))) for m in motions):
    key, sub = 'y' if m[0] in ('U', 'D') else 'x', False if m[0] in ('U', 'R') else True

    for _ in range(m[1]):
        rope[0][key] += -1 if sub else 1

        for i in range(1, len(rope)):
            if abs(rope[i - 1]['y'] - rope[i]['y']) < 2 and abs(rope[i - 1]['x'] - rope[i]['x']) < 2:
                break

            diagonal = rope[i - 1]['y'] != rope[i]['y'] and rope[i - 1]['x'] != rope[i]['x']

            if diagonal or rope[i - 1]['x'] == rope[i]['x']:
                rope[i]['y'] += 1 if rope[i - 1]['y'] > rope[i]['y'] else -1
            if diagonal or rope[i - 1]['y'] == rope[i]['y']:
                rope[i]['x'] += 1 if rope[i - 1]['x'] > rope[i]['x'] else -1

        visited.add(f"{rope[-1]['y']}:{rope[-1]['x']}")

print(len(visited))
