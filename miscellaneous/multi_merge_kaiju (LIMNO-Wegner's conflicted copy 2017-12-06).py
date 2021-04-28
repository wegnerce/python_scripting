# -*- coding: utf-8 -*-

'''
Created on October 9, 2012
@author: Carl-Eric Wegner - AG Liesack - Molecular Ecology - MPI Marburg
The given script renames all files of a specified file type in a given folder,
giving every file a number specified in variable rename_index_number.
'''

import glob
import re
import os

kaiju_out = "/home/cewegner/rocks_kaiju_summary_phylum_002.txt"

taxa_of_interest = {"Acidobacteria" : [], "Actinobacteria" : [], "Apicomplexa" : [],
                    "Armatimonadates" : [], "Bacteroidetes" : [], "Chloroflexi" : [],
                    "Firmicutes" : [], "Candidatus Rokubacteria" : [], "Planctomycetes" : [],
                    "Proteobacteria" : [], "Viruses" : []}

taxa_order = ("Acidobacteria", "Actinobacteria", "Apicomplexa",
                "Armatimonadates", "Bacteroidetes", "Chloroflexi",
                "Firmicutes", "Candidatus Rokubacteria", "Planctomycetes",
                "Proteobacteria", "Viruses")

processed = []                
i = 0
with open(kaiju_out, "rb") as infile:
    for line in infile:
        next(infile)
        print line
        #print line.split("\t")[4].replace("\n", "")
        if not line.split(",")[0] in processed:
            for taxon in taxa_of_interest:
                taxa_of_interest[taxon].append("0")
            if line.split(",")[4].replace("\n", "") in taxa_of_interest:
                taxa_of_interest[line.split(",")[4].replace("\n", "")][len(taxa_of_interest[line.split(",")[4].replace("\n", "")])-1] = line.split(",")[1]
        if line.split(",")[0] in processed:
            if line.split(",")[4].replace("\n", "") in taxa_of_interest:
                taxa_of_interest[line.split(",")[4].replace("\n", "")][len(taxa_of_interest[line.split(",")[4].replace("\n", "")])-1] = line.split(",")[1]
        processed.append(line.split(",")[0])                    

print taxa_of_interest                    

'''
with open("/home/calle/Storage/Data/Hainich_MG_fina_data/MT_kaiju_taxonomy.txt", "wb") as f_output:
    csv_output = csv.writer(f_output)
    csv_output.writerow(processed)
    for taxa in taxa_order:
        csv_output.writerow([taxa] + taxa_of_interest[taxa])
'''

