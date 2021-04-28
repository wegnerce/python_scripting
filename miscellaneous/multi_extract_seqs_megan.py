'''
Created on October 9, 2012
@author: Carl-Eric Wegner - AG Liesack - Molecular Ecology - MPI Marburg
The given script renames all files of a specified file type in a given folder,
giving every file a number specified in variable rename_index_number.
'''

import csv
import sys
from Bio import SeqIO

general_metabolism = ("Amino Acids and Derivatives", "Carbohydrates",
                    "Cofactors, Vitamins, Prosthetic Groups, Pigments",
                    "Fatty Acids, Lipids, and Isoprenoids", "Nucleosides and Nucleotides",
                    "Membrane Transport", "Motility and Chemotaxis",
                    "Phages, Prophages, Transposable elements", "Stress Response")

carbon_fixation = ("Calvin-Benson cycle", "Calvin-Benson-Bassham cycle in plants",
                    "Carboxysome",
                    "Formaldehyde assimilation: Ribulose monophosphate pathway",
                    "Carbon monoxide induced hydrogenase",
                    "fumarate reductase/succinate dehydrogenase flavoprotein, N-terminal:FAD dependent oxidoreductase")

N_cycling = ("Denitrification", "Dissimilatory nitrite reductase",
             "Nitrate and nitrite ammonification", "Nitrogen fixation", "IPR003393")

S_cycling = ("CFE Sulfur Oxidation", "Adenylylsulfate reductase",
                    "Dissimilatory sulfite reductase", "Heterodisulfide reductase")

seq_filter_ids = {"General metabolism" : set(), "Carbon fixation" : set(),
                  "Nitrogen cycling" : set(), "Sulfur cycling" : set()}

def seq_filter_function(megan_annot):
    with open(megan_annot, "rb") as infile:
        megan_reader = csv.reader(infile, delimiter = "\t")
        for line in megan_reader:
            hit_key = next((entry for entry in general_metabolism if entry in line[1]), None)
            if hit_key:
                seq_filter_ids["General metabolism"].add(line[0])
            hit_key = next((entry for entry in carbon_fixation if entry in line[1]), None)
            if hit_key:
                seq_filter_ids["Carbon fixation"].add(line[0])
            hit_key = next((entry for entry in N_cycling if entry in line[1]), None)
            if hit_key:
                seq_filter_ids["Nitrogen cycling"].add(line[0])
            hit_key = next((entry for entry in S_cycling if entry in line[1]), None)
            if hit_key:
                seq_filter_ids["Sulfur cycling"].add(line[0])

# write outout for respective program modes
def write_output(seqs):
    genmet_seqs = (r for r in SeqIO.parse(seqs, "fasta") if r.id in seq_filter_ids["General metabolism"])
    count = SeqIO.write(genmet_seqs, seqs + ".genmet.fa", "fasta")
    print " *** Saved %i sequences linked to General metabolism." % (count)
    Cfix_seqs = (r for r in SeqIO.parse(seqs, "fasta") if r.id in seq_filter_ids["Carbon fixation"])
    count = SeqIO.write(Cfix_seqs, seqs + ".Cfix.fa", "fasta")
    print " *** Saved %i sequences linked to Carbon fixation." % (count)
    Ncyc_seqs = (r for r in SeqIO.parse(seqs, "fasta") if r.id in seq_filter_ids["Nitrogen cycling"])
    count = SeqIO.write(Ncyc_seqs, seqs + ".Ncyc.fa", "fasta")
    print " *** Saved %i sequences linked to Nitrogen cycling." % (count)
    Scyc_seqs = (r for r in SeqIO.parse(seqs, "fasta") if r.id in seq_filter_ids["Sulfur cycling"])
    count = SeqIO.write(Scyc_seqs, seqs + ".Scyc.fa", "fasta")
    print " *** Saved %i sequences linked to Sulfur cycling." % (count)

seq_filter_function(sys.argv[1])
write_output(sys.argv[2])