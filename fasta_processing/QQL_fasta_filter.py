# -*- coding: utf-8 -*-

# needed modules
import sys
from Bio import SeqIO

# paths to files to be processed
#seq_ids = ""
#in_seqs = ""
#out_seqs = ""
#wanted = set(line.rstrip("\n")[1:].replace("\r", "") for line in open(seq_ids) if line.startswith(">"))
wanted = set(line.rstrip("\n").replace("\r", "") for line in open(sys.argv[1]))
subset_seqs = (r for r in SeqIO.parse(open(sys.argv[2], "rb"), "fasta") if r.id in wanted)
SeqIO.write(subset_seqs, sys.argv[3], "fasta")

#subset_blast = set(line for line in open(in_blast, "rb") if line.split(" ")[0] in wanted)
#print subset_blast
#for entry in subset_blast:
#    print entry
#    out_blast.write(entry)

