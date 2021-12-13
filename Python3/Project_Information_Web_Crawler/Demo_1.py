#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Combofish
# Filename: Demo_1.py

from bs4 import BeautifulSoup
import urllib.request, urllib.error, urllib.parse
import re
import xlwt
from tqdm import tqdm

url = ''
detail_url = "{}{}"
find_link = re.compile(r"javascript:openXmInfo(.*);")

# find detail
find_detail = re.compile(r'>(.*)</td>')
find_detail_res = re.compile(r'>(.*)</td>', re.S)


def make_up_link(link_args):
    xmdm, guid = link_args
    return detail_url.format(xmdm, guid)


def process_page(page_num):
    detail_links = []
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}
        data = bytes(urllib.parse.urlencode({'xzqh': 130000, 'rows': 25, 'page': page_num, }), encoding='utf-8')
        request = urllib.request.Request(url, data=data, headers=headers, method='POST')
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        for item in soup.select('tbody > tr'):
            item = str(item)
            link = re.findall(find_link, item)[0]
            link = link[1:-1]
            link_args = link.split(',')
            link_args = [link.strip('\'') for link in link_args]
            real_link = make_up_link(link_args)
            # print(real_link)
            detail_links.append(real_link)

    except urllib.error.URLError as e:
        if hasattr(e, 'code'):
            print(e.code)
        if hasattr(e, 'reason'):
            print(e.reason)

    return detail_links


def process_project_detail(link):
    # print(link)
    head = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}
    request = urllib.request.Request(link, headers=head)
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')
        # print(html)
        soup = BeautifulSoup(html, 'html.parser')
        datalist = []
        detail_sources = soup.select("table[class='tc_nr3'] > tr > td")
        code = re.findall(find_detail, str(detail_sources[1]))[0]
        name = re.findall(find_detail, str(detail_sources[3]))[0]
        depart = re.findall(find_detail, str(detail_sources[9]))[0]
        matter = re.findall(find_detail, str(detail_sources[10]))[0]
        result = re.findall(find_detail, str(detail_sources[11]))[0]
        date = re.findall(find_detail_res, str(detail_sources[12]))[0]
        app_num = re.findall(find_detail, str(detail_sources[13]))[0]

        date = date.strip()
        # print(code,name, depart, matter, result, date,app_num)

        datalist.append(code)
        datalist.append(name)
        datalist.append(depart)
        datalist.append(matter)
        datalist.append(result)
        datalist.append(date)
        datalist.append(app_num)

    except urllib.error.URLError as e:
        if hasattr(e, 'code'):
            print(e.code)
        if hasattr(e, 'reason'):
            print(e.reason)

    return datalist


def save2xls(data_list, save_file_name):
    workbook = xlwt.Workbook(encoding='utf-8')
    sheet = workbook.add_sheet('Projs', cell_overwrite_ok=True)
    col = ('项目代码', '项目名称', '审批部门', '审批事项', '审批结果', '审批日期', '审批文号')
    for i in range(0, 7):
        sheet.write(0, i, col[i])

    print("Saving...")
    for idx, detail in enumerate(tqdm(data_list)):
        for jdx, item in enumerate(detail):
            sheet.write(idx + 1, jdx, item)

    workbook.save(save_file_name)


def process():
    # 预定义参数
    limited_page = 25
    save_file_name = 'projects_detail.xls'

    links = []
    data_list = []
    print("Fetch page...")
    for page_num in tqdm(range(limited_page)):
        page_link = process_page(page_num + 1)
        links.extend(page_link)

    print('Fetch detail...')
    for link in tqdm(links):
        data = process_project_detail(link)
        data_list.append(data)

    save2xls(data_list, save_file_name)


if __name__ == '__main__':
    process()
    
