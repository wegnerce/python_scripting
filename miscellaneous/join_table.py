# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 11:18:23 2018

@author: calle
"""

import csv

fixed = []
fixed_b = {}

with open ("/home/calle/Storage/Data/parcu_netw/final/cluster5_neighbours_fixed.csv", "rb") as infile:
    in_reader = csv.reader (infile, delimiter = "\t")
    for line in in_reader:
        fixed_b[line[0]].append(col for col in line[1:] if col != "")
        print [col for col in line[1:] if col != ""]
        to_add = line[0] + "\t" + line[1]
        fixed.append(to_add)

with open ("/home/calle/Storage/Data/parcu_netw/final/cluster5_neighbours_fixed_joined.csv", "wb") as outfile:
    out_writer = csv.writer (outfile, delimiter = "\t")
    for line in fixed:
        out_writer.writerow(line)