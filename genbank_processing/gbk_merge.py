# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 18:29:16 2014

@author: calle
"""

from Bio import SeqIO

merged_rec = ''
infile = "/home/calle/Desktop/collected_genomes/Lachnospiraceae/gbk/Lachnospiraceae_genomes.gbk"

for rec in SeqIO.parse(open(infile,"r"), "genbank"):
    merged_rec += rec + ("N" *50)

merged_rec.id = "merged_lachno"
merged_rec.description = "Merged (complete) Lachnospiraceae Genomes"
SeqIO.write(merged_rec, "/home/calle/Desktop/collected_genomes/Lachnospiraceae/gbk/Lachnospiraceae_genomes_single_record.gbk", "genbank")