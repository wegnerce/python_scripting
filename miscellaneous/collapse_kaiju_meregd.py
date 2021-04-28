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

taxa_of_interest = {"Acidobacteria" : [], "Actinobacteria" : [],
                    "Armatimonadetes" : [], "Bacteroidetes" : [],
                    "Candidatus Omnitrophica" : [], "Candidatus Rokubacteria" : [],
                    "Chloroflexi" : [], "Cyanobacteria" : [],
                    "Deinococcus-Thermus" : [], "Elusimicrobia" : [], "FCB Group" : [],
                    "Firmicutes" : [], "Gemmatimonadetes" : [], "Ignavibacteria" : [],
                    "Nitrospinae Group" : [], "Nitrospirae" : [], "Planctomycetes" : [],
                    "PVC Group" : [], "Proteobacteria" : [], "Spirochaetes" : [],
                    "Other candidate phyla" : [], "Parcubacteria" : [],
                    "Microgenomates" : [], "ABY1" : [], "Euryarchaeota" : [],
                    "Thaumarchaeota" : [], "Unclassified" : [],
                    "Not assigned to tax level" : []}

taxa_order = ("Acidobacteria", "Actinobacteria", "Armatimonadetes", "Bacteroidetes",
              "Candidatus Omnitrophica", "Candidatus Rokubacteria", "Chloroflexi",
              "Cyanobacteria", "Deinococcus-Thermus", "Elusimicrobia", "FCB Group",
              "Firmicutes", "Gemmatimonadetes", "Ignavibacteria", "Nitrospinae Group",
              "Nitrospirae", "Planctomycetes", "PVC Group", "Proteobacteria",
              "Spirochaetes", "Other candidate phyla", "Parcubacteria", "Microgenomates",
              "ABY1", "Euryarchaeota", "Thaumarchaeota", "Unclassified", "Not assigned to tax level")

datasets = ["H3-2-1", "H3-2-2", "H3-2-3", "H4-1-1", "H4-1-2", "H4-1-3", "H4-2-1",
            "H4-2-2", "H4-2-3", "H4-3-1", "H4-3-2", "H4-3-3", "H5-1-1", "H5-1-2",
            "H5-1-3", "H5-2-1", "H5-2-2", "H5-2-3"]

with open("/home/calle/Dropbox/hainich_ongoing_v2/MG/CAZymes/for_fig6/all_substrates.out", "rb") as
f_input:
    csv_input =

with open("/home/calle/Dropbox/hainich_ongoing_v2/MG/CAZymes/for_fig6/all_substrates.out", "wb") as f_output:
    csv_output = csv.writer(f_output)
    csv_output.writerow(processed)
    for taxa in taxa_order:
        csv_output.writerow([taxa] + taxa_of_interest[taxa])


