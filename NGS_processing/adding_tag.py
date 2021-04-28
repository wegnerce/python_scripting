from Bio import SeqIO

input_handle1 = open("/home/calle/Desktop/resequencing/processing/4_ribo-tag/tagged/St7d_III_ribo.fasta","rU")
output_handle1 = open("/home/calle/Desktop/resequencing/processing/4_ribo-tag/tagged/St7d_III_ribo_tagged.fasta","w")

input_handle2 = open("/home/calle/Desktop/resequencing/processing/4_ribo-tag/tagged/St7d_IV_ribo.fasta","rU")
output_handle2 = open("/home/calle/Desktop/resequencing/processing/4_ribo-tag/tagged/St7d_IV_ribo_tagged.fasta","w")

input_handle3 = open("/home/calle/Desktop/resequencing/processing/4_ribo-tag/tagged/Con7d_III_ribo.fasta","rU")
output_handle3 = open("/home/calle/Desktop/resequencing/processing/4_ribo-tag/tagged/Con7d_III_ribo_tagged.fasta","w")

input_handle4 = open("/home/calle/Desktop/resequencing/processing/4_ribo-tag/tagged/Con7d_IV_ribo.fasta","rU")
output_handle4 = open("/home/calle/Desktop/resequencing/processing/4_ribo-tag/tagged/Con7d_IV_ribo_tagged.fasta","w")

input_handle5 = open("/home/calle/Desktop/resequencing/processing/4_ribo-tag/tagged/Cel7d_III_ribo.fasta","rU")
output_handle5 = open("/home/calle/Desktop/resequencing/processing/4_ribo-tag/tagged/Cel7d_III_ribo_tagged.fasta","w")


input_handle6 = open("/home/calle/Desktop/resequencing/processing/4_ribo-tag/tagged/Cel7d_IV_ribo.fasta","rU")
output_handle6 = open("/home/calle/Desktop/resequencing/processing/4_ribo-tag/tagged/Cel7d_IV_ribo_tagged.fasta","w")

input_handle7 = open("/home/calle/Desktop/resequencing/processing/4_ribo-tag/tagged/Chi7d_III_ribo.fasta","rU")
output_handle7 = open("/home/calle/Desktop/resequencing/processing/4_ribo-tag/tagged/Chi7d_III_ribo_tagged.fasta","w")

input_handle8 = open("/home/calle/Desktop/resequencing/processing/4_ribo-tag/tagged/Chi7d_IV_ribo.fasta","rU")
output_handle8 = open("/home/calle/Desktop/resequencing/processing/4_ribo-tag/tagged/Chi7d_IV_ribo_tagged.fasta","w")

input_handle9 = open("/home/calle/Desktop/resequencing/processing/4_ribo-tag/tagged/Xyl7d_III_ribo.fasta","rU")
output_handle9 = open("/home/calle/Desktop/resequencing/processing/4_ribo-tag/tagged/Xyl7d_III_ribo_tagged.fasta","w")

input_handle10 = open("/home/calle/Desktop/resequencing/processing/4_ribo-tag/tagged/Xyl7d_IV_ribo.fasta","rU")
output_handle10 = open("/home/calle/Desktop/resequencing/processing/4_ribo-tag/tagged/Xyl7d_IV_ribo_tagged.fasta","w")

input_handle11 = open("/home/calle/Desktop/resequencing/processing/4_ribo-tag/tagged/St28d_III_ribo.fasta","rU")
output_handle11 = open("/home/calle/Desktop/resequencing/processing/4_ribo-tag/tagged/St28d_III_ribo_tagged.fasta","w")

input_handle12 = open("/home/calle/Desktop/resequencing/processing/4_ribo-tag/tagged/St28d_IV_ribo.fasta","rU")
output_handle12 = open("/home/calle/Desktop/resequencing/processing/4_ribo-tag/tagged/St28d_IV_ribo_tagged.fasta","w")

input_handle13 = open("/home/calle/Desktop/resequencing/processing/4_ribo-tag/tagged/Con28d_III_ribo.fasta","rU")
output_handle13 = open("/home/calle/Desktop/resequencing/processing/4_ribo-tag/tagged/Con28d_III_ribo_tagged.fasta","w")

input_handle14 = open("/home/calle/Desktop/resequencing/processing/4_ribo-tag/tagged/Con28d_IV_ribo.fasta","rU")
output_handle14 = open("/home/calle/Desktop/resequencing/processing/4_ribo-tag/tagged/Con28d_IV_ribo_tagged.fasta","w")

input_handle15 = open("/home/calle/Desktop/resequencing/processing/4_ribo-tag/tagged/Cel28d_III_ribo.fasta","rU")
output_handle15 = open("/home/calle/Desktop/resequencing/processing/4_ribo-tag/tagged/Cel28d_III_ribo_tagged.fasta","w")

input_handle16 = open("/home/calle/Desktop/resequencing/processing/4_ribo-tag/tagged/Cel28d_IV_ribo.fasta","rU")
output_handle16 = open("/home/calle/Desktop/resequencing/processing/4_ribo-tag/tagged/Cel28d_IV_ribo_tagged.fasta","w")

input_handle17 = open("/home/calle/Desktop/resequencing/processing/4_ribo-tag/tagged/Chi28d_III_ribo.fasta","rU")
output_handle17 = open("/home/calle/Desktop/resequencing/processing/4_ribo-tag/tagged/Chi28d_III_ribo_tagged.fasta","w")

input_handle18 = open("/home/calle/Desktop/resequencing/processing/4_ribo-tag/tagged/Chi28d_IV_ribo.fasta","rU")
output_handle18 = open("/home/calle/Desktop/resequencing/processing/4_ribo-tag/tagged/Chi28d_IV_ribo_tagged.fasta","w")

input_handle19 = open("/home/calle/Desktop/resequencing/processing/4_ribo-tag/tagged/Xyl28d_III_ribo.fasta","rU")
output_handle19 = open("/home/calle/Desktop/resequencing/processing/4_ribo-tag/tagged/Xyl28d_III_ribo_tagged.fasta","w")

input_handle20 = open("/home/calle/Desktop/resequencing/processing/4_ribo-tag/tagged/Xyl28d_IV_ribo.fasta","rU")
output_handle20 = open("/home/calle/Desktop/resequencing/processing/4_ribo-tag/tagged/Xyl28d_IV_ribo_tagged.fasta","w")


'''
input_handle21 = open("/home/calle/Desktop/ribo-tag_polymer_eukarya/sorted_euk/fasta/ribo-tags_euk_con28dIII.fasta","rU")
output_handle21 = open("/home/calle/Desktop/ribo-tag_polymer_eukarya/tagged/ribo-tags_euk_con28dIII.fasta","w")

input_handle22 = open("/home/calle/Desktop/ribo-tag_polymer_eukarya/sorted_euk/fasta/ribo-tags_euk_cel28dI.fasta","rU")
output_handle22 = open("/home/calle/Desktop/ribo-tag_polymer_eukarya/tagged/ribo-tags_euk_cel28dI.fasta","w")

input_handle23 = open("/home/calle/Desktop/ribo-tag_polymer_eukarya/sorted_euk/fasta/ribo-tags_euk_cel28dII.fasta","rU")
output_handle23 = open("/home/calle/Desktop/ribo-tag_polymer_eukarya/tagged/ribo-tags_euk_cel28dII.fasta","w")

input_handle24 = open("/home/calle/Desktop/ribo-tag_polymer_eukarya/sorted_euk/fasta/ribo-tags_euk_cel28dIII.fasta","rU")
output_handle24 = open("/home/calle/Desktop/ribo-tag_polymer_eukarya/tagged/ribo-tags_euk_cel28dIII.fasta","w")

input_handle25 = open("/home/calle/Desktop/ribo-tag_polymer_eukarya/sorted_euk/fasta/ribo-tags_euk_chi28dI.fasta","rU")
output_handle25 = open("/home/calle/Desktop/ribo-tag_polymer_eukarya/tagged/ribo-tags_euk_chi28dI.fasta","w")

input_handle26 = open("/home/calle/Desktop/ribo-tag_polymer_eukarya/sorted_euk/fasta/ribo-tags_euk_chi28dII.fasta","rU")
output_handle26 = open("/home/calle/Desktop/ribo-tag_polymer_eukarya/tagged/ribo-tags_euk_chi28dII.fasta","w")

input_handle27 = open("/home/calle/Desktop/ribo-tag_polymer_eukarya/sorted_euk/fasta/ribo-tags_euk_chi28dIII.fasta","rU")
output_handle27 = open("/home/calle/Desktop/ribo-tag_polymer_eukarya/tagged/ribo-tags_euk_chi28dIII.fasta","w")

input_handle28 = open("/home/calle/Desktop/ribo-tag_polymer_eukarya/sorted_euk/fasta/ribo-tags_euk_xyl28dI.fasta","rU")
output_handle28 = open("/home/calle/Desktop/ribo-tag_polymer_eukarya/tagged/ribo-tags_euk_xyl28dI.fasta","w")

input_handle29 = open("/home/calle/Desktop/ribo-tag_polymer_eukarya/sorted_euk/fasta/ribo-tags_euk_xyl28dII.fasta","rU")
output_handle29 = open("/home/calle/Desktop/ribo-tag_polymer_eukarya/tagged/ribo-tags_euk_xyl28dII.fasta","w")

input_handle30 = open("/home/calle/Desktop/ribo-tag_polymer_eukarya/sorted_euk/fasta/ribo-tags_euk_xyl28dIII.fasta","rU")
output_handle30 = open("/home/calle/Desktop/ribo-tag_polymer_eukarya/tagged/ribo-tags_euk_xyl28dIII.fasta","w")
'''

def add_MID(records, mid):
    i=0
    for record in records:
        tagged_seq = mid + record.seq
        record.seq = tagged_seq
        yield record

# RLMIDs are used as tags, see GS Junior MIDConfig.parse

original_reads = SeqIO.parse(input_handle1,"fasta")
tagged_reads = add_MID(original_reads, "GAGATC")
count = SeqIO.write(tagged_reads, output_handle1, "fasta")
print "Saved %i reads" % count

original_reads = SeqIO.parse(input_handle2,"fasta")
tagged_reads = add_MID(original_reads, "GTCACA")
count = SeqIO.write(tagged_reads, output_handle2, "fasta")
print "Saved %i reads" % count

original_reads = SeqIO.parse(input_handle3,"fasta")
tagged_reads = add_MID(original_reads, "TAGCAT")
count = SeqIO.write(tagged_reads, output_handle3, "fasta")
print "Saved %i reads" % count

original_reads = SeqIO.parse(input_handle4,"fasta")
tagged_reads = add_MID(original_reads, "TCGAGA")
count = SeqIO.write(tagged_reads, output_handle4, "fasta")
print "Saved %i reads" % count

original_reads = SeqIO.parse(input_handle5,"fasta")
tagged_reads = add_MID(original_reads, "TTTGAG")
count = SeqIO.write(tagged_reads, output_handle5, "fasta")
print "Saved %i reads" % count

original_reads = SeqIO.parse(input_handle6,"fasta")
tagged_reads = add_MID(original_reads, "ACCAAC")
count = SeqIO.write(tagged_reads, output_handle6, "fasta")
print "Saved %i reads" % count

original_reads = SeqIO.parse(input_handle7,"fasta")
tagged_reads = add_MID(original_reads, "CCTTCT")
count = SeqIO.write(tagged_reads, output_handle7, "fasta")
print "Saved %i reads" % count

original_reads = SeqIO.parse(input_handle8,"fasta")
tagged_reads = add_MID(original_reads, "TTCCTC")
count = SeqIO.write(tagged_reads, output_handle8, "fasta")
print "Saved %i reads" % count

original_reads = SeqIO.parse(input_handle9,"fasta")
tagged_reads = add_MID(original_reads, "GGCCCG")
count = SeqIO.write(tagged_reads, output_handle9, "fasta")
print "Saved %i reads" % count

original_reads = SeqIO.parse(input_handle10,"fasta")
tagged_reads = add_MID(original_reads, "CCGGGC")
count = SeqIO.write(tagged_reads, output_handle10, "fasta")
print "Saved %i reads" % count

original_reads = SeqIO.parse(input_handle11,"fasta")
tagged_reads = add_MID(original_reads, "AACCCA")
count = SeqIO.write(tagged_reads, output_handle11, "fasta")
print "Saved %i reads" % count

original_reads = SeqIO.parse(input_handle12,"fasta")
tagged_reads = add_MID(original_reads, "CCAAAC")
count = SeqIO.write(tagged_reads, output_handle12, "fasta")
print "Saved %i reads" % count

original_reads = SeqIO.parse(input_handle13,"fasta")
tagged_reads = add_MID(original_reads, "AATTTA")
count = SeqIO.write(tagged_reads, output_handle13, "fasta")
print "Saved %i reads" % count

original_reads = SeqIO.parse(input_handle14,"fasta")
tagged_reads = add_MID(original_reads, "TTAAAT") 
count = SeqIO.write(tagged_reads, output_handle14, "fasta")
print "Saved %i reads" % count

original_reads = SeqIO.parse(input_handle15,"fasta")
tagged_reads = add_MID(original_reads, "GGAGAG")
count = SeqIO.write(tagged_reads, output_handle15, "fasta")
print "Saved %i reads" % count

original_reads = SeqIO.parse(input_handle16,"fasta")
tagged_reads = add_MID(original_reads, "AAGGGA")
count = SeqIO.write(tagged_reads, output_handle16, "fasta")
print "Saved %i reads" % count

original_reads = SeqIO.parse(input_handle17,"fasta")
tagged_reads = add_MID(original_reads, "ATTATA")
count = SeqIO.write(tagged_reads, output_handle17, "fasta")
print "Saved %i reads" % count

original_reads = SeqIO.parse(input_handle18,"fasta")
tagged_reads = add_MID(original_reads, "TAATAT")
count = SeqIO.write(tagged_reads, output_handle18, "fasta")
print "Saved %i reads" % count

original_reads = SeqIO.parse(input_handle19,"fasta")
tagged_reads = add_MID(original_reads, "GCCGCG")
count = SeqIO.write(tagged_reads, output_handle19, "fasta")
print "Saved %i reads" % count

original_reads = SeqIO.parse(input_handle20,"fasta")
tagged_reads = add_MID(original_reads, "CGGCGC")
count = SeqIO.write(tagged_reads, output_handle20, "fasta")
print "Saved %i reads" % count

'''
original_reads = SeqIO.parse(input_handle21,"fasta")
tagged_reads = add_MID(original_reads, "TACGTA")
count = SeqIO.write(tagged_reads, output_handle21, "fasta")
print "Saved %i reads" % count

original_reads = SeqIO.parse(input_handle22,"fasta")
tagged_reads = add_MID(original_reads, "TAGCAT")
count = SeqIO.write(tagged_reads, output_handle22, "fasta")
print "Saved %i reads" % count

original_reads = SeqIO.parse(input_handle23,"fasta")
tagged_reads = add_MID(original_reads, "TATACG")
count = SeqIO.write(tagged_reads, output_handle23, "fasta")
print "Saved %i reads" % count

original_reads = SeqIO.parse(input_handle24,"fasta")
tagged_reads = add_MID(original_reads, "TCAGAG")
count = SeqIO.write(tagged_reads, output_handle24, "fasta")
print "Saved %i reads" % count

original_reads = SeqIO.parse(input_handle25,"fasta")
tagged_reads = add_MID(original_reads, "TCGAGA")
count = SeqIO.write(tagged_reads, output_handle25, "fasta")
print "Saved %i reads" % count

original_reads = SeqIO.parse(input_handle26,"fasta")
tagged_reads = add_MID(original_reads, "TCTCTC")
count = SeqIO.write(tagged_reads, output_handle26, "fasta")
print "Saved %i reads" % count

original_reads = SeqIO.parse(input_handle27,"fasta")
tagged_reads = add_MID(original_reads, "TTTACG")
count = SeqIO.write(tagged_reads, output_handle27, "fasta")
print "Saved %i reads" % count

original_reads = SeqIO.parse(input_handle28,"fasta")
tagged_reads = add_MID(original_reads, "TTTGAG")
count = SeqIO.write(tagged_reads, output_handle28, "fasta")
print "Saved %i reads" % count

original_reads = SeqIO.parse(input_handle29,"fasta")
tagged_reads = add_MID(original_reads, "TCTAGA")
count = SeqIO.write(tagged_reads, output_handle29, "fasta")
print "Saved %i reads" % count

original_reads = SeqIO.parse(input_handle30,"fasta")
tagged_reads = add_MID(original_reads, "TTTCTC")
count = SeqIO.write(tagged_reads, output_handle30, "fasta")
print "Saved %i reads" % count
'''

input_handle1.close()
output_handle1.close()

input_handle2.close()
output_handle2.close()

input_handle3.close()
output_handle3.close()

input_handle4.close()
output_handle4.close()

input_handle5.close()
output_handle5.close()

input_handle6.close()
output_handle6.close()

input_handle7.close()
output_handle7.close()

input_handle8.close()
output_handle8.close()

input_handle9.close()
output_handle9.close()

input_handle10.close()
output_handle10.close()

input_handle11.close()
output_handle11.close()

input_handle12.close()
output_handle12.close()

input_handle13.close()
output_handle13.close()

input_handle14.close()
output_handle14.close()

input_handle15.close()
output_handle15.close()

input_handle16.close()
output_handle16.close()

input_handle17.close()
output_handle17.close()

input_handle18.close()
output_handle18.close()

input_handle19.close()
output_handle19.close()

input_handle20.close()
output_handle20.close()

'''
input_handle21.close()
output_handle21.close()

input_handle22.close()
output_handle22.close()

input_handle23.close()
output_handle23.close()

input_handle24.close()
output_handle24.close()

input_handle25.close()
output_handle25.close()

input_handle26.close()
output_handle26.close()

input_handle27.close()
output_handle27.close()

input_handle28.close()
output_handle28.close()

input_handle29.close()
output_handle29.close()

input_handle30.close()
output_handle30.close()
'''