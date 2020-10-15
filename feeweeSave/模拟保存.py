import requests

url ='http://admin.feewee.cn/api/cas/erp/work/item/save?_s=1'
# url = 'http://admin.feewee.cn/api/cas/erp/work/item/save?_s=1602726035429'
headers = {
'Accept': 'application/json, text/plain, */*',
'Accept-Encoding':'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
'Connection':'keep-alive',
'Content-Length': '161',
'Content-Type': 'application/json',
'Cookie': 'Hm_lvt_e8002ef3d9e0d8274b5b74cc4a027d08=1600245650,1601260301; fw-erp=11572EE3C7CAC0F7562947BA44D6F6175AB293604F8CCF5F7705EED43EF1E937105926B1D2FB08BE62CEEBC4A35553D2BBA298B8D365FDED39EBD58BA2A1F04C',
'Host': 'admin.feewee.cn',
'Origin': 'http://admin.feewee.cn',
'Referer': 'http://admin.feewee.cn/',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}

# 修改已有的作业项
data_update ={
'brandId':'28',
'id': '8112',
'itemCode': 'XT170004',
'itemName': 'XT更换右前门限位器总成',
'specGroupCode': 'C202-T',
'stdManHours': '1',
'stdType': '2',
'workType': '1'
}

# 新增的作业项
data_save ={
'brandId':'28',
'itemDesc':'测试作业项',
'itemName':'测试作业项aaa',
'specGroupCode':'CHANA',
'stdManHours':'15',
'stdType':'2',
'workType':'1'
}

r = requests.post(url, headers=headers, json=data_update)
print(r.status_code,r.text)

