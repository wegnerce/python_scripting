#!/usr/bin/python

# Author: Laurent Manchon (lmanchon@univ-montp2.fr)
# translate and split big blast output in txt format into several files in xml format
# then the files generated can be imported in Blast2GO application
# usage: ./blast2xml.py <input_filename>

import os
import sys

myfile=sys.argv[1]

numerofichier=1
chaine1=''
chaine2=''
nom_seq_req=''
fichier1=''
version_blast=''
compteur=1
compteur2=0
nombre_seq=''
compteur_seq=0
entete=1
fin=0

fichier_entree = open(myfile, "r")
fichier_sortie_temp = open("output_file.txt", 'w')
nombre_seq=raw_input('Number of sequences per output file : \n')

nombre_seq=int(nombre_seq)
version_blast=fichier_entree.readline()
version_blast=version_blast.split()


fichier1=fichier_entree.read()
fichier1=fichier1.replace("a new generation","\na new generation")
fichier1=fichier1.replace("\n","*")
fichier1=fichier1.replace("Query=","\nQuery=")
fichier1=fichier1.replace("**>gi","\ngi")
fichier1=fichier1.replace("***gi","\ngi")
fichier1=fichier1.replace("* gi","\ngi")
fichier1=fichier1.replace("BLAST:","\nBLAST:")
fichier_sortie_temp.write(fichier1+"\n")
fichier_sortie_temp.close()
fichier_entree.close()

fichier_sortie = open("output_blast_"+str(numerofichier)+".xml", 'w')

fichier_sortie_temp = open("output_file.txt", 'r')

while 1:

 chaine1 = fichier_sortie_temp.readline()
 
 if chaine1=='':
  break
   
 
 if chaine1[0] == 'Q':
  
  if entete==1 :
   
   fichier_sortie.write('<?xml version="1.0"?>'+'\n'+'<!DOCTYPE BlastOutput PUBLIC "-//NCBI//NCBI BlastOutput/EN" "http://www.ncbi.nlm.nih.gov/dtd/NCBI_BlastOutput.dtd">'+"\n")
   fichier_sortie.write('<BlastOutput>\n<BlastOutput_program>'+version_blast[0].lower()+'</BlastOutput_program>\n')
   fichier_sortie.write('<BlastOutput_version>'+version_blast[0].lower()+' '+version_blast[1]+' '+version_blast[2]+'</BlastOutput_version>\n')
   fichier_sortie.write('<BlastOutput_reference></BlastOutput_reference>\n')
   fichier_sortie.write('<BlastOutput_db></BlastOutput_db>\n')
   fichier_sortie.write('<BlastOutput_query-ID>lcl|'+str(compteur)+'_0</BlastOutput_query-ID>\n')
   fichier_sortie.write('<BlastOutput_query-def>Requete</BlastOutput_query-def>\n')
   fichier_sortie.write('<BlastOutput_query-len>300</BlastOutput_query-len>\n')
   fichier_sortie.write('<BlastOutput_param>\n<Parameters>\n')
   fichier_sortie.write('<Parameters_matrix></Parameters_matrix>\n')
   fichier_sortie.write('<Parameters_expect>1</Parameters_expect>\n')
   fichier_sortie.write('<Parameters_gap-open>1</Parameters_gap-open>\n')
   fichier_sortie.write('<Parameters_gap-extend>1</Parameters_gap-extend>\n')
   fichier_sortie.write('<Parameters_filter>F</Parameters_filter>\n')
   fichier_sortie.write('</Parameters>\n')
   fichier_sortie.write('</BlastOutput_param>\n<BlastOutput_iterations>\n') 
    
  entete=0   
  chaine1=chaine1.replace('Query= ','')
  nom_seq_req=chaine1.split("*")
  chaine2=chaine1
  compteur_seq=compteur_seq+1
  fichier_sortie.write("<Iteration>\n")
  fichier_sortie.write('<Iteration_iter-num>'+str(compteur)+'</Iteration_iter-num>\n')
  fichier_sortie.write('<Iteration_query-ID>lcl|'+str(compteur)+'_0</Iteration_query-ID>\n')
  fichier_sortie.write('<Iteration_query-def>'+nom_seq_req[0]+'</Iteration_query-def>\n')
  fichier_sortie.write('<Iteration_query-len>60</Iteration_query-len>\n<Iteration_hits>\n<Hit>\n<Hit_num>1</Hit_num>\n<Hit_id></Hit_id>\n<Hit_def>')
  compteur=compteur+1
  compteur2=0
  
 if chaine1[0] == 'g' :
  chaine2=chaine1.split("|")
  if compteur2 > 0 :
   fichier_sortie.write(" &gt;")
  fichier_sortie.write(chaine2[0]+'|'+chaine2[1]+'|'+chaine2[2]+'|'+chaine2[3]+'|')
  compteur2=compteur2+1
  
  
 if chaine1[0] == 'B' and compteur>1 :
  
  if compteur_seq<nombre_seq :
   fichier_sortie.write('</Hit_def>\n<Hit_accession></Hit_accession>\n<Hit_len>70</Hit_len>\n<Hit_hsps>\n<Hsp>\n<Hsp_num>1</Hsp_num>\n<Hsp_bit-score>1</Hsp_bit-score>\n<Hsp_score>1</Hsp_score>\n<Hsp_evalue>1e-300</Hsp_evalue>\n<Hsp_query-from>1</Hsp_query-from>\n<Hsp_query-to>1</Hsp_query-to>\n<Hsp_hit-from>1</Hsp_hit-from>\n<Hsp_hit-to>1</Hsp_hit-to>\n<Hsp_query-frame>-1</Hsp_query-frame>\n<Hsp_identity>1</Hsp_identity>\n<Hsp_positive>1</Hsp_positive>\n<Hsp_align-len>100</Hsp_align-len>\n</Hsp>\n</Hit_hsps>\n</Hit>\n</Iteration_hits>\n</Iteration>\n')
  
   fin=0
  
  if int(compteur_seq)==nombre_seq :
   fin=1
  
  
 if fin == 1 and chaine1[0]=='B':
  fichier_sortie.write("</Hit_def>\n<Hit_accession></Hit_accession>\n<Hit_len>70</Hit_len>\n<Hit_hsps>\n<Hsp>\n<Hsp_num>1</Hsp_num>\n<Hsp_bit-score>1</Hsp_bit-score>\n<Hsp_score>1</Hsp_score>\n<Hsp_evalue>1e-1</Hsp_evalue>\n<Hsp_query-from>1</Hsp_query-from>\n<Hsp_query-to>1</Hsp_query-to>\n<Hsp_hit-from>1</Hsp_hit-from>\n<Hsp_hit-to>1</Hsp_hit-to>\n<Hsp_query-frame>-1</Hsp_query-frame>\n<Hsp_identity>1</Hsp_identity>\n<Hsp_positive>1</Hsp_positive>\n<Hsp_align-len>100</Hsp_align-len>\n</Hsp>\n</Hit_hsps>\n</Hit>\n</Iteration_hits>\n</Iteration>\n</BlastOutput_iterations>\n</BlastOutput>")
  fichier_sortie.close()
  compteur_seq=0
  numerofichier=numerofichier+1
  fichier_sortie = open("output_blast_"+str(numerofichier)+".xml", 'w')
  entete=1
  fin=0
  
fichier_sortie.write("</Hit_def>\n<Hit_accession></Hit_accession>\n<Hit_len>70</Hit_len>\n<Hit_hsps>\n<Hsp>\n<Hsp_num>1</Hsp_num>\n<Hsp_bit-score>1</Hsp_bit-score>\n<Hsp_score>1</Hsp_score>\n<Hsp_evalue>1e-1</Hsp_evalue>\n<Hsp_query-from>1</Hsp_query-from>\n<Hsp_query-to>1</Hsp_query-to>\n<Hsp_hit-from>1</Hsp_hit-from>\n<Hsp_hit-to>1</Hsp_hit-to>\n<Hsp_query-frame>-1</Hsp_query-frame>\n<Hsp_identity>1</Hsp_identity>\n<Hsp_positive>1</Hsp_positive>\n<Hsp_align-len>100</Hsp_align-len>\n</Hsp>\n</Hit_hsps>\n</Hit>\n</Iteration_hits>\n</Iteration>\n</BlastOutput_iterations>\n</BlastOutput>")
os.remove('output_file.txt')  
print "\nYour input file",myfile,"has just been translated and splitted into",numerofichier,"XML files with",nombre_seq,"sequences per file:\n"
os.system("/bin/ls -1 output_blast_*.xml")
