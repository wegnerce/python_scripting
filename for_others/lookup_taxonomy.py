# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 08:26:50 2016

@author: calle
"""
# lets load all necessary modules
from collections import defaultdict # needed because we create a dict of lists later
import csv # for simple parsing of tables
import taxomias # for all the magic

# define dictionary of lists to write the taxonomic assignments to
tax_mapping = defaultdict(list)
# the format will in the end be like that:
# seq_ID cazy_assignment taxonomic_path

# lets go, we read the blast output and write seq_ids and cazy assignment to
# our dictionary
with open ("/home/lu87neb/data/RA_blast.out", "rb") as infile:
    for line in infile:
        tax_mapping[line.split("\t")[0]] = [] # we first add pro forma an empty list for every seq_id
        tax_mapping[line.split("\t")[0]].append(line.split("\t")[1].split("|")[1]) # now we add the cazy assignment
        tax_path = taxomias.PathByTaxid(taxomias.TaxidByAcc(line.split("\t")[1].split("|")[0])) # now we have the taxonomic path in form of taxids e.g. [1, 131567, 2, 57723]
        tax_path = [taxomias.NameByTaxid(int(entry)) for entry in tax_path] # look up names for taxids
        tax_path = ";".join(tax_path) # concatenate list to string
        tax_mapping[line.split("\t")[0]].append(tax_path) # add string to dict

writer = csv.writer(open("/home/lu87neb/data/RA_blast_mapped.txt", "wb")) # write the dictionary to a file
for k,v in tax_mapping.iteritems():
    writer.writerow([k] + v)
