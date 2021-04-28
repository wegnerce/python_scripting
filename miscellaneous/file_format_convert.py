'''
Created on May 12, 2012
@author: Carl-Eric Wegner - AG Liesack - Molecular Ecology - MPI Marburg
The given script converts a sequence file of a given format 
in any desired format.
'''
from Bio import SeqIO
import argparse
import os

parser = argparse.ArgumentParser(description = "Convert fastq -> fasta")
parser.add_argument("--file", "-f", type=file, help="file to convert", action="store")
parser.add_argument("--dirname", "-d", help="path to files (directory)", action="store")
args = parser.parse_args()

if args.file:
    if str(args.file).endswith(".fastq") or str(args.file).endswith(".fastaq"):
        handle = open(args.file)
        out_file = str(args.file)+".fasta"
        count = SeqIO.convert(handle, "fastq", out_file, "fasta")
        print "Converted %i records" % count
elif args.dirname:
    os.chdir(args.dirname)
    for in_file in os.listdir(args.dirname):
        if str(in_file).endswith(".fastq") or str(in_file).endswith(".fastaq"):
            handle = open(in_file)
            out_file = str(in_file)+".fasta"
            count = SeqIO.convert(handle, "fastq", out_file, "fasta")
            print "Converted %i records" % count
        