# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 09:49:22 2013

@author: calle
"""

from Bio import SeqIO
 
with open("/home/calle/Desktop/deduplicated.fasta", 'w') as target:
    ids={}
    
    for _record in SeqIO.parse("/media/BackUp_CEW_(1)/BackUp_Phd/BackUp_Sequencing_Data/other_projects/Svetlana_454/processed/QIIME/pmoA_peatbog.fasta", "fasta"):  
        curr_id=str(_record.id)
        if curr_id not in ids:
                ids[curr_id]=_record.id
                SeqIO.write(_record, target, "fasta")
        
        
       
        
        