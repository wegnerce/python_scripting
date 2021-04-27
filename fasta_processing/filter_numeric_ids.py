# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 23:34:39 2017

@author: calle
"""

from Bio import SeqIO

seq_ids = "/home/lu87neb/data/merge_alignment/FcC_smatrix.fas"
out_file = "/home/lu87neb/data/merge_alignment/acido_concat_phyl.fas"

wanted = set(line.rstrip("\n")[1:] for line in open(seq_ids))
records = (r for r in SeqIO.parse(open(in_file, "rb"), "fasta") if not r.id.isdigit())

count = SeqIO.write(records, out_file, "fasta")
