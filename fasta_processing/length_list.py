# -*- coding: utf-8 -*-
"""
Created on April 11, 2014
@author: Carl-Eric Wegner - AG Liesack - Molecular Ecology - MPI Marburg
The given script reads a .fasta file, extracts the length of each sequence
and saves the length information in a separate text file e.g.:
record.id (aka sequence name) -- length

Usage:

python length_list.py input.fasta output.txt
"""
from Bio import SeqIO
import csv

in_fasta = "/media/STORAGE2/phylopythias+_1.4/7_1000_contigs/RHD_SE_contigs.fa.1000"
output = "/media/STORAGE2/phylopythias+_1.4/7_1000_contigs/RHD_SE_contigs_stats.txt"


with open(output, "wb") as outfile:
    out = csv.writer(outfile, delimiter = ",")
    for seq_record in SeqIO.parse(in_fasta, "fasta"):
        output_line = '%s,%i\n' % \
        (seq_record.id, len(seq_record))
        print(output_line)  
        outfile.write(output_line)
 
'''
 with open(blast_output + ".tax", "wb") as outfile:
        out = csv.writer(outfile, delimiter = "\t")
        for row in modified_ublast_out:
            out.writerow(row)
    outfile.close()
'''

    


    



