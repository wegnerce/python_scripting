# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 09:25:49 2017

@author: calle
"""

from BCBio import GFF
from Bio import SeqIO

in_file = "/home/calle/Storage/Data/methylo_genomes/comparative_genomics/AL8_renamed.gbk"
out_file = "/home/calle/Storage/Data/methylo_genomes/comparative_genomics/AL8.gff"
in_handle = open(in_file)
out_handle = open(out_file, "w")

GFF.write(SeqIO.parse(in_handle, "genbank"), out_handle)

in_handle.close()
out_handle.close()

