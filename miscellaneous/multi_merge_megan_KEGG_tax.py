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

###KEGG
#list_of_files = glob.glob("/home/calle/Desktop/hainich_ongoing/MT/func_annot/*.annot")
###Taxonomy
list_of_files = glob.glob("/media/calle/TOSHIBA EXT/_projects/_Hainich_Omics/02_taxonomic_annotation/diamond_refseq/MG/a_overall/*family.txt")
list_of_files.sort()

func_of_interest = {"Glycolysis / Gluconeogenesis" : [], "Citrate cycle (TCA cycle)" : [],
                    "Pentose phosphate pathway" : [], "Starch and sucrose metabolism" : [],
                    "Amino sugar and nucleotide sugar metabolism" : [],
                    "Oxidative phosphorylation" : [], "Photosynthesis" : [],
                    "Carbon fixation in photosynthetic organisms" : [],
                    "Carbon fixation pathways in prokaryotes" : [],
                    "Methane metabolism" : [], "Nitrogen metabolism" : [],
                    "Sulfur metabolism" : [], "RNA polymerase" : [], "Ribosome" : [],
                    "ABC transporters" : [], "Bacterial secretion system" : [],
                    "Two-component system" : [], "No. of sequences with KEGG mapping" : [],
                    "No. of sequences" : []}

taxa_of_interest = {"Acidobacteria" : [], "Actinobacteria" : [], "Bacteroidetes" : [],
                    "Chloroflexi" : [],"Cyanobacteria" : [], "Elusimicrobia" : [],
                    "Firmicutes" : [], "Gemmatimonadetes" : [], "Nitrospirae" : [],
                    "Planctomycetes" : [], "Proteobacteria" : [], "Verrucomicrobia" : [],
                    "Euryarchaeota" : [], "Thaumarchaeota" : [], "No. of sequences assigned" : [],
                    "No. of sequences" : []}

#func_of_interest = {"K00367_narB" : [], "K00370_narG" : [], "K00371_narH" : [],
#                       "K00374_narI" : [], "K00372_nasA" : [], "K00360_nasB" : [],
#                       "K00368_nirK" : [], "K15864_nirS" : [], "K04561_norB" : [],
#                       "K02305_norC" : [], "K00376_nosZ" : [], "K02586_nifD" : [],
#                       "K02591_nifK" : [], "K02588_nifH" : [], "K10944_pmoA-amoA" : [],
#                       "K10945_pmoB-amoB" : [], "K10946_pmoC-amoC" : [],
#                       "K10535_hao" : [], "K20932_hzsX" : [], "K20933_hzsY" : [],
#                       "K20934_hzsZ" : [], "K20935_hdh" : [], "K00958_sat" : [],
#                       "K00394_aprA" : [], "K00395_aprB" : [], "K11180_dsrA" : [],
#                       "K11181_dsrB" : [], "K13811_PAPSS" : [], "K00955_cysNC" : [],
#                       "K00956_cysN" : [], "K00957_cysD" : [], "K00860_cysC" : [],
#                       "K00390_cysH" : [], "K00380_cysJ" : [], "K00381_cysI" : [],
#                       "K17224_soxB" : [], "K17226_soxY" : [], "K17227_soxZ" : [],
#                       "K17222_soxA" : [], "K17223_soxX" : [], "K17225_soxC" : [],
#                       "K08738_soxD" : [],"K00244_frdA" : [], "K00245_frdB" : [],
#                       "K00246_frdC" : [], "K00247_frdD" : [], "K01648_ACLY" : [],
#                       "K15230_aclA" : [], "K15231_aclB" : [], "K00198_cooS" : [],
#                       "K00196_cooF" : [], "K14138_acsB" : [], "K00197_cdhE" : [],
#                       "K00194_cdhD" : [], "K14469_3hdX" : [], "K15019_3hdY" : [],
#                       "K15020_acdX" : [], "K01601_rbcL" : [], "K01602_rbcS" : [],
#                       "No. of sequences with KEGG mapping" : [], "No. of sequences" : []}

func_checked = {"Glycolysis / Gluconeogenesis" : False, "Citrate cycle (TCA cycle)" : False,
                    "Pentose phosphate pathway" : False, "Starch and sucrose metabolism" : False,
                    "Amino sugar and nucleotide sugar metabolism" : False,
                    "Oxidative phosphorylation" : False, "Photosynthesis" : False,
                    "Carbon fixation in photosynthetic organisms" : False,
                    "Carbon fixation pathways in prokaryotes" : False,
                    "Methane metabolism" : False, "Nitrogen metabolism" : False,
                    "Sulfur metabolism" : False, "RNA polymerase" : False, "Ribosome" : False,
                    "ABC transporters" : False, "Bacterial secretion system" : False,
                    "Two-component system" : False, "No. of sequences with KEGG mapping" : False,
                    "No. of sequences" : False}

taxa_checked = {"Acidobacteria" : False, "Actinobacteria" : False, "Bacteroidetes" : False,
                    "Chloroflexi" : False,"Cyanobacteria" : False, "Elusimicrobia" : False,
                    "Firmicutes" : False, "Gemmatimonadetes" : False, "Nitrospirae" : False,
                    "Planctomycetes" : False, "Proteobacteria" : False, "Verrucomicrobia" : False,
                    "Euryarchaeota" : False, "Thaumarchaeota" : False,
                    "No. of sequences assigned" : False, "No. of sequences" : False}


#func_checked = {"K00367_narB" : False, "K00370_narG" : False, "K00371_narH" : False,
#                       "K00374_narI" : False, "K00372_nasA" : False, "K00360_nasB" : False,
#                       "K00368_nirK" : False, "K15864_nirS" : False, "K04561_norB" : False,
#                       "K02305_norC" : False, "K00376_nosZ" : False, "K02586_nifD" : False,
#                       "K02591_nifK" : False, "K02588_nifH" : False, "K10944_pmoA-amoA" : False,
#                       "K10945_pmoB-amoB" : False, "K10946_pmoC-amoC" : False,
#                       "K10535_hao" : False, "K20932_hzsX" : False, "K20933_hzsY" : False,
#                       "K20934_hzsZ" : False, "K20935_hdh" : False, "K00958_sat" : False,
#                       "K00394_aprA" : False, "K00395_aprB" : False, "K11180_dsrA" : False,
#                      "K11181_dsrB" : False, "K13811_PAPSS" : False, "K00955_cysNC" : False,
#                      "K00956_cysN" : False, "K00957_cysD" : False, "K00860_cysC" : False,
#                       "K00390_cysH" : False, "K00380_cysJ" : False, "K00381_cysI" : False,
#                       "K17224_soxB" : False, "K17226_soxY" : False, "K17227_soxZ" : False,
#                       "K17222_soxA" : False, "K17223_soxX" : False, "K17225_soxC" : False,
#                       "K08738_soxD" : False,"K00244_frdA" : False, "K00245_frdB" : False,
#                       "K00246_frdC" : False, "K00247_frdD" : False, "K01648_ACLY" : False,
#                       "K15230_aclA" : False, "K15231_aclB" : False, "K00198_cooS" : False,
#                       "K00196_cooF" : False, "K14138_acsB" : False, "K00197_cdhE" : False,
#                       "K00194_cdhD" : False, "K14469_3hdX" : False, "K15019_3hdY" : False,
#                       "K15020_acdX" : False, "K01601_rbcL" : False, "K01602_rbcS" : False,
#                       "No. of sequences with KEGG mapping" : False, "No. of sequences" : False}

func_order = ("Glycolysis / Gluconeogenesis", "Citrate cycle (TCA cycle)",
                    "Pentose phosphate pathway", "Starch and sucrose metabolism",
                    "Amino sugar and nucleotide sugar metabolism",
                    "Oxidative phosphorylation", "Photosynthesis",
                    "Carbon fixation pathways in prokaryotes",
                    "Methane metabolism", "Nitrogen metabolism",
                    "Carbon fixation in photosynthetic organisms",
                    "Sulfur metabolism", "RNA polymerase", "Ribosome",
                    "ABC transporters", "Bacterial secretion system",
                    "Two-component system", "No. of sequences with KEGG mapping",
                    "No. of sequences")

taxa_order = ("Acidobacteria", "Actinobacteria", "Bacteroidetes", "Chloroflexi",
            "Cyanobacteria", "Elusimicrobia", "Firmicutes", "Gemmatimonadetes",
            "Nitrospirae", "Planctomycetes", "Proteobacteria", "Verrucomicrobia",
            "Euryarchaeota", "Thaumarchaeota", "No. of sequences assigned", "No. of sequences")


#func_order = ("K00367_narB", "K00370_narG", "K00371_narH",
#                       "K00374_narI", "K00372_nasA", "K00360_nasB",
#                       "K00368_nirK", "K15864_nirS", "K04561_norB",
#                       "K02305_norC", "K00376_nosZ", "K02586_nifD",
#                       "K02591_nifK", "K02588_nifH", "K10944_pmoA-amoA",
#                       "K10945_pmoB-amoB", "K10946_pmoC-amoC",
#                       "K10535_hao", "K20932_hzsX", "K20933_hzsY",
#                       "K20934_hzsZ", "K20935_hdh", "K00958_sat",
#                       "K00394_aprA", "K00395_aprB", "K11180_dsrA",
#                       "K11181_dsrB", "K13811_PAPSS", "K00955_cysNC",
#                       "K00956_cysN", "K00957_cysD", "K00860_cysC",
#                       "K00390_cysH", "K00380_cysJ", "K00381_cysI",
#                       "K17224_soxB", "K17226_soxY", "K17227_soxZ",
#                       "K17222_soxA", "K17223_soxX", "K17225_soxC",
#                       "K08738_soxD","K00244_frdA", "K00245_frdB",
#                       "K00246_frdC", "K00247_frdD", "K01648_ACLY",
#                       "K15230_aclA", "K15231_aclB", "K00198_cooS",
#                       "K00196_cooF", "K14138_acsB", "K00197_cdhE",
#                       "K00194_cdhD", "K14469_3hdX", "K15019_3hdY",
#                       "K15020_acdX", "K01601_rbcL", "K01602_rbcS",
#                       "No. of sequences with KEGG mapping", "No. of sequences")

processed = [""]

i = 1

###KEGG
'''
for f in list_of_files:
    file_name = os.path.basename(f).split(".")[0]
    processed.append(file_name)
    with open(f, "rb") as infile:
        f_reader = csv.reader(infile, delimiter = ",")
        for line in f_reader:
            if line[0] in func_of_interest:
                print line[0]
                func_of_interest[line[0]].append(line[1])

with open("/home/calle/Desktop/hainich_ongoing/MT/func_annot/summary_KEGG_MT.txt", "wb") as f_output:
    csv_output = csv.writer(f_output)
    csv_output.writerow(processed)
    for func in func_order:
        csv_output.writerow([func.replace('"', '')] + func_of_interest[func])
'''
###Taxonomy
for f in list_of_files:
    no_seqs_assigned = 0
    no_of_seqs = 0
    file_name = os.path.basename(f).split(".")[0].split("_")[0]
    processed.append(file_name)
    with open(f, "rb") as infile:
        f_reader = csv.reader(infile, delimiter = "\t")
        for line in f_reader:
            if line:
                if len(line[0].split(";")) > 4:
                    contained = [taxa for taxa in taxa_of_interest.keys() if taxa in
                    line[0].split(";")[3] or taxa in line[0].split(";")[4] if len(line[0].split(";")) > 4]
                    if len(contained) > 0 and taxa_checked[contained[0]] == False:
                        taxa_of_interest[contained[0]].append(line[1])
                        taxa_checked[contained[0]] = True
                if line[0] == "root;":
                    taxa_of_interest["No. of sequences"].append(line[1])
                if line[0] == "root;cellular organisms;Bacteria;" or line[0] == "root;cellular organisms;Archaea;":
                    no_seqs_assigned = no_seqs_assigned + float(line[1])
        taxa_of_interest["No. of sequences assigned"].append(str(no_seqs_assigned))
    for key in taxa_checked:
        taxa_checked[key] = False

with open("/media/calle/TOSHIBA EXT/_projects/_Hainich_Omics/02_taxonomic_annotation/diamond_refseq/MG/a_overall/summary_refseq_MG.txt", "wb") as f_output:
    csv_output = csv.writer(f_output)
    csv_output.writerow(processed)
    for taxa in taxa_order:
        csv_output.writerow([taxa.replace('"', '')] + taxa_of_interest[taxa])

