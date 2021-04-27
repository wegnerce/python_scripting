'''
Created on December 3, 2012
@author: Carl-Eric Wegner - AG Liesack - Molecular Ecology - MPI Marburg
The script below searches a .fasta file of interest (fasta_to_be_queried) for
sequences of interest given the IDs of the respective sequences are kept in 
a .txt file one ID per line. Picked sequences are saved into a specified new
.fasta file (picked_sequences).
'''

import sys
from Bio import SeqIO

fasta_to_be_queried = sys.argv[1]
list_of_queries = sys.argv[2]
#wanted = sys.argv[2]
picked_sequences = sys.argv[3]
records_to_save = []

wanted = set(line.rstrip("\n") for line in open(list_of_queries)) #.split(None,1)[0]
print "Found %i unique identifiers in %s" % (len(wanted), list_of_queries)

#print wanted

#for item in wanted:    
for record in SeqIO.parse(fasta_to_be_queried, "fasta"):
	if record.id in wanted:
		records_to_save.append(record)
            
# records = (r for r in SeqIO.parse(fasta_to_be_queried, "fasta") if r.id[0:" "-1) in wanted)
count = SeqIO.write(records_to_save, picked_sequences, "fasta")

print "Saved %i records from %s to %s" % (count, fasta_to_be_queried, picked_sequences)
if count < len(wanted):
    print "Warning %i IDs not found in %s" % (len(wanted)-count, fasta_to_be_queried)