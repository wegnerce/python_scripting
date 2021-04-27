# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 17:37:53 2016

@author: calle
"""
# needed modules
import csv
import taxman
from Bio import SeqIO

# necessary paths
mcrA_out = "/home/calle/Desktop/mcr/mcrA.blastpout"
mcrB_out = "/home/calle/Desktop/mcr/mcrB.blastpout"
mcrG_out = "/home/calle/Desktop/mcr/mcrG.blastpout"
meth_genomes = "/home/calle/Desktop/mcr/methanogen_genomes_blastdb/methanogen_genomes.faa"
mcrA_picked = "/home/calle/Desktop/mcr/mcrA_seqs.fasta"
mcrB_picked = "/home/calle/Desktop/mcr/mcrB_seqs.fasta"
mcrG_picked = "/home/calle/Desktop/mcr/mcrG_seqs.fasta"

# required variables, lists, dictionaries
mcrA_ids = []
mcrB_ids = []
mcrG_ids = []

with open(mcrA_out, "rb") as infile:
    mcrA_reader = csv.reader(infile, delimiter = "\t")
    for line in mcrA_reader:
        if line[1] not in mcrA_ids:
            mcrA_ids.append(line[1])

with open(mcrB_out, "rb") as infile:
    mcrB_reader = csv.reader(infile, delimiter = "\t")
    for line in mcrB_reader:
        if line[1] not in mcrB_ids:
            mcrB_ids.append(line[1])

with open(mcrG_out, "rb") as infile:
    mcrG_reader = csv.reader(infile, delimiter = "\t")
    for line in mcrG_reader:
        if line[1] not in mcrG_ids:
            mcrG_ids.append(line[1])

print mcrA_ids[0]
print mcrB_ids[0]
print mcrG_ids[0]

mcrA_records = (r for r in SeqIO.parse(meth_genomes, "fasta") if r.id in mcrA_ids)
mcrB_records = (r for r in SeqIO.parse(meth_genomes, "fasta") if r.id in mcrB_ids)
mcrG_records = (r for r in SeqIO.parse(meth_genomes, "fasta") if r.id in mcrG_ids)

count_mcrA = SeqIO.write(mcrA_records, mcrA_picked, "fasta")
count_mcrB = SeqIO.write(mcrB_records, mcrB_picked, "fasta")
count_mcrG = SeqIO.write(mcrG_records, mcrG_picked, "fasta")
