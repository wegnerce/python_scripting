# needed modules
import os
from Bio import SeqIO

# helper variables, constants, paths
barcodes = ["GAGATC", "GTCACA", "TAGCAT", "TCGAGA", "TTTGAG", "ACCAAC", \
        "CCTTCT", "TTCCTC", "GGCCCG", "CCGGGC", "AACCCA", "CCAAAC", "AATTTA", \
        "TTAAAT", "GGAGAG", "AAGGGA", "ATTATA", "TAATAT", "GCCGCG", "CGGCGC", \
        "TACGTA", "TAGCAT", "TATACG", "TCAGAG", "TCGAGA", "TCTCTC", "TTTACG", \
        "TTTGAG", "TCTAGA", "TTTCTC"]

mapping_list = []
        
to_add_dir = "/home/calle/Desktop/MBGW_test/forward_for_tagging/"
i = 0

# add artificial barcode functions
def add_barcode(records, barcode):
    for record in records:
        tagged_seq = barcode + record.seq
        record.seq = tagged_seq
        yield record

def add_barcode_fastq(records, barcode):
    for record in records:
        tagged_seq = barcode + record.seq
        tagged_qual = [40] * 6 + record.letter_annotations["phred_quality"]
        record.letter_annotations = {}
        record.seq = tagged_seq[:-6]
        record.letter_annotations["phred_quality"] = tagged_qual[:-6]
        yield record

# iterate over files to process in given directory
os.chdir(to_add_dir)
for filename in sorted(os.listdir(to_add_dir)):
    if filename.endswith(".fasta"):
        print "Busy with: " + filename
        print "..adding barcode: " + barcodes[i]
        mapping_list.append([filename, barcodes[i]])
        input_handle = open(filename, "rU")
        original_reads = SeqIO.parse(input_handle,"fasta")
        barcoded_reads = add_barcode(original_reads, barcodes[i])
        barcoded_reads_path = open(filename + ".barcoded", "w")                
        count = SeqIO.write(barcoded_reads, barcoded_reads_path, "fasta")
        print "Barcode " + barcodes[i] + " added to %i reads." % count
        barcoded_reads_path.close()
        i = i + 1
    elif filename.endswith(".fastq"):
		 print "Busy with: " + filename
		 print "..adding barcode: " + barcodes[i] 
		 mapping_list.append([filename, barcodes[i]])
		 input_handle = open(filename, "rU")
		 original_reads = SeqIO.parse(input_handle,"fastq")
		 barcoded_reads = add_barcode_fastq(original_reads, barcodes[i])
		 barcoded_reads_path = open(filename + ".barcoded", "w")                
		 count = SeqIO.write(barcoded_reads, barcoded_reads_path, "fastq")
		 print "Barcode " + barcodes[i] + " added to %i reads." % count
		 barcoded_reads_path.close()
		 i = i + 1
 
print mapping_list