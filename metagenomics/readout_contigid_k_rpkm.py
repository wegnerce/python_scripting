# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 09:55:50 2016

@author: calle
"""

# Load required modules
from collections import defaultdict
import csv
import argparse

# Information about argument parsing
parser = argparse.ArgumentParser(description = "Hierarchical KEGG category annotation for metagenome contigs")
parser.add_argument("--megan", "-m", help="'MEGAN KEGG annotation output (contigid K-Number)", action="store")
parser.add_argument("--rpkm", "-r", help="path to a bbmpap output file containing rpkm information", action="store")    
args = parser.parse_args()

# Necessary dictionaries for calculating the relative transcript abundance
k_ids = defaultdict(list)
knumber_rpkm = {}
rpkm_stats = {}

# Path to the KEGG Orthology information file
kegg_orthology = "/home/calle/pCloud Sync/Python/metagenomics/kegg_orthology.txt"

# Necessary dictionaries, variables for the annotation process
knumber_annot = defaultdict(list)
kegg_lvl2_order = ("Carbohydrate metabolism", "Energy metabolism", "Lipid metabolism", \
    "Nucleotide metabolism", "Amino acid metabolism", "Metabolism of other amino acids", \
    "Glycan biosynthesis and metabolism", "Metabolism of cofactors and vitamins", \
    "Metabolism of terpenoids and polyketides", "Biosynthesis of other secondary metabolites", \
    "Xenobiotics biodegradation and metabolism", "Enzyme families", "Transcription", "Translation", \
    "Folding, sorting and degradation", "Replication and repair", "RNA family", "Membrane transport", \
    "Signal transduction", "Signaling molecules and interaction", "Transport and catabolism", \
    "Cell motility", "Cell growth and death", "Cellular commiunity")
kegg_lvl2_list = []
kegg_lvl2 = {}
tax4fun_kegg_lvl2 = defaultdict(list)
kegg_lvl3_order = ("Carbon metabolism", "Biosynthesis of amino acids", "Degradation of aromatic compounds", \
    "Glycolysis / Gluconeogenesis", "Citrate cycle (TCA cycle)", "Pentose phosphate pathway", \
    "Starch and sucrose metabolism", "Amino sugar and nucleotide sugar metabolism", \
    "Glyoxylate and dicarboxylate metabolism", "Oxidative phosphorylation", \
    "Carbon fixation pathways in prokaryotes", "Methane metabolism", "Nitrogen metabolism", "Sulfur metabolism", \
    "Fatty acid biosynthesis", "Glycerophospholipid metabolism", "Selenocompound metabolism", \
    "Glutathione metabolism", "Glycosaminoglycan degradation", \
    "Lipopolysaccharide biosynthesis", "Peptidoglycan biosynthesis", "Other glycan degradation", \
    "Biosynthesis of siderophore group nonribosomal peptides", "Benzoate degradation", \
    "Aminobenzoate degradation", "Fluorobenzoate degradation", "Chloroalkane and chloroalkene degradation", \
    "Chlorocyclohexane and chlorobenzene degradation", "Toluene degradation", "Xylene degradation", \
    "Nitrotoluene degradation", "Styrene degradation", "Bisphenol degradation", "Naphthalene degradation", \
    "ABC transporters", "Phosphotransferase system (PTS)", \
    "Bacterial secretion system", "Two-component system", "Bacterial chemotaxis", "Flagellar assembly")
ch_metabolism = ("Glycolysis / Gluconeogenesis", "Citrate cycle (TCA cycle)", "Pentose phosphate pathway", \
    "Pentose and glucuronate interconversions", "Fructose and mannose metabolism", "Galactose metabolism", \
    "Ascorbate and aldarate metabolism", "Starch and sucrose metabolism", "Amino sugar and nucleotide metabolism", \
    "Pyruvate metabolism", "Glyoxylate and dicarboxylate metabolism", "Propanoate metabolism", \
    "Butanoate metabolism", "C5-Branched dibasic and acid metabolism", "Inositol phosphate metabolism")
energy_metabolism = ("Oxidative phosphorylation", "Photosynthesis", "Carbon fixation in photosynthetic organisms", \
    "Carbon fixation pathways in prokaryotes", "Methane metabolism", "Nitrogen metabolism", "Sulfur metabolism")
translation = ("Ribosome", "Aminoacyl-tRNA biosynthesis", "RNA transport", "mRNA surveillance pathway", \
    "Messenger RNA biosynthesis", "Ribosome biogenesis", "Translation factors")
folding = ("Chaperones and folding catalysts", "Protein export", "Sulfur relay system", "Proteasome", \
    "RNA degradation")
repl_repair = ("DNA replication", "Base excision repair", "Nucleotide excision repair", "Mismatch repair", \
    "Homologous recombination", "DNA repair and recombination proteins")
transport = ("Transporter", "ABC transporter", "Phosphotransferase system(PTS)", "Bacterial secretion system", \
    "Secretion system")
signal_transduction = ("Two-component system")
kegg_lvl3 = {}
kegg_lvl4 = {}

# Read KEGG Orthology into a hierarchical  dictionary
def generate_kegg_orthology():
    global knumber_annot
    with open(kegg_orthology, "rb") as infile:
        for line in infile:
            if line.startswith("A"):
                to_search = line[4:]
                current_kegglvl1 = to_search[:to_search.find("<")]
            elif line.startswith("B"):
                to_search = line[6:]
                current_kegglvl2 = to_search[:to_search.find("<")]
            elif line.startswith("C"):
                to_search = line[11:]
                current_kegglvl3 = to_search[:to_search.find("[")-1]
            elif line.startswith("D"):
                to_extract = line[line.find("K"):]
                if not knumber_annot[to_extract[:to_extract.find(" ")]]:
                    for i in range (0, 3):
                        knumber_annot[to_extract[:to_extract.find(" ")]].append([])
                    knumber_annot[to_extract[:to_extract.find(" ")]][0].append(current_kegglvl1)
                    knumber_annot[to_extract[:to_extract.find(" ")]][1].append(current_kegglvl2)
                    knumber_annot[to_extract[:to_extract.find(" ")]][2].append(current_kegglvl3)
                else:
                    if current_kegglvl1 not in knumber_annot[to_extract[:to_extract.find(" ")]][0]:
                        knumber_annot[to_extract[:to_extract.find(" ")]][0].append(current_kegglvl1)
                    if current_kegglvl2 not in knumber_annot[to_extract[:to_extract.find(" ")]][1]:
                        knumber_annot[to_extract[:to_extract.find(" ")]][1].append(current_kegglvl2)
                    if current_kegglvl3 not in knumber_annot[to_extract[:to_extract.find(" ")]][2]:
                        knumber_annot[to_extract[:to_extract.find(" ")]][2].append(current_kegglvl3)
    for knumber, categories in knumber_annot.items():
        for lvl2 in categories[1]:
            if lvl2 not in kegg_lvl2_list:
                kegg_lvl2_list.append(lvl2)
    
# Read coverage information
def read_rpkm(rpkm_inf):
    global rpkm_stats
    with open(rpkm_inf, "rb") as infile:
            for line in infile:
                if not line.startswith("#"):
                    rpkm_stats[line.split("\t")[0][:line.split("\t")[0].find(" ")]] = line.split("\t")[5]

# Read MEGAN KEGG export, assemble a dictionary containing all valid K-Numbers
# and all contig IDs assigned to this K-Number
def process_megan(megan_out):
    global k_ids    
    with open(megan_out, "rb") as infile:
        megan_reader = csv.reader(infile, delimiter = "\t")
        for line in megan_reader:
            line[1] = " ".join(line[1].split())
            #split_line = line[0].split("_")
            if len(line[1]) == 6 and "-" not in line[1] and line[1] not in k_ids:
                k_ids[line[1]] = []
                #k_ids[line[1]].append("_".join(split_line[:2]))
                k_ids[line[1]].append(line[0])
            elif len(line[1]) == 6 and "-" not in line[1] and line[1] in k_ids:
                #k_ids[line[1]].append("_".join(split_line[:2]))
                k_ids[line[1]].append(line[0])

# Determine the total rpkm value per K number
def calc_rpkm():
    global knumber_rpkm, k_ids
    for knumber, contig_ids in k_ids.items():
        knumber_rpkm[knumber] = 0
        for contig_id in contig_ids:
            knumber_rpkm[knumber] = float(knumber_rpkm[knumber]) + float(rpkm_stats[contig_id])

# Generate a hierarchical KEGG annotation
def generate_KEGG_annot(k_rpkm):
    global knumber_annot, kegg_lvl2, kegg_lvl3, kegg_lvl4
    for entry, count in k_rpkm.items():
        if entry in knumber_annot:
            for i in knumber_annot[entry][1]:
                if i not in kegg_lvl2:
                    kegg_lvl2[i] = float(count)
                elif i in kegg_lvl2:
                    kegg_lvl2[i] = kegg_lvl2[i] + float(count)
            for j in knumber_annot[entry][2]:
                if j not in kegg_lvl3:
                    kegg_lvl3[j] = float(count)
                elif j in kegg_lvl3:
                    kegg_lvl3[j] = kegg_lvl3[j] + float(count)
            kegg_lvl4[entry] = float(count)   
    
# Calculate relative gene abundance for KEGG categories and sort
# the output
def sort_kegg_rpkm(kegg_annotation, kegg_mapping):
    global kegg_lvl2_order, kegg_lvl3_order, kegg_lvl4
    if kegg_annotation == kegg_lvl2:
        with open(kegg_mapping+".KEGGLvl2.summary", "wb") as kegg_annot_out:
            kegg_annot_out.write("KEGG-Lvl2 Category" + "\t" + "Total RPKM" + "\n")
            for key in kegg_lvl2_order:
                if key in kegg_annotation:
                    kegg_annot_out.write(key + "\t" + str(kegg_annotation[key]) + "\n")
    elif kegg_annotation == kegg_lvl3:
        with open(kegg_mapping+".KEGGLvl3.summary", "wb") as kegg_annot_out:
            kegg_annot_out.write("KEGG-Lvl3 Category" + "\t" + "Total RPKM" + "\n")
            for key in kegg_lvl3_order:
                if key in kegg_annotation:
                    kegg_annot_out.write(key + "\t" + str(kegg_annotation[key]) + "\n")
    elif kegg_annotation == kegg_lvl4:
        with open(kegg_mapping+ ".KEGGLvl4.summary", "wb") as kegg_annot_out:
            kegg_annot_out.write("KEGG-Lvl4" + "\t" + "Total RPKM" + "\n")
            for key in kegg_lvl4:
                kegg_annot_out.write(key + "\t" + str(kegg_lvl4[key]) + "\n")
                
# Script control structure
if args.megan and args.rpkm:
    generate_kegg_orthology()
    read_rpkm(args.rpkm)
    process_megan(args.megan)
    calc_rpkm()
    generate_KEGG_annot(knumber_rpkm)
    sort_kegg_rpkm(kegg_lvl4, args.megan)
else:
    print "Check the help by calling kegg_annotator.py -h"

