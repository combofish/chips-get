#!/usr/bin/env python
# author: combofish
# Filename: CoordinateConversion.py

import openpyxl
import os
import datetime
from datetime import date
import time
import configparser
import wx

APP_TITTLE = '坐标转换工具 V1.3'
APP_ICON = 'well.ico' # 请更换成你的icon
Usage = """>>> 软件使用
    * 点击  ‘开始转换’  按钮开始处理文件。
    * 默认的数据读取目录在  Data\ 文件夹下，导出文件存放在当前文件夹下的 Res\ 文件夹下。
 
>>>  软件设置
    * 可在当前目录下的  config.ini  文件来修改默认设置。
        * DataDir                            数据文件（Excel表格）存放的位置。
        * ResultDir                         导出坐标文件保存的位置。
        * ImageStartTag              生成的坐标文件对应的起始图标标号，可选数值1-200。
        * IngoreRowsNumber   软件处理时忽略Excel首部的行数，默认为1。

>>>  软件信息
    * @combofish    @Version-1.3

"""

class ConfContent():
    def __init__(self):
        self.currentDir = os.path.split(os.path.realpath(__file__))[0]
        configFilePath = os.path.join(self.currentDir, "config.ini")
        self.confTool = configparser.ConfigParser()
        self.confTool.read(configFilePath)
        self.sectionName = self.confTool.sections()[0]

        self.author = self.getPara("author")
        self.email = self.getPara("email")
        self.version = self.getPara("version")
        self.dataDir = self.getPara("datadir")
        self.resDir = self.getPara("resultDir")
        self.imageStartTagText = int(self.getPara("ImageStartTag"))
        self.ingoreRowsNumber = int(self.getPara("ingoreRowsNumber"))
        self.sheetName = self.getPara("SheetName")
        self.outputFileSuffix = self.getPara("OutputFileSuffix")

        self.dataDirPath = os.path.join(self.currentDir,self.dataDir)
        self.resDirPath = os.path.join(self.currentDir,self.resDir)
        if not os.path.exists(self.dataDirPath):
            os.mkdir(self.dataDirPath)
        if not os.path.exists(self.resDirPath):
            os.mkdir(self.resDirPath)

        fmt = "%Y-%m-%d"
        versionDate = self.getPara("date")
        versionDate = time.strptime(versionDate,fmt)[:3] # time.struct_time
        self.softwareDate = date(versionDate[0],versionDate[1],versionDate[2])
        self.now = datetime.date.today() # datetime.date
        self.dateDeltDays = (self.now - self.softwareDate) / datetime.timedelta(days = 1)

    def getPara(self,para):
        return self.confTool.get(self.sectionName,para)

    def getIntPara(self,para):
        return int(self.confTool.get(self.sectionName,para))


class ResultTextFrame(wx.Frame):
    def __init__(self,confCont):
        self.confCont = confCont
        dataDir = confCont.dataDir
        resDir = confCont.resDir
        imageStartTagText = confCont.imageStartTagText
        
        wx.Frame.__init__(self,None,title= APP_TITTLE,pos= (500,200),size= (630,500))
        icon = wx.Icon(APP_ICON, wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)
        panel=wx.Panel(self,-1)
        dataText = wx.StaticText(panel, -1, "源数据文件目录: " + dataDir + "\\",pos=(6,7), size=(160,24), style=wx.ALIGN_LEFT)
        resultText = wx.StaticText(panel,-1, "坐标文件输出目录: " + resDir + "\\",pos= (190,7),size= (200,24),style=wx.ALIGN_LEFT)
        imageStartTagText = wx.StaticText(panel,-1, "图标样式起始标号: " + str(imageStartTagText),pos= (380,7),size= (200,24),style=wx.ALIGN_LEFT)
        turnButton = wx.Button(panel,label= "开始转换",pos= (530,7),size= (80,24))
        self.contentText = wx.TextCtrl(panel,pos= (5,35),size= (620,460),style= wx.TE_MULTILINE)
        # wx.TE_MULTILINE可以实现以滚动条方式多行显示文本,若不加此功能文本文档显示为一行
        self.contentText.SetValue(Usage)
        self.contentTextString = []
        turnButton.Bind(wx.EVT_BUTTON,self.__tureFilesJudge)   # 绑定打开文件事件到open_button按钮上

    def setContentTextString(self,s):
        self.contentTextString.extend(s)
        str = '\n '.join(self.contentTextString)
        self.contentText.SetValue(str)

    def __tureFilesJudge(self,evt):
        if self.confCont.dateDeltDays > 30:
            self.contentText.SetValue(">>> 软件已达到使用期限，如需继续使用，请联系管理员！")
        else:
            processStrList = [">>> Processing..."]
            self.setContentTextString(processStrList)
            # frame.contentText.SetValue(">>> 请点击开始转换")
            self.__turnFilesProcess()

    def __turnFilesProcess(self):
        '''    处理数据文件    '''
        files = os.listdir(self.confCont.dataDirPath)
        # self.setContentTextString(files)
        fileCount = 0
        sumProcessLine = 0
        for f in files:
            fileName = os.path.join(self.confCont.dataDirPath,f)
            xlProcesser = Xl2location(fileName,fileCount,self.confCont)
            fileCount +=1
            fileProcessLineNumber,imageStartTagText = xlProcesser.processXlFile()
            sumProcessLine += fileProcessLineNumber
            fmt = " Done (%4d)  >>> Tag:%3d    FileName:%s"
            formatStr =  fmt % (fileProcessLineNumber,imageStartTagText,os.path.basename(fileName))
            self.setContentTextString([formatStr])
            xlProcesser.xlClose()
        
        self.setContentTextString([">>> Done."])
        self.setContentTextString([""])
        self.setContentTextString(["共处理个%3d 文件, 共处理 %3d 行" % (fileCount,sumProcessLine)])


class Xl2location:
    departments = {"水利部门":'S',"发改委":'F',"农业农村部门":'N',"自然资源部门":'G',"财政部门":'C',"其他":"Y"}

    def __init__(self,fileName,imageTag,confCont):
        self.confCont = confCont
        self.imgTag = imageTag + confCont.imageStartTagText
        self.f = fileName
        self.filePath = os.path.dirname(fileName)
        self.fileName = os.path.basename(fileName)
        
        self.sFilePath = self.confCont.resDirPath
        self.sFileName = self.fileName.split('.')[0] + '.' + self.confCont.outputFileSuffix

    def xlClose(self):
        self.xlsx.close()

    def processXlFile(self):
        self.xlsx = openpyxl.load_workbook(self.f,read_only=True)
        sheet = self.xlsx[self.confCont.sheetName]
        rows = sheet.rows
        i = 0
        count = 0
        mainContent = {}
        for row in rows:
            i = i + 1
            if i>self.confCont.ingoreRowsNumber:
                eachLine = []
                for cell in row:
                    eachLine.append(cell.value)

                if eachLine[1]:
                    mainContent[str(i-self.confCont.ingoreRowsNumber)] = eachLine
                    count = count + 1

        self.count = count
        self.__processLine(mainContent)
        return self.count,self.imgTag

    def __getInfoRowNumber(self,rowName):
        return self.confCont.getIntPara(rowName)

    def __processLine(self,mainContent):
        with open(os.path.join(self.sFilePath,self.sFileName),'w') as saveFile:
            for key, value in mainContent.items():
                well_locate = self.__nullJudge(value[self.__getInfoRowNumber("WellLocate")])
                well_number = value[self.__getInfoRowNumber("WellNumber")]
                well_name = self.__nullJudge(value[self.__getInfoRowNumber("WellName")])
                well_years = self.__nullJudge(value[self.__getInfoRowNumber("WellYear")])
                well_department = self.__nullJudge(value[self.__getInfoRowNumber("WellDepartment")])
                well_longitude,well_dimension = value[self.__getInfoRowNumber("WellLongDime")].split(',')
                well_description = self.__nullJudge(value[self.__getInfoRowNumber("WellDesc")])
                WellType = self.__nullJudge(value[self.__getInfoRowNumber("WellType")])

                lineInfoLocate = "/"+ well_locate
                if self.confCont.getIntPara("AddWellNumberName"):
                    lineInfoName = str(well_years)[-2:] + str(self.departments[well_department]) + "-#" + str(well_name) + \
                        '-' + str(well_number)[-5:]
                else:
                    lineInfoName = str(well_years)[-2:] + str(self.departments[well_department]) + "-#" + str(well_name)

                lineInfoDetail = str(well_years) + str(well_department[:2]) + "-共" + str(self.count) +"个-"
                if self.__getInfoRowNumber("WellIncludeDetail"):
                    # 是否为拟报废机井	"机井问题类型"	"泵问题类型"	"高压问题类型"	"低压问题类型"
                    lineInfoType = WellType + \
                        "-是否为拟报废机井" + self.__defaultJudge(value[self.__getInfoRowNumber("WellDetail")]) + \
                        "-机井"	  + self.__defaultJudge(value[self.__getInfoRowNumber("WellDetail")+1]) +\
                        "-泵"	  + self.__defaultJudge(value[self.__getInfoRowNumber("WellDetail")+2]) +\
                        "-高压"	  + self.__defaultJudge(value[self.__getInfoRowNumber("WellDetail")+3]) +\
                        "-低压"    + self.__defaultJudge(value[self.__getInfoRowNumber("WellDetail")+4]) 
                else:
                    lineInfoType = WellType

                wellDetail = lineInfoDetail + str(well_number) + '-' + lineInfoType + well_description
                if self.confCont.getIntPara("IncludeName"):
                    # 乡镇，名字（年份部门原机井编号），经度，纬度，图标样式，详情（年份，部门，机井类型，电类型，备注）
                    lineInfo = ','.join([lineInfoLocate,lineInfoName,str(well_longitude),str(well_dimension),\
                            str(self.imgTag),wellDetail])
                else:
                    # 乡镇，名字（年份部门原机井编号），经度，纬度，图标样式，详情（年份，部门，机井类型，电类型，备注）
                    lineInfo = ','.join([lineInfoLocate,str(well_longitude),str(well_dimension),\
                            str(self.imgTag),wellDetail])
                saveFile.write(lineInfo + '\n')

    def __nullJudge(self,value):
        if value:
            return str(value).replace(" ",'')
        if not value:
            return "null"

    def __defaultJudge(self,value):
        if value:
            return str(value).replace(" ",'')
        if not value:
            return ""


class CoordinateConversionApp(wx.App):
    def __init__(self):
        # 重构__init__方法，将错误信息重定位到文件中;
        # 默认redirect=True，输出到StdOut或StdError;
        # 为防止程序因错误一闪而过无法捕捉信息，可在
        # 控制台中使用python -i example.py来运行程序。
        wx.App.__init__(self,redirect=False,filename=r"Runlog.txt")
    def OnInit(self):
        confCont = ConfContent()
        frame=ResultTextFrame(confCont)
        frame.Show(True)
        return True


def process():
    app=CoordinateConversionApp()
    app.MainLoop()

process()
