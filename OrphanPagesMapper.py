#!/usr/bin/env python
import sys


for line in sys.stdin:
    link_from, links_to = line.strip().split(':')
    print('link_from\t%s' % (link_from.strip()))
    for link_to in links_to.strip().split():
        print('link_to\t%s' % (link_to))
