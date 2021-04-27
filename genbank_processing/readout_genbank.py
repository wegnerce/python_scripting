'''
Created on May 12, 2012
@author: Carl-Eric Wegner AG Liesack - Molecular Ecology - MPI Marburg
The given python scripts extracts the record ID's gives an 
excerpt of respective sequences and their length.
'''
from Bio import SeqIO
handle = open("/home/calle/Python/BioPython/tutorial/orchid.gbk")
for seq_record in SeqIO.parse(handle, "genbank"):
    print seq_record.id
    print repr(seq_record.seq)
    print len(seq_record)
    