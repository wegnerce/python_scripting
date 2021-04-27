# -*- coding: utf-8 -*-
"""
@author:      Carl-Eric Wegner
@affiliation: Küsel Lab - Aquatic Geomicrobiology
              Friedrich Schiller University of Jena

              carl-eric.wegner@uni-jena.de
"""

### needed modules/packages
from Bio import SeqIO

### declare important variables
spacer = "NNNNNNNNNNTTAGTTAGTTAGNNNNNNNNNN" # default GAMOLA2 spacer
contigs_in = "/home/calle/Downloads/Soxy_CL21_genome.fna"
contigs_out = "/home/calle/Downloads/Soxy_CL21_genome_concat.fasta"

merged = ""
chr_name = "Acp_C61_1"

i = 1
for record in SeqIO.parse(contigs_in, "fasta"):
    if not i == len(list(SeqIO.parse(contigs_in, "fasta"))):
        merged = merged + record.seq + spacer
    else:
        merged = merged + record.seq

with open(contigs_out, "wb") as outfile:
    outfile.write(">%s\n%s\n" % (
    chr_name,
    merged))

