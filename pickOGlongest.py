import os, re, sys
from Bio import SeqIO
from sys import argv

dict={}; transl=[]
def pickOG(seqfile):
	for Seq in SeqIO.parse(seqfile,'fasta'):
		dict.setdefault('_'.join(Seq.id.split('_')[0:-1]),[])
		dict['_'.join(Seq.id.split('_')[0:-1])].append(str(Seq.seq))
		if '_'.join(Seq.id.split('_')[0:-1]) not in transl:
			transl.append('_'.join(Seq.id.split('_')[0:-1]))
		
	for trans in transl:
# 		print(trans)
		sorted_x=sorted(dict[trans], key=len, reverse=True)
# 		print(sorted_x[0], len(sorted_x[0]))
		print(trans,'\t',len(sorted_x[0]))		
def main():
	script, seqfile = argv
	pickOG(seqfile)
main()