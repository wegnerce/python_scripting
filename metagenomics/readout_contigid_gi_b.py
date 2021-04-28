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
blast_out = "/media/STORAGE1/Stasja_pro/to_filter/mRNA_assemblies/ublast_contigs_trans/xylan_mRNA_trans.faa.out"
#id_gi_out = "/media/STORAGE1/Stasja_pro/to_filter/mRNA_assemblies/ublast_contigs_trans/cel_mRNA_trans_id_gi.txt"
cov_inf = "/media/STORAGE1/Stasja_pro/to_filter/mRNA_assemblies/xylan/xylan_rep3_covstats_trans.txt"
tax_rta_out = "/media/STORAGE1/Stasja_pro/to_filter/mRNA_assemblies/ublast_contigs_trans/re-analyis/xylan_rep3_tax_trans.txt"
id_gi = defaultdict(list)
tax_rta = {}
cov_stats = {}

# phyla to consider
consider = ["Actinobacteria", "Alveolata", "Amoebozoa", "Aquificae", "Bacteroidetes/Chlorobi group",\
    "Chlamydiae/Verrucomicrobia group", "Chloroflexi", "Cyanobacteria", "Deinococcus-Thermus",\
    "Elusimicrobia", "environmental samples", "Euglenozoa", "Euryarchaeota", "Fibrobacteres/Acidobacteria group",\
    "Firmicutes", "Fusobacteria", "Gemmatimonadetes", "Nitrospinae", "Nitrospirae", "Opisthokonta",\
    "Planctomycetes", "Proteobacteria", "Rhodophyta", "Spirochaetes", "unclassified Bacteria",\
    "Viridiplantae"]

# read coverage information
with open(cov_inf, "rb") as infile:
    for line in infile:
        if not line.startswith("#"):
            split_line = line.split("\t")[0].split("_")
            "_".join(split_line[:2])
            #cov_stats[line.split("\t")[0][:line.split("\t")[0].find(" ")]] = float(line.split("\t")[1])
            cov_stats["_".join(split_line[:2])] = float(line.split("\t")[1])
total_transcript_count = sum(cov_stats.values())
print "Total number of transcripts: " + str(total_transcript_count)
        

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
    if len(id_gi[entry]) > 2 and tx.getNameByTaxid(id_gi[entry][2]) not in tax_rta \
    and tx.getNameByTaxid(id_gi[entry][2]) in consider:
        tax_rta[tx.getNameByTaxid(id_gi[entry][2])] = 0
    elif len(id_gi[entry]) > 2 and tx.getNameByTaxid(id_gi[entry][2]) in tax_rta:
        tax_rta[tx.getNameByTaxid(id_gi[entry][2])] = tax_rta[tx.getNameByTaxid(id_gi[entry][2])] + float(cov_stats[entry])
   
with open(tax_rta_out, "wb") as outfile:
    for key, value in tax_rta.items():
        outfile.write("%s,%s\n" % (key, value))
        