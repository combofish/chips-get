#!/usr/bin/env python
# author: combofish
# Filename: python_crawler.py

import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        print(r.encoding)
        r.encoding = r.apparent_encoding
        print(r.encoding)
        return r.text
    except:
        print("Error")
        return ""

    
def fillUnivList(ulist,html): 
    soup = BeautifulSoup(html,'html.parser')
    # print(soup.find_all('div'))
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[i].string for i in range(5)])


def printUnivList(ulist, num):
    tplt = "{0:^6}\t{1:{5}^10}\t{2:^6}\t{3:^6}\t{4:^6}"
    print(tplt.format("排名","学校名称","省市","总分","指标得分",chr(12288)))
    for i in range(num):
        #print(ulist[i])
        u = ulist[i]
        print(tplt.format(u[0],u[1],u[2],u[3],u[4],chr(12288)))

        
if __name__ == '__main__':

    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html'
    uinfo = []

    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20)
