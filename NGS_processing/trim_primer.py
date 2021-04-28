# -*- coding: utf-8 -*-
"""
Created on May 29, 2013
@author: Carl-Eric - AG Liesack - Molecular Ecology - MPI Marburg
This little script trims away indicated primer sequences.
"""
from Bio import SeqIO
def trim_primers(records):
#def trim_primers(records, primer):
    """Removes perfect primer sequences at start of reads.
    
    This is a generator function, the records argument should
    be a list or iterator returning SeqRecord objects.
    """
    #len_primer = len(primer) #cache this for later
    for record in records:
        #if record.seq.startswith(primer):
		 yield record[25:1100]
        #else:
        #    yield record

original_reads = SeqIO.parse("/home/calle/Work/Isolates/16S/16S_re/CH11_16S_27F.txt", "fasta")
#trimmed_reads = trim_primers(original_reads, "GATGACGGTGT")
trimmed_reads = trim_primers(original_reads)
count = SeqIO.write(trimmed_reads, "/home/calle/Work/Isolates/16S/16S_re/CH11_trimmed.fasta", "fasta") 
print "Saved %i reads featuring the indicated primer." % count
print "THE END."
