# -*- coding: utf-8 -*-
'''
Created on April 12, 2017
@author: Carl-Eric Wegner - Küsel Lab - Geomicrobiology - FSU Jena
Subset .fasta files originating from QIIME (after split.seqs.py) according to
a given mapping file.
'''

# needed modules
import argparse
import csv
from Bio import SeqIO

# argument parsing
parser = argparse.ArgumentParser(description = "Split a QIIME .fasta file by sample ID")
parser.add_argument("--mapping", "-m", help="QIIME mapping file", action="store")
parser.add_argument("--sequences", "-s", help=".fasta file of interest [processed by split_seq,py]", action="store")
args = parser.parse_args()

# necessary lists to store sample IDs and subset records
sample_ids = []
subsets = [[]]

# function subsetting the original fasta
# first an empty list is created for every unique sample ID in the mapping
# file, the lists are then populated with the respective records
def subset(mapping, sequences):
    global sample_ids, subsets
    with open(mapping, "rb") as infile:
        mapping_reader = csv.reader(infile, delimiter = "\t")
        next(mapping_reader, None)
        for line in mapping_reader:
            if line[0] not in sample_ids:
                sample_ids.append(line[0])                
    for sample_id in sample_ids:
        subsets.append([])    
    for record in SeqIO.parse(sequences, "fasta"):
        to_add = sample_ids.index(record.id.split("_")[0])
        subsets[to_add].append(record)    
    j = 0
    for i in sample_ids:
        filename = sequences + "%s.fasta" % i
        handle = open(filename, "w")
        count = SeqIO.write(subsets[j], handle, "fasta")
        handle.close()
        print "Wrote %i records to %s" % (count, filename)
        j = j + 1

# script control structure
if args.mapping and args.sequences:
    subset(args.mapping, args.sequences)
else:
    print "check avg_rga.py -h"
        

    



            
        
