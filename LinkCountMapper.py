#!/usr/bin/env python
import sys


for line in sys.stdin:
    link_from, links_to = line.strip().split(':')
    
    for link_to in links_to.strip().split():
        print('%s\t1' % (link_to))
