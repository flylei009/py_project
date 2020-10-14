import requests,re,os
from pyquery import PyQuery as pq
from pathlib import Path

headers = {
'Accept': 'application/json, text/javascript, */*; q=0.01',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
'Connection': 'keep-alive',
'Cookie': 'locatecity=510100; CIGUID=916a5885-e797-449e-91f7-d8f1b0202d9c; selectcity=510100; selectcityid=2501; selectcityName=%E6%88%90%E9%83%BD; UserGuid=a76e10d4-5582-4d4b-8e4e-437b7fb9f655; bitauto_ipregion=110.191.216.96%3a%e5%9b%9b%e5%b7%9d%e7%9c%81%e6%88%90%e9%83%bd%e5%b8%82%3b2501%2c%e6%88%90%e9%83%bd%e5%b8%82%2cchengdu; auto_id=c374bb5f73ea430aba34d3e48954e9ce; CIGDCID=8a2a25e714dd49448bc46d2a76d0a28f-yiche; G_CIGDCID=8a2a25e714dd49448bc46d2a76d0a28f-yiche; CarStateForBitAuto=8e8d0406-ffb5-23f8-b38f-15e2170c57f2; BitAutoUserCode=9073a8f8-aded-1a64-8f3b-5b6570bbda3d; csids=5665_5008_3987; Hm_lvt_7b86db06beda666182190f07e1af98e3=1602467924,1602569651; Hm_lvt_03efd23dfd835817ac8b9504cf0e715d=1602464319,1602569653; Hm_lpvt_7b86db06beda666182190f07e1af98e3=1602578394; __xsptplus12=12.9.1602578395.1602578395.1%234%7C%7C%7C%7C%7C%23%23iy6Fe5SDRHbu63DXu-Iw4Su_D3bvZZ_m%23; report-cookie-id=501141479_1602580947609; XCWEBLOG_testcookie=yes; Hm_lpvt_03efd23dfd835817ac8b9504cf0e715d=1602581342',
'dvid': '916a5885-e797-449e-91f7-d8f1b0202d9c',
'gudpar': '7f813293da6872d5b6eff23df5bd27d3',
'gudslf': 'e507aee3d1fee344434758fe9901f0df',
'Host': 'car.bitauto.com',
'osl': '3',
'osvl': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
'Referer': 'http://car.bitauto.com/changancs75plus/m143938/peizhi/',
'reqid': 'd5e13d9d1bb399d3ef389d866acec819',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
'ver': 'v10.39.1',
'x-city-id': '2501',
'x-ip-address': '110.191.216.96',
'x-platform': 'pc',
'X-Requested-With': 'XMLHttpRequest',
'x-sign': 'fe374ee9ded5e7ede5c57d69a8cd83c1',
'x-timestamp': '1602582096094',
'X-Tingyun-Id': '8gU8qeI8HW4;r=582096121',
'x-user-guid': 'a76e10d4-5582-4d4b-8e4e-437b7fb9f655',
'uidl': '',
}

url = 'http://car.bitauto.com/web_api/car_model_api/api/v1/car/config_new_param?cid=508&param=%7B%22cityId%22%3A2501%2C%22carId%22%3A%22143938%22%7D'
doc = pq(requests.get(url, headers=headers).text)
print(doc)

