import requests, re, os
from pyquery import PyQuery as pq
from pathlib import Path
import json

# 品牌清单
brandList = []
seriesList = []


# 获取所有品牌
def getAllBrand():
    url = 'http://car.bitauto.com/'
    rs = requests.get(url, headers=headers).text
    doc = pq(rs)
    brandHtmlList = doc('div.brand-list div.item-brand')
    for brand in brandHtmlList.items():
        # print(brand)
        brandDic = {
            'brandId': brand.attr('data-id'),
            'brandName': brand('img.brand-icon').attr('data-name'),
            'img': brand('img.brand-icon').attr('data-original'),
            'href': domain + brand('a').attr('href'),
        }
        brandList.append(brandDic)
    # 保存到本地txt
    open('brandList.txt', 'w').write(json.dumps(brandList))
    print("resultList： ", brandList)


# 获取所有车系
def getAllSeries():
    # tempBrandList = brandList  #正式的时候用
    # 暂时从文本读取
    file = open('brandList.txt', 'r', encoding='utf-8')
    tempBrandList = json.loads(file.read())

    for brand in tempBrandList:
        if brand['brandId'] == '136':
            # print(brand)

            for page in range(1, 3, 1):
                url = brand['href'] + "&page=" + str(page)  # 暂时定的抓取3页
                print(url)

                seriesRs = requests.get(url, headers=headers).text
                sdoc = pq(seriesRs)

                seriesHtmlList = sdoc('div.search-result-list div.search-result-list-item')
                for ser in seriesHtmlList.items():
                    print(ser.attr('data-id'),ser('a p.cx-name').text())
                    seriesDic = {
                        'brandId': brand['brandId'],  # brandID
                        'seriesId': ser.attr('data-id'),  # 车系ID
                        'seriesName': ser('a p.cx-name').text(),  # 车系名
                        'seriesImg': ser('a img').attr('src'),  # 车系图片
                        'seriesPrice': ser('a p.cx-price').text(),  # 车系价格区间
                    }
                    seriesList.append(seriesDic)

    print("resultList： ", len(seriesList), seriesList)


def main(offset):
    # 获取所有的品牌信息
    # getAllBrand()

    # 获取车系信息
    getAllSeries()

headers = {
    'cookie': 'locatecity=510100; bitauto_ipregion=125.71.54.190%3a%e5%9b%9b%e5%b7%9d%e7%9c%81%e6%88%90%e9%83%bd%e5%b8%82%3b2501%2c%e6%88%90%e9%83%bd%e5%b8%82%2cchengdu; UserGuid=571d72b6-6ca9-4bee-a18e-8a6186542d4f; auto_id=ff5fcb92338a47dba2761f99e1ed625e; XCWEBLOG_testcookie=yes; CIGDCID=97328f262b5d4cfa93eebc90fe89ee96; G_CIGDCID=97328f262b5d4cfa93eebc90fe89ee96; selectcity=510100; selectcityid=2501; selectcityName=%E6%88%90%E9%83%BD; Hm_lvt_03efd23dfd835817ac8b9504cf0e715d=1602381656; Hm_lpvt_03efd23dfd835817ac8b9504cf0e715d=1602381896; report-cookie-id=207830170_1602381914562',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'referer': 'http://car.bitauto.com/',
    'Host': 'car.bitauto.com'
}

domain = 'http://car.bitauto.com'

if __name__ == '__main__':
    main(0)
