# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 16:48:04 2015

@author: calle
"""

# needed modules
from Bio.KEGG.REST import kegg_list

# needed paths, variables
to_lookup = "/home/calle/Desktop/common_RHA_RHB_keggmapper.txt"

# read list of K-Numbers to be looked up
with open (to_lookup, "rb") as infile:
    for line in infile:
        print line.split("\t")[1]
        #print kegg_list(line.split("\t")[1]).read().split("\t")[1].split(";")[0]
        print kegg_list(line.split("\t")[1]).read()