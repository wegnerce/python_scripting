# -*- coding: utf-8 -*-
"""
Created on Mon Dec 15 10:14:40 2014

@author: calle
"""

from Bio import SeqIO
from Bio.SeqUtils.CheckSum import seguid

def remove_dup_seqs(records):
    """"SeqRecord iterator to removing duplicate sequences."""
    checksums = set()
    for record in records:
        if len(record.seq) < 100:
            continue
        checksum = seguid(record.id)
        if checksum in checksums:
            print "Ignoring %s" % record.id
            continue
        checksums.add(checksum)
        yield record

in_file = "/home/calle/Desktop/_salt_stress/fix/6h-300mM1-mRNA-Bacteria.fasta"
out_file = open(in_file + ".fix", "w")

records = remove_dup_seqs(SeqIO.parse(in_file, "fasta"))
count = SeqIO.write(records, out_file, "fasta")
print "Saved %i records" % count