# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 11:15:08 2016

@author: calle
"""
# needed modules
import argparse
import csv
from collections import defaultdict

# argument parsing
parser = argparse.ArgumentParser(description = "Calculate average relative gene abundances")
parser.add_argument("--in1", "-1", help="1st file to process", action="store")
parser.add_argument("--in2", "-2", help="2nd file to process", action="store")
parser.add_argument("--klist", "-k", help="path to .txt file containing a list of K-Numbers of interest", action="store")    
args = parser.parse_args()

# needed lists, dictionaries, variables
rga = defaultdict(list)
rga_file1 = {}
rga_file2 = {}

#read K-list of interest, use ko's as dictionary keys
def read_klist(klist):
    global rga
    print "\n Read K-list of interest"
    with open(klist, "rb") as infile:
        for line in infile:
            rga[line[:line.find("\n")]] = []
    print "***DONE!"
    
def calc_avg(file1, file2):
    global rga, rga_file1, rga_file2
    print "\n Determine average RGAs"
    with open(file1, "rb") as infile:
        f1_reader = csv.reader(infile, delimiter = "\t")
        next(f1_reader, None)
        for line in f1_reader:
            if line[0] in rga:
                rga[line[0]].append(float(line[1]))
    with open(file2, "rb") as infile:
        f2_reader = csv.reader(infile, delimiter = "\t")
        next(f2_reader, None)
        for line in f2_reader:
            if line[0] in rga:
                rga[line[0]].append(float(line[1]))
    for key, values in rga.iteritems():
        rga[key].append(float((rga[key][0] + rga[key][1])/2))
    print "***DONE!"

def write_avg(klist):
    global rga
    print "\n Write output"
    with open(klist + ".avgrga", "wb") as avg_out:
        for key in rga:
            avg_out.write(key + "\t" + str(rga[key][2]) + "\n")
    print "***DONE!"

# script control structure
if args.in1 and args.in2 and args.klist:
    read_klist(args.klist)
    calc_avg(args.in1, args.in2)
    write_avg(args.klist)
else:
    print "check avg_rga.py -h"
    