# -*- coding: utf-8 -*-
"""
Created on July 2, 2012
@author: Carl-Eric Wegner - AG Liesack - Molecular Ecology - MPI Marburg
The given script processes BLAST results from multiparallel BLAST searches
and merges and trims BLAST output files for downstream analysis in MEGAN / BLAST2GO.
"""


import glob

list_of_files = glob.glob("/media/BackUp_CEW_(1)/BackUp_Phd/BackUp_Sequencing_Data/Blast2GO/XML/blast_output_BS28d/xml_BLASTX_BS28days_b/*.xml")           # create the list of file
FileOut = open("/media/BackUp_CEW_(1)/BackUp_Phd/BackUp_Sequencing_Data/Blast2GO/XML/blast_output_BS28d/BS28d_b.xml","w")
XML_template = open("/home/calle/Desktop/RS14d_to_SSU.xml","r")

XML_lines = XML_template.readlines()
FileOut.writelines(XML_lines[:21])

i=0
for file_name in list_of_files:
    FI = open(file_name, 'r')
    F_lines = FI.readlines()
    FileOut.writelines(F_lines[21:-2])
    print F_lines[21:-2]
    
    print "\n"
    i=i+1
    print i
    FI.close()

FileOut.writelines(XML_lines[-2:])

print "Merged and trimmed %i .XML files." % (i)
print "END"    
FileOut.close()
XML_template.close()
