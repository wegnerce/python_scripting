# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 11:41:15 2015

@author: calle
"""

# needed modules
import csv
from collections import defaultdict
from Bio.KEGG.REST import kegg_list

# mapping files for generating an interleaved KEGG mapping 
k2rn = open("/home/calle/Desktop/RN_K.txt", "rb")
rn2rc = open("/home/calle/Desktop/RC_RN.txt", "rb")
rn2rp = open("/home/calle/Desktop/RP_RN.txt", "rb")
rp2cpd = open("/home/calle/Desktop/RP_list.txt", "rb")
knum_list = open("/home/calle/Desktop/to_test.txt", "rb")
mapping = open("/home/calle/Desktop/mapping_test.txt", "wb")

# create an empty dictionary to hold KEGG mapping information:
# K-Number, reaction, reaction class, reaction pair, educts / products
kegg_mapping = defaultdict(list)
k2rn_map = {}
rn2rc_map = {}
rn2rp_map = {}
rp2cpd_map = {}
compounds = []
unwanted = ["H2O", "CO2", "H+", "H2", "NAD+", "NADH", "FAD", "FADH2", "NADP+"\
    , "NADPH", "ADP", "ATP", "O2"]
to_filter = []

# READ ALL NECESSARY MAPPING FILES

# (1) extract K-numbers and corresponding reactions
def read_k2rn(k2rnmap):    
    global k2rn_map
    print " Read K-Numbers and corresponding reactions"   
    with k2rnmap as to_process:
        k2rn_reader = csv.reader(to_process, delimiter = "\t")
        for row in k2rn_reader:
            k2rn_map[row[1]] = row[0]
    print " ***Done!"

# (2) read reaction to reaction class mapping
def read_rn2rc_map(rn2rcmap):
    global rn2rc_map
    print " Read reaction to reaction class mapping"
    with rn2rcmap as to_process:
        rn2rc_reader = csv.reader(to_process, delimiter = "\t")
        for row in rn2rc_reader:
            rn2rc_map[row[1][3:]] = row[0][3:]
    print " ***Done!"

# (3) read reaction to reaction class mapping
def read_rn2rp_map(rn2rpmap):
    global rn2rp_map
    print " Read reaction to reaction pair mapping"
    with rn2rpmap as to_process:
        rn2rp_reader = csv.reader(to_process, delimiter = "\t")
        for row in rn2rp_reader:
            rn2rp_map[row[1]] = row[0]
    print " ***Done!"
    
# (4) read reaction to reaction class mapping
def read_rp2cpd_map(rp2cpdmap):
    global rp2cpd_map
    print " Read reaction pair to compound mapping"
    with rp2cpdmap as to_process:
        rp2cpd_reader = csv.reader(to_process, delimiter = "\t")
        for row in rp2cpd_reader:
            rp2cpd_map[row[0]] = row[1].split("_")[0] + ";" + row[1].split("_")[1]
    print " ***Done!"
    
# INITIALIZE MAPPING FILE BY READING LIST OF K-NUMBERS TO PROCESS
def read_knumlist(knumlist):
    global kegg_mapping
    global k2rn_map
    to_delete = []
    print " Read K-Number list and initialize mapping file"   
    with knumlist as to_process:
        for line in to_process:
            kegg_mapping[line[:line.find("\n")]] = ["", "", ""]
    for key in k2rn_map:
        if key in kegg_mapping:
            if kegg_mapping[key][0] == "":
                if check_rc(k2rn_map[key]):
                    kegg_mapping[key][0] = k2rn_map[key] 
            else:
                if check_rc(k2rn_mapping[key]):
                    kegg_mapping[key][0] = kegg_mapping[key][0] + ";" + k2rn_map[key]
    for key in kegg_mapping:
        if kegg_mapping[key][0] == "":
            to_delete.append(key)
    for item in to_delete:
        kegg_mapping.pop(item)            
    print " ***Done!"
    
    
# CHECK WHETHER THE CORRESPONDING REACTION BELONGS TO A REACTION
# CLASS
def check_rc(rnid):
    global rn2rc_map
    if rnid in rn2rc_map:
        return True

def lookup_rn(knum):
    global k2rn_map
    if knum in k2rn_map:
        return k2rn_map[knum]

# LOOKUP REACTION PAIRS FOR REACTIONS
def lookup_rp(rnid):
    global kegg_mapping
    global rn2rp_map
    if rnid in rn2rp_map:
        return rn2rp_map[rnid]

# LOOKUP COMPOUNDS BELONGING to REACTION PAIRS
def lookup_cpds(rpid):
    global kegg_mapping
    global rp2cpd_map
    if rpid in rp2cpd_map:
        return rp2cpd_map[rpid]
        
# RUN THE PROGRAM
read_k2rn(k2rn)
read_rn2rc_map(rn2rc)
read_rn2rp_map(rn2rp)
read_rp2cpd_map(rp2cpd)
read_knumlist(knum_list)

print " Generate interleaved KEGG mapping file"
for key in kegg_mapping:
    if len(kegg_mapping[key][0].split(";")) == 1:
        kegg_mapping[key][1] = lookup_rp(kegg_mapping[key][0])
        kegg_mapping[key][2] = lookup_cpds(kegg_mapping[key][1])
    else:
        for entry in kegg_mapping[key][0].split(";"):
            if kegg_mapping[key][1] == "" and kegg_mapping[key][2] == "":
                kegg_mapping[key][1] = lookup_rp(entry)
                kegg_mapping[key][2] = lookup_cpds(kegg_mapping[key][1])
            else:
                if lookup_rp(entry) != None:
                    kegg_mapping[key][1] = str(kegg_mapping[key][1]) + ";" + str(lookup_rp(entry))
                if lookup_cpds(kegg_mapping[key][1]):
                    kegg_mapping[key][2] = str(kegg_mapping[key][2]) + ";" + str(lookup_cpds(kegg_mapping[key][1]))
    if kegg_mapping[key][2] != None:
        for cpd in kegg_mapping[key][2].split(";"):
            to_add = kegg_list(cpd).read().split("\t")[1].split(";")[0]
            if to_add not in unwanted:
                compounds.append(to_add.replace("\n", ""))
        kegg_mapping[key][2] = ";".join(compounds)
        print "Entry: %s RN: %s RP: %s CPDs: %s" % (key, \
            kegg_mapping[key][0], kegg_mapping[key][1], kegg_mapping[key][2])
        compounds[:] = []
    if kegg_mapping[key][1] == "" or kegg_mapping[key][2] == "":
        to_filter.append(key)
print " ***Done!"

print " Filter mapping file"
for to_del in to_filter:
    kegg_mapping.pop(to_del)
print " ***DONE!"
    
print " Write mapping file"
with mapping as outfile:
    mapping_writer = csv.writer(outfile, delimiter="\t", quoting=csv.QUOTE_MINIMAL)
    for key, values in kegg_mapping.items():
        mapping_writer.writerow([key] + values)
print " ***DONE!"