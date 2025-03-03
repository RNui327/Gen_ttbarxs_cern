###First step: Install QQbarThreshold
source mathe.sh
to set Mathematica environment.
Then follow the instructions on QQbarthreshold webpage (https://qqbarthreshold.hepforge.org/doc/v2/) to install it.
version: 2.2.1

###Generate script & submit jobs
To generate the script to calculate xs of ttbar:
./py.py --filepath /path/to/dir --width 1.33 --alphas 0.1184 --cepcls 1.0
default filepath: ./test
default width: 1.33
default alphas: 0.1184
default cepcls: 1.0

./test/mma_script: mathematica script to calculate ttbar xs
./test/submit: files to submit condor jobs in lxplus
./test/submit/result: output
You do not need to care about other directories if nothing is wrong
To submit condor jobs:
cd ./test/submit
source submit.sh
You will submit hundreds of jobs

###Check condor job results:
cd ./test/submit/result
./check_result.py
This will check all the result files and find the jobs that has failed.
Then generate a submit_failed.sh in test/submit
source submit_failed.sh
to resub the failed jobs

If after checking you are sure that you have all result files:
cd ./test/submit/result
./result.py
Then you can have a full results in  ./test/submit/result/fullresult.txt
