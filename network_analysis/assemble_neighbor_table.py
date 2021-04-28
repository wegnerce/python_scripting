# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 09:36:24 2017

@author: calle
"""

# import needed modules
import csv
import pandas as pd
from collections import defaultdict

# in and out
neighbor_in = "/home/calle/Storage_II/Data/network_revisited/first_degree_neighbours.txt"
neighbor_out = "/home/calle/Storage_II/Data/network_revisited/first_degree_neighbours_fixed.txt"
#met_assignment = "/home/calle/Storage/Data/parcu_netw/final/metabolisms_total.txt"
#proportion = "/home/calle/Storage/Data/parcu_netw/final/proportions_heterotrophs_all.txt"
#otus_of_interest = "/home/calle/Storage/Data/parcu_netw/final/list_ABY1_OTUs.txt"

neighbors = defaultdict(list)
neighbors_metabolism = defaultdict(list)
neighbors_results = {}
metabolism = {}

# read otu table, filter out OTUs with less than X counts over all samples
print "*** Assemble the vertex neighbor table."
with open(neighbor_in, "rb") as infile:
    for line in infile:
        print line.split(",")[0]
        if not line.split(",")[0] in neighbors or line.split(",")[0].startswith("l"):
            neighbors[line.split(",")[0]] = []
            neighbors[line.split(",")[0]].append(line.split(",")[1].replace("\n", ""))
        elif line.split(",")[0] in neighbors:
            neighbors[line.split(",")[0]].append(line.split(",")[1].replace("\n", ""))

#with open(otus_of_interest, "rb") as infile:
#    otus = infile.read().split("\n")
#    print otus
#neighbors_sub = {otu: neighbors[otu] for otu in otus}

print "*** Save the assembled neighbor table."
with open(neighbor_out, "wb") as outfile:
    #writer = csv.writer(outfile, delimiter = ",")
    for k,v in neighbors.iteritems():
        #writer.writerow([[k] + v])
        outfile.write(k + "\t" + ",".join(v) + "\n")

#print "*** Determine proportion of autotrophic neighbors"
#with open(met_assignment, "rb") as infile:
#    for line in infile:
#        metabolism[line.split("\t")[1].replace("\n", "")] = line.split("\t")[0]#

#for otu in neighbors:
#    for neighbor in neighbors[otu]:
#        neighbors_metabolism[otu].append(metabolism[neighbor])

#for otu in neighbors_metabolism:
#    neighbors_results[otu] = (float(neighbors_metabolism[otu].count("H") + #neighbors_metabolism[otu].count("S")) / float(len(neighbors_metabolism[otu])))*100

#print

#with open(proportion, "wb") as outfile:
#    [outfile.write('{0},{1}\n'.format(key, value)) for key, value in neighbors_results.items()]

