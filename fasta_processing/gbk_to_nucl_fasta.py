"""
Created on January 10, 2013
@author: Carl-Eric Wegner - AG Liesack - Molecular Ecology - MPI Marburg
The given script exracts nucleotide sequences from Genbank Nucleotide files.
"""

from Bio import SeqIO

gbk_input = "/home/calle/Desktop/transcriptome_session/S_CL21.gbk" # path to input .gbk file
NUCL_fasta_output = "/home/calle/Desktop/transcriptome_session/S_CL21.fna" # .fasta output

count = 0

input_handle  = open(gbk_input, "r")
output_handle = open(NUCL_fasta_output, "w")

for seq_record in SeqIO.parse(input_handle, "genbank") :
    count = count + 1
    print "Processing GenBank record %s" % seq_record.id # entry in .gbk file currently processed
    output_handle.write(">%s %s\n%s\n" % (
           seq_record.id,
           seq_record.description,
           seq_record.seq))

print "Done! " + str(count) + " Genbank records have been processed."

output_handle.close()
input_handle.close()
