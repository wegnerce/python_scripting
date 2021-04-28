# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 09:36:24 2017

@author: calle
"""

# import needed modules
import csv
import pandas as pd

# necessary paths, variables, etc.
#taxonomy = "/home/calle/Storage/Data/parcu_netw/OTU_all_tax_filtered.txt"
#taxonomy_stripped = "/home/calle/Storage/Data/parcu_netw/final/OTU_all_tax_filtered_cluster2_B.txt"
#otu_tab = "/home/calle/Storage/Data/parcu_netw/OTU_all.txt"
#otu_tab_stripped = #"/home/calle/Desktop/ultrasmall_ongoing/parcu_netw/final/OTU_all_noL_no01_100reads.txt"
#otu_tab_cluster = "/home/calle/Storage/Data/parcu_netw/final/OTU_all_cluster2_B.txt"
otu_in = "/home/calle/Storage/Data/parcu_netw/final/OTU_all_noL_no01_100reads.txt"
otu_out = "/home/calle/Storage/Data/parcu_netw/final/OTU_all_noL_no01_100reads_03.txt"


# read otu table, filter out OTUs with less than X counts over all samples
print "*** Filter the raw OTU table (OTUs in more than 30% of all samples)."
otu_raw = pd.read_csv(otu_in)
otu_filtered = otu_raw.dropna(thresh=15)
otu_filtered = otu_filtered.fillna(0)
#otu_filtered = otu_raw[otu_raw.sum(axis = 1) > 100]
print "*** Identified %d OTUs with more than 100 counts over all samples" % (len(otu_filtered))
print "    OTU table was stripped accordingly."
otu_filtered.to_csv(otu_out, sep=',', encoding='utf-8', index = False)
print ""
