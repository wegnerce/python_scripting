# -*- coding: utf-8 -*-
"""
Created on Thu Mar  16 23:34:39 2017

@author: CEW
"""

# needed modules
from Bio import SeqIO

# paths to files to be processed
seq_ids = "/home/calle/Storage_II/Data/MT_gmasS/seq_ids_gmaS_H_MG_sensitive_1000.txt"
in_seqs = "/home/calle/Storage_II/Data/H_MG_contigs/H_MG_sensitive_1000_trans.fna"
#in_blast = "/your/original/blast/output"
out_seqs = "/home/calle/Storage_II/Data/H_MG_contigs/H_MG_sensitive_1000_gmaS_candidates.fna"
#out_blast = open("/path/to/save/your/subsetted/blast_output", "wb")

# read file sequence identifiiers of interest
# filter fasta and blast output fule
#wanted = set(line.rstrip("\n")[1:].replace("\r", "") for line in open(seq_ids) if line.startswith(">"))
wanted = set(line.rstrip("\n")[:line.rstrip("\n").find(" ")].replace("\r", "") for line in open(seq_ids))
print wanted
subset_seqs = (r for r in SeqIO.parse(open(in_seqs, "rb"), "fasta") if r.id in wanted)
SeqIO.write(subset_seqs, out_seqs, "fasta")

#subset_blast = set(line for line in open(in_blast, "rb") if line.split(" ")[0] in wanted)
#print subset_blast
#for entry in subset_blast:
#    print entry
#    out_blast.write(entry)

