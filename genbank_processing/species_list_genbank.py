'''
Created on May 12, 2012
@author: Carl-Eric Wegner AG Liesack - Molecular Ecology - MPI Marburg
The given python script extracts all different species given
in the file read out.
'''

from Bio import SeqIO
all_species = []
handle = open("/home/calle/Python/BioPython/tutorial/orchid.gbk")
for seq_record in SeqIO.parse(handle, "genbank"):
    all_species.append(seq_record.annotations["organism"])
print all_species


