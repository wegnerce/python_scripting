# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 18:27:30 2016

@author: calle
"""

import csv

#to_keep = "/home/calle/Storage/Data/methylo_genomes/comparative_genomics/roary_methylos/coregenome_methylos_IDs.txt"
in_KOALA = "/home/calle/Storage/MBGW_PC/KEGG_MBGW_bins.txt"
out_KOALA = "/home/calle/Storage/MBGW_PC/KEGG_MBGW_bin_5.txt"

to_look_for = []
kept = []

#with open(to_keep, "rb") as infile:
#	to_keep_reader = csv.reader(infile, delimiter = "\t")
#	for line in to_keep_reader:
#		to_look_for.append(line[0])
#
#print to_look_for		
		
with open(in_KOALA, "rb") as infile:
    KOALA_reader = csv.reader(infile, delimiter = "\t")
    for line in KOALA_reader:
        #if line[0] in to_look_for:
		 if line[0].startswith("bin5"):
				kept.append(line)

with open(out_KOALA, "wb") as outfile:
    KOALA_writer = csv.writer(outfile, delimiter ="\t", lineterminator = "\n")
    for line in kept:
        KOALA_writer.writerow(line)

print "Done!"
    