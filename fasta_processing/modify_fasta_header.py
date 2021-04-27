# -*- coding: utf-8 -*-
"""
created on January 17, 2013
@author: Carl-Eric Wegner - AG Liesack - Molecular Ecology - MPI Marburg
A plain script extracting enabling the modification of fasta header lines, by easily
processing the headers as strings.
"""

from Bio import SeqIO
import taxman as tx

input_headers = open("/home/calle/Storage_II/Data/mxaF_xoxF/headers.txt", "rb")
input_handle = open("/home/calle/Storage_II/Data/mxaF_xoxF/PQQ_ADH_Keltjens.faa", "rb")
output_handle = open("/home/calle/Storage_II/Data/mxaF_xoxF/PQQ_ADH_Keltjens_renamed.faa", "wb")

new_headers = input_headers.read().split("\n")
print new_headers

#new_record_id = ""
#ids = []
#i = 0
#j = 0

for seq_record in SeqIO.parse(input_handle, "fasta"):
	#i = i + float(seq_record.description.split(" ")[3].split("_")[0])
	#j = j + float(seq_record.description.split(" ")[3].split("_")[1])
	#j = j + 1
    for entry in new_headers:
        if entry.split("|")[1] in seq_record.id:
            new_record_id = entry
	#seq_record.id = "H53_A13" + "_" + str(j) + "_" + str(len(seq_record.seq))
	#output_handle.write(">%s%s\n%s\n" % (
    output_handle.write(">%s\n%s\n" % (
			#seq_record.id[:13],
			#seq_record.id,
            new_record_id,
			#seq_record.description[seq_record.description.find(" "):],
			#seq_record.description,
			seq_record.seq))
#print str(i)
#print str(j)
'''
   print "_".join(seq_record.description.split("[")[1].replace("]", "").split(" "))
    i = i+1
    j = 1
    if "_".join(seq_record.description.split("[")[1].replace("]", "").split(" ")) not in ids:
        new_record_id = "_".join(seq_record.description.split("[")[1].replace("]", "").split(" "))
        ids.append(new_record_id)
        #new_record_id = "Xylan_" + str(i)
        #new_record_id = seq_record.id + ".2"
        output_handle.write(">%s\n%s\n" % (
               #seq_record.id[:13],
               new_record_id,
               #seq_record.description[15:],
               seq_record.seq))
    elif "_".join(seq_record.description.split("[")[1].replace("]", "").split(" ")) in ids:
        j = 2
        if not "_".join(seq_record.description.split("[")[1].replace("]", "").split(" ")) + "_" + str(j) in ids:
            new_record_id = "_".join(seq_record.description.split("[")[1].replace("]", "").split(" ")) + "_" + str(j)
            ids.append(new_record_id)
            output_handle.write(">%s\n%s\n" % (
               #seq_record.id[:13],
               new_record_id,
               #seq_record.description[15:],
               seq_record.seq))
        elif "_".join(seq_record.description.split("[")[1].replace("]", "").split(" ")) + "_" + str(j) in ids:
            j = 3
            new_record_id = "_".join(seq_record.description.split("[")[1].replace("]", "").split(" ")) + "_" + str(j)
            ids.append(new_record_id)
            output_handle.write(">%s\n%s\n" % (
               #seq_record.id[:13],
               new_record_id,
               #seq_record.description[15:],
               seq_record.seq))
'''
print "Done, Headers successfully modified!"
input_headers.close()
input_handle.close()
output_handle.close()