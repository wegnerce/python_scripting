# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 16:19:18 2017

@author: calle
"""

import csv

in_file = "/home/calle/Storage/Data/methylo_genomes/comparative_genomics/AL8.gff"
out_file = "/home/calle/Storage/Data/methylo_genomes/comparative_genomics/AL8_mod.gff"

with open(in_file, "rb") as infile:
	infile_reader = csv.reader(infile, delimiter = "\t")
	read_gff = [line for line in infile_reader if line[0].startswith("#") or line[2] == "CDS"]

for item in read_gff:
	if not item[0].startswith("#"):
		item[0] = "AL8"
		item[1] = "GAMOLA:2"

with open(out_file, "wb") as outfile:
	outfile_writer = csv.writer(outfile, delimiter  = "\t")
	for item in read_gff:
		outfile_writer.writerow(item)
				