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
read_go = {}

# write number mappings first
with open ("/home/calle/Downloads/KO_GO.txt", "rb") as infile:
    for line in infile:
        if kegg_to_go[line.split("\t")[0].split(":")[1]]:
            kegg_to_go[line.split("\t")[0].split(":")[1]][0] = kegg_to_go[line.split("\t")[0].split(":")[1]][0] + "_" + line.split("\t")[1].replace("go","GO")            
        else:
            kegg_to_go[line.split("\t")[0].split(":")[1]].append(line.split("\t")[1].replace("go","GO"))
            kegg_to_go[line.split("\t")[0].split(":")[1]].append("")

# add GO terms to mapping
with open ("/home/calle/Downloads/GO_biological_process.txt", "rb") as infile:
    for line in infile:
        read_go[line.split("\t")[3]] = line.split("\t")[1]

for key, value in kegg_to_go.iteritems():
    for value in kegg_to_go[key][0].split("_"):
			print value
			if value in read_go:
				kegg_to_go[key][1] = kegg_to_go[key][1] + read_go[value]
        #else:
        #    kegg_to_go[key][2] = kegg_to_go[key][2] + "_" + read_go[value]
            
writer = csv.writer(open("/home/calle/Desktop/go_kegg_map.txt", "wb")) 
for k,v in kegg_to_go.iteritems():
    writer.writerow([k] + v)


