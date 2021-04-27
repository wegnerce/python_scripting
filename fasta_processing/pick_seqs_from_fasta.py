'''
Created on November 5, 2012
@author: Carl-Eric Wegner - AG Liesack - Molecular Ecology - MPI Marburg
The script below extracts sequences from an indicated .fasta file (input_file)
using a specified list of sequences IDs(id_file, plain .txt file) and saves them
in a separate .fasta file (output_file)  
'''


from Bio import SeqIO
import sys

wanted = sys.argv[1]
input_file = sys.argv[2]
output_file = sys.argv[3]
### open files to be processed, original .fasta, files with IDs of interest,
### outpu file, .fasta
#input_file = "/home/lu87neb/databases/nr/nr_20160809.fasta"
#id_file = "/home/calle/Desktop/tonb.fasta"
#output_file = "/home/lu87neb/databases/nr/nr_20160809_bacteria.fasta"
#output_file = "/media/STORAGE1/Stasja_pro/to_filter/ribotags/Stasja_ribotag/assigned_taxonomy/plancto_seq_ids_seqids.txt"
records_to_save = []

### read ID file
#wanted = set(line.rstrip("\n").split(None,1)[0] for line in open(id_file))
#wanted = set(taxomias.AllAccByTaxid(2))
#primer = ".B"
#print "Found %i unique identifiers in %s" % (len(wanted), id_file)

### parse original .fasta and check respective IDs with IDs given
### in the ID file
#records = (r for r in SeqIO.parse(input_file, "fasta") if r.id in wanted and primer in r.description)
records = (r for r in SeqIO.parse(input_file, "fasta") if wanted in r.description)
#ids = (r.description[r.description.find(" ")+1:r.description.find("=")-8] for r in SeqIO.parse(input_file, "fasta") if r.id in wanted)
count = SeqIO.write(records, output_file, "fasta")
'''
with open(output_file, "wb") as outfile:
    for entry in ids:
        outfile.write("%s\n" % entry)
'''    

### Summary
print "Saved %i records from %s to %s" % (count, input_file, output_file)
#if count < len(wanted):
#    print "Warning %i IDs not found in %s" % (len(wanted)-count, input_file)

print "Job fulfilled!"



# THE VERSION BELOW IS MORE EFFICIENT IN TERMS OF COMPUTING, KEEP IN MIND
# WHILE WORKING ON BIG DATA SETS

'''
from Bio import SeqIO

input_file = "/home/calle/Desktop/cbbL/extracted_AA.fasta"
id_file = "/home/calle/Desktop/cbbL/ids.txt"
output_file = "/home/calle/Desktop/cbbL/extracted_AA_corr.fasta"

wanted = set(line.rstrip("\n").split(None,1)[0] for line in open(id_file))
print "Found %i unique identifiers in %s" % (len(wanted), id_file)

index = SeqIO.index(input_file, "fasta")
records = (index[r] for r in wanted)
count = SeqIO.write(records, output_file, "fasta")
assert count == len(wanted)

print "Saved %i records from %s to %s" % (count, input_file, output_file)
'''


