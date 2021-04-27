'''
Created on December 3, 2012
@author: Carl-Eric Wegner - AG Liesack - Molecular Ecology - MPI Marburg
The script below searches a .fasta file of interest (fasta_to_be_queried) for
sequences of interest given the IDs of the respective sequences are kept in 
a .txt file one ID per line. Picked sequences are saved into a specified new
.fasta file (picked_sequences). The script is designed for being used if only
few queries need to be picked.
'''

from Bio import SeqIO

fasta_to_be_queried = "/home/calle/Desktop/Svetlana_454_QIIME/TOP50_pmoA_OTUs/fastas/TOP50_otus_unique_mb661r_tax.fasta"
list_of_queries = "/home/calle/Desktop/Svetlana_454_QIIME/TOP50_pmoA_OTUs/TOP50_otus_lists/TOP50_unique_mb661r.txt"
picked_sequences = "/home/calle/Desktop/Svetlana_454_QIIME/TOP50_pmoA_OTUs/fastas/TOP50_otus_unique_mb661r_single.fasta"

wanted = set(line.rstrip("\n").split(None,1)[0] for line in open(list_of_queries))
print "Found %i unique identifiers in %s" % (len(wanted), list_of_queries)

input_fasta = list(SeqIO.parse(open(fasta_to_be_queried), "fasta"))
records = []

for item in wanted:
    for record in input_fasta:
        if item in record.description:
            records.append(record)
            break
                        
SeqIO.write(records, picked_sequences, "fasta")
count = len(wanted)

print "Saved %i records from %s to %s" % (count, fasta_to_be_queried, picked_sequences)