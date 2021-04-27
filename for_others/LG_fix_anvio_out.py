# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 14:40:11 2018

@author: calle
"""

# load necessary python modules
from Bio import SeqIO

# paths
fasta_in = "/home/calle/Desktop/Thaum_Single-Copy-Core-PCs_DNA-Sequences_NEW.fa"
fasta_out = "/home/calle/Desktop/fixed_test.faa"

# iterate over fasta
with open(fasta_out, "wb") as outfile:
    for record in SeqIO.parse(open(fasta_in, "rb"), "fasta"):
        new_id = "|".join(record.id.split("|")[1:3])
        new_seq = str(record.seq).replace("-", "")
        outfile.write(">%s\n%s\n" % (new_id, new_seq))
