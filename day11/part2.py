#!/usr/bin/env python3

from functools import reduce
from re import compile, findall

with open('input') as f:
    monkeys, pattern = [], compile('\d+')
    for l in f:
        match l.lstrip():
            case l if l.startswith('Monkey'):
                monkeys.append({'inspected': 0})
            case l if l.startswith('Starting items:'):
                monkeys[-1]['items'] = [int(i) for i in findall(pattern, l)]
            case l if l.startswith('Operation:'):
                monkeys[-1]['operation'] = l.split('=')[1].split()
            case l if l.startswith('Test:'):
                monkeys[-1]['test'] = int(findall(pattern, l)[-1])
            case l if l.startswith('If true:'):
                monkeys[-1]['true'] = int(findall(pattern, l)[-1])
            case l if l.startswith('If false:'):
                monkeys[-1]['false'] = int(findall(pattern, l)[-1])

mod = reduce(lambda x, y: x * y, (m['test'] for m in monkeys))

for _ in range(10000):
    for m in monkeys:
        for i in m['items']:
            d1, d2 = (int(o.replace('old', str(i))) for o in m['operation'][::2])
            i = (d1 + d2 if m['operation'][1] == '+' else d1 * d2) % mod

            monkeys[m['false'] if i % m['test'] else m['true']]['items'].append(i)

        m['inspected'], m['items'] = m['inspected'] + len(m['items']), []

inspected = sorted(m['inspected'] for m in monkeys)
print(inspected[-2] * inspected[-1])
