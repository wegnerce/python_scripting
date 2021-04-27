# -*- coding: utf-8 -*-
"""
@author:      Carl-Eric Wegner
@affiliation: Küsel Lab - Aquatic Geomicrobiology
              Friedrich Schiller University of Jena

              carl-eric.wegner@uni-jena.de
"""

### import necessary modules
import csv
import sys
csv.field_size_limit(sys.maxsize)

### required paths
gff_in = "/home/calle/Downloads/Soxy_CL21_dfast/genome.gff"
gff_out = "/home/calle/Downloads/Soxy_CL21_dfast/Soxy_CL21_genome_stripped.txt"

### lists, dicts etc.
stripped = []

### strip
to_keep = [0, 1, 2, 3, 4, 8]

with open(gff_in, "rb") as infile:
    gff_reader = csv.reader(infile, delimiter = "\t")
    next(gff_reader, None)
    for line in gff_reader:
        if not line[0].startswith(("#", ">", "A", "T", "C", "G")):
            new_line = list(line[i] for i in to_keep)
            annot_details = new_line[5]
            if "Aragorn" in new_line[5].split(";")[1]:
                new_line[5] = new_line[5].split(";")[4].replace("locus_tag=", "")
                new_line.append(annot_details.split(";")[2].replace("product=", ""))
            else:
                new_line[5] = new_line[5].split(";")[1].replace("locus_tag=", "")
                new_line.append(annot_details.split(";")[3].replace("product=", ""))
                new_line.append("//".join(annot_details.split(";")[4:]).replace("// ", "//").replace("note=",
            ""))
            stripped.append(new_line)

with open(gff_out, "wb") as outfile:
    gff_writer = csv.writer(outfile, delimiter = "\t")
    gff_writer.writerow(["Contig", "Identified by", "Type", "Start", "End", "Gene ID", "Product",
    "Annotation details DFAST"])
    for item in stripped:
        gff_writer.writerow(item)


