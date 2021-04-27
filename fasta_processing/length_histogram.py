# -*- coding: utf-8 -*-
"""
Created on Fri May  8 14:22:23 2015

@author: calle
"""

import pylab
from Bio import SeqIO

sizes = [len(rec) for rec in SeqIO.parse("/home/calle/Desktop/_RH_metagenome/7_1000_contigs/RHA_PE_contigs.fa.1000", "fasta")]

pylab.hist(sizes, bins=500000)
pylab.title("%i orchid sequences\nLengths %i to %i" \
            % (len(sizes),min(sizes),max(sizes)))
pylab.xlabel("Sequence length (bp)")
pylab.ylabel("Count")
pylab.show()
