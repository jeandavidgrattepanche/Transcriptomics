import re, sys, os
from sys import argv
from Bio import SeqIO

i=0; j=0
for folder in os.listdir('/Volumes/GoogleDrive/My Drive/Micromonas_BU'):
	if folder[0:3] == "SRR" and 'transcripts.fasta' in os.listdir('/Volumes/GoogleDrive/My Drive/Micromonas_BU/'+folder):
# 	if "SRR1588115" in folder and 'transcripts.fasta' in os.listdir('/Volumes/GoogleDrive/My Drive/Micromonas_BU/'+folder):
		i+=1
		dest="/Users/tuk61790/Documents/JD_work/Micromonas/"+folder+"_trans.fasta"
		orig='/Volumes/GoogleDrive/My\ Drive/Micromonas_BU/'+folder+"/transcripts.fasta"
		print(folder, i)
#		os.system('cp '+orig+" "+dest)
	else:
		if "done" in folder:
			for file in os.listdir('/Volumes/GoogleDrive/My Drive/Micromonas_BU/'+folder):
				if "cl_1" in file:
					j+=1
			print("\t\t\t\t", j, " SRR done!") 	
		else:
			print("ERROR!!! \t\t\t\t", folder)