#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: combofish
# Filename: test-net.py

import requests
from bs4 import BeautifulSoup
import urllib.request
import lxml
import json
from icecream import ic
import os
from tqdm import tqdm

departments = {"水利部门":'S',"发改委":'F',"农业农村部门":'N',"自然资源部门":'G',"财政部门":'C',"其他":"Y"}
imgDownBaseUrl = ''
DetailUrl = ""
cookie = {}


class NetDownload:
    def __init__(self,cookie,url):
        self.cookie = cookie
        self.url = url

    def process(self):
        webData = requests.get(self.url,cookies=self.cookie).text
        soup = BeautifulSoup(webData,"lxml")
        soupStr = self.__formart(str(soup))
        soup = self.__formartToJson(soupStr)
        return soup

    def __formart(self,soupStr):
        soupStr = soupStr[15:]
        soupStr = soupStr[:-18]
        return soupStr

    def __formartToJson(self,soupStr):
        soupJsonData = json.loads(soupStr)
        return soupJsonData


class WellInformation:
    def __init__(self,wellJsonData):
        self.wellJsonData = wellJsonData

        self.department = wellJsonData['BL_MOTORWELLPATROL']['DEPTNAME']
        self.locate = wellJsonData['BL_MOTORWELLPATROL']['XZDISTRICTNAME']
        self.year = wellJsonData['BL_MOTORWELLPATROL']['PRJECTYEAR']
        self.number = str(wellJsonData['BL_MOTORWELLPATROL']['WELLNUM'])

        self.imgLinks = []
        links = []
        for bl in wellJsonData['BL_ATTACH']:
            links.append(bl['FULLNAME'])

        for link in links:
            self.imgLinks.append(imgDownBaseUrl + link[1:].replace('\\','/'))


class ImageDownloader:
    def __init__(self,urls,name,savePath):
        self.savePath = savePath
        if(1 == len(urls)):
            self.__downloadImageProcess(urls[0],name)
        else:
            for i,links_ in enumerate(urls):
                # ic(i,links_)
                self.__downloadImageProcess(links_,name+'-'+ str(i+1))
    
    def __downloadImageProcess(self,url,name):
        # ic(url)
        r = urllib.request.urlopen(url)
        saveFile = os.path.join(self.savePath,str(name) + ".jpg")
        with open(saveFile, "wb") as f:
            f.write(r.read())

        # ic(saveFile)


def processWell(wellNumber):
    url = DetailUrl + str(wellNumber)
    data = NetDownload(cookie,url).process()

    well = WellInformation(data)
    # ic(well.imgLinks)
    # ic(well.department)
    # ic(well.locate)
    # ic(well.year)
    # ic(well.number)

    newDir = mkdirForWell(well.locate,well.department)
    imageName = well.number[-5:] + '-' + well.year[2:] + departments[well.department]
    ImageDownloader(well.imgLinks,imageName,savePath=newDir)    

def mkdirForWell(locate,department):
    if not os.path.exists(locate):
        os.mkdir(locate)

    newDir = os.path.join(locate,department)
    if not os.path.exists(newDir):
        os.mkdir(newDir)

    return newDir

def aprocess():
    with open('./well-5933.csv') as f:
        lines = f.readlines()
        totNumber = len(lines)
        for i in tqdm(range(0,totNumber)):
            line_ = lines[i]
            # for i,line_ in enumerate(lines):
            # outStr = ">>> Process file, wellNumber is " + line_.strip()
            # ic(outStr)
            processWell(str(line_).strip())

aprocess()
