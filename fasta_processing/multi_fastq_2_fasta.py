'''
Created on June 23, 2014
@author: Carl-Eric Wegner - AG Liesack - Molecular Ecology - MPI Marburg
The given script converts multiple files present in a specified directory
into the desired format by using an iterated function. 
'''

# needed modules
import os
from Bio import SeqIO

# where are the files to be converted?
convert_dir = "/home/calle/Desktop/ribo-tag_polymer_eukarya/sorted_euk/fastq/"
 
# CONVERSION FUNCTION
def process(filename):
    return SeqIO.convert(filename, "fastq", filename + '.fasta', "fasta")

# CONVERSION
# do the conversion, os.walk returns a tuple, tuple make
# processing more difficult, therefore we call our
# conversion function using absolute file paths instead of the
#returned 3-tuple
for root, dirs, files in os.walk(convert_dir):
    for filename in files:
            fullpath = os.path.join(root, filename)
            print process(fullpath) 
            print "Converted Reads."

print str(len(files)) + " files successfuly converted!"
print "DONE, Files converted :-)!"
