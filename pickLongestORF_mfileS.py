import os, re, sys
from Bio import SeqIO
from sys import argv

def pickOG(seqfile):
	dict={}; transl=[]; 
	for Seq in SeqIO.parse(seqfile,'fasta'):
		print("create a dictionnary of aa sequence to keep the longest one")
		dict.setdefault('_'.join(Seq.id.split('_')[0:-1]),[])
		if len(str(Seq.seq))> len(dict['_'.join(Seq.id.split('_')[0:-1])]):
			dict['_'.join(Seq.id.split('_')[0:-1])]=str(Seq.seq)
		if '_'.join(Seq.id.split('_')[0:-1]) not in transl:
			transl.append('_'.join(Seq.id.split('_')[0:-1]))

	i = 0 ; j = 1	
	print("save the longest ORF in a file")
	for trans in transl:
		i+=1 
		print(i )
		out = open(seqfile.split('_getORF.fasta')[0]+'_longestORF.fasta','a')
		out.write('>' + trans+'_'+str(len(dict[trans]))+'aa\n'+ str(dict[trans])+'\n')
		out.close()
def main():
	script, seqfolder, species = argv
	for seqfile in os.listdir(seqfolder):
		if species in seqfile:
			print(seqfile)
			os.system('getORF -sequence '+seqfolder+seqfile+' -outseq '+seqfile.split('.fasta')[0]+'_getORF.fasta -table 4 -find 1')
			pickOG(seqfile.split('.fasta')[0]+'_getORF.fasta')
main()
