# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 16:30:57 2018

@author: calle
"""

from Bio import SeqIO

silva_in = "/home/calle/Storage_II/silva_16s_v123.fa"
silva_out = "/home/calle/Storage_II/SILVA_132_tax_EDGAR_extracted.txt"

'''
with open(silva_out, "wb") as outfile, open(silva_in, "rb") as infile:
    for seq_record in SeqIO.parse(infile, "fasta"):
        if "p:" in seq_record.id and "c:" in seq_record.id and "o:" in seq_record.id \
        and "f:" in seq_record.id:
            outfile.write(">%s\n%s\n" % (
               seq_record.id,
               seq_record.seq))
'''

with open(silva_out, "wb") as outfile, open(silva_in, "rb") as infile:
    for seq_record in SeqIO.parse(infile, "fasta"):
        outfile.write("%s\n" % (
            seq_record.id))
