# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 13:53:14 2013

@author: calle
"""

from Bio import SeqIO
def trim_primer(record, primer):
    if record.seq.startswith(primer):
        return record[len(primer):]
    else:
        return record

trimmed_reads = (trim_primer(record, "TTACGGCC") for record in \
                 SeqIO.parse("/home/calle/Desktop/Busse_454/572.A/572_prinseq_good_lWps.fasta", "fasta"))
count = SeqIO.write(trimmed_reads, "/home/calle/Desktop/Busse_454/trimmed.fasta", "fasta")
print "Trimmed / sliced %i reads" % count 


