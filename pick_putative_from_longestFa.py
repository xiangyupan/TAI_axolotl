#!/usr/bin/env python3.4
'''
#-------------------------------------------------------------------------------
#Author:Pan Xiangyu(bendanpanxiangyu@163.com)
#Time:  2016/12/5
#Version: 1.0
#-------------------------------------------------------------------------------
'''
#######################modle####
import sys
import re
import os
import getopt
def usage():
    print('''Useage: python script.py [option] [parameter]
    -f/--gtf        input merge gtf
    -g/--gene            input gene fpkm
    -o/--output          extraction file
    -h/--help            show possible options''')
####################### argv ######
opts, args = getopt.getopt(sys.argv[1:], "hf:g:o:",["help","gtf=","gene","output="])
for op, value in opts:
    if op == "-f" or op == "--gtf":
        gtf = value
    elif op == "-g" or op == "--gene":
        gene = value
    elif op == "-o" or op == "--output":
        output = value
    elif op == "-h" or op == "--help":
        usage()
        sys.exit(1)
if len(sys.argv) < 5:
    usage()
    sys.exit(1)
f1=open(gtf)
f2=open(gene)
f3=open(output,'w')
'''
>AMEX60DD201000002.1; gene_id "AMEX60DD000002"; orf_type "Putative short"; annotation "LOC114595135 [nr]|ZNF268 [hs]|"
MAFLLDKTQSGGSCLQEQLYPCSECDKQFSHERHLTQHERTHIGEKPYQCPECQKKFIRKSQLSIHERIHTGEKPYQCSECQKRFSQKSNLTDHQKKHTGEKPYQCPECQKRFSRKENLRRHEQQHTGEKPHQCPECQKRFICKSQLTIHERIHTGEKPYQCSECQKRFSQKSNLTDHQKKHTGEKPYQCAECQKRFSRKENLKQHEQQH>
>AMEX60DD201000003.1; gene_id "AMEX60DD000003"; orf_type "Enforced PTC"; annotation "LOC101953204 [nr]|ZNF850 [hs]|"
IEQGAPFYSKIDTLTMELPLEFSECETTFNETGYLSQHQRLLTEEKEHKHFECCKAFTETNNLLTNQRNLPGEKPYACTECGKAFKRKSDLLIHQRIHTGENPYTCSGCDKSFKQKSNLTIHQRIHTGEKPYPCSECDKSFSQRGQLLSHQRIHTGEKPYTCSECEKSFAEKTHLLRHQRSHTGEKPYACSECSKAFKEKSNLMIHQRSH>
>AMEX60DD201000004.1; gene_id "AMEX60DD000004"; orf_type "Putative short PTC"; annotation "LOC115462503 [nr]|ZNF268 [hs]|"
MLQGFYRNKSIEKIREIAIGNP*TCSECDMSFMAKSASLILQRKHTREKPYSCSECDKSFNQKGELVLHQRNHTGVKPYKCSECDKAFKRNDHLKIHQRNHTGEKPYTCSECYKSFKQKGELVIHQRNHTGVKPYTCSECDESFMVKSNLLMHQRNHTGEKPYACPQCGKTFKRNDRLIIHQRNHTGVKPYPCTECYKSFKQKGQLVIHQ>
>AMEX60DD201000005.2; gene_id "AMEX60DD000005"; orf_type "Predicted"; annotation ""
###
AMEX60DD000016
AMEX60DD000038
AMEX60DD000042
AMEX60DD000048
AMEX60DD000050
AMEX60DD000051
AMEX60DD000102
AMEX60DD000110
AMEX60DD000111
AMEX60DD000124
AMEX60DD000129
AMEX60DD000131
AMEX60DD000133
AMEX60DD000134
'''
genename={}
protein = {}
for line in f1:
    line = line.strip()
    if line[0] == '>':
        chr = line.split(";")
        genename[chr[1][10:-1]] = ''
    else:
        genename[chr[1][10:-1]] = line
for gene in f2:
    gene = gene.strip()
    protein[gene] = ""
for key,value in protein.items():
    if key in genename:
        f3.write('>'+key+"\n"+genename[key]+"\n")
    else:
        print(key)
f1.close()
f2.close()
f3.close()