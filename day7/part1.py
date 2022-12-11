#!/usr/bin/env python3

from re import compile, sub

with open('input') as f:
    filesystem, output, pattern, working = {}, f.read().splitlines(), compile('/[a-z]+/$'), None

for o in output:
    if o.startswith('$ cd'):
        d = o.split()[-1]
        working = d if d == '/' else sub(pattern, '/', working) if d == '..' else working + d + '/'
    elif o.split()[0].isdigit():
        old, parent, size = None, working, int(o.split()[0])
        while old != parent:
            filesystem[parent] = filesystem.get(parent, 0) + size
            old, parent = parent, sub(pattern, '/', parent)

print(sum(s for s in filesystem.values() if s <= 100000))
