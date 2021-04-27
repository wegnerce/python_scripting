f0=open("/home/calle/Desktop/RL1_to_SSU_ribotag_end.xml","r")
f1=open("/home/calle/Desktop/RNASeq_20130627/RS28d_A_to_LSU.xml","r")

g=open("/home/calle/Desktop/RNASeq_20130627/RS28d_A_to_LSU_end.xml","w")


read_line=f0.readlines()
end_sentence=[]
print read_line[-5:]
end_sentence=read_line[-2:]
print end_sentence
################################################################

read_line=f1.readlines()
print read_line[-5:]
del read_line[-3:]
g.writelines(read_line)
g.writelines(end_sentence)

################################################################   


f0.close()
f1.close()
g.close()
