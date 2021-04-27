# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 16:30:59 2016

@author: calle
"""

from Bio import SeqIO

input_file = "/home/calle/Storage/Data/rh_reblast/final_metaglue/RH_pred_genes_prot.faa"
output_file = "/home/calle/Storage/Data/rh_reblast/final_metaglue/RH_pred_genes_prot_RHD.faa"

records = (r for r in SeqIO.parse(input_file, "fasta") if r.id.startswith("RHD"))
count = SeqIO.write(records, output_file, "fasta")

print "Saved %i records from %s to %s" % (count, input_file, output_file)