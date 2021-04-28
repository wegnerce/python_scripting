# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 17:11:42 2016

@author: calle
"""

# needed modules
import argparse
import csv
import matplotlib.pyplot as plt
from collections import defaultdict

# information about argument parsing
parser = argparse.ArgumentParser(description = "Plotting and coverage information of contigs with blast hit information")
parser.add_argument("--blast", "-b", help="path to blast output", action="store")
parser.add_argument("--cov", "-c", help="path to bbmap coverage information", action="store")
args = parser.parse_args()

# required variables, constants, lists. dictionaries
ids, length, coverage = [], [], []
cov_read = {}
contigs = defaultdict(list)
max_length = 0
max_coverage = 0

# read seq ids with blast hit, filter contigs accordingly and extract coverage and length for plotting
def process_blast_cov(blast_out, cov_info):
    global ids, length, coverage, cov_filtered, max_length, max_coverage
    with open(cov_info, "rb") as infile:
        for entry in infile:
            if float(entry.split(",")[1]) > 20:
                cov_read[entry.split(",")[0]] = float(entry.split(",")[1])
    with open(blast_out, "rb") as infile:
        for line in infile:
            if line.split("\t")[0].split(" ")[0] not in ids:
                if line.split("\t")[0].split(" ")[0] in cov_read:
                    if cov_read[line.split("\t")[0].split(" ")[0]] > 20:
                        ids.append(line.split("\t")[0].split(" ")[0])
                        length.append(int(line.split("\t")[0].split(" ")[3][4:]))
                        coverage.append(float(cov_read[line.split("\t")[0].split(" ")[0]]))
                        contigs[line.split("\t")[0].split(" ")[0]] = []
                        contigs[line.split("\t")[0].split(" ")[0]].append(int(line.split("\t")[0].split(" ")[3][4:]))
                        contigs[line.split("\t")[0].split(" ")[0]].append(float(cov_read[line.split("\t")[0].split(" ")[0]]))
                        
    max_length = float(max(length))+100
    max_coverage = max(coverage)
    return coverage, length, max_length, max_coverage

# function to plot the the contig length versus coverage for contigs featuring blast hits
def plot_length_coverage(seq_length, seq_coverage, lim_length, lim_coverage, blast_out):
    global contigs    
    plt.scatter(seq_length, seq_coverage, s=40, alpha = 0.50, color="black")
    plt.xlabel("Contig length [bp]")
    plt.ylabel("Coverage [x-fold]")
    plt.axis([150, lim_length, 0, lim_coverage])
    plt.savefig(blast_out + ".svg", dpi = 300, format = "svg")
    print "Saved length versus coverage plot: %s" % blast_out + ".svg"
    with open(blast_out + ".contigs", "wb") as outfile:
        writer = csv.writer(outfile, delimiter = "\t")    
        for k,v in contigs.iteritems():
            writer.writerow([k] + v)
  
# program control structure
if args.blast and args.cov:
    process_blast_cov(args.blast, args.cov)
    plot_length_coverage(length, coverage, 2000, 2000, args.blast)
else:
    print "Invalid program call, please check your input files."
