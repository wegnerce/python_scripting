'''
Created on October 9, 2012
@author: Carl-Eric Wegner - AG Liesack - Molecular Ecology - MPI Marburg
The script below counts the number of records in a given file (e.g. fasta). 
'''

# needed modules
import csv
from Bio import SeqIO

filter_for = "Subgroup 2"
of_interest = []
modified = []

sina = "/media/calle/TOSHIBA EXT/_projects/_red_hill_soft_coal/metagenome/processed/2_rRNA_analysis/B_emirge/RHA_emirge_SINA.csv"
emirge_fasta = "/media/calle/TOSHIBA EXT/_projects/_red_hill_soft_coal/metagenome/processed/2_rRNA_analysis/B_emirge/renamed_RHA.fasta"
subset_fasta = open("/media/calle/TOSHIBA EXT/_projects/_red_hill_soft_coal/metagenome/processed/2_rRNA_analysis/B_emirge/renamed_RHA_DA052.fasta", "w")

with open(sina, "rb") as sina_output:
    sina_reader = csv.reader(sina_output, delimiter = ";")
    next(sina_reader, None)
    for entry in sina_reader:
        print entry[15]
        if filter_for in entry[15]:
            of_interest.append(entry[2])

print "%i sequences identified!" % len(of_interest)

records = (r for r in SeqIO.parse(emirge_fasta, "fasta") if r.id in of_interest)
i = 1
for record in records:
    record.id = "RHA_" + filter_for + "_%i" % i
    i = i + 1    
    print record
    modified.append(record)
    
for seq_record in modified:
    subset_fasta.write(">%s %s\n%s\n" % (
           #seq_record.id[:13],
           seq_record.id,
           seq_record.description,
           seq_record.seq))    

subset_fasta.close()

