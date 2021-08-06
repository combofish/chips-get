#!/usr/bin/env python
# author: combofish
# Filename: MapExportTest2.py

import openpyxl
import os

departments = {"水利部门":0,"发改委":1,"农业农村部门":2,"自然资源部门":3}

def nullJudge(value):
    if value:
       return value
    if not value:
       return "null"

def processSingleLine(l,count,f):
    # 排除机井编号为空
    if l[1]:
        # print("机井编号",l[1])
       # print(l)

        i = 0
        for ln in l:
            #print(i,ln)
            i=i+1

        well_number = l[1]
        well_name = nullJudge(l[2])
        well_years = nullJudge(l[3])
        well_department = nullJudge(l[4])
        well_locate = nullJudge(l[7])

        well_longitude,well_dimension = l[21].split(',')
        well_description = nullJudge(l[24])

        imgTag = 53
      
        # print(well_name,well_department,well_description,well_locate,well_dimension,well_longitude)
        lineInfo = "/"+ well_locate + "," + str(well_years) + str(departments[well_department]) + "-#" + str(well_name) + \
          "," + str(well_longitude) + "," + str(well_dimension) + "," + str(imgTag) + "," + str(well_years[-2:]) + \
          str(well_department[:2]) + "-共" + str(count) +"个-" + str(well_description) + '-' + str(well_number)
        # print(lineInfo)
        saveLineInformation(lineInfo,f)


def saveLineInformation(line,f):
    f.write(line+"\n")


def countWell(rows):
    ## printing the values of cells using rows
    i = 0
    count = 0

    for row in rows:
        i=i+1
        if i>3:
            ll = []
            for cell in row:
              #print(cell.value, end = ' ')
                ll.append(cell.value) 
                # print("use>>>"+ str(ll))

            if ll[1]:
                count = count + 1
    return count

def splitLines(rows,count,f):             
    j = 0
    for row in rows:
        j = j + 1
        lineInfo = []
        if j>3:
            for cell in row:
              # print(cell.value)
                lineInfo.append(cell.value)
            processSingleLine(lineInfo,count,f)
             # print("processSingleLine")

def process(filename):
    ## opening the previously created xlsx file using 'load_workbook()' method
    xlsx = openpyxl.load_workbook(filename,read_only=True)

    ## getting the sheet to active
    # sheet = xlsx.active
    sheet = xlsx['sheet1']

    ## getting the reference of the cells which we want to get the data from
    rows = sheet.rows
    return rows

def processAll(path):
    files= os.listdir(path) #得到文件夹下的所有文件名称
    s = []
    for file in files: #遍历文件夹
       if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开
           processFile(path,file)

def processFile(path,file):
    fileName = path + '/' + file
    rows = process(fileName)
    count = countWell(rows)
    print("count = ",count)

    rows = process(fileName)
    print("Process >>> " + fileName)
    savePath = "/home/larry/WorkFiles/Nutstore/wuyang-7-6/mapExportTest/Res/"
    f = open(savePath + file[:-5] + ".txt",'a')
    splitLines(rows,count,f)
    f.close()

if __name__ == '__main__':
    count = 0
    savePath = "/home/larry/WorkFiles/Nutstore/wuyang-7-6/mapExportTest/Res/"
    path = "/home/larry/WorkFiles/Nutstore/wuyang-7-6/mapExportTest/Data"
    # f = open('use.txt','a')
    processAll(path)
    # f.close()

