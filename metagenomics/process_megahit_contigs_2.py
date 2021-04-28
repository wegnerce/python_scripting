# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 11:16:30 2015

@author: calle
"""

# needed modules
#import argparse
#import numpy
from Bio import SeqIO

# in / out handles
input_handle = open("/home/calle/Storage/submission_genbank_genomes/RHA_bin20_Acidobacteria.fasta")
#cov_table = "/home/calle/Storage/submission_genbank_genomes/RHA_cov.txt"

#id_list = []
forward = 0
reverse = 0

for seq_record in SeqIO.parse(input_handle, "fasta"):
	forward = forward + 1
	reverse = reverse + float(seq_record.description.split(" ")[2])
#	id_list.append(seq_record.id)
	 
#with open (cov_table, "r") as coverage:
#	for line in coverage:
#		if not line.startswith("#"):
#			line = line.split("\t")
#			if line[0].split(" ")[0] in id_list:
#				forward = forward + int(line[6])
#				reverse = reverse + int(line[7])
			
input_handle.close()

#print "Forward: " + str(forward)
#print "Reverse: " + str(reverse)
print str(reverse/forward)
