# -*- coding: utf-8 -*-
"""
Created on May 29, 2013
@author: Carl-Eric - AG Liesack - Molecular Ecology - MPI Marburg
This little script trims away indicated adaptor sequences sequences.
"""

from Bio import SeqIO

def trim_adaptors(records, adaptor, min_len):
    """Trims perfect adaptor sequences, checks read length.
    
    This is a generator function, the records argument should
    be a list or iterator returning SeqRecord objects.
    """
    len_adaptor = len(adaptor) #cache this for later
    for record in records:
        len_record = len(record) #cache this for later
        if len(record) < min_len:
           #Too short to keep
           continue
        index = record.seq.find(adaptor)
        if index == -1:
            #adaptor not found, so won't trim
            yield record
        elif len_record - index - len_adaptor >= min_len:
            #after trimming this will still be long enough
            yield record[index+len_adaptor:]

original_reads = SeqIO.parse("SRR020192.fastq", "fasta")

trimmed_adaptor1 = trim_adaptors(original_reads, "GATGACGGTGT", 100) # indicate adaptors of interest, plus minimal length of trimmed sequences
count = SeqIO.write(trimmed_adaptor1, "trimmed.fasta", "fasta") 

print "Saved %i reads featuring the first indicated adaptor." % count

"""
trimmed_adaptor2 = trim_adaptors(original_reads, "GATGACGGTGT", 100) 
count = SeqIO.write(trimmed_adaptor2, "trimmed.fasta", "fasta")

print "Saved %i reads featuring the second indicated adaptor." % count

trimmed_adaptor3 = trim_adaptors(original_reads, "GATGACGGTGT", 100) 
count = SeqIO.write(trimmed_adaptor3, "trimmed.fasta", "fasta")

print "Saved %i reads featuring the third indicated adaptor." % count

trimmed_adaptor4 = trim_adaptors(original_reads, "GATGACGGTGT", 100) 
count = SeqIO.write(trimmed_adaptor4, "trimmed.fasta", "fasta")

print "Saved %i reads featuring the fourth indicated adaptor." % count

trimmed_adaptor5 = trim_adaptors(original_reads, "GATGACGGTGT", 100) 
count = SeqIO.write(trimmed_adaptor5, "trimmed.fasta", "fasta")

print "Saved %i reads featuring the fifth indicated adaptor." % count

trimmed_adaptor6 = trim_adaptors(original_reads, "GATGACGGTGT", 100) 
count = SeqIO.write(trimmed_adaptor6, "trimmed.fasta", "fasta")

print "Saved %i reads featuring the sixth indicated adaptor." % count

trimmed_adaptor7 = trim_adaptors(original_reads, "GATGACGGTGT", 100) 
count = SeqIO.write(trimmed_adaptor7, "trimmed.fasta", "fasta")

print "Saved %i reads featuring the seventh indicated adaptor." % count

trimmed_adaptor8 = trim_adaptors(original_reads, "GATGACGGTGT", 100) 
count = SeqIO.write(trimmed_adaptor8, "trimmed.fasta", "fasta")

print "Saved %i reads featuring the eight indicated adaptor." % count
"""

print "THE END"

