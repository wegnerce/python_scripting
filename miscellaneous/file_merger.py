"""
Created on June 18, 2012
@author: Carl-Eric Wegner - AG Liesack - Molecular Ecology - MPI Marburg
The given script merges files (.xml, .txt, .csv) given in a particular folder
into one single file.
"""

file_ext = ".xml" #set type of files to be merged e.g. .txt, .xml, .csv
dir_path = "/home/calle/Desktop/RNASeq_20120613/RL6/mRNA_BLASTX_out/out/" #refer directory containing files to be merged
merged_input = "/home/calle/Desktop/RNASeq_20120613/RL6/mRNA_BLASTX_out/merged.xml" #define the output file, containing the merged data

import os

os.chdir(dir_path) #define folder containing files to be merged as working directory

files = os.listdir(dir_path) #assign list of all files present in the indicated directory

for f in files: #walk through files present in the indicated directory
  if f.endswith(file_ext): #check for file type
    data = open(f)
    out = open(merged_input, 'a')
    for l in data:
      out.write(str(l))        
    data.close()
    out.close()
    
