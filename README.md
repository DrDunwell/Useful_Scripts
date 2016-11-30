A collection of python scripts and shell commands for high throughput bioinformatics work.

Core_optimisation_for_large_blast_runs.txt

The commands in this file can be used, when combined with the output of fasta_file_split.py, to optmise core usage with large scale blastp(n) runs. The folder this is run in should also contain a file named 'number_of_cores.txt', this file is peridoicallly read so that the loops know how many insances of blast to trigger. This file can be edited after the loops have been triggered to expand or reduce the total core usage as you want. The response time to reducing the total core usage is mainly depended on the size of the fasta files and the blastDB size. Using this command it is possible to compete ~550,000 reciprocal blastp using ~55 threads on an intel 2.3 GHz server in just under 48 hours.

GFF3_to_GTF_conversion.py

This script will take a NCBI GFF3 files (as of october 2016) and convert it into GTF format sutiable for programs such as cufflinks and featureCounts.

The script will do the following;

chr1    Gnomon  exon    3199731 3207317 .       -       .       ID=id4;Parent=rna0;Dbxref=GeneID:497097,Genbank:XM_006495550.2,MGI:MGI:3528744;gbkey=mRNA;gene=Xkr4;product=X Kell blood group precursor related family member 4%2C transcript variant X1;transcript_id=XM_006495550.2
to
chr1    Gnomon  exon    3199731 3671742 .       -       .       gene_id "497097"; gene_name "Xkr4"; transcript_id "XM_006495550.2";

chr1    BestRefSeq      CDS     3421702 3421901 .       -       1       ID=cds1;Parent=rna1;Dbxref=CCDS:CCDS14803.1,GeneID:497097,Genbank:NP_001011874.1,MGI:MGI:3528744;Name=NP_001011874.1;gbkey=CDS;gene=Xkr4;product=XK-related protein 4;protein_id=NP_001011874.1
to
chr1    BestRefSeq      CDS     3421702 3421901 .       -       1       gene_id "497097"; gene_name "Xkr4"; transcript_id "NP_001011874.1";

fasta_file_split.py

This script will split up any fasta formatted file into a series of smaller files with a user defined subset of fasta entries. For example will split a fasta file with 550,000 entries into 550 files with 1000 entries in each in about 5 seconds.
