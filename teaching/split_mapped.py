# -*- coding: utf-8 -*-
"""
Created on Thu 20th of July, '17
@author: Carl-Eric Wegner - Küsel Lab - FSU Jena
"""
# needed modules
import argparse
from Bio import SeqIO

# necessary data structures
splitted_f = []
splitted_r = []

# information about argument parsing
parser = argparse.ArgumentParser(description = "Splitting mapped sequence data originating from BBMAP")
parser.add_argument("--mapped", "-m", help="indicate mapped sequence data from BBMAP", action="store")
args = parser.parse_args()

# function splitting the mapped sequences
def split_mapped(infasta, ftype):
    global splitted_f, splitted_r
    for record in SeqIO.parse(infasta, ftype):
        if record.description.split(" ")[1].startswith("1"):
            splitted_f.append(record)
        else:
            splitted_r.append(record)
    SeqIO.write(splitted_f, infasta + ".split_f." + ftype, ftype)
    SeqIO.write(splitted_r, infasta + ".split_r." + ftype, ftype)

# program control structure
fasta_out = (".fasta", ".fna")
fastq_out = (".fastq", ".fq")
if args.mapped:
    if args.mapped.endswith(fasta_out):
        split_mapped(args.mapped, "fasta")
    elif args.mapped.endswith(fastq_out):
        split_mapped(args.mapped, "fastq")
    else:
        print "Invalid program call, please check split_mapped.py -h"

