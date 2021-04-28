# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 09:55:50 2016

@author: calle
"""

# load required modules
import csv
import taxman as tx
from collections import defaultdict

# necessary paths, variables
blast_out = "/media/STORAGE1/Stasja_pro/to_filter/mRNA_assemblies/ublast_contigs_trans/cellulose_mRNA_trans.faa.out"
#id_gi_out = "/media/STORAGE1/Stasja_pro/to_filter/mRNA_assemblies/ublast_contigs_trans/cel_mRNA_trans_id_gi.txt"
cov_inf = "/media/STORAGE1/Stasja_pro/to_filter/mRNA_assemblies/cellulose/cellulose_rep1_covstats.txt"
tax_rta_out = "/media/STORAGE1/Stasja_pro/to_filter/mRNA_assemblies/ublast_contigs_trans/re-analyis/cel_rep1_tax.txt"
id_gi = defaultdict(list)
tax_rta = {}
cov_stats = {}

# read coverage information
with open(cov_inf, "rb") as infile:
        for line in infile:
            if not line.startswith("#"):
                cov_stats[line.split("\t")[0][:line.split("\t")[0].find(" ")]] = line.split("\t")[1]

# read blast output, extract contig id and assigned GIs
# lookup the taxid based on the GI, lookup the lineage and extract
# the taxid of the corresponding phylum, this taxid is used key in a new
# dictionary, which collects the relative transcript abundance per phylum
with open(blast_out, "rb") as infile:
    blast_reader = csv.reader(infile, delimiter = "\t")
    for line in blast_reader:
        split_line = line[0].split("_")
        gi = line[1].split("|")[1]
        if not "_".join(split_line[:2]) in id_gi:
            id_gi["_".join(split_line[:2])] = []
            id_gi["_".join(split_line[:2])].append(gi)
for entry in id_gi:
    id_gi[entry].append(tx.getTaxidByGi(int(id_gi[entry][0])))
    if id_gi[entry][1] != -1:
        id_gi[entry].append(tx.getPathByTaxid(int(id_gi[entry][1]))[3])
    if len(id_gi[entry]) > 2 and id_gi[entry][2] not in tax_rta:
        tax_rta[id_gi[entry][2]] = 0
    elif len(id_gi[entry]) > 2 and id_gi[entry][2] in tax_rta:
        tax_rta[id_gi[entry][2]] = tax_rta[id_gi[entry][2]] + float(cov_stats[entry])
    
with open(tax_rta_out, "wb") as outfile:
    for key, value in tax_rta.items():
        outfile.write("%s,%s\n" % (key, value))



     
        

        
    