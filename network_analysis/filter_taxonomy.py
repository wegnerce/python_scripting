# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 09:36:24 2017

@author: calle
"""

# import needed modules
import csv
import pandas as pd

# necessary paths, variables, etc.
taxonomy = "/home/calle/Desktop/ultrasmall_ongoing/OTU_all_SILVA132_tax_100reads.txt"
taxonomy_stripped = "/home/calle/Desktop/ultrasmall_ongoing/OTU_all_SILVA132_tax_noL_no01_200reads_03.txt"
#otu_tab = "/home/calle/Storage/Data/parcu_netw/OTU_all.txt"
otu_tab_stripped = "/home/calle/Storage/Data/parcu_netw/final/OTU_all_noL_no01_100reads_03.txt"
otu_tab_cluster = "/home/calle/Storage/Data/parcu_netw/final/final_cluster1_OTUs.txt"

#taxa =["Candidatus_Nomurabacteria", "Parcubacteria_unclassified", "Planctomycetacia",
#       "Candidatus_Azambacteria", "Candidatus_Adlerbacteria", "Saccharibacteria_cl",
#       "Gemmatimonadetes", "Omnitrophica_cl", "Gracilibacteria_cl", "JG-KF-CM",
#       "JG-AG-", "Chloroplast", "Candidatus_Jorgensenbacteria", "S",
#       "Latescibacteria_cl", "MLJ-", "Bacteroidetes_unclassified", "Bacilli",
#       "Chloroflexi_unclassified", "Candidatus_Woesebacteria", "WWE_cl"]
#taxa = ("Nitrospira", "Parcubacteria_cl", "Parcubacteria_unclassified", "Candidatus_Magasanikbacteria",
#        "Candidatus_Wolfebacteria", "Elusimicrobia", "Candidatus_Jorgensenbacteria",
#        "Candidatus_Amesbacteria")
#taxa = ("Candidatus_Nomurabacteria", "Candidatus_Azambacteria", "Candidatus_Moranbacteria",
#        "Candidatus_Adlerbacteria", "Candidatus_Woesebacteria")

with open("/home/calle/Desktop/ultrasmall_ongoing/OTUs_for_tax.txt", "rb") as infile:
    taxa = set(infile.read().split("\n"))

otus = []

print "*** Filter available taxonomic assignments for taxa of interest."
# read taxonommy file
with open(taxonomy, "rb") as infile, open(taxonomy_stripped, "wb") as outfile:
    taxonomy_reader = csv.reader(infile, delimiter = "\t")
    taxonomy_writer = csv.writer(outfile, delimiter = "\t")
    next(taxonomy_reader, None) # skip the header
    for line in taxonomy_reader:
        #if line[1].split(";")[2] in taxa:
        if line[0] in taxa:
            otus.append(line[0])
            taxonomy_writer.writerow(line)
print "*** Identified %d OTUs of interest." % (len(otus))
print "    Taxonomic assignments were stripped accordingly."
print ""
print otus[:10]

# read otu table, filter out OTUs with less than X counts over all samples
#print "*** Filter the raw OTU table (OTUs > 100 seqs over all samples)."
#otu_raw = pd.read_csv("/home/calle/Storage/Data/parcu_netw/OTU_all.txt")
#otu_filtered = pd.read_csv("/home/calle/Storage/Data/parcu_netw/final/OTU_all_noL_no01_200reads_03.txt")
#otu_filtered = otu_raw[otu_raw.sum(axis = 1) > 100]
#print "*** Identified %d OTUs with more than 100 counts over all samples" % (len(otu_filtered))
#print "    OTU table was stripped accordingly."
#otu_filtered.to_csv(otu_tab_stripped, sep='\t', encoding='utf-8', index = False)
#print ""

# filter the stripped OTU table for OTUs of interest
#print "*** Filter the stripped OTU table based on identified OTUs of interest."
#otu_filtered = otu_filtered[otu_filtered['#OTUID'].isin(otus)] # that is the beauty of pandas ;-)
#otu_filtered.to_csv(otu_tab_cluster, encoding='utf-8', index = False)