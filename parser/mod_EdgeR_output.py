# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 18:27:30 2016

@author: calle
"""

import csv

prot_SO_map = "/home/calle/Storage/Data/becca_transcriptome/SO_2_protID.txt"
edgerout = "/home/calle/Dropbox/BC_CEW/mapped_read_counts/MR1_read_counts_III_MR.txt"
edgerout_mod = "/home/calle/Dropbox/BC_CEW/mapped_read_counts/MR1_read_counts_III_MR_mod.txt"

prot2SO = {}
edgermod = []

with open(prot_SO_map, "rb") as infile:
	map_reader = csv.reader(infile, delimiter = "\t")
	for line in map_reader:
		prot2SO[line[1]] = line[0]		

with open(edgerout, "rb") as infile:
    edger_reader = csv.reader(infile, delimiter = "\t")
    next(edger_reader, None) 
    for line in edger_reader:
		#if not line[4].startswith("Soxy") and line[4] != "id":
	   if not line[0].startswith("Soxy"):
			line[0] = prot2SO[line[0].split("_")[2]]
			edgermod.append(line)
	   else:
			edgermod.append(line)

with open(edgerout_mod, "wb") as outfile:
	outfile_writer = csv.writer(outfile, delimiter  = "\t")
	for item in edgermod:
		outfile_writer.writerow(item)

print "Done!"
