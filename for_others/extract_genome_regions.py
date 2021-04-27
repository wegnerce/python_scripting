# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 14:36:42 2015

@author: calle
"""

# load required modules
from Bio import SeqIO
from collections import defaultdict
import csv

# necessary paths
coord_file = "/home/calle/Desktop/coordinates_3.txt"
genome = "/home/calle/Desktop/usti_genome.fna"
extract = open("/home/calle/Desktop/extract.fasta", "wb")

# variables, constants
to_extract = defaultdict(list)

# read the coordinates file into a dictionary, key = chromosome, value =
# coordinates
with open (coord_file, "rb") as infile:
    coord_reader = csv.reader(infile, delimiter = ";")
    next(coord_reader, None) # skip header of the coordinates file
    for line in coord_reader:
        for col in line:
            col.replace('"', '')
        if not line[0] in to_extract:
            to_extract[line[0]] = []
            to_extract[line[0]].append(line[1])
        else:
            to_extract[line[0]].append(line[1])


# extract sequence segments based on read coordinates and write them to
# a new file
for seq_record in SeqIO.parse(genome, "fasta"):
    if seq_record.id in to_extract:
        for coord in to_extract[seq_record.id]:
            if coord.split("..")[0].isdigit() and coord.split("..")[1].isdigit():
                extract.write(">%s\n%s\n" % (seq_record.id + " " + \
                coord, seq_record.seq[int(coord.split("..")[0])-1:int(coord.split("..")[1])]))

