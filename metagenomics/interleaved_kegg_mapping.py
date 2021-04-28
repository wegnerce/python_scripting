# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 11:41:15 2015

@author: calle
"""

# needed modules
from __future__ import division
import argparse
import csv
import sqlite3
import textwrap
from Bio import SeqIO
from collections import defaultdict

# mapping files for generating an interleaved KEGG mapping 
k2rn = open("/media/STORAGE2/Databases_II/mappings/pfam2go.txt", "rb")
rn2rc = open("/media/STORAGE2/Databases_II/mappings/tigrfams2go.txt", "rb")
rn2rp = open("/media/STORAGE2/Databases_II/mappings/ec2go.txt", "rb")
rp2cpd = "/media/STORAGE2/Databases_II/mappings/uni902taxid"

# the anticipated annotation file is stored in a dictionary containing lists
# as elements, seq lengths stores seq_id seq_length pairs to calculate
# the coverage of mblast hits later
mg_annotation = defaultdict(list)
seq_lengths = {}


