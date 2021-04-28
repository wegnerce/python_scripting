# -*- coding: utf-8 -*-
"""

"""
# load required modules
from Bio import SeqIO
from Bio.SeqUtils import GC
 
# necessary paths, variables 
sequences_of_interest = [] # Setup an empty list
filter_term = "K02038"
input_handle = "/home/calle/Desktop/RH_MG/functional_analysis_metagenomes/functional_profiles/total/RHA_ko.txt"
output_handle = "/home/calle/Google Drive/MPI Marburg/RH/KEGG/taxonomic_analysis/RHA_PtsA_k02038.txt"

# read annotation file, extract sequence id's of interest
with open(input_handle, "rb") as infile:
    content = infile.read().splitlines()
    for line in content:
        if len(line.split("\t")) > 1:
            if line.split("\t")[1] == filter_term:
                sequences_of_interest.append(line.split("\t")[0])

with open(output_handle, "wb") as outfile:
    for seqid in sequences_of_interest:
        outfile.write("%s\n" % seqid)
