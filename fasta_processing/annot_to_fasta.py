# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 12:40:41 2016

@author: calle
"""

from Bio import SeqIO
import csv

input_handle = open("/home/calle/Storage/Data/becca_peat_genomes/Acidithrix_sp.annotation_cut.txt")
output_handle = open("/home/calle/Storage/Data/becca_peat_genomes/Acidithrix_sp.annotation_cut.faa", "w")

with input_handle as infile:
	next(infile)
	for line in infile:
		output_handle.write(">%s %s %s %s\n%s" % (
					line.split("\t")[0],
					line.split("\t")[1],
					line.split("\t")[2],
					line.split("\t")[3],
					line.split("\t")[5]))

