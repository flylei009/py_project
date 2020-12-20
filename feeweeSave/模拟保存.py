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
'Cookie': 'fw-erp=76E528D81AEC8B69A9171096E4218C8228FA89C5287EAE6087D09443977EEFD861980FE628034198C316F8002B6C61B9FEC2268564EC6583F55CCC71E4528E73',
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

