# import requests
# from pyquery import PyQuery as pq
#
# url = 'https://www.zhihu.com/explore'
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
# }
# html = requests.get(url, headers=headers).text
# print(html)
# doc = pq(html)
# items = doc('.explore-tab .feed-item').items()
# for item in items:
#     question = item.find('h2').text()
#     author = item.find('.author-link-line').text()
#     answer = pq(item.find('.content').html()).text()
#     file = open('explore.txt', 'a', encoding='utf-8')
#     file.write('\n'.join([question, author, answer]))
#     file.write('\n' + '=' * 50 + '\n')
#     file.close()

# 我们可以调用 JSON 库的 loads 方法将 JSON 文本字符串转为 JSON 对象，
print("")
import json
str = '''
[{
    "name": "Bob",
    "gender": "male",
    "birthday": "1992-10-18"
}, {
    "name": "Selina",
    "gender": "female",
    "birthday": "1995-10-18"
}]
'''
print(type(str))
data = json.loads(str)
# data=json.loads(str)
print(data)
print(type(data))
print(data[0])
print(type(data[0]))
print(data[0].get('name'))
# 请千万注意 JSON 字符串的表示需要用双引号，否则 loads 方法会解析失败



# 可以通过 dumps() 方法将 JSON 对象转为文本字符串病保存
import json
data = [{
    'name': 'Bob',
    'gender': 'male',
    'birthday': '1992-10-18'
}]
with open('data.json', 'w') as file:
    file.write(json.dumps(data))


# with open('data1.json','w') as file:
#     file.write(json.dumps(data))

with open('data1.json', 'w') as file:
    file.write(json.dumps(data, indent=2))

# 如果json中有中文，需要指定 ensure_ascii
with open('data.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(data, indent=2, ensure_ascii=False))