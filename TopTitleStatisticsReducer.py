#!/usr/bin/env python
import sys


values = []
min_val = 99999
max_val = 0

for line in sys.stdin:
    word, count = line.strip().split('\t')
    val = int(count)
    values.append(val)
    if val < min_val:
        min_val = val
    if val > max_val:
        max_val = val

total = sum(values)        
mean = total / len(values)
variance = sum([(v - mean)**2 for v in values]) / len(values)

print('Mean\t%i' % mean)
print('Sum\t%i' % total)
print('Min\t%i' % min_val)
print('Max\t%i' % max_val)
print('Var\t%i' % variance)
