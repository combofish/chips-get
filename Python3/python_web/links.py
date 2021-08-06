#!/usr/bin/env python
# coding:utf-8
# Filename: links.py

def get_links(url):
    from bs4 import BeautifulSoup as soup
    import requests
    result = requests.get(url)
    page = result.text
    doc =  soup(page)
    links = [ element.get('href') for element in doc.find_all('a')]
    return links

if __name__ == '__main__':
    import sys
    for url in sys.argv[1:]:
        # url = 'http://www.baidu.com'
        print('Links in ',url)
        for num, link in enumerate(get_links(url), start=1):
            print(num,link)

        print()
