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

list_of_files = glob.glob("/home/calle/Storage/Data/Hainich_MG_fina_data/MG/*_refseq_SEED.txt")
list_of_files.sort()

func_of_interest = {"Amino Acids and Derivatives" : [], "Carbohydrates" : [],
                    "Cofactors, Vitamins, Prosthetic Groups, Pigments" : [],
                    "Fatty Acids, Lipids, and Isoprenoids" : [], "Nucleosides and Nucleotides" : [],
                    "Membrane Transport" : [], "Motility and Chemotaxis" : [],
                    "Phages, Prophages, Transposable elements" : [], "Stress Response" : [],
                    "Calvin-Benson cycle" : [], "Calvin-Benson-Bassham cycle in plants" : [],
                    "Carboxysome" : [], "Formaldehyde assimilation: Ribulose monophosphate pathway" : [],
                    "Carbon monoxide induced hydrogenase" : [], "fumarate reductase/succinate dehydrogenase flavoprotein, N-terminal:FAD dependent oxidoreductase" : [],
                    "Glycolysis and Gluconeogenesis" : [], "Glycolysis and Gluconeogenesis, including Archaeal enzymes" : [],
                    "Pentose phosphate pathway" : [], "Fermentations in Streptococci" : [], "Fermentations: Lactate" : [],
                    "Fermentations: Mixed acid" : [], "Methanogenesis" : [], "Particulate methane monooxygenase (pMMO)" : [],
                    "Soluble methane monooxygenase (sMMO)" : [], "Ammonia assimilation" : [],
                    "Denitrification" : [], "Dissimilatory nitrite reductase" : [], "Nitrate and nitrite ammonification" : [],
                    "Nitrogen fixation" : [], "CFE Sulfur Oxidation" : [], "Adenylylsulfate reductase" : [],
                    "Dissimilatory sulfite reductase" : [], "Heterodisulfide reductase" : [], "/w hit" : [],
                    "Not assigned" : [], "No hits" : []}

func_checked = {"Amino Acids and Derivatives" : False, "Carbohydrates" : False,
                    "Cofactors, Vitamins, Prosthetic Groups, Pigments" : False,
                    "Fatty Acids, Lipids, and Isoprenoids" : False, "Nucleosides and Nucleotides" : False,
                    "Membrane Transport" : False, "Motility and Chemotaxis" : False,
                    "Phages, Prophages, Transposable elements" : False, "Stress Response" : False,
                    "Calvin-Benson cycle" : False, "Calvin-Benson-Bassham cycle in plants" : False,
                    "Carboxysome" : False, "Formaldehyde assimilation: Ribulose monophosphate pathway" : False,
                    "Carbon monoxide induced hydrogenase" : False, "fumarate reductase/succinate dehydrogenase flavoprotein, N-terminal:FAD dependent oxidoreductase" : False,
                    "Glycolysis and Gluconeogenesis" : False, "Glycolysis and Gluconeogenesis, including Archaeal enzymes" : False,
                    "Pentose phosphate pathway" : False, "Fermentations in Streptococci" : False, "Fermentations: Lactate" : False,
                    "Fermentations: Mixed acid" : False, "Methanogenesis" : False, "Particulate methane monooxygenase (pMMO)" : False,
                    "Soluble methane monooxygenase (sMMO)" : False, "Ammonia assimilation" : False,
                    "Denitrification" : False, "Dissimilatory nitrite reductase" : False, "Nitrate and nitrite ammonification" : False,
                    "Nitrogen fixation" : False, "CFE Sulfur Oxidation" : False, "/w hit" : False, "Not assigned" : False, "No hits" : False}

func_order = ("Amino Acids and Derivatives", "Carbohydrates", "Cofactors, Vitamins, Prosthetic Groups, Pigments",
              "Fatty Acids, Lipids, and Isoprenoids", "Nucleosides and Nucleotides",
              "Membrane Transport", "Motility and Chemotaxis", "Phages, Prophages, Transposable elements",
              "Stress Response", "Calvin-Benson cycle", "Calvin-Benson-Bassham cycle in plants",
              "Carboxysome", "Formaldehyde assimilation: Ribulose monophosphate pathway",
              "Carbon monoxide induced hydrogenase", "fumarate reductase/succinate dehydrogenase flavoprotein, N-terminal:FAD dependent oxidoreductase",
              "Glycolysis and Gluconeogenesis", "Glycolysis and Gluconeogenesis, including Archaeal enzymes",
              "Pentose phosphate pathway", "Fermentations in Streptococci", "Fermentations: Lactate",
              "Fermentations: Mixed acid", "Methanogenesis", "Particulate methane monooxygenase (pMMO)",
              "Soluble methane monooxygenase (sMMO)", "Ammonia assimilation", "Denitrification",
              "Dissimilatory nitrite reductase", "Nitrate and nitrite ammonification",
              "Nitrogen fixation", "CFE Sulfur Oxidation", "Adenylylsulfate reductase", "Dissimilatory sulfite reductase",
              "Heterodisulfide reductase", "/w hit", "Not assigned", "No hits")

to_sum = ("Adenylylsulfate reductase", "Dissimilatory sulfite reductase",
          "Heterodisulfide reductase")

processed = [""]

i = 1

for f in list_of_files:
    file_name = os.path.basename(f).split(".")[0]
    processed.append(file_name)
    with open(f, "rb") as infile:
        f_reader = csv.reader(infile, delimiter = "\t")
        for line in f_reader:
            line[0].replace('"', '')
            if len(line[0].split(";")) == 2:
                func_of_interest["/w hit"].append(line[1].replace(" ", ""))
            for entry in to_sum:
                if any(entry in s for s in line[0].split(";")):
                    if len(func_of_interest[entry]) == 0 or len(func_of_interest[entry]) == i - 1:
                        func_of_interest[entry].append(line[1].replace(" ", ""))
                    else:
                        func_of_interest[entry][-1] = str(float(func_of_interest[entry][-1]) + float(line[1].replace(" ", "")))
            for entry in func_order:
                if any(entry == s for s in line[0].split(";")) and entry not in to_sum:
                    if func_checked[entry] == False:
                        print entry
                        func_of_interest[entry].append(line[1].replace(" ", ""))
                        func_checked[entry] = True
        for key in func_checked:
            func_checked[key] = False
        i = i + 1

with open("/home/calle/Storage/Data/Hainich_MG_fina_data/MG/summary_SEED.txt", "wb") as f_output:
    csv_output = csv.writer(f_output)
    csv_output.writerow(processed)
    for func in func_order:
        csv_output.writerow([func.replace('"', '')] + func_of_interest[func])