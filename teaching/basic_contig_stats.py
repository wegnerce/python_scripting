# -*- coding: utf-8 -*-
"""
Created on Thu 20th of July, '17
@author: Carl-Eric Wegner - Küsel Lab - FSU Jena
"""

# needed modules
import argparse
import numpy
from Bio import SeqIO
from Bio.SeqUtils import GC

# information about argument parsing
parser = argparse.ArgumentParser(description = "Determining basic contig statistics")
parser.add_argument("--contigs", "-c", help="indicate contigs in .fasta format", action="store")
args = parser.parse_args()

# calculate basic contig stats incl. total bp, max contig length, median contig
# length, N50
def contig_stats(infasta):
    global contig_stats
    seq_length = []
    unique = []
    N50 = []
    avg = []
    GC_content = []
    total_bp = 0
    no_contigs = 0
    for record in SeqIO.parse(infasta, "fasta"):
        no_contigs += 1
        GC_content.append(GC(record.seq))
        bp = len(record.seq)
        seq_length.append(bp)
        total_bp += len(record.seq)
    avg_GC = sum(GC_content) / float(len(GC_content))
    seq_length_sorted = sorted(seq_length)
    numpy.median(numpy.array(seq_length_sorted))
    print "No. of contigs: %d" % no_contigs
    print "Total bp: %d" % total_bp
    print "Maximal contig length [bp]: %d" % seq_length_sorted[-1]
    print "Median contig length [bp]: %d" % numpy.median(numpy.array(seq_length_sorted))
    print "Average contig GC content [percent]: %d" % avg_GC
    for length in seq_length_sorted:
        if not length in unique:
            unique.append(length)
    for length in unique:
        multiplier = seq_length_sorted.count(length) * length
        for i in range(multiplier):
            N50.append(length)
    index = len(N50)/2
    if index % 2==0:
        first = N50[index-1]
        second = N50[index]
        avg.append(first)
        avg.append(second)
        N50 = numpy.mean(avg)
        print "N50 [bp]: %d" % N50
    else:
        print "N50 [bp]: %d" % N50[index-1]

# program control structure
fasta_ext = (".fasta", ".fna", ".fa", ".1000")
if args.contigs:
    if args.contigs.endswith(fasta_ext):
        contig_stats(args.contigs)
else:
    print "Invalid program call, please check your input files."
 
