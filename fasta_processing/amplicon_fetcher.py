"""
Created on Mon Jul 29 15:59:45 2013
@author: Carl-Eric Wegner - AG Liesack - Molecular Ecology - MPI Marburg
The rationale behind this script is to check collections/databases of sequences
deposited as .fasta fo the presence of particular amplicons. This is for instance
of importance when setting up reference databases for less-well covered
functional genes.
"""

from Bio import SeqIO


def check_sequences(input, primer):
    for rec in input:
        if any(item in rec.seq for item in primer): #check the presence of primers
            yield rec  # if primer present, retrieve record

for_primer = ('ACCACCAAGCCGAAGCTCGG', 'ACCACCAAGCCGAAGCTGGG', #degenerate primers of interest
           'ACCACCAAGCCCAAGCTGGG', 'ACCACCAAGCCCAAGCTCGG',
           'ACCATCAAGCCGAAGCTCGG', 'ACCATCAAGCCGAAGCTGGG',
           'ACCATCAAGCCCAAGCTGGG', 'ACCATCAAGCCCAAGCTCGG')
'''            
rev_primer = ('GCCTTCCAGCTTGCCCACCAC', 'GCCTTCCAGCTTGCCCACCGC',
           'GCCTTCCAGCTTGCCGACCGC', 'GCCTTCCAGCTTGCCGACCAC',
           'GCCTTCGAGCTTGCCCACCAC', 'GCCTTCGAGCTTGCCCACCGC',
           'GCCTTCGAGCTTGCCGACCGC', 'GCCTTCGAGCTTGCCGACCAC')
'''

rev_primer = ('CGGAAGGTCGAACGGGTGGTG', 'CGGAAGGTCGAACGGGTGGCG',
           'CGGAAGGTCGAACGGCTGGCG', 'CGGAAGGTCGAACGGCTGGTG',
           'CGGAAGCTCGAACGGGTGGTG', 'CGGAAGCTCGAACGGGTGGCG',
           'CGGAAGCTCGAACGGCTGGCG', 'CGGAAGCTCGAACGGCTGGTG')
           
SeqIO.write(check_sequences(SeqIO.parse('/home/calle/Desktop/refdb_test_filtered.fasta', 'fasta'), for_primer),
            '/home/calle/Desktop/fetched.fasta', 'fasta') #two-step check, sequences containing the forwards primer are stored...
        
SeqIO.write(check_sequences(SeqIO.parse('/home/calle/Desktop/fetched.fasta', 'fasta'), rev_primer),
            '/home/calle/Desktop/refdb_amplicons_only.fasta', 'fasta') #...and subsequently checked for the reverse primer
            

