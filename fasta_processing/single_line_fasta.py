'''
Created on May 13, 2012
@author: Carl-Eric Wegner - AG Liesack - Molecular Ecology - MPI Marburg
Script converts multiline .fasta files into singleline .fasta files.
'''

from Bio import SeqIO
infile = open("/home/calle/Desktop/cbbL/DAFGA/IA_single.fasta") 

with open("/home/calle/Desktop/cbbL/DAFGA/IA_single.fasta.fixed", 'w') as target:
    for _record in SeqIO.parse(infile, "fasta"):  
        target.write('>%s\n' % _record.description)
        target.write('%s\n' % _record.seq.tostring())
