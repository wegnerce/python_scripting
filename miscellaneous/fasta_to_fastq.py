"""
reated on May 31, 2013
@author: Carl-Eric Wegner - AG Liesack - Molecular Ecology - MPI Marburg
A simple script converting normal .fasta files into .fastaq files by making use
of the PairedFastaQualIterator.
"""

from Bio import SeqIO
from Bio.SeqIO.QualityIO import PairedFastaQualIterator

handle = open("/home/calle/Desktop/Busse_454/data/raw/test.fastq", "w") #w=write
records = PairedFastaQualIterator(open("/home/calle/Desktop/Busse_454/data/raw/test.fasta"), open("/home/calle/Desktop/Busse_454/data/raw/test.qual"))
count = SeqIO.write(records, handle, "fastq")

handle.close()
print "Converted %i records" % count
