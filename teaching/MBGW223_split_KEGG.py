# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 10:47:45 2018

@author: calle
"""
# import necessary modules
import csv

in_file = "/home/calle/Dropbox/KEGG_MBGW_bins.txt"
out_file_1 = "/home/calle/Dropbox/KEGG_bin1.txt"
out_file_2 = "/home/calle/Dropbox/KEGG_bin2.txt"
out_file_3 = "/home/calle/Dropbox/KEGG_bin3.txt"
out_file_4 = "/home/calle/Dropbox/KEGG_bin4.txt"
out_file_5 = "/home/calle/Dropbox/KEGG_bin5.txt"

bin1_kegg = []
bin2_kegg = []
bin3_kegg = []
bin4_kegg = []
bin5_kegg = []

with open(in_file, "rb") as kegg_in:
    for line in kegg_in:
        print(line)
        if line.startswith("bin1"):
            bin1_kegg.append(line)
            print line
        if line.startswith("bin2"):
            bin2_kegg.append(line)
        if line.startswith("bin3"):
            bin3_kegg.append(line)
        if line.startswith("bin4"):
            bin4_kegg.append(line)
        if line.startswith("bin5"):
            bin5_kegg.append(line)

print bin1_kegg

with open(out_file_1, "wb") as kegg_out:
    for entry in bin1_kegg:
        kegg_out.write("%s" % entry)

with open(out_file_2, "wb") as kegg_out:
    for entry in bin2_kegg:
        kegg_out.write("%s" % entry)

with open(out_file_3, "wb") as kegg_out:
    for entry in bin3_kegg:
        kegg_out.write("%s" % entry)

with open(out_file_4, "wb") as kegg_out:
    for entry in bin4_kegg:
        kegg_out.write("%s" % entry)

with open(out_file_5, "wb") as kegg_out:
    for entry in bin5_kegg:
        kegg_out.write("%s" % entry)