# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 16:29:06 2017

@author: calle
"""

lines_seen = set() # holds lines already seen
outfile = open("/home/calle/Storage/uniref90_GO_unique.csv", "w")
for line in open("/home/calle/Storage/uniref90_GO.csv", "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()