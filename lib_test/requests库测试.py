# import requests
# r = requests.get('https://www.baidu.com/')
# print(type(r))
# print(r.status_code)
# print(type(r.text))
# print(r.text)
# print(r.cookies)
#
# print("请求带参数，参数是字典值------------------------------------------------------------------------------------------------------------------------")
#
# import requests
# r = requests.get('http://httpbin.org/get')
# print(r.text)
#
# # 输出结果
# """{
#   "args": {},
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.24.0",
#     "X-Amzn-Trace-Id": "Root=1-5f707bdf-a306d4cdeab5408649f60337"
#   },
#   "origin": "218.88.54.71",
#   "url": "http://httpbin.org/get"
# }"""
#
#
#
#
# print("请求带参数，参数是字典值------------------------------------------------------------------------------------------------------------------------")
# import requests
# data = {
#     'name': 'germey',
#     'age': 22
# }
# r = requests.get("http://httpbin.org/get", params=data)
# print(r.text)
#
# print("r.json ------------------------------------------------------------------------------------------------------------------------")
# import requests
# r = requests.get("http://httpbin.org/get")
# print(type(r.text))
# print(r.json())
# print(r.json()['headers'])
# print(type(r.json()))
#
# print("requests 加入header  ------------------------------------------------------------------------------------------------------------------------")
# import requests
# import re
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
# }
# r = requests.get("https://www.zhihu.com/explore", headers=headers)
# # r = requests.get("https://www.zhihu.com/explore")
# pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
# titles = re.findall(pattern, r.text)
# print(r.text)
# # print(r.text.encode('utf-8'))
# print(titles)
#
# print("保存图片  ------------------------------------------------------------------------------------------------------------------------")
# import requests
# r = requests.get("https://github.com/favicon.ico")
# with open('favicon.ico', 'wb') as f:
#     f.write(r.content)


# import requests
# r = requests.get("https://www.zhihu.com/explore")    #不加头信息，要报错
# print(r.text)
#
# import requests
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
# }
# r = requests.get("https://www.zhihu.com/explore", headers=headers)
# print(r.text)

# print("POST 请求  ------------------------------------------------------------------------------------------------------------------------")

# import requests
# data = {'name': 'germey', 'age': '22'}
# r = requests.post("http://httpbin.org/post", data=data)
# print(r.text)
# print(type(r))
#
# import requests
# data = {'name': 'germey', 'age': '22'}
# r = requests.get("http://httpbin.org/get")
# print(r.text)
# print(type(r))


# print("Response的各种属性  ------------------------------------------------------------------------------------------------------------------------")
# import requests
# r = requests.get('http://www.jianshu.com')
# print(type(r.status_code), r.status_code)
# print(type(r.headers), r.headers)
# print(type(r.cookies), r.cookies)
# print(type(r.url), r.url)
# print(type(r.history), r.history)

#
# import requests
# r = requests.get('http://www.baidu.com')
# exit() if not r.status_code == requests.codes.ok else print('Request Successfully')

# print("获取cookie  ------------------------------------------------------------------------------------------------------------------------")
#

import requests

requests.get('http://httpbin.org/cookies/set/number/123456789')
r = requests.get('http://httpbin.org/cookies')
print(r.text)

