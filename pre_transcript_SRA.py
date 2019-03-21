##replace /Users/...path.../bbmap by bbmap installation path
## replace Micromonas by your project title/species

import re, sys, os
from sys import argv
from Bio import SeqIO

def main():
	script, SRR_list = argv
	for data in open(SRR_list):
		lr=0; check= 0
		dataname = data.split('\n')[0]
		print("Downloading and preparing ",dataname)
		while check == 0:
			os.system('fasterq-dump -v '+dataname)
			if os.path.isfile(dataname+'_1.fastq'):
				check = 1
		for read in SeqIO.parse(dataname+'_1.fastq','fastq'):
			lr=int(read.description.split('length=')[1])-25
			if lr > 0:
				break
		os.system('bbduk.sh in1='+dataname+'_1.fastq in2='+dataname+'_2.fastq out1='+dataname+'_cl_1.fastq out2='+dataname+'_cl_2.fastq qtrim=rl trimq=10 maq=30 ref=/Users/...path.../bbmap/resources/adapters.fa ktrim=r k=23 mink=11 hdist=1 tpe tbo minlen='+str(lr))
		if os.path.isfile(dataname+'_cl_1.fastq'):
			os.system('rm '+dataname+'_1.fastq')
			os.system('rm '+dataname+'_2.fastq')
			os.system('rm ../public/sra/'+dataname+'.sra.*')
		else:
			print("Issue with bbduk!")
			break
		print("Compressing files ",dataname," \n")
		os.system('gzip '+dataname+'*.fastq')
		print("Assembling "+dataname+" with rnaSPAdes \n"
		os.system('rnaspades.py -1 '+dataname+'_cl_1.fastq -2 '+dataname+'_cl_2.fastq -o '+dataname+'_SPAdes -m 10 -t 2')
		print("moving files (reads and assembled data) ",dataname," in Google Drive \n")
		os.system('mv '+dataname+'*.fastq.gz /Volumes/GoogleDrive/My\ Drive/Micromonas_BU/done_cl_files/')
		os.system('mv '+dataname+'_SPAdes/ /Volumes/GoogleDrive/My\ Drive/Micromonas_BU/')
		
main()
