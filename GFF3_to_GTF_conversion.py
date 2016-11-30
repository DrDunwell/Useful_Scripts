# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 09:51:52 2016

@author: Thomas Dunwell
"""

GFF_file_name = raw_input("What is the name of the GFF3 files you want to convert? (it must be in the same folder you are running this script from): ")
New_GTF_file_name = raw_input("What do you want the name of the output GTF file to be? (It will be created in the same folder you are running this script from): ")
def GFF3_to_GTF_conversion(GFF_file_name):
    GFF3_file = open(GFF_file_name,"r")
    Made_GTF_file = open(New_GTF_file_name,"w")
    for GFF3_file_line in GFF3_file:
        GFF3_file_line_split = GFF3_file_line.split("\t")
        GFF3_file_line_split_col_1_8 = ""
        GFF3_file_line_split_col_9 = ""
        GFF3_file_line_split_col_9_split = []
        if len(GFF3_file_line_split) == 9:
            GFF3_file_line_split_col_1_8 = str(GFF3_file_line_split[0]) + "\t" + str(GFF3_file_line_split[1]) + "\t" + str(GFF3_file_line_split[2]) + "\t" + str(GFF3_file_line_split[3]) + "\t" + str(GFF3_file_line_split[4]) + "\t" + str(GFF3_file_line_split[5]) + "\t" + str(GFF3_file_line_split[6]) + "\t" + str(GFF3_file_line_split[7]) + "\t"
        if len(GFF3_file_line_split_col_1_8) == 0:
            Made_GTF_file.write(str(GFF3_file_line))
        elif len(GFF3_file_line_split_col_1_8) > 0:
            Made_GTF_file.write(str(GFF3_file_line_split_col_1_8))
            GFF3_file_line_split_col_9 = str(GFF3_file_line_split[8])
            GFF3_file_line_split_col_9_split = GFF3_file_line_split_col_9.split(",")
            #This portion of the code looks for the gene ID and writes it to file.
            index = 0
            found = 0
            for i in GFF3_file_line_split_col_9_split:
                if "GeneID" in i:
                    GFF3_file_line_split_col_9_split_split = GFF3_file_line_split_col_9_split[index].split(":")
                    if ";" in GFF3_file_line_split_col_9_split_split[1]:
                        GFF3_file_line_split_col_9_split_split = GFF3_file_line_split_col_9_split_split[1].split(";")
                        Made_GTF_file.write("gene_id \""+ GFF3_file_line_split_col_9_split_split[0] + "\"")
                    else:
                        Made_GTF_file.write("gene_id \""+ GFF3_file_line_split_col_9_split_split[1] + "\"")
                    found += 1
                index +=1
            if found == 0:
                Made_GTF_file.write("gene_id \"\"")
            #This portion of the code looks for the gene NAME and writes it to file.
            index = 0
            found = 0
            GFF3_file_line_split_col_9_split = GFF3_file_line_split_col_9.split(";")
            for i in GFF3_file_line_split_col_9_split:
                if "gene=" in i:
                    GFF3_file_line_split_col_9_split_split = GFF3_file_line_split_col_9_split[index].split("=")
                    Made_GTF_file.write("; gene_name \""+ GFF3_file_line_split_col_9_split_split[1].rstrip('\n') + "\"")
                    found += 1
                index +=1
            if found == 0:
                Made_GTF_file.write("; gene_name \"\"")
            #This portion of the code looks for the gene TRANSCRIPT ID and writes it to file.
            index = 0
            found = 0
            length = 0
            GFF3_file_line_split_col_9_split = GFF3_file_line_split_col_9.split(",")
            for i in GFF3_file_line_split_col_9_split:
                if "Genbank:" in i:
                    #print i
                    GFF3_file_line_split_col_9_split_split = GFF3_file_line_split_col_9_split[index].split(":")
                    if ";" in GFF3_file_line_split_col_9_split_split[1]:
                        GFF3_file_line_split_col_9_split_split = GFF3_file_line_split_col_9_split_split[1].split(";")
                        Made_GTF_file.write("; transcript_id \""+ GFF3_file_line_split_col_9_split_split[0] + "\";\n")
                    else:
                        Made_GTF_file.write("; transcript_id \""+ GFF3_file_line_split_col_9_split_split[1] + "\";\n")
                    if len(GFF3_file_line_split_col_9_split_split)>length:
                        length = len(GFF3_file_line_split_col_9_split_split)
                    found += 1
                index +=1
            if found == 0:
                Made_GTF_file.write("; transcript_id \"\";\n")
    GFF3_file.close()
    Made_GTF_file.close()            
            
GFF3_to_GTF_conversion(GFF_file_name)