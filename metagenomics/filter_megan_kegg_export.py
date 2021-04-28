# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 18:27:30 2016

@author: calle
"""

import csv

in_kegg = "/home/calle/Storage/Data/rh_reblast/RHD_trans_gene_kegg.txt"
out_kegg = "/home/calle/Storage/Data/rh_reblast/RHD_trans_gene_kegg_fixed.txt"

to_keep = []

with open(in_kegg, "rB") as infile:
    kegg_reader = csv.reader(infile, delimiter = "\t")
    for line in kegg_reader:
        if not "-" in line[1] and len(line[1]) == 7:
            line[1] = line[1].replace(" ", "")
            to_keep.append(line)

with open(out_kegg, "wb") as outfile:
    kegg_writer = csv.writer(outfile, delimiter ="\t", lineterminator = "\n")
    for line in to_keep:
        kegg_writer.writerow(line)

print "Done!"
    