'''
Created on June 20, 2012
@author: Carl-Eric Wegner - AG Liesack - Molecular Ecology - MPI Marburg
The given script processes BLAST results from BLASTing putative mRNA reads against the latest
release of RFAM. It is intended to RFAM hit and non-hit sequences. Reads with RFAM hits and 
mRNA reads are written to separate files for downstream processing.
'''
from Bio.Blast import NCBIXML
from Bio import SeqIO

blastRFAM = NCBIXML.parse(open("/home/calle/Desktop/RNA_Seq_20130827/BS7dB_to_RFAM.xml","rU"))    #xml searched against RFAM
output_RFAM = open("/home/calle/Desktop/RNA_Seq_20130827/BS7dB_to_RFAM.fasta","w")    #seqs assigned to as RFAM RNA
output_mRNA = open("/home/calle/Desktop/RNA_Seq_20130827/BS7dB_mRNA_reads.fasta","w")  #seqs assigned to mRNA
fasta_handle = open("/home/calle/Desktop/RNA_Seq_20130827/BS7dB_to_non_rRNA.fasta","rU")   #fasta used in BLAST search

seq_list0=[]
bits_against_RFAM=[]
RFAM_hits=[]
mRNA=[]

##  sequences feature matches in RFAM
for record0 in blastRFAM:   ## referring to RFAM output
    if record0.alignments:
        ab=record0.query
        cd=ab[0:14]
        seq_list0.append(cd)
        bits_against_RFAM.append(record0.alignments[0].hsps[0].bits)

## write sequence IDs to RFAM hits
for name in seq_list0:
    RFAM_hits.append(name)
    
RFAM_reads=[]
mRNA_reads=[]

## match RFAM hits sequence IDs with IDs from original .fasta
for record in SeqIO.parse(fasta_handle,"fasta"):
    if record.id in RFAM_hits:
        RFAM_reads.append(record)
    else:
        mRNA_reads.append(record)

SeqIO.write(RFAM_reads, output_RFAM, "fasta")
SeqIO.write(mRNA_reads, output_mRNA, "fasta")
print "Found %i reads with RFAM hits." % len(RFAM_reads)
print "Found %i high probability mRNA reads." % len(mRNA_reads)

blastRFAM.close()
output_RFAM.close()
output_mRNA.close()
