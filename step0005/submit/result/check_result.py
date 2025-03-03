#!/usr/bin/python3
import os
import os.path
import numpy as np
f = open("../submit_failed.sh","w")
flist = open("target.list","r")
tarlines=flist.readlines()
fsublist = open("sub.list","r")
sublines=fsublist.readlines()
for i in range(len(tarlines)):
    filename=tarlines[i].strip("\n")
    if not os.path.exists(filename):
        print(filename+" failed")
        infilename=sublines[i]
        comdstr='condor_submit '+infilename
       	f.write(comdstr)
f.close()
