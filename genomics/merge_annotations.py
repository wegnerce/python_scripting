# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 14:40:39 2018

@author: calle
"""

import csv
"""
inhmmer = "/media/calle/mistress_ex/_Ca_Methylotracia/AL8_protein_kegg_filtered.tab"
outhmmer = "/media/calle/mistress_ex/_Ca_Methylotracia/AL8_protein_kegg_filtered_unique.tab"

id_score = {}
filtered = []

with open(inhmmer, "rb") as infile:
    for line in infile:
        to_process = line.split("\t")
        if not to_process[0].startswith("t"):
            if not to_process[0] in id_score:
                id_score[to_process[0]] = float(to_process[4])
                filtered.append(to_process)
            elif to_process[0] in id_score:
                if id_score[to_process[0]] > float(to_process[4]):
                    id_score[to_process[0]] = float(to_process[4])
                    filtered = filtered[:-1]
                    filtered.append(to_process)

with open(outhmmer, "wb") as outfile:
    for line in filtered:
        outfile.write("%s" % ("\t".join(line)))
"""

inhmmertab = "/media/calle/mistress_ex/_Ca_Methylotracia/CH11_protein_tigrfam_filtered_unique.tab"
strippedhmmertab = "/media/calle/mistress_ex/_Ca_Methylotracia/CH11_protein_tigrfam_filtered_unique_stripped.tab"

stripped = []
current = []

with open (inhmmertab, "rb") as infile:
    for line in infile:
        current.append(line.split("\t")[0])
        current.append(" ".join([line.split("\t")[2], line.split("\t")[-1].replace("\n", "")]))
        print current
        current = []