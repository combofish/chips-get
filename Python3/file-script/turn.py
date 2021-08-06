#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: combofish
# Filename: turn.py

import os
import shutil

def process():
    files = os.listdir('./')
    for f in files:
        suffix = f.split('.')[1]
        if suffix == 'xlsx':
            print(f)
            moveFile(f)

def moveFile(f):
    fName = f.split('.')[0]
    newFileName = '整修确认单'+ '.' + f.split('.')[1]
    dirName = fName+'#号'
    os.mkdir(dirName)
    shutil.copyfile(f,os.path.join(dirName,newFileName))

process() 
