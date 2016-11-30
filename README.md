A collection of python scripts and shell commands for high throughput bioinformatics work.

Core_optimisation_for_large_blast_runs.txt

The commands in this file can be used, when combined with the output of fasta_file_split.py, to optmise core usage with large scale blastp(n) runs. The folder this is run in should also contain a file named 'number_of_cores.txt', this file is peridoicallly read so that the loops know how many insances of blast to trigger. This file can be edited after the loops have been triggered to expand or reduce the total core usage as you want. The response time to reducing the total core usage is mainly depended on the size of the fasta files and the blastDB size. Using this command it is possible to compete ~550,000 reciprocal blastp using ~55 threads on an intel 2.3 GHz server in just under 48 hours.

fasta_file_split.py

This script will split up any fasta formatted file into a series of smaller files with a user defined subset of fasta entries. For example will split a fasta file with 550,000 entries into 550 files with 1000 entries in each in about 5 seconds.
