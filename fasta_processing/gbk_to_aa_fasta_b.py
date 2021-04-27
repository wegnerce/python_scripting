"""
Created on January 10, 2013
@author: Carl-Eric Wegner - AG Liesack - Molecular Ecology - MPI Marburg
The given script exracts amino acid sequences from Genbank Nucleotide
entries. Please consider that the whole (!) nucleotide entry is translated 
and not only the translated protein, meaning everything behind the first 
start codon.
"""

from Bio import SeqIO

gbk_input = "/home/calle/Desktop/cbbL/cbbL_NCBI_20130111.gb" # path to input gbk. file
AA_fasta_output = "/home/calle/Desktop/cbbL/extracted_AA.fasta" # output .fasta file 

input_handle  = open(gbk_input, "r") 
output_handle = open(AA_fasta_output, "w")

count = 0

for seq_record in SeqIO.parse(input_handle, "genbank") :
    count = count + 1
    print "Processing GenBank record %s" % seq_record.id
    for seq_feature in seq_record.features :
        if seq_feature.type=="CDS" : # scan for CDS feature
            assert len(seq_feature.qualifiers['translation'])==1
            output_handle.write(">%s %s\n%s\n" % (  
                   seq_record.id,                         # extracted from which .gbk file
                   seq_record.description[:40],
                   seq_feature.qualifiers['translation'][0])) # last but not least the AA sequence

print "Done! " + str(count) + " Genbank records have been processed."

output_handle.close()
input_handle.close()
