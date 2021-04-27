# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 12:45:01 2013

@author: calle
"""

from Bio import SeqIO

records = (rec.upper() for rec in SeqIO.parse("/home/calle/Desktop/to_tax_b/ATP_RS7d.fasta", "fasta")) # Python generator expression
count = SeqIO.write(records, "/home/calle/Desktop/to_tax_b/ATP_RS7d.fas", "fasta")
print "Converted %i records to upper case" % count