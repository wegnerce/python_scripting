# -*- coding: utf-8 -*-
"""
@author:      Carl-Eric Wegner
@affiliation: Küsel Lab - Aquatic Geomicrobiology
              Friedrich Schiller University of Jena

              carl-eric.wegner@uni-jena.de
"""

from Bio import SeqIO
import sys

fasta_in = sys.argv[1]
fasta_out = open(sys.argv[2], "wb")
genus = sys.argv[3]

for seq_record in SeqIO.parse(fasta_in, "fasta"):
    new_id = seq_record.id + " " + genus
    fasta_out.write(">%s\n%s\n" % (
			new_id,
			seq_record.seq))