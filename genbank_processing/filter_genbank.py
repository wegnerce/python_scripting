# -*- coding: utf-8 -*-

"""
Filtering Genbank files based on sequence IDs

@author:      Carl-Eric Wegner
@affiliation: Küsel Lab - Aquatic Geomicrobiology
              Friedrich Schiller University of Jena

              carl-eric.wegner@uni-jena.de
"""
from Bio import SeqIO

# genbank_file to read
gbk_in = "/home/calle/BIOPHA/AquaGeomicro/1 - group member folders-contacts/Qia\
nqian/Acidithrx_sp_c25.fasta.cb.gb"

# locustags of interests
wanted = [line.rstrip("\n") for line in open("/home/calle/Desktop/list_of_locu\
stags.txt")]

# get all sequence records for the specified genbank file
recs = [rec for rec in SeqIO.parse(gbk_in, "genbank")]
for record in recs:
    for f in record.features:
        if f.type == "gene" and "locus_tag" in f.qualifiers:
            locus_tag = f.qualifiers["locus_tag"][0]
            if locus_tag in wanted:
                try:
                    out1 = f.qualifiers["locus_tag"][0] + "," \
                            + f.qualifiers["gene"][0] + "\n"
                    file.write(out1)
                except:
                    out2 = f.qualifiers["locus_tag"][0] + ",\
                            no gene name" + "\n"
                    file.write(out2)
