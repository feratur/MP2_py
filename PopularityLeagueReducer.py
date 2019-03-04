#!/usr/bin/env python
import sys

link_counts = {}

for line in sys.stdin:
    link, count = line.strip().split('\t')
    link_counts[link] = int(count)

result = {}
for k1, v1 in link_counts.items():
    rank = 0
    for k2, v2 in link_counts.items():
        if v1 > v2:
            rank += 1
    result[k1] = rank
    
for link, count in sorted(result.items(), reverse=True):
    print('%s\t%s' % (link, count))
