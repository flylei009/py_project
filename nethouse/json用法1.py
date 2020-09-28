#!/usr/bin/python3

import json

# Python 字典类型转换为 JSON 对象
data1 = {
    'no': 1,
    'name': 'Runoob',
    'url': 'http://www.runoob.com'
}
# 字典转换为字符串
json_str = json.dumps(data1)
print("Python 原始数据：", repr(data1))
print("JSON 对象：", json_str)

print("json_str 的类型：",type(json_str))

  # 将字符转换为字典
data2 = json.loads(json_str)
print("data2['name']: ", data2['name'])
print("data2['url']: ", data2['url'])

# 写入 JSON 数据
# with open('data.json', 'w') as f:
#     json.dump(data, f)
#
# # 读取数据
# with open('data.json', 'r') as f:
#     data = json.load(f)

print(type(data1))
print(type(data2))
