'''
Created on December 11, 2012
@author: Carl-Eric Wegner - AG Liesack - Molecular Ecology - MPI Marburg
The given script subsamples input .fasta files (located in the same folder),
extracting a specified number of random reads from all .fasta files present.
'''

import random
import glob
inFiles = glob.glob('/media/STORAGE1/Stasja_pro/to_filter/mRNA_assemblies/*.fasta') # potential input files are indexed
outFiles = [] # file names generated based on existing names
num = int(raw_input("Enter number of random sequences to select:\n"))


for i in range(len(inFiles)):

        for k in range(1):
                fNames = []
                fSeqs = []
                outFiles.append(file(str(inFiles[i])+'_'+'Rand_'+str(num)+'-'+str(k+1)+'.fasta', 'wt'))
                for line in open(inFiles[i]):
                        if (line[0] == '>'):
                                fNames.append(line)
                        else:
                                fSeqs.append(line)
                curr = (len(outFiles)-1)
                for j in range(num):
                        a = random.randint(0, (len(fNames)-1))
                        outFiles[curr].write(fNames.pop(a))
                        outFiles[curr].write(fSeqs.pop(a))
raw_input("Done.")