# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 17:32:28 2016

@author: calle
"""
import petl as etl

#Load the table
table1 = etl.fromcsv('/home/calle/Storage/assembly_summary_refseq.txt', delimiter = "\t")
# Alter the colums
table2 = etl.cut(table1, 'taxid','ftp_path')
#have a quick look to make sure things are ok. Prints a nicely formatted table to your console
print etl.look(table2)
# Save to new file
etl.tocsv(table2, "/home/calle/Storage/assembly_summary_refseq_stripped.txt", delimiter = "\t")
