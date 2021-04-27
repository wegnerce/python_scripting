# -*- coding: utf-8 -*-
"""
@author:      Carl-Eric Wegner
@affiliation: Küsel Lab - Aquatic Geomicrobiology
              Friedrich Schiller University of Jena

              carl-eric.wegner@uni-jena.de
"""

WD = "/media/calle/mistress_ex/_Ca_Methylotracia/genomes/comparative_genomics/v_final/"
summary_in = WD+"BEIJERINCKIACEAE_vFINAL_SUMMARY/summary.txt"
summary_out = WD+"BEIJERINCKIACEAE_vFINAL_SUMMARY/summary_RH_METH_KEGG.txt"

current_entry = ""
subset = {}
i = 1

with open(summary_in, "rb") as infile, open(summary_out, "wb") as outfile:
    next(infile)
    lines = [line.strip() for line in infile if line.split("\t")[2] == "RH_METH_spec"]
    for line in lines:
        print line
        line = line.split("\t")
        if len(line) > 18:
            if line[18] != "" and line[1] not in subset:
                subset[line[1]] = []
                if len(line[18].split(",")) > 1:
                    to_add = line[18].split(",")
                    to_add = [entry.replace(" ", "") for entry in to_add]
                    for entry in to_add:
                        if entry not in subset[line[1]]:
                            subset[line[1]].append(entry)
                else:
                    if line[18].replace(" ", "") not in subset[line[1]]:
                        subset[line[1]].append(line[18].replace(" ", ""))
            elif line[18] != "" and line[1] in subset:
                if len(line[18].split(",")) > 1:
                    to_add = line[18].split(",")
                    to_add = [entry.replace(" ", "") for entry in to_add]
                    for entry in to_add:
                        if entry not in subset[line[1]]:
                            subset[line[1]].append(entry)
                else:
                    if line[18].replace(" ", "") not in subset[line[1]]:
                        subset[line[1]].append(line[18].replace(" ", ""))
    for key in subset:
        i = 1
        for entry in subset[key]:
            outfile.write("%s\t%s\n" % (key + "_" + str(i), entry))
            i = i + 1
