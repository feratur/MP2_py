#!/usr/bin/env python
import sys


for line in sys.stdin:
    word, count = line.strip().split('\t')
    print('stat\t%s' % (count))
