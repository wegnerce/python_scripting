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

list_of_files = glob.glob("/home/calle/Storage/Data/Hainich_MG_final_data/MT/CAZYmes/*_dbcan.out.tophit.annot")
list_of_files.sort()

CAZy_modules = {"3.2.1.4_Cellulase" : [],
            "3.2.1.91_Cellulose 1_4-beta-cellobiosidase" : [],
            "3.2.1.150_Oligoxyloglucan reducing-end-specific cellobiohydrolase" : [],
            "2.4.1.20_Cellobiose phosphorylase" : [],
            "1.1.99.19_Cellobiose dehydrogenase" : [],
            "3.2.1.14_Chitinase" : [],
            "3.5.1.41_Chitin deacetylase" : [],
            "3.5.1.21_N-acetylglucosamine-6-phosphate deacetylase" : [],
            "3.5.1.28_N-acetylmuramoyl-L-alanine amidase" : [],
            "3.5.1.89_N-acetylglucosaminylphosphatidylinositol deacetylase" : [],
            "3.2.1.52_N-acetylglucosaminidase" : [],
            "3.2.1.8_Endo-1_4-beta-xylanase" : [],
            "3.2.1.37_Xylan 1_4-beta xylosidase" : [],
            "3.1.1.72_Acetylxylan esterase" : [],
            "3.2.1.151_Xyloglucanase" : [],
            "4.2.2.10_Pectin lyase" : [],
            "3.1.1.11_Pectinesterase" : [],
            "3.2.1.113_Mannosidase" : [],
            "3.2.1.22_Alpha-galactosidase" : [],
            "3.2.1.23_Beta-galactosidase" : [],
            "3.2.1.51_Alpha-fucosidase" : [],
            "No. of sequences with hits in CAZy" : [],
            "No. of sequences" : []}

CAZy_order = ("3.2.1.4_Cellulase",
            "3.2.1.91_Cellulose 1_4-beta-cellobiosidase",
            "3.2.1.150_Oligoxyloglucan reducing-end-specific cellobiohydrolase",
            "2.4.1.20_Cellobiose phosphorylase",
            "1.1.99.19_Cellobiose dehydrogenase",
            "3.2.1.14_Chitinase",
            "3.5.1.41_Chitin deacetylase",
            "3.5.1.21_N-acetylglucosamine-6-phosphate deacetylase",
            "3.5.1.28_N-acetylmuramoyl-L-alanine amidase",
            "3.5.1.89_N-acetylglucosaminylphosphatidylinositol deacetylase",
            "3.2.1.52_N-acetylglucosaminidase",
            "3.2.1.8_Endo-1_4-beta-xylanase",
            "3.2.1.37_Xylan 1_4-beta xylosidase",
            "3.1.1.72_Acetylxylan esterase",
            "3.2.1.151_Xyloglucanase",
            "4.2.2.10_Pectin lyase",
            "3.1.1.11_Pectinesterase",
            "3.2.1.113_Mannosidase",
            "3.2.1.22_Alpha-galactosidase",
            "3.2.1.23_Beta-galactosidase",
            "3.2.1.51_Alpha-fucosidase",
            "No. of sequences with hits in CAZy",
            "No. of sequences")

processed = [""]

i = 1

for f in list_of_files:
    file_name = os.path.basename(f).split(".")[0]
    processed.append(file_name)
    with open(f, "rb") as infile:
        #f_reader = csv.reader(infile, delimiter = ",")
        for line in infile:
            line = line.replace("1,4", "1_4")
            if line.split(",")[0][0].isdigit() or line.split(",")[0][0] == "N":
                CAZy_modules[line.split(",")[0]].append(line.split(",")[1].replace("\n", ""))

print CAZy_modules

with open("/home/calle/Storage/Data/Hainich_MG_final_data/MT/CAZYmes/CAZyme_summary.txt", "wb") as f_output:
    csv_output = csv.writer(f_output)
    csv_output.writerow(processed)
    for func in CAZy_order:
        csv_output.writerow([func] + CAZy_modules[func])


