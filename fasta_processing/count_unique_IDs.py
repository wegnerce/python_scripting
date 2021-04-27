'''
Created on June 13, 2014
@author: Carl-Eric Wegner - AG Liesack - Molecular Ecology - MPI Marburg
Script converts multiline .fasta files into singleline .fasta files.
'''
import sys
import csv
from Bio import SeqIO

infile = open("/home/calle/Desktop/_salt_stress/4_megan/Bacillaceae_subtranscriptome/early_control_2.fasta") 

unique = []

for record in SeqIO.parse(infile, "fasta"):
    if not record.id in unique: #[:13]
        unique.append(record.id)

print "Done! Identified " + str(len(unique)) + " unique sequence IDs."

        
'''
with open ("/home/calle/Desktop/mRNA_polymer/mBLAST_results/S/Xyl_7d_III_l_mRNA.out") as infile:
    to_check = csv.reader(infile, delimiter='\t')
    next(to_check, None)
    for row in to_check:
        if len(row) < 2:
            continue
        if not row[0] in unique:
            unique.append(row[0])

print "Done! Identified " + str(len(unique)) + " unique sequence IDs."
'''







    