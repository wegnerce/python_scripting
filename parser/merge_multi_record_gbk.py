# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 10:14:16 2014

@author: calle
"""
from Bio import SeqIO

merged_rec = ''
infile = "multi-rec.gbk"

for rec in SeqIO.parse(open(infile,"r"), "genbank") :
    merged_rec += rec
    merged_rec += rec + ("N" * 50)

merged_rec.id = "mergedseq"
merged_rec.description = "merged seq"
SeqIO.write(merged_rec, "merged.gbk", "genbank") 