# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 09:36:24 2017

@author: calle
"""

# import needed modules
import csv
import pandas as pd

# necessary paths, variables, etc.
taxonomy = "/home/calle/Desktop/OTU_tax_all.txt"
taxonomy_stripped = "/home/calle/Desktop/OTU_tax_all_stripped.txt"


# read otu table, filter out OTUs with less than X counts over all samples
print "*** Read the taxonomy table."
otu_raw = pd.read_csv(taxonomy)
otu_raw.Rank1 = otu_raw.Rank1.str.replace('[\d+()]', '')
otu_raw.Rank2 = otu_raw.Rank2.str.replace('[\d+()]', '')
otu_raw.Rank3 = otu_raw.Rank3.str.replace('[\d+()]', '')
otu_raw.Rank4 = otu_raw.Rank4.str.replace('[\d+()]', '')
otu_raw.Rank5 = otu_raw.Rank5.str.replace('[\d+()]', '')
otu_raw.Rank6 = otu_raw.Rank6.str.replace('[\d+()]', '')
otu_raw.to_csv(taxonomy_stripped, sep=",", index=False)
