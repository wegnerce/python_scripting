# -*- coding: utf-8 -*-
"""
@author:      Carl-Eric Wegner
@affiliation: Küsel Lab - Aquatic Geomicrobiology
              Friedrich Schiller University of Jena

              carl-eric.wegner@uni-jena.de
"""

# needed mopdules/packages
import sys
import matplotlib
matplotlib.use('Qt4Agg')
import matplotlib.pyplot as plt

# declare necessary filepaths/variables
# diamond_out = sys.argv[1]
# qs_ratios = sys.argv[2]
# ratios = {}
diamond_out = "/media/calle/mistress_ex/_Ca_Methylotracia/genomes/RH_Beijerinckiaceae_bacteria_revisions/Beijerinckiaceae_bacterium_RHAL1_chromosome_indel_corrected_proteins_AL8_diamond.out"
qs_ratios = "/media/calle/mistress_ex/_Ca_Methylotracia/genomes/RH_Beijerinckiaceae_bacteria_revisions/indels_Beijerinckiaceae_bacterium_RHAL1_chromosome_indel_corrected_proteins_AL8_diamond.out"
ratios = {}

# process tabular (outfmt 6) diamond output
with open(diamond_out, "rb") as infile:
    lines = (line.rstrip() for line in infile)
    lines = (line for line in lines if line)
    for line in lines:
        if not line.split("\t")[0] in ratios:
            #ratios[line.split("\t")[0]] = (float(line.split("\t")[7])-float(line.split("\t")[6]))/\
            #    (float(line.split("\t")[9])-float(line.split("\t")[8]))
            ratios[line.split("\t")[0]] = float(line.split("\t")[1])/float(line.split("\t")[3])

# plot distribution of length ratios as histogram
f = plt.figure()
plt.hist(ratios.values(), 200, color="g")
plt.ylim((0, 2500))
plt.xlim((0, 2))
f.savefig(qs_ratios + ".pdf", bbox_inches="tight")

f = plt.figure()
plt.hist(ratios.values(), 200, color="g")
plt.ylim((0, 500))
plt.xlim((0, 2))
f.savefig(qs_ratios + "_zoomed.pdf", bbox_inches="tight")

with open(qs_ratios, "wb") as outfile:
    for k, v in ratios.items():
        outfile.write(str(k) + '\t' + str(v) + '\n')
