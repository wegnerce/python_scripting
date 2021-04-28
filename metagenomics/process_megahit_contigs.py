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
input_handle = open("/media/STORAGE1/megahit_output_merged/RHB_SE.final.contigs.fa.1000")
output_handle = open("/media/STORAGE1/megahit_output_merged/RHB_SE_1000.cov.fa", "w")
cov_table = "/media/STORAGE1/megahit_output_merged/RHB_cov.txt"

new_record_description = ""

with open (cov_table, "r") as coverage:
    cov_dict = {}    
    for line in coverage:
        if not line.startswith("#"):
            line = line.split("\t")
            if line:
                cov_dict[line[0][0:line[0].find(" ")]]=line[1]
        else:
            continue

for seq_record in SeqIO.parse(input_handle, "fasta"):
    print seq_record.id
    seq_record.description = seq_record.description.split(" ")[3][4:]
    seq_record.description = seq_record.description + " " + cov_dict[seq_record.id]
    output_handle.write(">%s %s\n%s\n" % (
           seq_record.id,
           seq_record.description,
           seq_record.seq))

input_handle.close()
output_handle.close()

print "Done..."
