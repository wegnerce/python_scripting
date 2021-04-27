'''
Created on October 9, 2012
@author: Carl-Eric Wegner - AG Liesack - Molecular Ecology - MPI Marburg
The script below counts the number of records in a given file (e.g. fasta). 
'''

# needed modules
import os
from Bio import SeqIO

# paths, constants, variables
to_count_dir = "/media/calle/TOSHIBA EXT/_projects/_red_hill_soft_coal/metagenome/raw_merged/"

os.chdir(to_count_dir)
for filename in sorted(os.listdir(to_count_dir)):
    count = 0
    if filename.endswith("f.fastq.fasta"):
        for record in SeqIO.parse (filename, "fasta"):
            count = count + 1
        print "Done! " + str(count) + " sequences in: " + filename
    
# /home/calle/Desktop/mRNA_polymer/mRNA/Cel_7d_III_l_mRNA.fasta
# /media/TOSHIBA EXT/_projects/_polymer_breakdown/ribotag/processed/trimmed/St_7d_repII_L.fastq.fastq
