import requests, re, os, sys
from pyquery import PyQuery as pq

# sys.setdefaultencoding('utf-8')

headers = {
    'cookie': 'locatecity=510100; bitauto_ipregion=125.71.54.190%3a%e5%9b%9b%e5%b7%9d%e7%9c%81%e6%88%90%e9%83%bd%e5%b8%82%3b2501%2c%e6%88%90%e9%83%bd%e5%b8%82%2cchengdu; UserGuid=571d72b6-6ca9-4bee-a18e-8a6186542d4f; auto_id=ff5fcb92338a47dba2761f99e1ed625e; XCWEBLOG_testcookie=yes; CIGDCID=97328f262b5d4cfa93eebc90fe89ee96; G_CIGDCID=97328f262b5d4cfa93eebc90fe89ee96; selectcity=510100; selectcityid=2501; selectcityName=%E6%88%90%E9%83%BD; Hm_lvt_03efd23dfd835817ac8b9504cf0e715d=1602381656; Hm_lpvt_03efd23dfd835817ac8b9504cf0e715d=1602381896; report-cookie-id=207830170_1602381914562',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'referer': 'http://car.bitauto.com/',
    'Host': 'car.bitauto.com'
}


from selenium import webdriver
from pyquery import PyQuery as pq
import time
"""
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)

browser.get('http://car.bitauto.com/changancs75plus/m143938/peizhi/')
chrome_options.add_argument('--headless')
html = browser.page_source
print(html)
"""

url = 'http://car.bitauto.com/changancs75plus/m143938/peizhi/'
html = requests.get(url, headers=headers).text
# open('车型参数.html', 'wb').write(html)  # 保存车系到seriesList
print(html)