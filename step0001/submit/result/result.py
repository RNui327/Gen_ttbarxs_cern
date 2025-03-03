#!/usr/bin/python3
import os
import os.path
import numpy as np

flist = open("target.list","r")
tarlines=flist.readlines()
s=[]
for lines in tarlines:
    infilename=lines.strip("\n")
    if os.path.exists(infilename):
        with open(infilename,"r") as fi:
            lines=fi.readlines()
            str0=""
            for line in lines:
                if '"\\t"' in line:
                    line = line.replace('"\\t"','\t',4)
                if line == '\n':
                    line = line.strip("\n")
                str0 = str0 + line
            s.append(str0)
        print(infilename+' finished')
    else:
        print('no file named '+infilename)
outfilename='fullresult.txt'

with open(outfilename,"w") as fo:
    fo.writelines(s)
if not os.path.isfile(outfilename):
    print(outfilename+" generated failed")
