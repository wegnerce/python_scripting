'''
Created on June 18, 2012
@author: Carl-Eric - AG Liesack - Molecular Ecology - MPI Marburg
The given script compares BLAST outputs from PRINSEQ processed .fasta files, which have
been BLASTed against the latest release of SILVA NR SSU/LSU. Based on the comparison the
script generates three output files:
(1) sequence reads assigned to SILVA SSU - XYZ_to_SSU.fasta
(2) sequence reads assigned to SILVA LSU - XYZ_to_LSU.fasta
(3) sequence reads assigned to putative mRNA - XYZ_to_non_rRNA
'''
from Bio.Blast import NCBIXML
from Bio import SeqIO

blastLSU = NCBIXML.parse(open("/home/calle/Desktop/RNA_Seq_20130827/BS7dB_to_LSU.xml","rU"))    #xml searched against LSU
blastSSU = NCBIXML.parse(open("/home/calle/Desktop/RNA_Seq_20130827/BS7dB_to_SSU.xml","rU"))    #xml searched against SSU
output_LSU = open("/home/calle/Desktop/RNA_Seq_20130827/BS7dB_to_LSU.fasta","w")    #seqs assigned to LSU rRNA
output_SSU = open("/home/calle/Desktop/RNA_Seq_20130827/BS7dB_to_SSU.fasta","w")    #seqs assigned to SSU rRNA
output_mRNA = open("/home/calle/Desktop/RNA_Seq_20130827/BS7dB_to_non_rRNA.fasta","w")  #seqs assigned to mRNA
fasta_handle=open("/home/calle/Desktop/RNA_Seq_20130827/BS7d_controlB_prinseq_good.fasta","rU")   #fasta used in BLAST search

i=0
ii=0
seq_list0=[]
bits_against_LSU=[]

##  Sequences have matches in LSU
for record0 in blastLSU:   ## LSU
    if record0.alignments:
        ab=record0.query
        cd=ab[0:14]
        seq_list0.append(cd)
        bits_against_LSU.append(record0.alignments[0].hsps[0].bits)
        i=i+1
    else:
        ii=ii+1
print "LSU:",i, ii

## Sequences have matches in SSU
j=0
jj=0
seq_list1=[] 
bits_against_SSU=[]
ab=[]
for record1 in blastSSU:  ## SSU
    if record1.alignments:
        ab=record1.query
        cd=ab[0:14]
        seq_list1.append(cd)
        bits_against_SSU.append(record1.alignments[0].hsps[0].bits)
        j=j+1
    else:
        jj=jj+1
print "SSU:",j,jj


count_LSU_SSU=0
count_SSU_LSU=0
count_only_LSU=0
count_SSU=0
p=0
LSU=[]
SSU=[]
for name in seq_list0:
#    print name
    if name in seq_list1:
        x=seq_list1.index(name)
        if bits_against_LSU[p] > bits_against_SSU[x]:
            count_LSU_SSU = count_LSU_SSU + 1
            LSU.append(name)
        else:
            count_SSU_LSU = count_SSU_LSU + 1
    else:
        count_only_LSU=count_only_LSU+1
        LSU.append(name)
    p=p+1
print "##########################################################################"
print "LSU:", p
print "LSU > SSU:", count_LSU_SSU
print "SSU > LSU:", count_SSU_LSU
print "only found in LSU:", count_only_LSU

count_LSU_SSU=0
count_SSU_LSU=0
count_only_SSU=0
count_SSU=0
p=0

for name in seq_list1:
    if name in seq_list0:
        x=seq_list0.index(name)
        if bits_against_SSU[p] >= bits_against_LSU[x]:
            count_SSU_LSU = count_SSU_LSU + 1
            SSU.append(name)
        else:
            count_LSU_SSU = count_LSU_SSU + 1
    else:
        count_only_SSU=count_only_SSU+1
        SSU.append(name)
    p=p+1
print "########################################################################"
print "SSU:", p
print "SSU > LSU:", count_SSU_LSU
print "LSU > SSU:", count_LSU_SSU
print "only found in SSU:", count_only_SSU 

print len(LSU)
print len(SSU)

z=0
LSU_rRNA=[]
SSU_rRNA=[]
non_rRNA=[]
for record in SeqIO.parse(fasta_handle,"fasta"):
    if record.id in LSU:
        LSU_rRNA.append(record)
    elif record.id in SSU:
        SSU_rRNA.append(record)
    else:
        non_rRNA.append(record)

SeqIO.write(LSU_rRNA, output_LSU, "fasta")
SeqIO.write(SSU_rRNA, output_SSU, "fasta")
SeqIO.write(non_rRNA, output_mRNA, "fasta")     
print "Found %i LSU rRNA" % len(LSU_rRNA)
print "Found %i SSU rRNA" % len(SSU_rRNA)
print "Found %i non rRNA" % len(non_rRNA)

blastLSU.close()
blastSSU.close()
output_LSU.close()
output_SSU.close()
output_mRNA.close()

xml_handle = open("/home/calle/Desktop/RNA_Seq_20130827/BS7dB_to_SSU.xml","rU")   #XML blasted against SILVA SSU

output_handle0=open("/home/calle/Desktop/RNA_Seq_20130827/BS7dB_to_SSU_ribotag.xml","w") #new XML assigned to SSU rRNA

handle0 = open("/home/calle/Desktop/RNA_Seq_20130827/BS7dB_to_SSU.fasta","rU")   #seq of SSU rRNA




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
