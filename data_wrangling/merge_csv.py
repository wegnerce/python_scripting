# -*- coding: utf-8 -*-
"""
@author:      Carl-Eric Wegner
@affiliation: Küsel Lab - Aquatic Geomicrobiology
              Friedrich Schiller University of Jena

              carl-eric.wegner@uni-jena.de
              https://github.com/wegnerce
              https://www.exploringmicrobes.science
"""

# needed packages
import glob
import os
import pandas as pd
import numpy as np
import matplotlib as plt

# NOTES:
# - set path with files to merge
# - create empty dataframe, BUT specify column that will be used for merging
#   later
# - specify columns to keep, plus the one used for merging
# - fill empty values
# - write merged dataframa as .csv
path = "/home/cewegner/Droptmp_work/tax_profiles_c/w_contaminants/phylum"
allcsv = glob.glob(path + "/*.out")
df = pd.DataFrame(columns=["path"])
for file in allcsv:
    print(file)
    dataframe = pd.read_csv(os.path.join(file), sep="\t", usecols=[1, 2], header=0)
    #print(df["path"])
    df = df.merge(dataframe, on="path", how="outer").fillna("0")
print(df)
df.to_csv(path + "/g_merged.csv", sep="\t", index=False)

# calculate relative abundances:
# - take all numeric data containing columns
# - make sure they are float to avoid divison errors
# - divide values by column sums, multiply with 100
df_col_names = list(df.columns.values)[1:]
df[df_col_names] = df[df_col_names].astype(np.float)
df_perc = \
    df[df_col_names].div(df[df_col_names].sum(axis=0), axis=1).multiply(100)
df[df_col_names] = df_perc
print(df)
df.to_csv(path + "/p_merged_rel_abd.csv", sep="\t", index=False)

# transpose plus add columns
# make std wide long --> merge w and wo --> transpose --> add columns
# index on dataset, columns: path, dataset_type, contaminants, blank

# convert to long format
df = pd.read_csv(path + "p_merged_rel_abd.csv", sep="\t", header=0)
df_long = \
 pd.melt(frame=df, id_vars=["path"], var_name="dataset", value_name="rel_abd")
print(df_long)
#df_long.to_csv(path + "/p_merged_rel_abd_long.csv", sep="\t", index=False)

# add columns
# - blank true/False
# - sample type
df_long['blank'] = \
    np.where(df_long['dataset'].str.contains('blk'), 'True', 'False')
df_long.head()

col = 'dataset'
conditions = [df_long[col].str.contains("_pc_"), \
    df_long[col].str.contains("_pwd_"), df_long[col].str.contains("_blk_")]
choices = [ 'pieces', 'powder', 'control' ]
df_long["dataset_type"] = np.select(conditions, choices, default=np.nan)
df_long.to_csv(path + "/p_merged_rel_abd_long.csv", sep="\t", index=False)

# back to wide format
conditions = [df_long['dataset_type'] == 'pieces', \
    df_long['dataset_type'] == 'powder', df_long['dataset_type'] == \
    'control']
choices = [ df_long['dataset'] + '_pc', df_long['dataset'] + '_pwd', \
    df_long['dataset'] ]
df_long["dataset"] = np.select(conditions, choices, default=np.nan)

conditions = [df_long['contaminants'] == 'wo', \
    df_long['contaminants'] == 'w', df_long['contaminants'] == 'w' \
    and df_long['dataset_type'] == 'control']
choices = [ df_long['dataset'] + '_wo', df_long['dataset'] + '_w' ]
df_long["dataset"] = np.select(conditions, choices, default=np.nan)

df_wide = df_long.pivot_table(index=['dataset', 'dataset_type', 'contaminants'], \
    columns='path', values='rel_abd')
df_wide.head()

df_wide.to_csv(path + "/f_rel_abd_wide.csv", sep="\t", index=True)

