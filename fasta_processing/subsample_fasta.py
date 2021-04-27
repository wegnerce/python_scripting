'''
Created on May 13, 2012
@author: Carl-Eric Wegner - AG Liesack - Molecular Ecology - MPI Marburg
The given script subsamples an input .fasta file, extracting a specified number of random
reads.
Example: python subsample_fasta.py <desired number of random reads> <input.fasta> 
'''

#!/usr/bin/env python
import random
import sys

random.seed()
#number of sequences to subsample
numSeq = int(sys.argv[1])
#name of the input file (fasta or fastq)
#assumes input file is standard fasta/fastq format
fileName1 = sys.argv[2]
fileName2 = sys.argv[3]
increment = 0

#if it's a fasta file
if (fileName1.find(".fasta") != -1):
  increment = 2
#else if it's a fastq file
elif (fileName1.find(".fastq") != -1):
  increment = 4
#quit if neither
else:
  sys.stdout.write("not a fasta/fastq file\n")
  sys.exit()

FILE1 = open(fileName1, 'r')
totalReads1 = list()
index = 0
for line in FILE1:
  if(index % increment == 0):
    totalReads1.append(index/increment)
  index += 1
FILE1.close()
if(len(totalReads1) < numSeq):
  sys.stdout.write("You only have "+str(len(totalReads1))+" reads!\n")
  sys.exit()
  
ttl = len(totalReads1)
random.shuffle(totalReads1)
totalReads1 = totalReads1[0: numSeq]
totalReads1.sort()

FILE1 = open(fileName1, 'r')
listIndex = 0

#if (increment == 4):  
# OUTFILE1 = open('/home/calle/Desktop/ribotag_additional_analysis/RiboTag_20130627/BS28d_ribotag_to_SSU_tagged_random10k.fastq', 'w')
#else:
# OUTFILE1 = open('/home/calle/Desktop/ribotag_additional_analysis/RiboTag_20130627/BS28d_ribotag_to_SSU_tagged_random10k.fasta', 'w')

OUTFILE1 = open(fileName2, 'w')
 
for i in range(0, ttl):
  curRead1 = ""
  for j in range(0, increment):
    curRead1 += FILE1.readline()
  if (i == totalReads1[listIndex]):
    OUTFILE1.write(curRead1)
    listIndex += 1
    if(listIndex == numSeq):
      break
  
FILE1.close()
OUTFILE1.close()
