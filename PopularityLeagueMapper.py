#!/usr/bin/env python
import sys


leaguePath = sys.argv[1]


with open(leaguePath) as f:
	links = set([line.strip() for line in f.readlines()])





for line in sys.stdin:
	link, count = line.strip().split('\t')
    if link in links:
        print('%s\t%s' % (link, count))
