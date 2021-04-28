# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 14:48:31 2018

@author: calle
"""

diamond_out = "/home/calle/Storage_II/Data/H_MT/PNK69-H5-2-3_anammox.out"

hdh_ids = ("OD34178.1", "WP_099324501.1", "WP_099327045.1", "SOH04857.1")

with open(diamond_out, "rb") as infile:
    hzs = 0
    hdh = 0
    for line in infile:
        if line.split("\t")[1] in hdh_ids:
            hdh = hdh + 1
        else:
            hzs = hzs + 1

print "hzsAB-linked sequences: " + str(hzs)
print "hdh-linked sequences: " + str(hdh)