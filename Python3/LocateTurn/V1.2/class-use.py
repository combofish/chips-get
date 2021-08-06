#!/usr/bin/env python
# author: combofish
# Filename: class-use.py

import Xl2location
import os


def processAll(path,startImgTag = 1):
    files= os.listdir(path) #得到文件夹下的所有文件名称
    # print("files = ",files)
    files.remove('Res')
    for file in files: #遍历文件夹
        if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开
            # print("path = ",path,"file = ",file)
            # print(os.path.join(path,file))
            fileName = os.path.join(path,file)
            # print("fileName = ", fileName)
            useFile = Xl2location.Xl2location(fileName,imgTag = startImgTag)
            rows = useFile.processXlFile()
            count,mainContent = useFile.mainInfoAndCount(rows)
            useFile.processLine(mainContent)
            useFile.xlClose()
            print(" Done (%4d)  >>> Tag:%3d    FileName:%s" % (count,startImgTag,file))
            startImgTag = startImgTag + 1

if __name__ == '__main__':
    path = '/home/larry/WorkFiles/Nutstore/wuyang-7-15/pyUse/Data'
    processAll(path,startImgTag = 1)
