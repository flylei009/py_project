import requests, re, os
from pyquery import PyQuery as pq
from pathlib import Path
import json
import pathlib
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",  # 数据库主机地址
    user="root",  # 数据库用户名
    passwd="mysql@pwd123",  # 数据库密码
    database="yan_test"  # 之前已经创建了
)

mycursor = mydb.cursor()




# 获取所有区域
areaList = []

# 品牌清单
brandList = []
seriesList = []
specList = []

# 获取所有区域
def getAllAreas():
    # 如果文件已经存在了，读取文件进行遍历保存到数据库
    if os.path.exists('areaList.txt'):  # True/False  判断路径是否存在
        file = open('areaList.txt', 'r', encoding='utf-8')
        areaList = json.loads(file.read())

        listKeys = areaList[0].keys()
        # print(type(listKeys))
        # print(listKeys)
        tableName = 'areacode'
        createTable(tableName,listKeys)
        for area in areaList:
            # print(area)
            # print(type(area))
            values = area.values()
            # print(values)
            # print(type(values))

            temp1 = str(values).replace('dict_values([', '')
            temp2 = temp1.replace("])", "")
            sql = 'insert into '+tableName+' values ('+temp2+')'
            # print(sql)
            mycursor.execute(sql)
            mydb.commit()

        print('插入完成')
        mycursor.execute('select * from areacode')
        i = 0
        for column in mycursor:
            i +=1
            print(i,column)



    # 如果文件不存在了，则从网上下载数据
    else:
        areaurl = 'http://car.bitauto.com/web_api/web_app/api/v1/city/get_area_list?cid=508'
        areaStr = requests.get(areaurl, headers=headers).text
        # print(type(areaStr))
        tempDic = eval(areaStr)
        # print(tempDic)
        # print(type(tempDic))
        tempDic2 = tempDic['data']
        areaList = tempDic2['list']
        open('areaList.txt', 'w').write(json.dumps(areaList))
        # print("areaList： ", areaList)

        # print(type(areaList))
        # print(tempDic2)
        # print(areaList)
        # for area in areaList:
            # print(area)

# 生成对应的表
def createTable(tableName, columnstemp):
    # mycursor = mydb.cursor()
    # 如果表不存在需要创建
    if (table_exists(mydb, tableName) != 1):
        temp1  = str(columnstemp).replace('dict_keys([','')
        temp2  = temp1.replace("',"," varchar(50),")
        temp3  = temp2.replace("'])"," varchar(50)")
        temp4  = temp3.replace("'","")
        # 有ID的写法
        # sql = "create table "+tableName  +"( `id` int(11) NOT NULL AUTO_INCREMENT, "+temp4+", PRIMARY KEY (`id`))"
        sql = "create table "+tableName  +"(  "+temp4+")"
        print(sql)
        mycursor.execute(sql)

# 判断表是否存在
def table_exists(con,table_name):        #这个函数用来判断表是否存在
    sql = "show tables;"
    mycursor = con.cursor()
    mycursor.execute(sql)
    tables = [mycursor.fetchall()]
    table_list = re.findall('(\'.*?\')',str(tables))
    table_list = [re.sub("'",'',each) for each in table_list]
    if table_name in table_list:
        return 1        #存在返回1
    else:
        return 0        #不存在返回0


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

    # 创建对应的表，只需要一次
    # sql = 'create table brand( brandId varchar(50), brandName varchar(50), img varchar(400), href varchar(400))'
    # mycursor.execute(sql)
    for brand in brandList:
        # print(brand)
        # print(brand['brandId'])
        sql = "insert into brand values ('"+ brand['brandId']+ "','"+brand['brandName']+ "','"+brand['img'] + "','"+brand['href']+"')"
        # print(sql)
        mycursor.execute(sql)
    mydb.commit()

# 获取所有车系
def getAllSeries():
    # tempBrandList = brandList  #正式的时候用
    seriesList =[]
    # 暂时从文本读取
    if os.path.exists('seriesList.txt'):
        file = open('seriesList.txt', 'r', encoding='utf-8')
        seriesList = json.loads(file.read())

        # 如果车系数据文件已经下载了，就直接读取文件，并且导入数据库
        sql = 'create table series( brandId varchar(50), seriesId varchar(50), seriesDetail varchar(200), seriesName varchar(50),seriesImg varchar(400),seriesPrice  varchar(100))'
        print(sql)
        mycursor.execute(sql)

        for series in seriesList:
            print(series)
            print(series['brandId'])
            sql = "insert into series values ('" + series['brandId'] + "','" + series['seriesId'] + "','" + series[
                'seriesDetail'] + "','" + series['seriesName'] + "','" + series['seriesImg'] + "','" + series['seriesPrice'] +"')"
            print(sql)
            mycursor.execute(sql)
        mydb.commit()

    # 如果车系文件没有生成，则从 brandList 中加载车系页面，下载车系
    else:
        file = open('brandList.txt', 'r', encoding='utf-8')
        tempBrandList = json.loads(file.read())
        for brand in tempBrandList:
            # if brand['brandId'] == '136':     #之前只想下载长安的
            # 暂时定的抓取3页
            for page in range(1, 3, 1):
                url = brand['href'] + "&page=" + str(page)
                print(url)

                seriesRs = requests.get(url, headers=headers).text
                sdoc = pq(seriesRs)

                seriesHtmlList = sdoc('div.search-result-list div.search-result-list-item')
                for ser in seriesHtmlList.items():
                    # print(ser.attr('data-id'), ser('a p.cx-name').text())
                    seriesDic = {
                        'brandId': brand['brandId'],  # brandID
                        'seriesId': ser.attr('data-id'),  # 车系ID
                        'seriesDetail': domain + ser('a').attr('href'),  # 车系详情页面
                        'seriesName': ser('a p.cx-name').text(),  # 车系名
                        'seriesImg': ser('a img').attr('src'),  # 车系图片
                        'seriesPrice': ser('a p.cx-price').text(),  # 车系价格区间
                    }
                    seriesList.append(seriesDic)
        open('seriesList.txt', 'w').write(json.dumps(seriesList))  #保存车系到seriesList
        print("seriesList： ", len(seriesList), seriesList)



# 获取所有车型
def getAllSpec():
    specList = []
    # 如果specList.txt 赢存在 则从文本读取
    if os.path.exists('specList.txt'):
        file = open('specList.txt', 'r', encoding='utf-8')
        specList = json.loads(file.read())

        # （建表语句，只执行一次）如果车系数据文件已经下载了，就直接读取文件，并且导入数据库
        # sql = 'create table spec( brandId varchar(50), seriesId varchar(50), specId varchar(50), specUrl varchar(200), specName varchar(100),specImg varchar(200), specParam varchar(200),specPrice varchar(50),specAcPrice varchar(50))'
        # print(sql)
        # mycursor.execute(sql)

        for spec in specList:
            print(spec)
            print(spec['brandId'])
            sql = "insert into spec values ('" + spec['brandId'] + "','" + spec['seriesId'] + "','" + spec[
                'specId'] + "','" + spec['specUrl'] + "','" + spec['specName'] + "','" + spec['specImg']  + "','" + spec['specParam']+ "','" + spec['specPrice']+ "','" + spec['specAcPrice'] + "')"
            print(sql)
            mycursor.execute(sql)
        mydb.commit()

    # 如果车型文件没有生成，需要先生成车型文件
    else:
        file = open('seriesList.txt', 'r', encoding='utf-8')
        tempseriesList = json.loads(file.read())

        for series in tempseriesList:

            # 136是只爬取长安的
            # if series['brandId'] == '136':
            print(series)
            specHtml = series['seriesDetail']

            specRs = requests.get(specHtml, headers=headers).text
            specdoc = pq(specRs)

            seriesHtmlList = specdoc('div.power-name tr.list-info')
            for ser in seriesHtmlList.items():
                # print(ser)
                specDic = {
                    'brandId': series['brandId'],  # brandID
                    'seriesId': series['seriesId'],  #车系
                    'specId': ser.attr('data-id'), # 车型

                    'specUrl': domain + ser('td.first a').attr('href'), #车型网址
                    'specName': ser('td.first a').text(), #车型名

                    'specImg': ser('td.third a.car-item-pic').attr('href'), #车型图片
                    'specParam': ser('td.third a.car-item-param').attr('href'), #车型参数
                    'specPrice': ser('td.fouth span').text(), #指导价
                    'specAcPrice': ser('td.five').text() #本地报价

                }
                specList.append(specDic)
                    # print(specList)
        open('specList.txt', 'w').write(json.dumps(specList))  #保存车型到specList
        print("specList： ", len(specList), specList)



def main(offset):
    #获取区域信息, 只需要执行一次即可
    # getAllAreas()

    # 获取所有的品牌信息
    # getAllBrand()

    # 获取车系信息
    # getAllSeries()

    # 获取车型信息
    getAllSpec()




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
