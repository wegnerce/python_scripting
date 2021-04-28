# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 18:27:30 2016

@author: calle
"""

import csv

in_roary = "/home/calle/Storage/Data/methylo_genomes/comparative_genomics/roary_methylos/gene_presence_absence.csv"
in_KOALA = "/home/calle/Storage/Data/methylo_genomes/comparative_genomics/roary_methylos/blastkoala_AL1_comp_genom.txt"
out_KOALA = "/home/calle/Storage/Data/methylo_genomes/comparative_genomics/roary_methylos/blastkoala_AL1_AL8_comp_genom__shared_unqiue.txt"

to_look_for = []
kept = []

with open(in_roary, "rb") as infile:
	roary_reader = csv.reader(infile, delimiter = ",")
	for line in roary_reader:
		if (line[15] != "" and line[14] != "") and line[16] == "":
			to_look_for.append(line[14])

print to_look_for		
		
with open(in_KOALA, "rb") as infile:
    KOALA_reader = csv.reader(infile, delimiter = "\t")
    for line in KOALA_reader:
        if line[0] in to_look_for:
            kept.append(line)

with open(out_KOALA, "wb") as outfile:
    KOALA_writer = csv.writer(outfile, delimiter ="\t", lineterminator = "\n")
    for line in kept:
        KOALA_writer.writerow(line)

print "Done!"
    