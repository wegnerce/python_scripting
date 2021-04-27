# -*- coding: utf-8 -*-
"""
Created on Mon May 22 15:30:56 2017

@author: calle
"""

import csv

incov = "/home/calle/Storage/Data/becca_transcriptome/9_cov.txt"
outcov = "/home/calle/Storage/Data/becca_transcriptome/9_cov_mod.txt"
temptable = []

with open(incov, "rb") as infile:
	readcov = csv.reader(infile, delimiter = "\t")
	next(readcov, None)
	for line in readcov:
		print line
		line[0] = line[0].split(" ")[0]
		line[1] = int(line[6]) + int(line[7])
		print line[0]
		temptable.append(line)

with open(outcov, "wb") as outfile:
	writecov = csv.writer(outfile, delimiter = "\t")
	for row in temptable:
		writecov.writerow(row)

