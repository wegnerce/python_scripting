# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 15:33:12 2018

@author: calle
"""
# needed modules
from Bio import SeqIO

# necessary paths
annot_rast = "/home/calle/Storage/Data/Sideroxydans_RAST/6666666.375277.txt"
orfs_rast = "/home/calle/Storage/Data/Sideroxydans_RAST/6666666.375277.fna"
orfs_modified = "/home/calle/Storage/Data/Sideroxydans_RAST/6666666.375277_mod.fna"
genome_rast = "/home/calle/Storage/Data/Sideroxydans_RAST/CL21_HGAP4.fasta"

# variables to play with
new_ids = {}
contig_ids = []
i = 0

# we read the annotation and write prodigal like headers into a dictionary
with open(annot_rast, "rb") as infile:
    next(infile)
    for line in infile:
        row = line.split("\t")
        if row[0] not in contig_ids:
            contig_ids.append(row[0])
            i = i + 1
        if row[6] == "+":
            strand = "1"
        else:
            strand = "-1"
        k = row[1].rfind(".")
        new_row_1 = row[1][:k] + "_" + row[1][k+1:]
        new_ids[row[1]] = row[0] + "_" + row[1].split(".")[-1] + " # " + \
                row[4] + " # " + row[5] + " # " + strand + " # " + "ID=" + \
                str(i) + "_" + row[1].split(".")[-1] + ";;;;;"

output_handle = open(orfs_modified, "w")

for seq_record in SeqIO.parse(open(orfs_rast), "fasta"):
    new_record_id = new_ids[seq_record.id]
    # seq_record.id = "H53_A13" + "_" + str(j) + "_" + str(len(seq_record.seq))
    # output_handle.write(">%s%s\n%s\n" % (
    output_handle.write(">%s\n%s\n" % (
        new_record_id,
        seq_record.seq))
