OBSOLETE SCRIPT => USE pre_transcript_SRA.py

#!/usr/bin/python3
#dta for download, trim and assembled
#use google drive as files can be huge and in large number

#replace /Users/...path.../bbmap by bbmap installation path

import re, sys, os
from sys import argv
from Bio import SeqIO

def main():
	script, SRR_list = argv
	for data in open(SRR_list):
		lr=0
		dataname = data.split('\n')[0]
		print("Downloading and preparing ",dataname)
		os.system('fasterq-dump '+dataname)
		for read in SeqIO.parse(dataname+'_1.fastq','fastq'):
			lr=int(read.description.split('length=')[1])-25
			if lr > 0:
				break
		os.system('bbduk.sh in1='+dataname+'_1.fastq in2='+dataname+'_2.fastq out1='+dataname+'_cl_1.fastq out2='+dataname+'_cl_2.fastq qtrim=rl trimq=10 maq=30 ref=/Users/...path.../bbmap/resources/adapters.fa ktrim=r k=23 mink=11 hdist=1 tpe tbo minlen='+str(lr))
		os.system('rm '+dataname+'_1.fastq')
		os.system('rm '+dataname+'_2.fastq')
		os.system('rm ../public/sra/'+dataname+'.sra.*')
		os.system('rnaspades.py -1 '+dataname+'_cl_1.fastq -2 '+dataname+'_cl_2.fastq -o '+dataname+'_SPAdes -m 10 -t 2')
		print("Compressing and moving files ",dataname," in Google Drive/n")
		os.system('gzip '+dataname+'*.fastq')
		os.system('mv '+dataname+'*.fastq.gz /Volumes/GoogleDrive/My\ Drive/Micromonas_BU/done_cl_files/')
		os.system('mv '+dataname+'_SPAdes/ /Volumes/GoogleDrive/My\ Drive/Micromonas_BU/')
		
main()
