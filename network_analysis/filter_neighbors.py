# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 12:41:15 2018

@author: calle
"""
import csv

neighbors = "/home/calle/Desktop/ultrasmall_ongoing/neighbors_total_reordered.txt"
neighbors_filtered = "/home/calle/Desktop/ultrasmall_ongoing/neighbors_auto_proteos.txt"

with open("/home/calle/Desktop/ultrasmall_ongoing/list_of_otus_auto.txt", "rb") as infile:
    taxa = set(infile.read().split("\n"))

with open(neighbors, "rb") as infile, open(neighbors_filtered, "wb") as outfile:
    taxonomy_reader = csv.reader(infile, delimiter = "\t")
    taxonomy_writer = csv.writer(outfile, delimiter = "\t")
    for line in taxonomy_reader:
        print line
        #if line[1].split(";")[2] in taxa:
        if line[0] in taxa:
            taxonomy_writer.writerow(line)
