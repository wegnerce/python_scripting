'''
Created on October 9, 2012
@author: Carl-Eric Wegner - AG Liesack - Molecular Ecology - MPI Marburg
The given script renames all files of a specified file type in a given folder,
giving every file a number specified in variable rename_index_number.
'''

import glob
import re
import os

list_of_files = glob.glob("/home/calle/Databases/CAZy/GT/*.fasta_noblanks.fasta")
list_of_files.sort()

rename_index_number = 1

for f in list_of_files:
    original = f
    
    #result = re.search(r'blastout_(\d+)_(\d+).xml', f)
    #if result:
    new_name = '/home/calle/Databases/CAZy/GT/GT' + str(rename_index_number) + '.fasta'
    print "%s => %s" % (original, new_name)
    os.rename (original, new_name)
    rename_index_number +=1
        
print "DONE! :-)"




