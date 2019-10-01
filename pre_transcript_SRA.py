##replace /Users/...path.../bbmap by bbmap installation path line 24
## replace Mixo_Ciliates by your project title/species
## create Mixo_Ciliates/ and Mixo_Ciliates/done_cl_files/ in your google drive (l38-39, 45-46) or delete these line

import re, sys, os
from sys import argv
from Bio import SeqIO

def main():
	script, SRR_list, download = argv
	for data in open(SRR_list):
		lr=0; check= 0
		dataname = data.split('\t')[0]
		species = data.split('\n')[0].split('\t')[1]
		if download.lower()[0] == "y":
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
			print("Assembling "+dataname+" with rnaSPAdes \n")
			os.system('rnaspades.py -1 '+dataname+'_cl_1.fastq.gz -2 '+dataname+'_cl_2.fastq.gz -o '+species+'_SPAdes -m 10 -t 2')
			print("moving files (reads and assembled data) ",dataname," in Google Drive \n")
			os.system('mv '+dataname+'*.fastq.gz /Volumes/GoogleDrive/My\ Drive/Mixo_Ciliates/done_cl_files/')
			os.system('mv '+species+'_SPAdes/ /Volumes/GoogleDrive/My\ Drive/Mixo_Ciliates/')

		elif download.lower()[0] == "n":
			print("Assembling "+dataname+" with rnaSPAdes \n")
			os.system('rnaspades.py -1 '+dataname+'_cl_1.fastq.gz -2 '+dataname+'_cl_2.fastq.gz -o '+species+'_SPAdes -m 10 -t 2')
			print("moving files (reads and assembled data) ",dataname," in Google Drive \n")
			os.system('mv '+dataname+'*.fastq.gz /Volumes/GoogleDrive/My\ Drive/Mixo_Ciliates/done_cl_files/')
			os.system('mv '+species+'_SPAdes/ /Volumes/GoogleDrive/My\ Drive/Mixo_Ciliates/')
		else:
			print("error in input, should be : python3 pre_transcript_SRA.py list-of-SRR-number [yes or no] to download data (no = running SPAdes for multiple transcriptomes)")
main()
