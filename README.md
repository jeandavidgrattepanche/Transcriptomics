# Transcriptomics
Some scripts to download, trim and assembled transcriptomes from SRA GenBank

pre_transcript_SRA.py download SRA data from a list of SRR, trim them using BBmap, and assemble each of them using SPAdes.
by default the min quality is 30 and the min lenght is max length - 25

There is also some script to run the tools to associate transcriptome to trophic mode (see Burns et al 2018 NEE)
