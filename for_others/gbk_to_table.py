# -*- coding: utf-8 -*-
"""
@author:      Carl-Eric Wegner
@affiliation: Küsel Lab - Aquatic Geomicrobiology
              Friedrich Schiller University of Jena

              carl-eric.wegner@uni-jena.de
"""

### import necessary modules
import csv
from Bio import SeqIO

### required paths
genome_in = ""
table_out = ""

record = SeqIO.read("/home/calle/Dropbox/Acidiphilium_sp_c61.fasta.cb.gb", "genbank")
print (len(record.features))

