# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 10:50:17 2016

@author: calle
"""
# needed modules
import csv
import taxman as tx

# required paths
blast_out = "/media/STORAGE1/Stasja_pro/to_filter/mRNA_assemblies/total/total_mRNA_contigs_trans.faa.out"
blast_out_filtered = "/media/STORAGE1/Stasja_pro/to_filter/mRNA_assemblies/total/total_mRNA_contigs_trans_out_filtered.out"



# process blast output, filter hits originating from plants
with open(blast_out, "rb") as infile, open(blast_out_filtered, "wb") as outfile:
    blast_reader = csv.reader(infile, delimiter = "\t")
    for line in blast_reader:
        gi_hit = line[1].split("|")[1]
        if not 33090 in tx.getPathByTaxid(tx.getTaxidByGi(gi_hit)):
            print tx.getPathByTaxid(tx.getTaxidByGi(gi_hit))
            outfile.write("\t".join(line)+"\n")
