# -*- coding: utf-8 -*-
"""
@author:      Carl-Eric Wegner
@affiliation: Küsel Lab - Aquatic Geomicrobiology
              Friedrich Schiller University of Jena

              carl-eric.wegner@uni-jena.de
"""

# needed modules
import csv

# needed variables
species = ["Acp_C61_07", "Acp_angustum_01", "Acp_rubrum_04", "Acp_sp_JA12_05", "Acp_multivorum_03",
            "Acp_sp_PM_06", "Acp_cryptum_02"] # this list can be adapted dependent on the (number of) genomes you are working on

upsetr_matrix = {}

# functions
def domatrix(anvio_out):
    with open(anvio_out, "rb") as infile:
        next(infile)
        for line in infile:
            if not line.split("\t")[1] in upsetr_matrix:
                upsetr_matrix[line.split("\t")[1]] = [0,0,0,0,0,0,0]
            for i in range(1, 8, 1):
                if line.split("\t")[3] == species[i-1]:
                    upsetr_matrix[line.split("\t")[1]][i-1] = 1
    print upsetr_matrix

def printmatrix(output):
    with open(output, "wb") as outfile:
        csv_outfile = csv.writer(outfile, delimiter = "\t")
        csv_outfile.writerow(["\t"] + species)
        for key in sorted(upsetr_matrix.keys()):
            csv_outfile.writerow([key] + upsetr_matrix[key])

domatrix("output_from_anvio.txt") # obviously you have to change these paths!
printmatrix("upsetr_input.txt")

