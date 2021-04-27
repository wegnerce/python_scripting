# -*- coding: utf-8 -*-
"""
@author:      Carl-Eric Wegner
@affiliation: Küsel Lab - Aquatic Geomicrobiology
              Friedrich Schiller University of Jena

              carl-eric.wegner@uni-jena.de
"""
from itertools import islice
from collections import defaultdict
import csv

### paths, variables
cluster_membership = "/home/cewegner/DATA_II/Data/TU_Ilmenau/TU_Ilmenau_networks_cluster_membership.csv"
otu_table = "/home/cewegner/DATA_II/Data/TU_Ilmenau/koehler_otus.csv"
summed = "/home/cewegner/DATA_II/Data/TU_Ilmenau/koehler_cluster_table.csv"

cluster_otus = defaultdict(list)
cluster_table = defaultdict(list)

### read cluster membership table
with open(cluster_membership, "r") as infile:
    for line in islice(infile, 1, None):
        if not line.split(";")[1] in cluster_otus:
            cluster_otus[line.split(";")[1]].append(line.split(";")[0])
        else:
            cluster_otus[line.split(";")[1]].append(line.split(";")[0])

### summarize OTU table on cluster level
with open(otu_table, "r") as infile:
    header = infile.readline()
    for line in islice(infile, 1, None):
        for key in cluster_otus:
            if line.split("\t")[0] in cluster_otus[key] and not key in \
            cluster_table:
                cluster_table[key] = [int(i) for i in line.split("\t")[1:]]
            if line.split("\t")[0] in cluster_otus[key] and key in\
            cluster_table:
                to_add = [int(i) for i in line.split("\t")[1:]]
                cluster_table[key] = [sum(x) for x in zip(cluster_table[key], to_add)]
                
with open(summed, "w") as outfile:
    outfile.write(header)
    csv_output = csv.writer(outfile, delimiter = "\t")
    for key in cluster_table:
        csv_output.writerow([key] + cluster_table[key])
    
    