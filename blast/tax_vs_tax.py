'''
Created on May 1, 2014
@author: Carl-Eric - AG Liesack - Molecular Ecology - MPI Marburg
The given script compares BLAST outputs from PRINSEQ processed .fasta files, which have
been BLASTed against the latest release of SILVA NR SSU/LSU. Based on the comparison the
script generates three output files:
(1) sequence reads assigned to SILVA SSU - XYZ_to_SSU.fasta
(2) sequence reads assigned to SILVA LSU - XYZ_to_LSU.fasta
(3) sequence reads assigned to putative mRNA - XYZ_to_nohit_reads
'''
from Bio.Blast import NCBIXML
from Bio import SeqIO
from Bio import SearchIO

blast_taxA = NCBIXML.parse(open("/home/calle/Desktop/taxon_specific_blastdbs/to_be_blasted/Day_28/mRNA_BS28day_clost.xml","rU"))    #blast output from taxon A specific database
blast_taxB = NCBIXML.parse(open("/home/calle/Desktop/taxon_specific_blastdbs/to_be_blasted/Day_28/mRNA_BS28day_lachno.xml","rU"))    #blast output from taxon B specific database
output_taxA = open("/home/calle/Desktop/taxon_specific_blastdbs/to_be_blasted/Day_28/mRNA_BS28day_clost_lachno.fasta","w")    #seqs assigned to taxon A
output_taxB = open("/home/calle/Desktop/taxon_specific_blastdbs/to_be_blasted/Day_28/mRNA_BS28day_lachno_clost.fasta","w")    #seqs assigned taxon B
output_specific = open("/home/calle/Desktop/taxon_specific_blastdbs/to_be_blasted/Day_28/clost_lachno_nohit_reads.fasta","w")  #seqs with no macthes in either A or B
fasta_handle=open("/home/calle/Desktop/taxon_specific_blastdbs/to_be_blasted/Day_28/mRNA_BS28day.fasta","rU")   #fasta used in BLAST search

i=0
ii=0
seq_list0=[]
bits_against_taxA=[]

##  Sequences have matches to taxon A
for record0 in blast_taxA:   
    if record0.alignments:
        ab=record0.query
        cd=ab[0:14]
        seq_list0.append(cd)
        bits_against_taxA.append(record0.alignments[0].hsps[0].bits)
        i=i+1
    else:
        ii=ii+1
print "Matches for Taxon A:",i, ii

## Sequences have matches to taxon B
j=0
jj=0
seq_list1=[] 
bits_against_taxB=[]
ab=[]
for record1 in blast_taxB:  
    if record1.alignments:
        ab=record1.query
        cd=ab[0:14]
        seq_list1.append(cd)
        bits_against_taxB.append(record1.alignments[0].hsps[0].bits)
        j=j+1
    else:
        jj=jj+1
print "Matches for Taxon B:",j,jj

count_taxA_taxB=0
count_taxB_taxA=0
count_only_taxA=0
count_taxB=0
p=0
taxA=[]
taxB=[]
for name in seq_list0:
#    print name
    if name in seq_list1:
        x=seq_list1.index(name)
        if bits_against_taxA[p] > bits_against_taxB[x]:
            count_taxA_taxB = count_taxA_taxB + 1
            taxA.append(name)
        else:
            count_taxB_taxA = count_taxB_taxA + 1
    else:
        count_only_taxA=count_only_taxA+1
        taxA.append(name)
    p=p+1
print "##########################################################################"
print "Matches for Taxon A:", p
print "Bit score Taxon A > Taxon B:", count_taxA_taxB
print "Taxon B > Taxon A:", count_taxB_taxA
print "Only hits for Taxon A:", count_only_taxA

count_taxA_taxB=0
count_taxB_taxA=0
count_only_taxB=0
count_taxB=0
p=0

for name in seq_list1:
    if name in seq_list0:
        x=seq_list0.index(name)
        if bits_against_taxB[p] >= bits_against_taxA[x]:
            count_taxB_taxA = count_taxB_taxA + 1
            taxB.append(name)
        else:
            count_taxA_taxB = count_taxA_taxB + 1
    else:
        count_only_taxB=count_only_taxB+1
        taxB.append(name)
    p=p+1
print "########################################################################"
print "Matches for Taxon B:", p
print "Bit score Taxon B > Taxon A:", count_taxB_taxA
print "Taxon A > Taxon B", count_taxA_taxB
print "Only hits for Taxon B:", count_only_taxB 

print len(taxA)
print len(taxB)

z=0
taxA_reads=[]
taxB_reads=[]
nohit_reads=[]
for record in SeqIO.parse(fasta_handle,"fasta"):
    if record.id in taxA:
        taxA_reads.append(record)
    elif record.id in taxB:
        taxB_reads.append(record)
    else:
        nohit_reads.append(record)

SeqIO.write(taxA_reads, output_taxA, "fasta")
SeqIO.write(taxB_reads, output_taxB, "fasta")
SeqIO.write(nohit_reads, output_specific, "fasta")     
print "Found %i Taxon A specific reads" % len(taxA_reads)
print "Found %i Taxon B specific reads" % len(taxB_reads)
print "Found %i no hit reads" % len(nohit_reads)

blast_taxA.close()
blast_taxB.close()
output_taxA.close()
output_taxB.close()
output_specific.close()

input_xml = open("/home/calle/Desktop/taxon_specific_blastdbs/to_be_blasted/Day_28/mRNA_BS28day_clost.xml","rU")   #XML blasted against SILVA SSU
output_xml=open("/home/calle/Desktop/taxon_specific_blastdbs/to_be_blasted/Day_28/mRNA_BS28day_clost_f_lachno.xml","w") #new XML assigned to SSU rRNA
tax_fasta = open("/home/calle/Desktop/taxon_specific_blastdbs/to_be_blasted/Day_28/mRNA_BS28day_clost_lachno.fasta","rU")   #seq of SSU rRNA

# create a generator for the raw BLAST results
raw_qresults = (qresult for qresult in SearchIO.parse(input_xml, 'blast-xml'))
# parse gene contigs, removing trailing whitespace
to_filter = []
for seq_record in SeqIO.parse(tax_fasta, "fasta"):
    to_filter.append(seq_record.id)
# filter the BLAST results
filtered_records = (qresult for qresult in raw_qresults if qresult.id in to_filter)
# and write to an XML file
SearchIO.write(filtered_records, output_xml, 'blast-xml')

print "DONE... !"

'''
xml_handle = open("/home/calle/Desktop/taxon_specific_blastdbs/to_be_blasted/mRNA_BS1day_clost.xml","rU")   #XML blasted against SILVA SSU

output_handle0=open("/home/calle/Desktop/taxon_specific_blastdbs/to_be_blasted/mRNA_BS1day_clost_f_lachno.xml","w") #new XML assigned to SSU rRNA

handle0 = open("/home/calle/Desktop/taxon_specific_blastdbs/to_be_blasted/mRNA_BS1day_clost.fasta","rU")   #seq of SSU rRNA

target_0=[]

archaea_seq=[]
n=0
m=0
str_list=[]
query_id=[]

#########################################################################
#   import target sequences as fasta files in which we are interested   #
#   put sequence id in list(target_no)                                  #
#########################################################################
no_target_seq0=0
for record in SeqIO.parse(handle0,"fasta"): 
    target_0.append(record.id)
    no_target_seq0=no_target_seq0+1

no_target_seq1=0

print "No. of target sequence 0:", no_target_seq0

########################################################################
#   write blastout of target sequences                                 #
########################################################################
no_query_in_xml=0
name=[]
only_id={}
no_target_0=0
#no_target_1=0
#no_target_2=0
i=0
judge=3
for line in xml_handle.readlines():
    str_line=line.encode('ascii','ignore')
    if i < 22:
        output_handle0.write(str_line)
        i=i+1
    str_list=str_line.split(">")
    if str_list[0] == "      <Iteration_query-def":
        query_id=str_list[1].split("<")
        name=query_id[0]
        only_id=name[0:14]
        no_query_in_xml=no_query_in_xml+1
        if only_id in target_0:
            judge = 0
            no_target_0=no_target_0+1
        else:
            judge = 3
    if judge == 0:
        output_handle0.write(str_line)

print "no_of_queries_in_original xml output:", no_query_in_xml  
print "no. of query in target sequence files:", no_target_0
handle0.close()
xml_handle.close()
output_handle0.close()
'''