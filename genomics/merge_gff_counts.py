
# -*- coding: utf-8 -*-
"""
@author:      Carl-Eric Wegner
@affiliation: Küsel Lab - Aquatic Geomicrobiology
              Friedrich Schiller University of Jena

              carl-eric.wegner@uni-jena.de
"""

# needed modules/packages
# import sys
from collections import defaultdict

# declare necessary filepaths/variables
# gff_in = sys.argv[1]
'''
gff_in = "/home/calle/Storage_II/Data/BC_RNA-Seq_201906/Shewanella_oneidensis_MR1.gff"
counts_in = "/home/calle/Storage_II/Data/BC_RNA-Seq_201906/cpm_log_MR1.csv"
merged_out = "/home/calle/Storage_II/Data/BC_RNA-Seq_201906/cpm_log_MR1_annotated.csv"
'''
gff_in = "/media/cewegner/CEW_I/_Ca_Methylotracia/RNA_seq/PyLa_vs_Py/late/RHAL1_chromosome_plasmid.gff"
counts_in = "/media/cewegner/CEW_I/_Ca_Methylotracia/RNA_seq/PyLa_vs_Py/late/DGE_AL1_PyLa_up_20200331.csv"
kegg_annot = "/media/cewegner/CEW_I/_Ca_Methylotracia/RNA_seq/PyLa_vs_Py/late/RHAL1_KEGG.txt"
merged_out = "/media/cewegner/CEW_I/_Ca_Methylotracia/RNA_seq/PyLa_vs_Py/late/DGE_AL1_PyLa_up_20200331_annotated.csv"

locus_product = {}
locus_kegg = {}
counts_annot_merged = defaultdict(list)
current_locus = ""

'''
# code for MR1
# go through gff, extract locus plus gene product as dictionary
with open(gff_in, "rb") as infile:
    lines = (line.rstrip() for line in infile)
    lines = (line for line in lines if line)
    for line in lines:
        if not line.startswith("#"):
            if line.split("\t")[2] == "gene":
                locus_product[line.split("\t")[8].split(";")[-1].split("=")[1]] = ""
                current_locus = line.split("\t")[8].split(";")[-1].split("=")[1]
            if line.split("\t")[2] == "CDS":
                locus_product[current_locus] = line.split("\t")[8].split(";")[-3].split("=")[1]
'''
'''
# code for CL21
# go through gff, extract locus plus gene product as dictionary
with open(gff_in, "rb") as infile:
    lines = (line.rstrip() for line in infile)
    lines = (line for line in lines if line)
    for line in lines:
        if not line.startswith("#") and line.split("\t")[2] == "CDS":
            locus_product[line.split("\t")[8].split(";")[0].split("=")[1]] = line.split("\t")[8].split(";")[1]\
                .split("=")[1]
'''


# code for AL1
# go through gff, extract locus plus gene product as dictionary
with open(gff_in, "r") as infile:
    lines = (line.rstrip() for line in infile)
    lines = (line for line in lines if line)
    for line in lines:
        if not line.startswith("#") and line.split("\t")[2] == "CDS":
            locus_product[line.split("\t")[8].split(";")[0].split("=")[1]] = line.split("\t")[8].split(";")[-2]\
                .split("=")[1]


with open(kegg_annot, "r") as infile:
    lines = (line.rstrip() for line in infile)
    lines = (line for line in lines if line)
    for line in lines:
        locus_kegg[line.split("\t")[0][1:]] = " ".join(line.split("\t")[1:])
print (locus_kegg)

# add annotation data to count table
with open(counts_in, "r") as infile:
    lines = (line.rstrip() for line in infile)
    lines = (line for line in lines if line)
    for line in lines:
        if not line.startswith("\t"):
            counts_annot_merged[line.split("\t")[0]] = line.split("\t")[1:]
        else:
            print (line)
            header = line + "\t" + "product"

for key, value in locus_product.items():
    if key in counts_annot_merged:
        counts_annot_merged[key].append(value)

for key, value in locus_kegg.items():
    if key in counts_annot_merged:
        counts_annot_merged[key].append(value)

# write annotated count table to file
with open(merged_out, "w") as outfile:
    outfile.write(header + "\n")
    for k, v in counts_annot_merged.items():
        outfile.write(str.join("\t", [k] + [str(i) for i in v]) + "\n")
