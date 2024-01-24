# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 11:30:27 2023

@author: Xiangyu Pan
E-mail:pan_xiangyu@nwafu.edu.cn
To: Trust yourself, you are the king of your world.
"""

import sys

if len(sys.argv) < 1:
    print('Usage: python3.5 '+sys.argv[0]+'[input file1] [output file]')
    exit(1)
infile1 = open(sys.argv[1])
infile2 = open(sys.argv[2])
outfile=open(sys.argv[3],'w')

'''
Gene    Stage1_1        Stage1_2        Stage2_1        Stage2_2        Stage2_3        Stage3_1        Stage3_2        Stage3_3        Stage4_1        Stage4_2        Stage4_3        Stage5_1        Stage5_2        Stage5_3        Stage6_1
AMEX60DD000002  1.224572        1.00485 1.535284        0       0.76827 3.078361        1.921641        1.754865        3.02521 2.571713        1.502693        1.410664        2.315918        1.917015        2.086607        1.545883        1.9
AMEX60DD000016  0.032494        0       0.040951        0       0.06193 0.076721        0.014571        0.0915  0.15692 0.139134        0.079576        0.167602        0.63089 0.32804 0.138764        1.487288        1.909515        1.261487
AMEX60DD000026  1.282269        1.302932        1.174195        0       1.552922        2.86144 1.221454        1.114648        2.351825        2.47228 2.308083        1.054678        0.942761        1.313132        1.303141        1.282906
###
PS      query_id
1       AMEX60DD017011
1       AMEX60DD017055
13      AMEX60DD017014
2       AMEX60DD017057
2       AMEX60DD017052
5       AMEX60DD017051
'''
embryo = {}
psdic = {}
outfile.write(infile2.readline().strip()+"\t"+infile1.readline())
for line in infile1:
    line = line.strip().split("\t")
    embryo[line[0]] = "\t".join(line[0:])

for ps in infile2:
    ps = ps.strip().split("\t")
    psdic[ps[1]] = ps[0]

for key,value in embryo.items():
    if key in psdic:
        outfile.write(psdic[key]+"\t"+value+"\n")
    else:
        print(key)
infile1.close()
infile2.close()
outfile.close()
                         
