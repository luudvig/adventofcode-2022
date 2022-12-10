#!/usr/bin/env python3

with open('input') as f:
    datastream = f.readline().rstrip()

for i in range(3, len(datastream)):
    if len(set(datastream[i - 4:i])) == 4:
        print(i)
        break
