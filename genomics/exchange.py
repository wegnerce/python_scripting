# -*- coding: utf-8 -*-
"""
@author:      Carl-Eric Wegner
@affiliation: Küsel Lab - Aquatic Geomicrobiology
              Friedrich Schiller University of Jena

              carl-eric.wegner@uni-jena.de
"""
ids_loci = {}

with open("/home/calle/Storage_II/Data/BC_RNA-Seq_201906/final_analyses_201909/loci_IDs.txt", "rb") as infile:
    for line in infile:
        ids_loci[line.split(",")[0][3:]] = line.split(",")[1].replace("\r\n","")

print ids_loci

with open("/home/calle/Storage_II/Data/BC_RNA-Seq_201906/final_analyses_201909/counts_CL21_annotated.txt", "rb") as infile, open("/home/calle/Storage_II/Data/BC_RNA-Seq_201906/final_analyses_201909/counts_CL21_annotated_renamed.csv", "wb") as outfile: 
    for line in infile:
        if line.split("\t")[0] in ids_loci:
            outline = ids_loci[line.split("\t")[0]] + "\t" + "\t".join(line.split("\t")[1:])
            print outline
            outfile.write(outline)
        else:
            outfile.write(line)

