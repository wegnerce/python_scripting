'''
Created on December 3, 2012
@author: Carl-Eric Wegner - AG Liesack - Molecular Ecology - MPI Marburg
The script below searches a .fasta file of interest (fasta_to_be_queried) for
sequences of interest given the IDs of the respective sequences are kept in 
a .txt file one ID per line. Picked sequences are saved into a specified new
.fasta file (picked_sequences).
'''

import sys
import csv

tax_to_be_queried = sys.argv[1]
list_of_queries = sys.argv[2]
picked_taxonomy = sys.argv[3]
taxonomy_to_save = []

wanted = set(line.rstrip("\n") for line in open(list_of_queries)) #.split(None,1)[0]
print "Found %i unique identifiers in %s" % (len(wanted), list_of_queries)

print wanted

with open(tax_to_be_queried, "rb") as infile:
    read_tax = csv.reader(infile, delimiter = ",")
    next(read_tax, None)
    for line in read_tax:
        if line[0] in wanted:
            taxonomy_to_save.append(line)

with open(picked_taxonomy, "wb") as outfile:
    for entry in taxonomy_to_save:
        outfile.write("%s\n" % entry)