#!/usr/bin/env python
# author: combofish
# Filename: crawler_dangdang_goods.py

import requests
import re

def getHTMLText(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        # rint(">>>>>>>>>>>")
        # print(r.text)
        return r.text
    except:
        return ""

def parsePage(ilt, html):
    try:
        plt = re.findall(r'now\_.*?[\d\.]+', html)
        tlt = re.findall(r'nbsp\;\([\d\.]*', html)
        print(plt)
        print(tlt)
        
        for i in range(len(plt)):
            price = eval(plt[i].split(';')[1])
            title = eval(tlt[i].split('(')[1])
            ilt.append([title, price])

    except:
        print('function- parsePage Error')


def printGoodsList(ilt):
    tplt = '{:4}\t{:16}\t{:8}'
    print(tplt.format('序号','商品名称','价格'))
    count = 0
    for g in ilt:
        count = count + 1
        if count < 20:
            print(tplt.format(count, g[0], g[1]))


if __name__ == '__main__':
    
    goods = '数学之美'
    depth = 2
    start_url = "http://search.dangdang.com/?key=" + goods + "&act=input" 
    infoList = []
    for i in range(depth):
        try:
            # http://search.dangdang.com/?key=%E6%95%B0%E5%AD%A6%E4%B9%8B%E7%BE%8E&act=input&page_index=3
            url = start_url + '&page_index=' + str(i+1)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            print('Error')
            continue

    printGoodsList(infoList)



    
