'''
Created on November 5, 2012
@author: Carl-Eric Wegner - AG Liesack - Molecular Ecology - MPI Marburg
The given script merges reverse complements a given .fasta file.
'''

import sys, fasta

fasta_to_rc = open("home/calle/Desktop/to_be_processed.fasta")

(name,seq) = fasta.load(fasta_to_rc).items()[0]

print '>%s(RC)\n%s' % (name, fasta.reverse_complement(seq))
