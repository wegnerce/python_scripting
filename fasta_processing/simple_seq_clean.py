"""
Created on Tue Sep  3 12:18:24 2013
@author: Carl-Eric Wegner - AG Liesack - Molecular Ecology - MPI Marburg
Based on a list of otus of interest, this script exracts the rows of interest
belonging to the OTUs, including the sequence identifiers assigned to this
OTU. As input files, a list of OTUs of interest is required as well as the
output file of QIIMEs pick_otu.py script.   
"""

import re
input_file = '/home/calle/Desktop/RDP_AOB_diversity/AOB_diversity_015_repr_seq.fasta'
output_file = '/home/calle/Desktop/RDP_AOB_diversity/AOB_diversity_015_repr_seq_cleaned.fasta'
regex = re.compile("[.-]+ *")    

with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    for line in infile:
        outfile.write(regex.sub("", line))

print "****** DONE SEQS CLEANED ******"
