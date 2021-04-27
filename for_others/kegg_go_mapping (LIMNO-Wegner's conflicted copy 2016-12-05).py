# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 08:26:50 2016

@author: calle
"""
# import necessaey modules
from collections import defaultdict
import csv

# define dictionary of lists to write mappings to
kegg_to_go = defaultdict(list)

# write number mappings first
with open ("/home/calle/Downloads/KO_GO.txt", "rb") as infile:
    for line in infile:
        kegg_to_go[line.split("\tab")[1].replace("go","GO")] = line.split("\tab")[0].split(":")[1]

# add GO terms to mapping
with open ("/home/calle/Downloads/GO_biological_process.txt", "rb") as infile:
    for line in infile:
        if line.split("\t")[3] in kegg_to_go:
            kegg_to_go[line.split("\t")[3]].append(line.split("\t")[3])

writer = csv.writer(open("/home/calle/Desktop/go_kegg_map.txt", "wb")) 
for k,v in kegg_to_go.iteritems():
    writer.writerow([k ,v])


