# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 22:14:52 2017

@author: calle
"""

import csv

with open("/home/calle/Dropbox/MH_PG_CEW/ISSM Talk/parcu_euk_OTU_IDs.txt", "rb") as infile, \
    open("/home/calle/Dropbox/MH_PG_CEW/ISSM Talk/parcu_euk_OTU_IDs_renamed.txt", "wb") as outfile:
    tax_reader = csv.reader(infile, delimiter = "\t")
    tax_writer = csv.writer(outfile, delimiter = "\t")
    for line in tax_reader:
        if not line[0].startswith("bac"):
            line[0] = "Euk" + line[0]
            line[0].replace(" ","")
            line[0].replace(" ","")
            outfile.write("\t".join(line)+"\n")
        else:
            outfile.write("\t".join(line)+"\n")

#wanted = set(line.rstrip("\n") for line in open("/home/calle/Dropbox/MH_PG_CEW/ISSM Talk/parcu_euk_OTU_IDs.txt", "rb")) #.split(None,1)[0]
#filtered = (line for line in open("/home/calle/Dropbox/MH_PG_CEW/ISSM Talk/parcu_euk_taxonomy.txt", "rb") if line.split("\t")[0] in wanted)
#with open("/home/calle/Dropbox/MH_PG_CEW/ISSM Talk/parcu_euk_taxonomy_filtered.txt", "wb") as outfile:
    #for line in filtered:
    #    outfile.write(line)