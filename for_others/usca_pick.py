# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 09:18:14 2016

@author: calle
  """

# Load required modules
from Bio import SeqIO
import csv

# necessary paths
fasta_in = "/whatever/pmoA_DB.fasta"
tax_in = "/whatever/pmoA_DB.tax"
usca_seqs = "/whatever/usca.fasta"

# needed variables
usc_ids = []

# process taxonomy file, extract ids of interest
with open(tax_in, "rb") as infile:
    tax_reader = csv.reader(infile, delimiter = "\t")
    for line in tax_reader:
        if len(line[1].split(";")) > 3:
            if line[1].split(";")[3] == "USC-a":
                usc_ids.append(line[0])

# pick sequences of interest from the provided fasta file
records = (r for r in SeqIO.parse(fasta_in, "fasta") if r.id in usc_ids)
SeqIO.write(records, usca_seqs, "fasta")

            