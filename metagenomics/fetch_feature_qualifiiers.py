# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 17:42:16 2016

@author: calle
"""
# needed modules
from Bio import Entrez, SeqIO

# list of NCBI accessions to be processed one accession per line
list_of_accessions = "/home/calle/Desktop/DA111_acc.txt"

# NCBI always wants to know who you are
Entrez.email = "your@dummyemail.com"

# define lists for collected records and extracted sample isolation sources
records_to_scan = []
isolation_sources = []
product = []

# lets fetch genbank entries of interest based on the specified list of accessions
wanted_entries = set(line.rstrip("\n") for line in open(list_of_accessions))
print wanted_entries
print "%i NCBI accessions to be looked up" % len(wanted_entries)
for accession in wanted_entries:
	fetch_seqs = Entrez.efetch(db="nucleotide", id=accession, rettype="gb", retmode="text")
	records_to_scan.append(SeqIO.read(fetch_seqs, "gb"))

# extract the sample origin from collected genbank records
for record in records_to_scan:
    for f in record.features:
        if f.type == "source" and "source" in f.qualifiers:
            isolation_sources.append(f.qualifiers["source"][0])
												
# write looked up samples origins to a new txtfile
with open(list_of_accessions + ".origins", "wb") as outfile:
	for item in isolation_sources:
		outfile.write("%s\n" % item)