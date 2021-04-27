# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 08:26:50 2016

@author: calle
"""
# lets load all necessary modules
import sqlite3 # needed for database handlin

# paths, parameters
db = "/home/calle/Storage/uniref_GO.db"

# we are interested in methanogenesis-related GO terms, so lets create a 
# dictionary for them to later count the number of reads linked to individual
# GO categories (BP)
methanogenesis_mapping = {"Methanogenesis_GO:0015948" : 0,
							  "Methanogenesis (from acetate)_GO:0019385" : 0,
							  "Methanogenesis (from CO2)_GO:0019386" : 0,
							  "Methanogenesis (from methanol)_GO:0019387" : 0}

methanogenesis_ids = ("GO:0015948", "GO:0019385", "GO:0019386", "GO:0019387")
									
# dedicated function to parse uniref90 ids
def check_GO(uni90id):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    command = "SELECT GO_tags FROM uniref_GO WHERE uniref_id = '" + uni90id +  "';"      
    cursor.execute(command)
    result = cursor.fetchone()
    cursor.close()    
    if result:
		return result[0].split("; ")
    else:
		return "no hit"
	
# alright, let's do it, we have a sql database in the format:
# GO_tag //UniRef90_id																										
with open ("/home/calle/Dropbox/JJP_CEW/45-11-1-mRNA_filter.fasta.out", "rb") as infile:
	for line in infile:
		look_up = check_GO(line.split("\t")[1])
		for entry in look_up:
			for k, v in methanogenesis_mapping.items():
				if entry == k.split("_")[1]:
					methanogenesis_mapping[k] = methanogenesis_mapping[k] + 1

with open("/home/calle/Dropbox/JJP_CEW/45-11-1-mRNA_filter.fasta.out.methanogenesis.out", 'w') as f:
    [f.write('{0},{1}\n'.format(key, value)) for key, value in methanogenesis_mapping.items()]