# -*- coding: utf-8 -*-
"""
@author:      Carl-Eric Wegner
@affiliation: Küsel Lab - Aquatic Geomicrobiology
              Friedrich Schiller University of Jena

              carl-eric.wegner@uni-jena.de
"""

# needed modules
import csv
from collections import defaultdict

# paths of files to be used
input_MAGE = "/home/calle/Downloads/AL1.1.tab"
input_eggNOG = "/home/calle/Downloads/AL1.1-EGGNOG.txt"
input_KEGG = "/home/calle/Downloads/AL1.1-KEGG.txt"

# necessary variables, lists, dicts
annotation = defaultdict(list)

# read MAGE annotation, keep selected fields of interest
with open(input_MAGE, "rb") as infile:
    MAGE_reader = csv.reader(infile, delimiter = "\t")
    for line in MAGE_reader:
        annotation[line[0]] = [line[1], line[2], line[3], line[4], line[5], line[8], line[10], line[13], line[15]]

# read eggNOG annotation, add fields of interest to created annotation dictionary
with open(input_eggNOG, "rb") as infile:
    eggNOG_reader = csv.reader(infile, delimiter = "\t")
    for line in eggNOG_reader:
        annotation[line[0]] = annotation[line[0]] + [line[10],line[11],line[12]]

# read KEGG annotation, add fields of interest to created annotation dictionary
with open(input_KEGG, "rb") as infile:
    KEGG_reader = csv.reader(infile, delimiter ="\t")
    for line in KEGG_reader:
        annotation[line[0].split("|")[0]] = annotation[line[0].split("|")[0]] + [line[1], line[2]]

header = ["GeneID","Type","Frame","Begin","End","Length","Gene","Product","Localization","EC","COGClassID","ClassDescription","COGProcess","KO","KEGGAnnot"]
# write annotation 
with open("/home/calle/AL1_annot.tab", "wb") as outfile:
    annot_writer = csv.writer(outfile, delimiter="\t", quoting=csv.QUOTE_MINIMAL)
    annot_writer.writerow(header) 
    for key, values in annotation.items():
            annot_writer.writerow([key] + values)