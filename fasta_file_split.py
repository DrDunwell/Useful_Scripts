# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 15:21:13 2016

@author: Thomas Dunwell

"""

import os

def splitting_fasta_files():
    correct_name = 0
    correct_number = 0
    entry_count = 0
    completed_loops = 0
    fasta_file = ""
    total_enteries = 0
    total_enteries_written = 0
    total_lines = 0
    total_lines_written = 0
    while correct_name != 1:
        FASTA_file_name = raw_input("What is the name of the FASTA files you want to convert? (it must be in the same folder you are running this script from): ")
        if os.path.isfile(FASTA_file_name):
            correct_name = 1
        else:
            print "\n" + "I'm sorry, but that file is not in the directory you ran this script from. Please try again." + "\n"
    while correct_number != 1:
        number_of_enteries_per_file = raw_input("How many enteries do you want per file?: ")
        if number_of_enteries_per_file.isdigit():
            number_of_enteries_per_file = int(number_of_enteries_per_file)
            correct_number = 1
        else:
            print "\n"+ "Please only type numbers." + "\n"
    fasta_file = open(FASTA_file_name, "r")
    name = FASTA_file_name + "_enteries_" + str((completed_loops*number_of_enteries_per_file)+1) + "_" + str((completed_loops+1)*number_of_enteries_per_file) 
    new_out_put_file = open(name,"w") 
    for line in fasta_file:
        if line[0] == ">":
            total_enteries += 1
        total_lines += 1
    #print total_enteries
    fasta_file.seek(0)
    while total_lines != total_lines_written:
        for line in fasta_file:  
            #print line
            if line[0] == ">" and entry_count == number_of_enteries_per_file and total_enteries > total_enteries_written+number_of_enteries_per_file:
                completed_loops += 1 
                new_out_put_file.close
                name = FASTA_file_name + "_enteries_" + str((completed_loops*number_of_enteries_per_file)+1) + "_" + str((completed_loops+1)*number_of_enteries_per_file) 
                new_out_put_file = open(name,"w")
                new_out_put_file.write(line)
                entry_count = 1
                total_enteries_written += 1
                total_lines_written += 1
                break
            elif line[0] == ">" and entry_count == number_of_enteries_per_file and total_enteries < total_enteries_written+number_of_enteries_per_file:
                completed_loops += 1   
                new_out_put_file.close
                name = FASTA_file_name + "_enteries_" + str((completed_loops*number_of_enteries_per_file)+1) + "_" + str(total_enteries) 
                new_out_put_file = open(name,"w")
                new_out_put_file.write(line)
                entry_count = 1
                total_enteries_written += 1
                total_lines_written += 1
                break
            elif line[0] == ">" and entry_count <= number_of_enteries_per_file:
                entry_count += 1
                total_enteries_written += 1
                total_lines_written += 1
                new_out_put_file.write(line)
            else:
                new_out_put_file.write(line)
                total_lines_written += 1
            if total_lines == total_lines_written:
                new_out_put_file.close                
                break
    new_out_put_file.close
    fasta_file.close
    
if __name__ == "__main__":
    splitting_fasta_files()