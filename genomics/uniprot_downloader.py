# -*- coding: utf-8 -*-
"""
@author:      Carl-Eric Wegner
@affiliation: Küsel Lab - Aquatic Geomicrobiology
              Friedrich Schiller University of Jena

              carl-eric.wegner@uni-jena.de
"""

### needed modules
import os
import argparse

# information about argument parsing
parser = argparse.ArgumentParser(description = "Download UniProt Proteomes")
parser.add_argument("--mapping", "-m", help="indicate UniProt Mapping file", action="store")
parser.add_argument("--taxids", "-t", help="list of NCBI TaxIDs of interest", action="store")
args = parser.parse_args()

### helper functions
def screen_mapping(id_list, mapping):
    lookup = []
    uniprot_ids = []
    print "Lookup Uniprot proteome IDs for provided NCBI TaxID."
    with open(id_list, "rb") as infile:
        for line in infile:
            lookup.append(line.replace("\n", ""))
    print lookup
    with open(mapping, "rb") as infile:
        for line in infile:
            if line.split(",")[1] in lookup:
                uniprot_ids.append(line.split(",")[0])
    print "Done."
    print uniprot_ids
    return uniprot_ids

def download_proteomes(ids):
    for id in ids:
        print "Download proteome for " + id + "."
        cmd = "wget ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/reference_proteomes/Bacteria/" + id + "_*.fasta.gz"
        os.system(cmd)        
        cmd = "wget ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/reference_proteomes/Archaea/" + id + "_*.fasta.gz"
        os.system(cmd)        
        
# program control structure
if args.mapping and args.taxids:
    download_proteomes(screen_mapping(args.taxids, args.mapping))
else:
    print "Invalid program call, please check your input files."


