import re, sys, os
from sys import argv
from Bio import SeqIO

def main():
	script, SRR_list = argv
	for data in open(SRR_list):
		dataname = data.split('\n')[0]
		os.system('cp /Volumes/GoogleDrive/My\ Drive/Micromonas_BU/done_cl_files/'+dataname+'*.fastq.gz ../Micromonas/')
		os.system('gunzip '+dataname+'*.fastq.gz') 
		os.system('rnaspades.py --restart-from as -o '+dataname+'_SPAdes -m 10 -t 2')
		print("Compressing and moving files ",dataname," in Google Drive \n")
		os.system('rm '+dataname+'*.fastq')
		os.system('cp -av '+dataname+'_SPAdes/* /Volumes/GoogleDrive/My\ Drive/Micromonas_BU/'+dataname+'_SPAdes/')
		
main()
