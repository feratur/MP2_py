#!/usr/bin/env python
import sys


word_counts = {}

for line in sys.stdin:
    word, count = line.strip().split('\t')
    word_counts[word] = int(count)
    
for word, count in sorted(word_counts.items(), key=lambda kvp: (-kvp[1], kvp[0]))[:10]:
    print("%s\t%i" % (word, count))
