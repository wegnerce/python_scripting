# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 10:09:25 2016

@author: calle
"""
import sys
from Bio import SeqIO

common = set()

# determine intact read pairs by checking for sequence id's present in
# both files (forward.fastq, reverse.fastq)		
def common_ids(forward, reverse):
	global common
	R1 = (r.id for r in SeqIO.parse(forward, "fastq"))
	R2 = (r.id for r in SeqIO.parse(reverse, "fastq"))
	R1_ids = list(R1)
	print len(R1_ids)
	R2_ids = list(R2)
	print len(R2_ids)
	common = set(R1_ids).intersection(R2_ids)
	print len(common)
	return common

# filter original files based identified sequence id's
def filter_fasta(forward, reverse):
	global common
	common_ids(forward, reverse)	
	R1_filtered = (r for r in SeqIO.parse(forward, "fastq") if r.id in common)
	R2_filtered = (r for r in SeqIO.parse(reverse, "fastq") if r.id in common)
	SeqIO.write(R1_filtered, forward + "filtered.fastq", "fastq")
	SeqIO.write(R2_filtered, reverse + "filtered.fastq", "fastq")
	
filter_fasta(sys.argv[1], sys.argv[2])

# script usage: e.g. python common_seqs.py forward.fastq reverse.fastq
	
	
	