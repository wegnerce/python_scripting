# -*- coding: utf-8 -*-
"""
@author:      Carl-Eric Wegner
@affiliation: Küsel Lab - Aquatic Geomicrobiology
              Friedrich Schiller University of Jena

              carl-eric.wegner@uni-jena.de
"""

in_table = "/home/cewegner/Documents/koehler_taxonomy.csv"
out_table = "/home/cewegner/Documents/koehler_taxonomy_fixed.csv"

with open(in_table, "rb") as infile, open(out_table, "wb") as outfile:
    for line in infile:
        outfile.write(line.split(",")[0] + "\t" + ",".join(line.split(",")[1:]))

            
