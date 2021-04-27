# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 13:40:07 2016

@author: calle
"""

# load required modules
import argparse
import csv
from Bio.SeqUtils.ProtParam import ProteinAnalysis
from Bio import SeqIO
from collections import defaultdict

# necessary variables, lists, dicts
prot_comp = defaultdict(list)
#dict_holder = ""

# details about argument parsing, one argument to parse namely 
# the input amino acid .fasta file
parser = argparse.ArgumentParser(description = "Determine basic protein composition information")
parser.add_argument("--seqs", "-s", help = "indicate the AA .fasta file to be processed", action = "store")
args = parser.parse_args()

# determine basic protein composition information including AA proportions, 
# instability (according to Guruparsad et al., 1990), and the aromaticity
def process_AA_seqs(aa_seqs):
    global prot_comp
    seqs = SeqIO.parse(aa_seqs, "fasta")
    for record in seqs:
        analysed_seq = ProteinAnalysis(str(record.seq).replace("-", ""))
        if "[" in record.description:           
            if record.description.count("I") == 1:
                trans_id = record.description.split("[")[1][:-1] + " I"
            elif record.description.count("I") == 2:
                trans_id = record.description.split("[")[1][:-1] + " II"
            else:
                trans_id = record.description.split("[")[1][:-1]
        else:
            if record.description.count("I") == 1:
                trans_id = record.description + " I"
            elif record.description.count("I") == 2:
                trans_id = record.description + " II"
            else:
                trans_id = record.description
        prot_comp[trans_id] = []
        for key, value in analysed_seq.get_amino_acids_percent().iteritems():
            prot_comp[trans_id].append(value)
        prot_comp[trans_id].append(analysed_seq.instability_index())
        prot_comp[trans_id].append(analysed_seq.aromaticity())
        #prot_comp[trans_id] = analysed_seq.get_amino_acids_percent()
        #prot_comp[trans_id]["aromaticity"] = analysed_seq.aromaticity()
        #prot_comp[trans_id]["instability"] = analysed_seq.instability_index()

# write determined parameters to csv files
def write_summary(infile):
    global prot_comp
    with open(infile + ".comp", "wb") as outfile:
        writer = csv.writer(outfile, delimiter="\t")
        writer.writerow(["ID", "A", "C", "E", "D", "G", "F", "I", \
        "H", "K", "M", "L", "N", "Q", "P", "S", "R", "T", "W", "V", "Y", \
        "instability", "aromaticity"])
        for k,v in prot_comp.iteritems():
            writer.writerow([k] + v)

# script control structure 
fasta_ext = (".fasta", ".faa", ".aa")
if args.seqs:
    if args.seqs.endswith(fasta_ext):
        process_AA_seqs(args.seqs)
        write_summary(args.seqs)
else:
    print "Invalid program call, please check your input file."
    print "The script works exclusively with AA .fasta files."
