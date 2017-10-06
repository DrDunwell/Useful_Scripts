# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 15:21:13 2016
@author: Thomas Dunwell
"""

import os
import argparse

def check_file_is_valid(parser, file):
	if not os.path.exists(file):
		parser.error("The file %s does not exist! Please ensure you have spelled it correctly." % file)
	else:
		return file
		
def splitting_fasta_files(FASTA_file_name,number_of_enteries_per_file):
	entry_count = 0
	completed_loops = 0
	total_enteries = 0
	total_enteries_written = 0
	total_lines = 0
	total_lines_written = 0
	
	fasta_file = open(FASTA_file_name, "r")
	name = FASTA_file_name + "_enteries_" + str((completed_loops*number_of_enteries_per_file)+1) + "_" + str((completed_loops+1)*number_of_enteries_per_file) + ".splitout" 
	new_out_put_file = open(name,"w") 
	#count number of lines in fasta file, necessary to know when we have reached the end of the input file
	for line in fasta_file:
		if line[0] == ">":
			total_enteries += 1
		total_lines += 1
	fasta_file.seek(0)
	#itterate through the input file again and write each line to a new file until the total number of enteries requested to be in each new file have been written, then, close the file and open another and continue.
	while total_lines != total_lines_written:
		for line in fasta_file:  
			if line[0] == ">" and entry_count == number_of_enteries_per_file:
				completed_loops += 1 
				new_out_put_file.close
				#this IF works out if there are enough enteries left to populate a whole new file or not and adjusts the file name accordingly. In this loop if there are less than the required number of enteries to populate a whole new file the total number of enteries is used in the file name.
				if (total_enteries - total_enteries_written) >= number_of_enteries_per_file:
					name = FASTA_file_name + "_enteries_" + str((completed_loops*number_of_enteries_per_file)+1) + "_" + str((completed_loops+1)*number_of_enteries_per_file) + ".splitout" 
				else:
					name = FASTA_file_name + "_enteries_" + str((completed_loops*number_of_enteries_per_file)+1) + "_" + str(total_enteries) + ".splitout" 
				new_out_put_file = open(name,"w")
				new_out_put_file.write(line)
				entry_count = 1
				total_enteries_written += 1
				total_lines_written += 1
				break
			elif line[0] == ">" and entry_count < number_of_enteries_per_file:
				entry_count += 1
				total_enteries_written += 1
				total_lines_written += 1
				new_out_put_file.write(line)
			else:
				new_out_put_file.write(line)
				total_lines_written += 1
	new_out_put_file.close
	fasta_file.close

parser = argparse.ArgumentParser(description='This script will take any style of fasta file, nucleotide, protein, or other, and split the file up so N number of enteries are in seperate files.')

parser.add_argument("-f", action='store', dest="FileName", required=True, type=lambda x: check_file_is_valid(parser, x), help='The name of the input fasta file.')
parser.add_argument("-n", action='store', dest="Integer", type=int, default=1000, help='The number of fasta enteries in each output file')
args = parser.parse_args()

if __name__ == "__main__":
	splitting_fasta_files(args.FileName,args.Integer)
