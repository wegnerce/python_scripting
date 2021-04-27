'''
Created on May 21, 2012
@author: Carl-Eric Wegner - AG Liesack - Molecular Ecology - MPI Marburg
The given script divides an input .fasta file, into block .fasta files containing
x reads.
'''

from Bio import SeqIO

def batch_iterator(iterator, batch_size) :
    """Returns lists of length batch_size.

    This can be used on any iterator, for example to batch up
aaaaa    Alignment objects from Bio.AlignIO.parse(...), or simply
    lines from a file handle.

    This is a generator function, and it returns lists of the
    entries from the supplied iterator.  Each list will have
    batch_size entries, although the final list may be shorter.
    """
    entry = True #Make sure we loop once
    while entry :
        batch = []
        while len(batch) < batch_size :
            try :
                entry = iterator.next()
            except StopIteration :
                entry = None
            if entry is None :
                #End of file
                break
            batch.append(entry)
        if batch :
            yield batch
'''
from Bio import SeqIO
record_iter = SeqIO.parse(open("/media/STORAGE1/Stasja_pro/to_filter/mRNA_assemblies/xylan_nonrRNA_rep3_r.fasta"),"fasta")
for i, batch in enumerate(batch_iterator(record_iter, 665792)) :
    filename = "/media/STORAGE1/Stasja_pro/to_filter/mRNA_assemblies/xylan_nonrRNA_rep3_%i_r.fasta" % (i+1)
    handle = open(filename, "w")
    count = SeqIO.write(batch, handle, "fasta")
    handle.close()
    print "Wrote %i records to %s" % (count, filename)


import csv
from Bio import SeqIO

mapping_file = ""
sequences = ""

sample_ids = []
subsets = [[]]

with open(mapping_file, "rb") as infile:
    mapping_reader = csv.reader(infile, delimiter = "\t")
    next(mapping_reader, None)
    for line in mapping_reader:
        if mapping_reader[0] not in sample_ids:
            sample_ids.append(mapping_reader[0])

for sample_id in sample_ids:
    subsets.append([])
'''
i = 1
record_iter = SeqIO.parse(open("NCBI_refseq.faa"),"fasta")
for i, batch in enumerate(batch_iterator(record_iter, 765000)):
    #if i == 1:
    filename = "NCBI_refseq_%i.fasta" % i
    with open(filename, "w") as handle:
        count = SeqIO.write(batch, handle, "fasta")
    print("Wrote %i records to %s" % (count, filename))






