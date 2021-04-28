# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 18:27:30 2016

@author: calle
"""

import csv

in_gff = "/home/calle/Dropbox/BC_CEW/differential_gene_expression_analysis/S_oneidensis_MR1.gff3"
out_assign = "/home/calle/Dropbox/BC_CEW/differential_gene_expression_analysis/SO_2_protID.txt"

prot2SO = {}

with open(in_gff, "rb") as infile:
	gff_reader = csv.reader(infile, delimiter = "\t")
	for line in gff_reader:
		if not line[0].startswith("#") and line[2] == "gene":
			print line[8]
			print line[8].split(";")[-1]
			prot2SO[line[8].split(";")[-1].split("=")[1]] = ""
			SO = line[8].split(";")[-1].split("=")[1]
		elif not line[0].startswith("#") and line[2] == "CDS":
			prot2SO[SO] = line[8].split(";")[2].split(":")[1]
		
with open(out_assign, "wb") as outfile:
    assign_writer = csv.writer(outfile, delimiter ="\t", lineterminator = "\n")
    for key, value in prot2SO.items():
		 print key
		 print value
		 if value != "":
				assign_writer.writerow([key,  value])
				
print "Done!"
