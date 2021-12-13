#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Combofish
# Filename: ForUseHebpi.py

from bs4 import BeautifulSoup
import urllib.request, urllib.error, urllib.parse
import re
import xlwt
import gzip
from tqdm import tqdm

base_url = '{}'
detail_url = '{}'
find_code = re.compile(r'm=11&amp;d=(\d*)"')


def make_up_url(code):
    return detail_url.format(code)


def process_page(page_num):
    links = []

    url = base_url.format(page_num)
    head = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}
    request = urllib.request.Request(url, headers=head)
    try:
        # print(url)
        response = urllib.request.urlopen(request)
        html = response.read().decode('unicode_escape')
        # print(html)
        soup = BeautifulSoup(html, 'html.parser')
        for item in soup.find_all('li'):
            item = str(item)
            # print(item)
            data = re.findall(find_code, item)[0]
            links.append(make_up_url(data))

    except urllib.error.URLError as e:
        if hasattr(e, 'code'):
            print(e.code)
        if hasattr(e, 'reason'):
            print(e.reason)

    return links


def process_page_detail(url):
    data_list = []

    head = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-US,en;q=0.9',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}
    request = urllib.request.Request(url, headers=head)
    try:
        response = urllib.request.urlopen(request)
        html = response.read()
        # print(html)
        soup = BeautifulSoup(html, 'html.parser')
        name = soup.find_all('h1')[0].text
        city = name.split('-')[0]

        items = [str(item.text) for item in soup.select('li > span')]
        item_number = items[0][:6]
        progressive_stage = items[1]
        total_investment = items[2]
        construction_nature = items[3]
        construction_period = items[4]
        industry = items[5]
        device_source = items[6]
        funding_source = items[7]
        major_device = items[8]
        construction_content = items[9]
        update_time = items[10]

        # print(name)
        # print(item_number, progressive_stage, total_investment, construction_nature)
        # print(construction_period, industry, device_source, funding_source)
        # print(major_device, construction_content, update_time)

        data_list.append(city)
        data_list.append(name)
        data_list.append(item_number)
        data_list.append(progressive_stage)
        data_list.append(total_investment)
        data_list.append(construction_nature)
        data_list.append(construction_period)
        data_list.append(industry)
        data_list.append(device_source)
        data_list.append(funding_source)
        data_list.append(major_device)
        data_list.append(construction_content)
        data_list.append(update_time)

        # print('...')
        # for i in items:
        #     print(i)

    except urllib.error.URLError as e:
        if hasattr(e, 'code'):
            print(e.code)
        if hasattr(e, 'reason'):
            print(e.reason)

    return data_list


def save2xls(data_list, save_file_name):
    workbook = xlwt.Workbook(encoding='utf-8')
    sheet = workbook.add_sheet('Hebpi', cell_overwrite_ok=True)
    col = (
        '地区', '项目名称', '项目编号', '进展阶段', '投资总额', '建设性质', '建设周期', '所属行业', '设备来源', '资金来源:(万元)', '主要设备', '建设内容/主要产品', '更新时间')
    for i in range(0, len(col)):
        sheet.write(0, i, col[i])

    print("Saving...")
    for idx, detail in enumerate(tqdm(data_list)):
        for jdx, item in enumerate(detail):
            sheet.write(idx + 1, jdx, item)

    workbook.save(save_file_name)


def process():
    limited_page_number = 50
    save_file_name = 'demo2_projects_detail.xls'

    links = []
    data_lists = []
    print('Getting page...')
    for page_number in tqdm(range(limited_page_number)):
        link = process_page(page_number + 1)
        links.extend(link)
        # break

    print("Fetching detail...")
    for link in tqdm(links):
        # print(l)
        data_list = process_page_detail(link)
        data_lists.append(data_list)
        # break

    print('Saving to file...')
    save2xls(data_lists, save_file_name)

    print('Done...')


if __name__ == '__main__':
    process()
