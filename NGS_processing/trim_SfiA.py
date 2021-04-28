"""
Created on May 31, 2013
@author: Carl-Eric - AG Liesack - Molecular Ecology - MPI Marburg
This little script removes SfiA site from amplicon data sets originating
from the Max Planck Genome Centre Cologne.
"""

from Bio import SeqIO

def remove_SfiA(records, sfi_variants):
    for variant in sfi_variants:
        for record in records:
            if record.seq.startswith(variant):
                yield record[len(variant):]                
               
        

"""
        if record.seq.startswith(variant[0]):
            yield record[len(variant[0]):]
        elif record.seq.startswith(variant[1]):
            yield record[len(variant[1]):]
        elif record.seq.startswith(variant[2]):
            yield record[len(variant[2]):]
        elif record.seq.startswith(variant[3]):
            yield record[len(variant[3]):]
        elif record.seq.startswith(variant[4]):
            yield record[len(variant[4]):]
        elif record.seq.startswith(variant[5]):
            yield record[len(variant[5]):]
        elif record.seq.startswith(variant[6]):
            yield record[len(variant[6]):]
        elif record.seq.startswith(variant[7]):
            yield record[len(variant[7]):]
        elif record.seq.startswith(variant[8]):
            yield record[len(variant[8]):]
        elif record.seq.startswith(variant[9]):
            yield record[len(variant[9]):]
        elif record.seq.startswith(variant[10]):
            yield record[len(variant[10]):]
        elif record.seq.startswith(variant[11]):
            yield record[len(variant[11]):]
        elif record.seq.startswith(variant[12]):
            yield record[len(variant[12]):]
        elif record.seq.startswith(variant[13]):
            yield record[len(variant[13]):]
        elif record.seq.startswith(variant[14]):
            yield record[len(variant[14]):]
        elif record.seq.startswith(variant[15]):
            yield record[len(variant[15]):]
        else:
            yield record
"""
           
sfi_variants = ['TTGATGGCCATTACGGCC', 'TTGATGGCCATTAACGGCC', 'TGATGGCCATTACGGCC',
                'TGATGGCCATTAACGGCC', 'TTTTACGGCC', 'TTTACGGCC', 'TTACGGGCC',
                'TTACGGCC','TACGGCC', 'TTTACGGC', 'TTACGGC', 'TTACGCC', 
                'TTACGC', 'ACGGCC', 'TACGCC', 'TACGC']

original_reads = SeqIO.parse("/home/calle/Desktop/Busse_454/data/raw/test.fasta", "fasta")            

output_file = "/home/calle/Desktop/Busse_454/data/raw/SfiA_clipped.fasta"
output_handle = open(output_file, "w")

trimmed_sfi = remove_SfiA(original_reads, sfi_variants) 
count = SeqIO.write(trimmed_sfi, output_handle, "fasta") 
output_handle.close()

print "Processed %i reads." % count      
print "Variable SfiA sites successfully removed!"


