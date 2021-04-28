# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 11:41:15 2015

@author: calle
"""

# needed modules
import csv
from collections import defaultdict

# input mapping file generated from initial KEGG annotation /
# list of K-Numbers
kegg_mapping = "/home/calle/Desktop/mapping_test.txt"

# create an empty dictionary to write a CPD <-> K- Number dictionary
cpd_dict = defaultdict(list)
interactions = []

# read the KEGG mapping file
def read_mapping(mapping):
    global cpd_dict
    print " Read the previously generated KEGG mapping file"
    with open(mapping, "rb") as to_read:
        kegg_reader = csv.reader(to_read, delimiter = "\t")
        for row in kegg_reader:
            if ";" in row[3]:
                for cpd in row[3].split(";"):
                    if cpd not in cpd_dict:
                        cpd_dict[cpd] = []
                        cpd_dict[cpd].append(row[0])
                    elif cpd in cpd_dict:
                        cpd_dict[cpd].append(row[0])
    print " ***DONE!"

def generate_interaction_file(cpd2k):
    global interactions
    print " Generate an interaction file from the read KEGG mapping file"
    for key in cpd2k:
        to_add = ""
        if len(cpd2k[key]) > 1:
            for i in range(0, len(cpd2k[key])):
                if i == 0:
                    to_add = to_add + cpd2k[key][i] + " pp "
                else:
                    to_add = to_add + " " + cpd2k[key][i]
            if to_add not in interactions:
                interactions.append(to_add)
    print " ***DONE!"

def write_interaction_file(intacts):
    global interactions
    print " Save interaction file %s" % (kegg_mapping+ ".interactions")
    with open (kegg_mapping + ".interactions", "wb") as outfile:
        for nedges in interactions:
            outfile.write(nedges + "\n")
        outfile.write("\n")
    print " ***DONE!"
        
        
read_mapping(kegg_mapping)
generate_interaction_file(cpd_dict)
write_interaction_file(interactions)
