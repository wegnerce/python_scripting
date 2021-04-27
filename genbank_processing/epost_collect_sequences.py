# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 13:46:23 2017

@author: calle
"""

# needed modules
import sys
from Bio import Entrez

# parameters asked for by NCBI
db           = "protein"
Entrez.email = "c.e.wegner@uni-jena.de"
batchSize    = 100
retmax       = 10**9

# file handles
accs_file = ""
collected_records = ""

# read accessions from accession file handle, join them and look for them
wanted = set(line.rstrip("\n")[1:].replace("\r", "") for line in open(accs_file) if line.startswith(">"))
query  = " ".join(wanted)
search = Entrez.esearch(db="protein", term = query)
search_result = Entrez.read(search)
search.close()

# and now we download them and write them to a file
i = 0
for seq_id in search_result["IdList"]:
    fetch_seqs = Entrez.efetch(db , id=seq_id, rettype="fasta", retmode="text")
    read_seqs = SeqIO.read(fetch_seqs, "fasta")
    collected_records.write(">%s %s\n%s\n" % (
               read_seqs.id,
               read_seqs.description[read_seqs.description.find(" ")+1:],
               read_seqs.seq)) 
    i = i + 1
fetch_seqs.close()
collected_records.close()

print "Found and downloaded %i sequences" % i