#!/usr/bin/env python

import sys
import string



stopWordsPath = sys.argv[1]
delimitersPath = sys.argv[2]


# TODO
with open(stopWordsPath) as f:
    stop_words = [line.strip() for line in f.readlines()]
    

#TODO 
with open(delimitersPath) as f:
    delims = f.read()

for line in sys.stdin:
    norm_line = line.lower().strip()
    for d in delims:
        norm_line = norm_line.replace(d, ' ')
    
    output_words = [word for word in norm_line.split() if word not in stop_words]
    
    for word in output_words:
        print('%s\t%s' % (word, 1))
   

