#!/usr/bin/env python
import sys

result = {}

# input comes from STDIN
for line in sys.stdin:
    word, count = line.strip().split('\t')
    result[word] = result.get(word, 0) + int(count)

for word, count in result.items():
    print("%s\t%i" % (word, count))
