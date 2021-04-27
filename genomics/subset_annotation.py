# -*- coding: utf-8 -*-
"""
@author:      Carl-Eric Wegner
@affiliation: Küsel Lab - Aquatic Geomicrobiology
              Friedrich Schiller University of Jena

              carl-eric.wegner@uni-jena.de
"""

# needed modules/packages
import csv
import sys

# declare necessary filepaths/variables
annot_in = sys.argv[1]
to_keep = set(open(sys.argv[2]).read().split())
kept = sys.argv[3]

# read annotation input, iterate over lines, split based on genome tag
with open(annot_in, "rb") as infile, open(kept, "wb") as outfile:
    outfile.write("GeneID" + "\t" + "KO" + "\n")
    line = infile.next()
    for line in infile:
        if line.split("\t")[0] in to_keep:
            outfile.write(line.split("\t")[0]+"\t"+line.split("\t")[13]+"\n")