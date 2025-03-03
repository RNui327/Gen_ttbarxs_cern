#!/usr/bin/python3
#script to generte mathematica file
import os
import numpy as np
import argparse
import shutil


def generate_differentmass(filepath, width, alphas,cepcls):
    if not os.path.exists(filepath):
        shutil.copytree('./prototype',filepath)
    f = open("generate.m","r")
    lines=f.readlines()
    f.close()
    
    fsh = open("./prototype/run.sh","r")
    fsub = open("./prototype/run.sub","r")
    
    
    lines0_sh=fsh.readlines()
    lines0_sub=fsub.readlines()
    fsh.close()
    fsub.close()
    filepath=os.path.abspath(filepath)
    outmmapath=os.path.join(filepath,'mma_script')
    outsubpath=os.path.join(filepath,'submit')
    outputpath=os.path.join(filepath,'submit','output')
    outerrpath=os.path.join(filepath,'submit','error')
    outlogpath=os.path.join(filepath,'submit','log')
    outrespath=os.path.join(filepath,'submit','result')
    
    
    if not os.path.exists(outmmapath):
        os.mkdir(outmmapath)
    if not os.path.exists(outsubpath):
        os.mkdir(outsubpath)
    if not os.path.exists(outputpath):
        os.mkdir(outputpath)
    if not os.path.exists(outerrpath):
        os.mkdir(outerrpath)
    if not os.path.exists(outlogpath):
        os.mkdir(outlogpath)
    if not os.path.exists(outrespath):
        os.mkdir(outrespath)
    
    fcmd = open(outsubpath+"/submit.sh","w")
    target_list=[]
    sub_list=[]
    for delmass in np.arange(-0.05,0.05,0.001):
        s=[]
        str0=""
        dmass=('%.4f' % delmass)
        realmass=('%.4f' % (171.5+delmass))
        for line in lines:
            if 'strm=OpenWrite' in line:
                line = 'strm=OpenWrite["'+outrespath+'/mass'+str(realmass)+'.txt"];\n'
            if 'delmass=' in line:
                line = '       delmass='+str(dmass)+';\n'
            if 'width = ' in line and ('mu' not in line):
                line = '     width = '+('%.2f' % width)+',\n'
            if 'alphas=' in line:
                line = '     alphas = '+('%.4f' % alphas)+'\n'
            if 'kew=' in line:
                line = '     kew = '+('%.2f' % cepcls)+',\n'
            str0 = str0 + line
        s.append(str0)
        outfilename='mass'+str(realmass)+'.m'
        outmmafilepath=os.path.join(outmmapath,outfilename)
        with open(outmmafilepath,"w") as fo:
            fo.writelines(s)
        
        outfilename_sh='run_mass'+str(realmass)+'.sh'
        outfilename_sub='run_mass'+str(realmass)+'.sub'
        outfilename_log='run_mass'+str(realmass)+'.log'
        outfilename_out='run_mass'+str(realmass)+'.out'
        outfilename_err='run_mass'+str(realmass)+'.err'
        
        
        outshfilepath=os.path.join(outsubpath,outfilename_sh)
        outsubfilepath=os.path.join(outsubpath,outfilename_sub)
        s0_sh=[]
        s0_sub=[]
        str0_sh=""
        str0_sub=""
    
        for line0_sh in lines0_sh:
            if 'mathe.sh' in line0_sh:
                mmaabspath=os.path.abspath('./mathe.sh')
                line0_sh = 'source '+mmaabspath+'\n'
            if 'math<' in line0_sh:
                line0_sh = 'math<'+outmmafilepath+'\n'
            str0_sh = str0_sh + line0_sh
        s0_sh.append(str0_sh)
    
        with open(outshfilepath,"w") as fo:
            fo.writelines(s0_sh)
    
        for line0_sub in lines0_sub:
            if 'executable' in line0_sub:
                line0_sub = 'executable = '+outshfilepath+'\n'
            if 'log' in line0_sub:
                line0_sub = 'log = log/'+outfilename_log+'\n'
            if 'output = output' in line0_sub:
                line0_sub = 'output = output/'+outfilename_out+'\n'
            if 'error' in line0_sub:
                line0_sub = 'error = error/'+outfilename_err+'\n'
            str0_sub = str0_sub + line0_sub
        s0_sub.append(str0_sub)
    
        with open(outsubfilepath,"w") as fsubo:
            fsubo.writelines(s0_sub)
    
        comdstr0='condor_submit '+outfilename_sub+'\n'
        fcmd.write(comdstr0)
        if os.path.isfile(outmmafilepath):
            print(outfilename+" generated successfully")
        else:
            print(outfilename+" generated failed")    
        target_list.append('mass'+str(realmass)+'.txt\n')
        sub_list.append(outfilename_sub+'\n')
    target_list_filepath=os.path.join(outrespath,"target.list")
    sub_list_filepath=os.path.join(outrespath,"sub.list")
    with open(target_list_filepath,"w") as folist:
        folist.writelines(target_list)
    with open(sub_list_filepath,"w") as fosublist:
        fosublist.writelines(sub_list)
    fcmd.close()
    
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--filepath", default='/afs/cern.ch/user/z/zhan/private/qqbarthreshold/myls/ttbarxs_genscript/test', help='the filepath for script')
    parser.add_argument("--width", default=1.33, help='width of top quark, default 1.33 GeV')
    parser.add_argument("--alphas", default=0.1184, help='alpha_S of top quark, default 0.1184')
    parser.add_argument("--cepcls", default=1.0, help='Luminosity spectrum, default 1.0 which means 1.0 times cepcls energy width')

    args = parser.parse_args()
    filepath = args.filepath
    width = args.width
    alphas= args.alphas
    cepcls = args.cepcls

    generate_differentmass(filepath, width, alphas,cepcls)