# -*- coding: utf-8 -*-
"""
Created on Wed July 27 2017
@author: Carl-Eric Wegner - Küsel Lab - FSU Jena
"""

# import necessary modules
import argparse
import os

# information about argument parsing
parser = argparse.ArgumentParser(description = "Renaming genome bin contig .fasta files based on sequence identifiers")
parser.add_argument("--path", "-p", help="path containing .fasta files to be renamed", action="store")
args = parser.parse_args()

# program control structure
if args.path:
    if os.access(args.path, os.F_OK):
        for filename in args.path:
            if filename.endswith(".fasta") or filename.endswith(".fna"):
                with open(filename, "rb") as infile:
                    firstline = infile.readline().strip().replace(">", "")
                    newname = firstline.split(" ")[0]
        os.rename(filename, newname)
else:
    print "Invalid program call, please check python multiple_rename.py -h"



