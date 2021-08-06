#!/usr/bin/env python
# author: combofish
# Filename: Xl2location.py

import openpyxl
import os

class Xl2location:
    departments = {"水利部门":'S',"发改委":'F',"农业农村部门":'N',"自然资源部门":'G',"财政部门":'C',"其他":"Y"}

    def __init__(self,fileName,imgTag = 1):
        self.imgTag = imgTag
        self.filePath = os.path.dirname(fileName)
        self.fileName = os.path.basename(fileName)
        self.sFilePath = os.path.join(self.filePath,'Res')
        self.sFileName = self.fileName.split('.')[0] + '.txt'
        self.xlsx = openpyxl.load_workbook(fileName,read_only=True)
        
    def xlClose(self):
        self.xlsx.close()

    def processXlFile(self):
        # xlsx = openpyxl.load_workbook(self.fileName,read_only=True)
        sheet = self.xlsx['sheet1']
        rows = sheet.rows
        return rows

    def __countWell(self,rows):
        '''No use'''
        i = 0
        count = 0
        for row in rows:
            i=i+1
            if i>3:
                eachLine = []
                for cell in row:
                    eachLine.append(cell.value)
                if eachLine[1]:
                    count = count + 1
        return count

    def mainInfoAndCount(self,rows):
        # print("in mainInfo")
        i = 0
        count = 0
        mainContent = {}
        for row in rows:
            i = i + 1
            # print("i = ", i)
            if i>3:
                eachLine = []
                for cell in row:
                    eachLine.append(cell.value)

                if eachLine[1]:
                    mainContent[str(i-3)] = eachLine
                    count = count + 1

                # print(i,eachLine)
        self.count = count
        return count,mainContent

    def __nullJudge(self,value):
        if value:
            return str(value).replace(" ",'')
        if not value:
            return "null"

    def processLine(self,mainContent):
        with open(os.path.join(self.sFilePath,self.sFileName),'w') as saveFile:
            for key, value in mainContent.items():
                well_number = value[1]
                well_name = self.__nullJudge(value[2])
                well_years = self.__nullJudge(value[3])
                well_department = self.__nullJudge(value[4])
                well_locate = self.__nullJudge(value[7])
                well_longitude,well_dimension = value[21].split(',')
                well_description = self.__nullJudge(value[24])
                lineInfo = "/"+ well_locate + "," + str(well_years) + str(self.departments[well_department]) + "-#" + \
                    str(well_name) + "," + str(well_longitude) + "," + str(well_dimension) + "," + str(self.imgTag) + \
                    "," + str(well_years) + str(well_department[:2]) + "-共" + str(self.count) +"个-" + \
                    str(well_number) + '-' + str(well_description)
                saveFile.write(lineInfo + '\n')
