# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 18:10:11 2018

@author: calle
"""

from collections import defaultdict
import csv
import os

map_ko = "/home/calle/Desktop/KEGG_pathways/KEGG_maps_KO.txt"
pathway_maps = "/home/calle/Desktop/KEGG_pathways/pathway.list"
pathway_maps_ko = "/home/calle/Desktop/KEGG_pathways/KEGG_pathway_maps_KOs.txt"

path_map_ko = defaultdict(list)

def search(keys, searchFor):
    for k in keys:
        if searchFor in k:
                return k
    return None

with open (pathway_maps, "rb") as infile:
    for line in infile:
        line = line.replace("\t", ";")
        path_map_ko[line.replace("\n", "")] = []

with open (map_ko, "rb") as infile:
    for line in infile:
        if search(path_map_ko, line.split("\t")[0]) != None:
            path_map_ko[search(path_map_ko, line.split("\t")[0])].append(line.split("\t")[1].replace("\n", ""))

with open(pathway_maps_ko, "wb") as outfile:
    for key in path_map_ko:
        outfile.write(key + "\t" + ",".join(path_map_ko[key]) + os.linesep)