#!/usr/bin/env python3.6

'''
-----------------------------------------------------------------------------------------
Author: Xiangyu Pan
Email: pan_xiangyu@nwafu.edu.cn
Time: 2023/05/11
Version: 1.0
------------------------------------------------------------------------------------------
'''

import sys
if len(sys.argv) < 1:
    print('Usage: python3.5 '+sys.argv[0]+'[input file1] [input file2] [infile3][infile4][infile5][infile6][output file]')
    exit(1)
infile1 = open(sys.argv[1])
infile2 = open(sys.argv[2])
outfile =open(sys.argv[3],'w')
#############################default
'''
>AMMEX-AMEX60DD012307
VLQNPYSCQSPCHHCVRLVLLNPYSCQSPCHHCVRLILLNPYSCQSPCHNCVRLVLQNPYRCQSPCRHCVRLVLLNPYSCQSPGHHCVRLVLQNPYRCQSPCRHCVRLVLLNPYSCQSP
>AMMEX-AMEX60DD012308
QWRHGNWQLXGFRSTSRTQWWHGDWQLXGFRSTCLTQWWFGDWQLXGFRSTSLKQWWHGSWQLLRVQKYESDTMVAWQLAVVRVQKHESDTMVAWQSATVRVQKXESDTMVAWRLATVRVQKYESDTMVAWRLATVRVQKYESDT
>AMMEX-AMEX60DD012313
ASCQLSGKVGSTIQAPLVPLPVVGIPFERVGIDIVGPLDPQTSSGNRFILVLVDHATRYPEAIPLKTVTAKSVAKALLGIFTRVGFPKEVVSDRGSN
>AMMEX-AMEX60DD012317
'''
chrom = {}
for line in infile1:
    line = line.strip()
    if line[0]=='>':
        print(line)
        if line not in chrom:
            chr = line
            chrom[chr]=''
        elif line in chrom:
            pass
    else:
        chrom[chr] = line
for gene in infile2:
    gene= gene.strip()
for key,value in chrom.items():
    outfile.write(key+" | "+gene+"\n"+value+"\n")
    
    
infile1.close()
infile2.close()
outfile.close()

