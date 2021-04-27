# -*- coding: utf-8 -*-
"""
@author:      Carl-Eric Wegner
@affiliation: Küsel Lab - Aquatic Geomicrobiology
              Friedrich Schiller University of Jena

              carl-eric.wegner@uni-jena.de
"""

import csv

embl_in = "/media/calle/CEW_I1/_Ca_Methylotracia/EBI_ENA_submission/CL21_PRJEB33828.embl"
loci_ids_out = csv.writer(open("/home/calle/Storage_II/Data/BC_RNA-Seq_201906/final_analyses_201909/loci_IDs.txt", "wb"))
locus_id = {}
found_locus = 0
found_ID = 0 

with open(embl_in, "rb") as infile:
    for line in infile:
        if "locus_tag" in line:
            locus_tag = line.split("=")[1][1:-2]
            found_locus = 1
        if 'note="ID:' in line:
            ID = line.split("=")[1][1:-2]
            found_ID = 1
        if found_locus == 1 and found_ID == 1:
            locus_id[ID] = locus_tag
            found_locus = 0
            found_ID = 0


for key, val in locus_id.items():
    loci_ids_out.writerow([key, val])