#!/bin/sh
# author:combofish
# email:combofish49@gmail.com
# Filename: turnLocate.sh


echo  ">>> Shell File: current dir"
pwd
pathDir=$1
echo ">>> Shell File: Process " $0 $1
# uploadDir="upload"

# use=$2$uploadDir
echo  ">>> Shell File: pathDir " $pathDir
cd $pathDir
pwd
python3 ./class-use.py
