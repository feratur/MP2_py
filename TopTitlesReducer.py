#!/usr/bin/env python
import sys


word_counts = {}

for line in sys.stdin:
    word, count = line.strip().split('\t')
    word_counts[word] = int(count)
    
result_items = sorted(word_counts.items(), key=lambda kvp:(kvp[1], kvp[0]), reverse=True)[:10]
    
for word, count in sorted(result_items, key=lambda kvp:kvp[0]):
    print("%s\t%i" % (word, count))
