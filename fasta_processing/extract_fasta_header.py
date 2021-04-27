"""
created on January 17, 2013
@author: Carl-Eric Wegner - AG Liesack - Molecular Ecology - MPI Marburg
A plain script extracting the header lines from fast sequences and writing them
into a separate .txt file.
"""

from Bio import SeqIO

input_handle = open("/home/calle/Storage/Data/methylo_genomes/CH11_spades/scaffolds.fna.1000")
output_handle = open("/home/calle/Desktop/ids.txt", "w")

count = 0

for seq_record in SeqIO.parse(input_handle, "fasta") :
    count = count + 1    
    #output_handle.write("%s\n" % (seq_record.id))
    print seq_record.id.split("_")[5]
    print float(seq_record.id.split("_")[5])
    
print "Done, " + str(count) + " IDs extracted!"
    
input_handle.close()
output_handle.close()