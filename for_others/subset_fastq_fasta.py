# -*- coding: utf-8 -*-
"""
Created on Fri Mar 04 15:25:20 2016

@author: Carl-Eric Wegner
"""

from Bio import SeqIO
import csv

qc_fastq = "/home/calle/Storage/Data/stasja_resubmission/total_mRNA_contigs.fna"
ids = "/home/calle/Storage/Data/stasja_resubmission/archaea.ids"
outfile = "/home/calle/Storage/Data/stasja_resubmission/total_mRNA_contigs_archaea.fna"

wanted = []

#with open(ids, "rb") as infile:
#    id_reader = csv.reader(infile, delimiter = "\t")
#    for line in id_reader:
#        wanted.append(line[0])
       
#for record in SeqIO.parse(open(subset, "rU"), "fasta"):
#    wanted.append(str(record.seq))

with open(ids, "rb") as infile:
    for line in infile:
        wanted.append(line.replace("\n", ""))
        
print wanted

records = SeqIO.parse(qc_fastq, "fasta")
filtered = (record for record in records if str(record.id) in wanted)
SeqIO.write(filtered, outfile, "fasta")

print "Done!"