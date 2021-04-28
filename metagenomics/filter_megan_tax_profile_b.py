# -*- coding: utf-8 -*-
"""
@author:      Carl-Eric Wegner
@affiliation: Küsel Lab - Aquatic Geomicrobiology
              Friedrich Schiller University of Jena

              carl-eric.wegner@uni-jena.de
"""

# needed packages
import csv
import sys

# paths, variables
#megan_in = "/home/calle/Desktop/to_strip_megan_taxonomy/PNK69-H5-2-2_refseq_family.txt"
#megan_out = "/home/calle/Desktop/to_strip_megan_taxonomy/PNK69-H5-2-2_refseq_family_stripped_b.txt"
megan_in = sys.argv[1]
megan_out = sys.argv[2]
to_keep = []
final = []

of_interest = ["Solibacterales","Flavobacteriia", "Chitinophagia", "Gemmatimonadales",
               "Nitrospiraceae", "Caulobacterales", "Rhizobiales", "Rhodospirillales",
               "Sphingomonadales", "Burkholderiales", "Comamonadales",
               "Nitrosomonadaceae", "Thiobacillaceae", "Bdellovibrionales",
               "Desulfarculales", "Desulfobacterales", "Desulfovibrionales",
               "Desulfurellales", "Desulfuromonadales", "Myxococcales",
               "Syntrophobacterales", "Acidiferrobacteraceae", "Shewanellaceae",
               "Thiotrichaceae", "Xanthomonadaceae", "Planctomycetales",
               "Candidatus Brocadiales", "Anaerolineales", "Dehalococcoidia",
               "Peptococcaceae", "Veillonellales", "Nitrosopumilaceae"]

'''
of_interest = ["Alteromonadales", "Desulfobacteriales", "Desulfarculales",
               "Desulfovibrionales", "Desulfurellales", "Desulfuromonadales",
               "Myxococalles", "Peptococcaceae", "Acetobacteraceae", "Veillonellaceae",
               "Syntrophobacterales", "Thiobacillaceae", "Thiotrichaceae",
               "Acidiferrobacteraceae"]
'''

of_interest_checked = {"Solibacterales" : False,"Flavobacteriia" : False,
    "Chitinophagia" : False, "Gemmatimonadales" : False, "Nitrospiraceae" : False,
    "Caulobacterales" : False, "Rhizobiales" : False, "Rhodospirillales" : False,
    "Sphingomonadales" : False, "Burkholderiales" : False, "Comamonadales" : False,
    "Nitrosomonadaceae" : False, "Thiobacillaceae" : False, "Bdellovibrionales" : False,
    "Desulfarculales" : False, "Desulfobacterales" : False, "Desulfovibrionales" : False,
    "Desulfurellales" : False, "Desulfuromonadales" : False, "Myxococcales" : False,
    "Syntrophobacterales" : False, "Acidiferrobacteraceae" : False,
    "Shewanellaceae" : False, "Thiotrichaceae" : False, "Xanthomonadaceae" : False,
    "Planctomycetales" : False, "Candidatus Brocadiales" : False,
    "Anaerolineales" : False, "Dehalococcoidia" : False, "Peptococcaceae" : False,
    "Veillonellales" : False, "Nitrosopumilaceae" : False}

'''
of_interest_checked = {"Alteromonadales":False, "Desulfobacteriales":False,
                       "Desulfarculales":False, "Desulfovibrionales":False,
                       "Desulfurellales":False, "Desulfuromonadales":False,
                       "Myxococalles":False, "Peptococcaceae":False,
                       "Acetobacteraceae":False, "Veillonellaceae":False,
               "Syntrophobacterales":False, "Thiobacillaceae":False, "Thiotrichaceae":False,
               "Acidiferrobacteraceae":False}
'''

assigned = 0

# actual magic
with open(megan_in, "rb") as infile:
    megan_reader = csv.reader(infile, delimiter ="\t")
    for line in megan_reader:
        if line:
            for taxa in of_interest:
                if taxa in line[0] and of_interest_checked[taxa] == False:
                    to_keep.append(line)
                    of_interest_checked[taxa] = True

with open(megan_out, "wb") as outfile:
    megan_writer = csv.writer(outfile, delimiter ="\t")
    for line in to_keep:
       megan_writer.writerow(line)