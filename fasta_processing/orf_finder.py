# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 12:03:40 2014

@author: calle
"""
from Bio import SeqIO

#define an empty list to keep sequences of interest
seq_interest = []
start_codons = ["ATG"]
stop_codons = []

#boolean variables to check for presence of start/stop codons
start_present = 0
stop_present = 0

#function splitting sequences into triplets
def seq_chunks(s, n):
    #Produce `n`-character chunks from the input sequence(s)"
    for start in range(0, len(s), n):
        yield s[start:start+n]
 
for record in SeqIO.parse(open("test.fasta", "rU"), "fasta"):
    to_check = str(record.seq)
    for chunk in seq_chunks(to_check, 3):
        if chunk in start_codons:
            start_present = 1
        if chunk in stop_codons:
            stop_presen = 1

'''    
    queried = record.id    
    if queried.find(filter_term): 
        # Add this record to our list
        sequences_of_interest.append(record)
 
print "Found %i sequences of interest!" % len(sequences_of_interest)
 
output_handle = open("sequences_of_interest.fasta", "w")
SeqIO.write(sequences_of_interest, output_handle, "fasta")
output_handle.close()


for chunk in chunks(chars, 3):
    print chunk
    '''