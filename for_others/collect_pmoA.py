# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 16:13:44 2016

@author: calle
"""
# we need these biopython modules
from Bio import Entrez, SeqIO

# lets identify ourselves and define an input and output file
Entrez.email = "c.e.wegner@gmx.net"
input_file = open("")
output_file = open("/home/calle/Desktop/carboxysome_shell_proteins.faa", "wb")

# we look up all non-genome gene sequences of interest NOTE: you need to specify
# whether you are interested in nucleotide or amino acid sequences --> "db" argument
search = Entrez.esearch(db="protein", retmax = 2000, term = "carboxysome shell protein'"' NOT genome")
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