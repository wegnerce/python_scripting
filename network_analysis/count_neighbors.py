# -*- coding: utf-8 -*-
"""
Created on Thu May 17 09:54:44 2018

@author: calle
"""

import csv
from collections import defaultdict

in_neighbors = "/home/calle/Desktop/neighbors_total_fixed_b.txt"

degrees = {}
OTU_lists = defaultdict(list)

with open(in_neighbors, "rb") as infile:
    in_reader = csv.reader(infile, delimiter = "\t")
    for line in in_reader:
        degrees[line[0]] = str(len(line[1].split(",")))

print degrees

for key, value in degrees.iteritems():
    if not value in OTU_lists:
        OTU_lists[value] = []
        OTU_lists[value].append(key)
    elif value in OTU_lists:
        OTU_lists[value].append(key)

print OTU_lists

for key, value in OTU_lists.iteritems():
    with open("/home/calle/Desktop/"+key+".txt", "wb") as outfile:
        for OTU in value:
            outfile.write(OTU+"\n")