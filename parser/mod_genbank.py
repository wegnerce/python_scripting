# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 21:51:23 2017

@author: calle
"""

from Bio import SeqIO
gb_file = "/home/calle/Storage/Data/methylo_genomes/comparative_genomics/CH11.gbk"
gb_records = SeqIO.parse(open(gb_file, "r+"), "genbank")
prefix = 'CH11_'
gene_counter = 1
CDS_counter = 1

for record in gb_records:
    for feature in record.features:
        if feature.type == "gene": 
            feature.qualifiers["locus_tag"] = prefix + str(gene_counter)
            gene_counter = gene_counter + 1
        if feature.type == "CDS": 
            feature.qualifiers["locus_tag"] = prefix + str(CDS_counter)
            CDS_counter = CDS_counter + 1

with open("/home/calle/Storage/Data/methylo_genomes/comparative_genomics/CH11_renamed.gbk","w") as testest:
    SeqIO.write(record, testest, "genbank")