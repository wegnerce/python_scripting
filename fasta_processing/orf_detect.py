# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 11:44:39 2014

@author: calle
"""

from Bio import Entrez
from Bio import SeqIO
from matplotlib import pyplot as plt
 
handle = "/media/TOSHIBA EXT/_projects/_rice_straw_breakdown/mRNA-tag/analysis/CAZymes/SigP_THMM/data/GHs/GH_BS1day.fasta"
rec = SeqIO.parse(handle, "fasta")
#handle.close()
seq = str(rec.seq)
comp_seq = str(rec.seq.reverse_complement())
 
def getORF(sequence, treshold, start_codons, stop_codons):
    start_codon_index = 0
    end_codon_index = 0
    start_codon_found = False
 
    orfs = []
 
    for j in range(0, 3):
        for indx in range(j, len(sequence), 3):
            current_codon = sequence[indx:indx+3]
            if current_codon in start_codons and not start_codon_found:
                start_codon_found = True
                start_codon_index = indx
            if current_codon in stop_codons and start_codon_found:
                end_codon_index = indx
                length = end_codon_index - start_codon_index + 1
                if length >= treshold * 3:
                    orfs.append(start_codon_index)
                start_codon_found = False
 
        start_codon_index = 0
        end_codon_index = 0
        start_codon_found = False
 
    return len(orfs), orfs
 
def getComplementORF(sequence, treshold, start_codons, stop_codons):
    start_codon_index = 0
    end_codon_index = 0
    start_codon_found = False
 
    complement_orfs = []
 
    for j in range(0, 3):
        for indx in range(j, len(sequence), 3):
            current_codon = sequence[indx:indx+3]
            if current_codon in start_codons and not start_codon_found:
                start_codon_found = True
                start_codon_index = indx
            if current_codon in stop_codons and start_codon_found:
                end_codon_index = indx
                length = end_codon_index - start_codon_index + 1
                if length >= treshold * 3:
                    complement_orfs.append(len(sequence)-end_codon_index-3)
                start_codon_found = False
 
        start_codon_index = 0
        end_codon_index = 0
        start_codon_found = False
 
    return len(complement_orfs), complement_orfs
 
def countTP(orfs, orfs_complement):
 
    TP_count = 0
 
    for f in rec.features:
        if f.type == "CDS":
            if f.strand == -1:
                if f.location.start.position in orfs_complement:
                    TP_count += 1
            if f.strand == 1:
                if f.location.start.position in orfs:
                    TP_count += 1
 
    return TP_count
 
def countCDS():
 
    CDS_count = 0
 
    for f in rec.features:
        if f.type == "CDS":
            CDS_count += 1
 
    return CDS_count
 
def calculatePrecisionRecall(orfs, orfs_complement):
    TP = countTP(orfs, orfs_complement)
    precision = TP / float(len(orfs)+len(orfs_complement))
    recall = TP / float(countCDS())
 
    return precision, recall
 
def drawGraph(r1, r2, width):
 
    v1 = []
    v2 = []
 
    for treshold in range(r1, r2, width):
        length_orf, orfs = getORF(seq, treshold, start, stop)
        length_orf_complement, orfs_complement = getComplementORF(comp_seq, treshold, start, stop)
        precision, recall = calculatePrecisionRecall(orfs, orfs_complement)
        v1.append(precision)
        v2.append(recall)      
 
    plt.xlabel("ORF length treshold (L)")
    plt.title("Paramecium tetraurelia gene candidate discovery")
    plt.plot(range(r1, r2, width), v1, label="Precision")
    plt.legend()
    plt.plot(range(r1, r2, width), v2, label="Recall")
    plt.legend()
    plt.show()
 
# Detect open reading frames (ORFs). How many ORFs code for at least 60 amino acids?
 
start = ["ATG"]
stop = ["TGA"]
 
length_orf, orfs = getORF(seq, 60, start, stop)
length_orf_complement, orfs_complement = getComplementORF(comp_seq, 60, start, stop)
 
sum_orfs = length_orf + length_orf_complement
 
print "+ ", length_orf
print "- ", length_orf_complement
print "Detected ORF number: ", sum_orfs
 
precision, recall = calculatePrecisionRecall(orfs, orfs_complement)
 
print "Precision for 60 codons: ", precision
print "Recall for 60 codons: ", recall
 
# Draw precision and recall as a function of minimum ORF length (measured in codon size).
 
drawGraph(0, 400, 10)
 
# What are the precision and recall for 125 codons?
 
length_orf, orfs = getORF(seq, 125, start, stop)
length_orf_complement, orfs_complement = getComplementORF(comp_seq, 125, start, stop)
 
sum_orfs = length_orf + length_orf_complement
 
print "+ ", length_orf
print "- ", length_orf_complement
print "Detected ORF number: ", sum_orfs
 
precision, recall = calculatePrecisionRecall(orfs, orfs_complement)
 
print "Precision for 125 codons: ", precision
print "Recall for 125 codons: ", recall