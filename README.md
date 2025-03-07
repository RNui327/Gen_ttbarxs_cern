# Gen_ttbarxs_cern
This repo is designed to calculate the cross section of ttbar production from ee collision. It is intended to be run on lxplus.cern.ch. Credit to Zhan Li from ihep for his distribution.

### First step: Install QQbarThreshold
`source mathe.sh`
to set Mathematica environment.
Then follow the instructions on QQbarthreshold webpage (https://qqbarthreshold.hepforge.org/doc/v2/) to install it.
version: 2.2.1

### Generate script & submit jobs
To generate the script to calculate xs of ttbar:
`./py.py --filepath /path/to/dir --width 1.33 --alphas 0.1184 --cepcls 1.0`

default filepath: ./test

default width: 1.33

default alphas: 0.1184

default cepcls: 1.0

./test/mma_script: mathematica script to calculate ttbar xs

./test/submit: files to submit condor jobs in lxplus

./test/submit/result: output

You do not need to care about other directories if nothing is wrong.

To submit condor jobs:
`cd ./test/submit`
`source submit.sh`
You will submit hundreds of jobs.

### Check condor job results:
`cd ./test/submit/result`
`./check_result.py`
This will check all the result files and find the jobs that has failed.
Then generate a submit_failed.sh in test/submit.
`source submit_failed.sh`
to resub the failed jobs

If after checking you are sure that you have all result files:
`cd ./test/submit/result`
`./result.py`
Then you can have a full results in  ./test/submit/result/fullresult.txt

### Examples
step0001 was generated with a scan step of 0.001 GeV, while step0005 was generated with a scan step of 0.005 GeV.

To change the step and range of scan, just modify the lines `for delmass in np.arange(-0.05,0.05,0.001):` and `realmass=('%.4f' % (171.5+delmass))` in py.py.
