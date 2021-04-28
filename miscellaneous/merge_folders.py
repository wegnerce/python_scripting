'''
Created on October 9, 2012
@author: Carl-Eric Wegner - AG Liesack - Molecular Ecology - MPI Marburg
The script below merges two indicated directories, meaning root_src_dir is merged INTO
root_dest_dir.
'''

import os
import shutil

root_src_dir = '/media/BackUp_CEW_(1)/BackUp_Phd/BackUp_Sequencing_Data/Blast2GO/XML/blast_output_BS1d'
root_dst_dir = '/media/BackUp_CEW_(1)/BackUp_Phd/BackUp_Sequencing_Data/Blast2GO/XML/blast_output_BS1d/merged'

for src_dir, dirs, files in os.walk(root_src_dir):
    dst_dir = src_dir.replace(root_src_dir, root_dst_dir)
    if not os.path.exists(dst_dir):
        os.mkdir(dst_dir)
    for file_ in files:
        src_file = os.path.join(src_dir, file_)
        dst_file = os.path.join(dst_dir, file_)
        if os.path.exists(dst_file):
            os.remove(dst_file)
        shutil.move(src_file, dst_dir)
        
print "DONE :-)!"



