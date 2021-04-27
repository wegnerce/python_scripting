'''
CCreated on May 12, 2012
@author: Carl-Eric Wegner AG Liesack - Molecular Ecology - MPI Marburg
The given python scripts lists the number of records and
gives the first and last entry.
'''
from Bio import SeqIO
handle = open("/home/calle/Python/BioPython/tutorial/orchid.gbk")
records = list(SeqIO.parse(handle, "genbank"))

print "Identified %i records" % len(records)

print "The last record"
last_record = records [-1] 
print last_record.id
print repr(last_record.seq)
print len(last_record)

print "The first record"
first_record = records [0] 
print first_record.id
print repr(first_record.seq)
print len(first_record)
