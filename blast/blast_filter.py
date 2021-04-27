# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 10:27:55 2013

@author: calle
"""

import csv
from Bio.Blast import NCBIXML
blast_records = NCBIXML.parse(open('PGblast.xml', 'rU'))

output = csv.writer(open('PGhit.csv','w'), delimiter =',',
                    quoting=csv.QUOTE_NONNUMERIC)
output.writerow(["Query","Hit ID", "Hit Def", "E-Value"])

E_VALUE_THRESH = 0.00000000000000001

for blast_record in blast_records:
    for alignment in blast_record.alignments:
        for hsp in alignment.hsps:
            if hsp.expect < E_VALUE_THRESH:
                output.writerow([blast_record.query[:8],
                                 alignment.hit_id, alignment.hit_def,hsp.expect])

blast_records.close()