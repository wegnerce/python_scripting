# -*- coding: utf-8 -*-
"""
Created on Wed May  9 13:58:16 2018

@author: calle
"""

from __future__ import print_function

import pandas as pd

#categories = set(['H3-2-1', 'H3-2-2', 'H3-2-3', 'H3-2-3', 'H4-1-1', 'H4-1-2',
#                  'H4-1-3', 'H4-2-1', 'H4-2-2', 'H4-2-3', 'H4-3-1', 'H4-3-2',
#                  'H4-3-3', 'H5-1-1', 'H5-1-2', 'H5-1-3', 'H5-1-3', 'H5-2-1',
#                  'H5-2-2', 'H5-2-3'])

categories = set(['PNK66-H3-2', 'PNK66-H4-1', 'PNK66-H4-2', 'PNK66-H4-3',
                  'PNK66-H5-1', 'PNK66-H5-2', 'PNK69-H4-1-1', 'PNK69-H4-1-2',
                  'PNK69-H4-1-3', 'PNK69-H4-3-1', 'PNK69-H4-3-2', 'PNK69-H4-3-3',
                  'PNK69-H5-1-1', 'PNK69-H5-1-2', 'PNK69-H5-1-3', 'PNK69-H5-2-1',
                  'PNK69-H5-2-2', 'PNK69-H5-2-3'])

print (categories)

def correct_categories(cols):
    return [cat for col in cols for cat in categories if col.startswith(cat)]

df = pd.read_csv('/home/calle/Dropbox/hainich_ongoing_v2/MT/CAZymes/for_fig6/all_substrates_polymers.csv', sep=',', index_col='Phylum')

print (df)

print(df.groupby(correct_categories(df.columns),axis=1).sum())
df.groupby(correct_categories(df.columns),axis=1).sum().to_csv('/home/calle/Dropbox/hainich_ongoing_v2/MT/CAZymes/for_fig6/all_substrates_polymers_collapsed.tsv', sep='\t')

