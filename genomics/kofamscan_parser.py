# -*- coding: utf-8 -*-
"""
@author:      Carl-Eric Wegner
@affiliation: Küsel Lab - Aquatic Geomicrobiology
              Friedrich Schiller University of Jena

              carl-eric.wegner@uni-jena.de
"""

# ~~~~~ Import modules
import sys

# ~~~~~ IO paths
kofamscan_in = sys.argv[1]
kofamscan_parsed = sys.argv[2]
# kofamscan_parsed_split = sys.argv[3]

# ~~~~~~ Parse kofamscan output
# read kofamscan output ("detail"), keep only hits above threshold and write them to output
with open(kofamscan_in, "r") as infile, open(kofamscan_parsed, "w") as outfile:
    lines = (line.rstrip() for line in infile)
    lines = (line for line in lines if line)
    for line in lines:
        if not line.startswith("#"):
            if line[0] == "*":
                outfile.write(line.split("\t")[0].replace("*", "") + "\t" + line.split("\t")[1] + "\t" + line.split("\t")[5] + "\n")
