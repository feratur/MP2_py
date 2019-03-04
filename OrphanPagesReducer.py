#!/usr/bin/env python
import sys


links = { 'link_from': [], 'link_to': [] }

for line in sys.stdin:
    link_type, link_value = line.strip().split('\t')
    links[link_type].append(link_value)
  
link_to_set = set(links['link_to'])
orphan_links = sorted([link for link in links['link_from'] if not link in link_to_set])

for link in orphan_links:
    print(link)

