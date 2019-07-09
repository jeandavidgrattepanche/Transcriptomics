import re, sys, os
from sys import argv
from Bio import SeqIO

i=0; j=0; dict={}
for file in os.listdir():
	if "SPAdes" in file:
		species = file.split('_')[0]
# 		print(species)
		dict.setdefault(species,[])
		dict[species].append(file)
# 		print(species, len(dict[species]))
	
for species in dict:
	print(len(dict[species]), species, ','.join(dict[species]))
	os.system("dedupe.sh in="+','.join(dict[species])+" out="+species+".fasta s=5")
		
