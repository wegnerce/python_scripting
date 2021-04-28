'''
Created on October 9, 2012
@author: Carl-Eric Wegner - AG Liesack - Molecular Ecology - MPI Marburg
The given script renames all files of a specified file type in a given folder,
giving every file a number specified in variable rename_index_number.
'''

import glob
import re
import os
import csv

list_of_files = glob.glob("/home/calle/Desktop/to_strip_megan_taxonomy/*_stripped_b.txt")
list_of_files.sort()

taxa_of_interest = {"Solibacterales" : [],"Flavobacteriia" : [],
    "Chitinophagia" : [], "Gemmatimonadales" : [], "Nitrospiraceae" : [],
    "Caulobacterales" : [], "Rhizobiales" : [], "Rhodospirillales" : [],
    "Sphingomonadales" : [], "Burkholderiales" : [],
    "Nitrosomonadaceae" : [], "Thiobacillaceae" : [], "Bdellovibrionales" : [],
    "Desulfarculales" : [], "Desulfobacterales" : [], "Desulfovibrionales" : [],
    "Desulfurellales" : [], "Desulfuromonadales" : [], "Myxococcales" : [],
    "Syntrophobacterales" : [], "Acidiferrobacteraceae" : [],
    "Shewanellaceae" : [], "Thiotrichaceae" : [], "Xanthomonadaceae" : [],
    "Planctomycetales" : [], "Candidatus Brocadiales" : [],
    "Anaerolineales" : [], "Dehalococcoidia" : [], "Peptococcaceae" : [],
    "Veillonellales" : [], "Nitrosopumilaceae" : []}

taxa_order = ["Solibacterales","Flavobacteriia", "Chitinophagia", "Gemmatimonadales",
               "Nitrospiraceae", "Caulobacterales", "Rhizobiales", "Rhodospirillales",
               "Sphingomonadales", "Burkholderiales",
               "Nitrosomonadaceae", "Thiobacillaceae", "Bdellovibrionales",
               "Desulfarculales", "Desulfobacterales", "Desulfovibrionales",
               "Desulfurellales", "Desulfuromonadales", "Myxococcales",
               "Syntrophobacterales", "Acidiferrobacteraceae", "Shewanellaceae",
               "Thiotrichaceae", "Xanthomonadaceae", "Planctomycetales",
               "Candidatus Brocadiales", "Anaerolineales", "Dehalococcoidia",
               "Peptococcaceae", "Veillonellales", "Nitrosopumilaceae"]

processed = [""]

i = 1

for f in list_of_files:
    file_name = os.path.basename(f).split(".")[0].split("_")[0]
    processed.append(file_name)
    with open(f, "rb") as infile:
        f_reader = csv.reader(infile, delimiter = "\t")
        for line in f_reader:
            for key in taxa_of_interest.keys():
                if key in line[0]:
                    taxa_of_interest[key].append(line[1])
        for taxon in taxa_of_interest:
            if len(taxa_of_interest[taxon]) < i:
                taxa_of_interest[taxon].append("0")
    i = i + 1

with open("/home/calle/Desktop/to_strip_megan_taxonomy/taxonomy_megan_resolved_summary.txt", "wb") as f_output:
    csv_output = csv.writer(f_output)
    csv_output.writerow(processed)
    for taxa in taxa_order:
        csv_output.writerow([taxa] + taxa_of_interest[taxa])


