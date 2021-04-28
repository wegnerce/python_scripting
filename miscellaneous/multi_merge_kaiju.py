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

list_of_files = glob.glob("/home/calle/Dropbox/hainich_ongoing_v2/MG/CAZymes/for_fig6/*_kaiju.summary")
list_of_files.sort()

#taxa_of_interest = {"Proteobacteria" : [], "Candidatus Omnitrophica" : [], "Actinobacteria" : [],
#                    "Bacteroidetes" : [], "Planctomycetes" : [], "Acidobacteria" : [],
#                    "Nitrospirae" : [], "Firmicutes" : [], "Gemmatimonadetes" : [],
#                    "Verrucomicrobia" : [], "Chloroflexi" : [], "Cyanoabacteria" : [],
#                    "Euryarchaeota" : [], "Elusimicrobia" : [], "Ignaviabcteria" : [],
#                    "Candidatus Rokubacteria" : [], "Candidatus Giovanonnibacteria" : [],
#                    "Candidatus Yonathbacteria" : [], "Fibrobacteres" : [],
#                    "Candidatus Magasanikbacteria" : [], "Candidatus Buchananbacteria" : [],
#                    "Candidatus Handelsmanbacteria" : [], "Candidatus Kryptonia" : [],
#                    "Lentisphaerae" : [], "Classified" : []}

#taxa_of_interest = {"Firmicutes" : [], "Proteobacteria" : [], "Actinobacteria" : [],
#                    "Bacteroidetes" : [], "Acidobacteria" : [], "Chloroflexi" : [],
#                    "Deinococcus-Thermus" : [], "Armatimonadetes" : [], "Planctomycetes" : [],
#                    "Verrucomicrobia" : [], "Thermotogae" : [], "Lentisphaerae" : [],
#                    "Classified" : [], "Not assigned to tax level" : []}

#taxa_of_interest = {"Acidobacteria" : [], "Actinobacteria" : [], "Aquificiae" : [],
#                    "Bacteroidetes" : [], "Chlorobi" : [], "Chloroflexi" : [],
#                    "Cyanobacteria" : [], "Elusimicrobia" : [], "Firmicutes" : [],
#                    "Gemmatimonadetes" : [], "Lentisphaerae" : [], "Nitrospinae" : [],
#                    "Nitrospirae" : [], "Planctomycetes" : [], "Proteobacteria" : [],
#                    "Spirochaetes" : [], "Verrucomicrobia" : [], "Candidatus Desantisbacteria" : [],
#                    "Candidatus Firestonebacteria" : [], "Candidatus Gottesmanbacteria" : [],
#                    "Candidatus Kaiserbacteria" : [], "Candidatus Levybacteria" : [],
#                    "Candidatus Magasanikbacteria" : [], "Candidatus Nomurabacteria" : [],
#                    "Candidatus Omnitrophica" : [], "Candidatus Riflebacteria" : [],
#                    "Candidatus Rokubacteria" : [], "Euryarchaeota" : [],
#                    "Thaumarchaeota" : [], "Candidatus Bathyarchaeota" : [],
#                    "Classified" : [], "Not assigned to tax level" : []}

ABY1 = ("Candidatus Buchananbacteria", "Candidatus Falkowbacteria", "Candidatus Magasanikbacteria",
       "Candidatus Uhrbacteria")

Microgenomates = ("Candidatus Daviesbacteria", "Candidatus Gottesmanbacteria",
                  "Candidatus Levybacteria", "Candidatus Woesebacteria",
                  "Candidatus Roizmanbacteria")

Parcubacteria = ("Candidatus Azambacteria", "Candidatus Campbellbacteria",
                 "Candidatus Doudnabacteria", "Candidatus Giovannonibacteria",
                 "Candidatus Harrisonbacteria", "Candidatus Jorgensenbacteria",
                 "Candidatus Kaiserbacteria", "Candidatus Moranbacteria",
                 "Candidatus Nomurabacteria", "Candidatus Ryanbacteria",
                 "Candidatus Staskawiczbacteria", "Candidatus Sungbacteria",
                 "Candidatus Taylorbacteria", "Candidatus Yanofskybacteria",
                 "Candidatus Zambryskibacteria")

OC_phyla = ("Candidatus Aminicenantes", "Candidatus Eisenbacteria", "Candidatus Handelsmanbacteria",
            "Candidatus Lindowbacteria", "Candidatus Peregrinibacteria",
            "Candidatus Raymondbacteria", "Candidatus Schekmanbacteria",
            "candidate division NC10")

TN_group = ("Candidatus Tectomicrobia", "Nitrospinae")

FCB_group = ("Gemmatimonadetes", "candidate division Zixibacteria", "Chlorobi",
             "Candidatus Kryptonia", "Candidatus Cloacimonetes", "Latescibacteria")

PVC_group = ("Verrucomicrobia", "Chlamydiae", "Lentisphaerae")

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

#taxa_of_interest = {"Nitrospiraceae" : [], "Nitrosomonadaceae" : [], "Candidatus Brocadiaceae" : [],
#                    "Planctomycetaceae" : [], "Comamonadaceae" : [], "Nitrosopumilaceae" : [],
#                    "Classified" : [], "Not assigned to tax level" : []}

#taxa_of_interest = {"Proteobacteria" : [], "Nitrospirae" : [], "Candidatus Omnitrophica" : [],
#                    "Actinobacteria" : [], "Planctomycetes" : [], "Firmicutes" : [],
#                    "Bacteroidetes" : [], "Acidobacteria" : [], "Chloroflexi" : [],
#                    "Candidatus Rokubacteria" : [], "Verrucomicrobia" : [], "Elusimicrobia" : [],
#                    "Cyanobacteria" : [], "Euryarchaeota" : [], "Nitrospinae" : [],
#                    "Gemmatimonadetes" : [], "Candidatus Nomurabacteria" : [],
#                    "Candidatus Uhrbacteria" : [], "Candidatus Magasanikbacteria" : [],
#                    "Ignavibacteriae" : [], "Thaumarchaeota" : [],
#                    "Candidatus Levybacteria" : [], "Candidatus Yanofskybacteria" : [],
#                    "Candidatus Sungbacteria" : [], "candidate division NC10" : [],
#                    "Candidatus Gottesmanbacteria" : [], "Candidatus Moranbacteria" : [],
#                    "Armatimonadetes" : [], "Spirochaetes" : [], "Candidatus Wolfebacteria" : [],
#                    "Candidatus Taylorbacteria" : [], "Candidatus Roizmanbacteria" : [],
#                    "Candidatus Giovannonibacteria" : [], "Candidatus Tectomicrobia" : [],
#                    "Candidatus Daviesbacteria" : [], "Lentisphaerae":[],
#                    "Candidatus Woesebacteria" : [], "Classified" : []}
#taxa_of_interest = {"Bacillaceae" : [], "Paenibacillaceae" : [], "Clostridiaceae" : [],
#                    "Lachnospiraceae" : [], "Ruminococcaceae" : [], "Sporomusaceae" : [],
#                    "Thermoanaerobacteraceae" : [], "Actinomycetaceae" : [], "Streptomycetaceae" : [],
#                    "Enterobacteriaceae" : [], "Peptococcaceae" : [], "Symbiobacteriaceae" : [],
#                    "Solibacteriaceae" : [], "Planctomycetaceae" : [], "Methanosarcinaceae" : [],
#                    "Methanocellaceae" : [], "Methanoregulaceae" : [],
#                    "Methanobacteriaceae" : [], "Classified" : [], "Not assigned to tax level" : []}

#taxa_of_interest = {"Firmicutes" : [], "Proteobacteria" : [], "Actinobacteria" : [],
#                    "Bacteoroidetes" : [], "Acidobacteria" : [], "Chloroflexi" : [],
#                    "Deinococcus-Thermus" : [], "Armatimonadetes" : [], "Planctomycetes" : [],
#                    "Verrucomicrobia" : [], "Thermotogae" : [], "Lentisphaerae" : [],
#                    "Classified" : []}

#taxa_order = ("Firmicutes", "Proteobacteria", "Actinobacteria", "Bacteroidetes",
#              "Acidobacteria", "Chloroflexi", "Deinococcus-Thermus", "Armatimonadetes",
#              "Planctomycetes", "Verrucomicrobia", "Thermotogae", "Lentisphaerae",
#              "Classified", "Not assigned to tax level")

#taxa_order = ("Acidobacteria", "Actinobacteria", "Aquificiae",
#              "Bacteroidetes", "Chlorobi", "Chloroflexi",
#              "Cyanobacteria", "Elusimicrobia", "Firmicutes",
#              "Gemmatimonadetes", "Lentisphaerae", "Nitrospinae",
#              "Nitrospirae", "Planctomycetes", "Proteobacteria",
#              "Spirochaetes", "Verrucomicrobia", "Candidatus Desantisbacteria",
#              "Candidatus Firestonebacteria", "Candidatus Gottesmanbacteria",
#              "Candidatus Kaiserbacteria", "Candidatus Levybacteria",
#              "Candidatus Magasanikbacteria", "Candidatus Nomurabacteria",
#              "Candidatus Omnitrophica", "Candidatus Riflebacteria",
#              "Candidatus Rokubacteria", "Euryarchaeota",
#              "Thaumarchaeota", "Candidatus Bathyarchaeota",
#              "Classified", "Not assigned to tax level")

#taxa_order = ("Nitrospiraceae", "Nitrosomonadaceae", "Candidatus Brocadiaceae",
#                    "Planctomycetaceae", "Comamonadaceae", "Nitrosopumilaceae",
#                    "Classified", "Not assigned to tax level")

taxa_order = ("Acidobacteria", "Actinobacteria", "Armatimonadetes", "Bacteroidetes",
              "Candidatus Omnitrophica", "Candidatus Rokubacteria", "Chloroflexi",
              "Cyanobacteria", "Deinococcus-Thermus", "Elusimicrobia", "FCB Group",
              "Firmicutes", "Gemmatimonadetes", "Ignavibacteria", "Nitrospinae Group",
              "Nitrospirae", "Planctomycetes", "PVC Group", "Proteobacteria",
              "Spirochaetes", "Other candidate phyla", "Parcubacteria", "Microgenomates",
              "ABY1", "Euryarchaeota", "Thaumarchaeota", "Unclassified", "Not assigned to tax level")

#taxa_order = ("Proteobacteria", "Candidatus Omnitrophica", "Actinobacteria",
#                    "Bacteroidetes", "Planctomycetes", "Acidobacteria",
#                    "Nitrospirae", "Firmicutes", "Gemmatimonadetes", "Verrucomicrobia",
#                    "Chloroflexi", "Cyanoabacteria", "Euryarchaeota", "Elusimicrobia",
#                    "Ignaviabcteria", "Candidatus Rokubacteria", "Candidatus Giovanonnibacteria",
#                    "Candidatus Yonathbacteria", "Fibrobacteres", "Candidatus Magasanikbacteria",
#                    "Candidatus Buchananbacteria", "Candidatus Handelsmanbacteria",
#                    "Candidatus Kryptonia", "Lentisphaerae", "Classified")

#taxa_order = ("Proteobacteria", "Nitrospirae", "Candidatus Omnitrophica",
#              "Actinobacteria", "Planctomycetes", "Firmicutes",
#              "Bacteroidetes", "Acidobacteria", "Chloroflexi",
#              "Candidatus Rokubacteria", "Verrucomicrobia", "Elusimicrobia",
#              "Cyanobacteria", "Euryarchaeota", "Nitrospinae",
#              "Gemmatimonadetes", "Candidatus Nomurabacteria",
#              "Candidatus Uhrbacteria", "Candidatus Magasanikbacteria",
#              "Ignavibacteriae", "Thaumarchaeota",
#              "Candidatus Levybacteria", "Candidatus Yanofskybacteria",
#              "Candidatus Sungbacteria", "candidate division NC10",
#              "Candidatus Gottesmanbacteria", "Candidatus Moranbacteria",
#              "Armatimonadetes", "Spirochaetes", "Candidatus Wolfebacteria",
#              "Candidatus Taylorbacteria", "Candidatus Roizmanbacteria",
#              "Candidatus Giovannonibacteria", "Candidatus Tectomicrobia",
#             "Candidatus Daviesbacteria", "Lentisphaerae",
#             "Candidatus Woesebacteria", "Classified")

#taxa_order = ("Bacillaceae", "Paenibacillaceae", "Clostridiaceae", "Lachnospiraceae",
#              "Ruminococcaceae", "Sporomusaceae", "Thermoanaerobacteraceae", "Actinomycetaceae",
#              "Streptomycetaceae", "Enterobacteriaceae", "Peptococcaceae", "Symbiobacteriaceae",
#              "Solibacteriaceae", "Planctomycetaceae", "Methanosarcinaceae",
#              "Methanocellaceae", "Methanoregulaceae", "Methanobacteriaceae", "Classified", "Not assigned to tax level")

#taxa_order = ("Firmicutes", "Proteobacteria", "Actinobacteria", "Bacteoroidetes",
#              "Acidobacteria", "Chloroflexi", "Deinococcus-Thermus", "Armatimonadetes",
#              "Planctomycetes", "Verrucomicrobia", "Thermotogae", "Lentisphaerae",
#              "Classified")

processed = [""]

i = 1

for f in list_of_files:
    file_name = os.path.basename(f).split(".")[0]
    processed.append(file_name)
    with open(f, "rb") as infile:
        f_reader = csv.reader(infile, delimiter = "\t")
        next(f_reader, None)
        for line in f_reader:
            #for entry in line:
            #    entry.replace(" ", "")
            if not line[0].startswith("-"):
                if line[2] in taxa_order or \
                line[2] == "unclassified" or line[2].startswith("cannot"):
                    if line[2] != "unclassified" and not line[2].startswith("cannot"):
                        print line[2]
                        if line[2] in ABY1:
                            taxa_of_interest["ABY1"].append(line[1].replace(" ", ""))
                        if line[2] in Microgenomates:
                            taxa_of_interest["Microgenomates"].append(line[1].replace(" ", ""))
                        if line[2] in Parcubacteria:
                            taxa_of_interest["Parcubacteria"].append(line[1].replace(" ", ""))
                        if line[2] in OC_phyla:
                            taxa_of_interest["Other candidate phyla"].append(line[1].replace(" ", ""))
                        if line[2] in TN_group:
                            taxa_of_interest["Nitrospinae Group"].append(line[1].replace(" ", ""))
                        if line[2] in FCB_group:
                            taxa_of_interest["FCB Group"].append(line[1].replace(" ", ""))
                        if line[2] in PVC_group:
                            taxa_of_interest["PVC Group"].append(line[1].replace(" ", ""))
                        if line[2] in taxa_order:
                            taxa_of_interest[line[2]].append(line[1].replace(" ", ""))
#                    elif line[2] == "unclassified":
#                        taxa_of_interest["Classified"].append(str(100-float(line[0].replace(" ", ""))))
                    elif line[2] == "unclassified":
                        taxa_of_interest["Unclassified"].append(float(line[1].replace(" ", "")))
                    elif line[2].startswith("cannot"):
                        taxa_of_interest["Not assigned to tax level"].append(line[1].replace(" ", ""))
        for taxon in taxa_of_interest:
            if len(taxa_of_interest[taxon]) < i:
                taxa_of_interest[taxon].append("0")
    i = i + 1

with open("/home/calle/Dropbox/hainich_ongoing_v2/MG/CAZymes/for_fig6/all_substrates.summary", "wb") as f_output:
    csv_output = csv.writer(f_output)
    csv_output.writerow(processed)
    for taxa in taxa_order:
        csv_output.writerow([taxa] + taxa_of_interest[taxa])


