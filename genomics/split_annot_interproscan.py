# -*- coding: utf-8 -*-
"""
@author:      Carl-Eric Wegner
@affiliation: Küsel Lab - Aquatic Geomicrobiology
              Friedrich Schiller University of Jena

              carl-eric.wegner@uni-jena.de
"""
# needed modules/packages

# declare necessary filepaths/variables
annot_in = ("/home/cewegner/Downloads/user_ko.txt")
genome_tags = []


# read annotation input, iterate over lines, split based on genome tag
with open(annot_in, "r") as infile:
    for line in infile:
        print (line)
        if line.split("\t")[0][:line.split("\t")[0].rfind("_")]not in genome_tags:
            outfile = open("/home/cewegner/Downloads/%s_KEGG_annot.txt"
                           % line.split("\t")[0][:line.split("\t")[0].rfind("_")], "w")
            genome_tags.append(line.split("\t")[0][:line.split("\t")[0].rfind("_")])
        outfile.write(line.replace(line.split("\t")[0], line.split("\t")[0].split("_")[-1]))
