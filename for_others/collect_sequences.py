# -*- coding: utf-8 -*-
"""
created on January 14, 2013

@author: Carl-Eric Wegner - AG Liesack - Molecular Ecology - MPI Marburg

Using NCBI's Entrez utilities, the script below collects AA or nt sequences from
NCBI given a specified query.

TODO: include an argparse-based CLI interface
"""
# we need these biopython modules
from Bio import Entrez, SeqIO

# lets identify ourselves and define an output file
Entrez.email = "your@dummyemail.com"
output_file = open("/path/to/output/file.fasta", "wb")

# NOTE: consider whether you want to collect genome and partial sequences
# nucleotide or amino acid sequences --> "db" argument
# the query limit aka number of looked up sequences is controlled via "retmax"
search = Entrez.esearch(db="protein", retmax = 25000, term = "amoA AND ammonia monooxygenase[Protein] NOT genome NOT pmoA NOT hypothetical NOT putative")
search_result = Entrez.read(search)
search.close()

# and now we download them and write them to a file
i = 0
for seq_id in search_result["IdList"]:
    fetch_seqs = Entrez.efetch(db="protein", id=seq_id, rettype="fasta", retmode="text")
    read_seqs = SeqIO.read(fetch_seqs, "fasta")
    output_file.write(">%s %s\n%s\n" % (
               read_seqs.id,
               read_seqs.description[read_seqs.description.find(" ")+1:],
               read_seqs.seq)) 
    i = i + 1
fetch_seqs.close()
output_file.close()

print "Found and downloaded %i sequences" % i