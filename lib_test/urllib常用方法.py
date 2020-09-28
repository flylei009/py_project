"""
import urllib.request
# from  urllib.request import *
# urllib.request 对应： 库.模块   urlopen 对应 模块request下的方法

response = urllib.request.urlopen('https://www.python.org')
# response = urllib.request.urlopen('https://www.python.org')    # 如果引用方式为   import urllib.request

# 返回服务器端接收请求后的反馈内容
# print(response.read().decode('utf-8'))
print("--------------------------------------------------------------------------")
print(response.read())
print("--------------------------------------------------------------------------")


# 显示  response 对应的各种属性
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))




# urlopen 方法全貌，如果data有数据说明是是post请求
# urllib.request.urlopen(url, data=None, [timeout,]*, cafile=None, capath=None, cadefault=False, context=None)


print(" post请求的访问方式    --------------------------------------------------------------------------")
data = bytes(urllib.parse.urlencode({'word': 'hello','name': 'jenny'}), encoding='utf8')
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
# print(response.read().deco)
print(response.read().decode('utf-8'))


# print(" timeout 参数     --------------------------------------------------------------------------")
# response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
# print(response.read())

print(" timeout 参数 异常处理    --------------------------------------------------------------------------")
import socket
import urllib.request
import urllib.error

try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')


print(" Request 构造构造方法    --------------------------------------------------------------------------")

from urllib import request, parse

url = 'http://httpbin.org/post'
headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'httpbin.org'}

# headers 的全量参数
# headers = {"args": {}, "data": "","files": {},"form": {"name":"Germey"},"headers": {"Accept-Encoding":"identity","Content-Length":"11","Content-Type":"application/x-www-form-urlencoded","Host":"httpbin.org","User-Agent":"Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"},"json": '',"origin":"219.224.169.11","url":"http://httpbin.org/post"}

dict = {'name': 'Germey'}
data = bytes(parse.urlencode(dict), encoding='utf8')
req = request.Request(url=url, data=data, headers=headers, method='POST')

# 额外添加其他头部信息
req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')


response = request.urlopen(req)
print(response.read().decode('utf-8'))


print(" 代理的使用方法    --------------------------------------------------------------------------")

from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

proxy_handler = ProxyHandler({
    'http': 'http://127.0.0.1:9743',
    'https': 'https://127.0.0.1:9743'
})
opener = build_opener(proxy_handler)
try:
    response = opener.open('https://www.baidu.com')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)

print(" 验证    --------------------------------------------------------------------------")
from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.error import URLError

username = 'username'
password = 'password'
url = 'http://192.168.0.77:8888/5.x/'

p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, username, password)
auth_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handler)

try:
    result = opener.open(url)
    html = result.read().decode('utf-8')
    print(html)
except URLError as e:
    print(e.reason)

print(" 获取网站的cookie    --------------------------------------------------------------------------")
import http.cookiejar, urllib.request

cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
for item in cookie:
    print(item.name+"="+item.value)

print(" 获取网站的cookie（保存为文本）    --------------------------------------------------------------------------")
import http.cookiejar, urllib.request

filename = 'cookies.txt'
cookie = http.cookiejar.MozillaCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)
"""

# print(" 获取网站的cookie(自己改造了下，没有成功)    --------------------------------------------------------------------------")
# import http.cookiejar, urllib.request
# from urllib import request, parse
#
# cookie = http.cookiejar.CookieJar()
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
#
#
# req = request.Request(url='http://admin.feewee.cn')
# req.add_header('Cookie','Hm_lvt_e8002ef3d9e0d8274b5b74cc4a027d08=1600245650; fw-erp=EC16CD9A6B9A6DD74255930E7E8DA61F5AB293604F8CCF5F7705EED43EF1E9377CD3237AFA3D66E1A1990B213DA0FC71D8B469CF97A7ACB255C02EBAEFE311C8')
# # 额外添加其他头部信息
# response = request.urlopen(req)
# # print(response.read().decode('utf-8'))
#
# for item in cookie:
#     print(item.name+"="+item.value)


# import urllib.request
# import urllib.error
# import socket
#
# try:
#     response  = urllib.request.urlopen("http://www.baidu.com")
# except urllib.error.URLError as e:
#     print(e.reason)
#
# try:
#     response  = urllib.request.urlopen("http://www.baidu.com")
# except urllib.error.HTTPError as e:
#     if isinstance(e.reason, socket.timetout):
#         print(e.reason)


print(" 解析URL urlparse   --------------------------------------------------------------------------")
from urllib.parse import urlparse
result = urlparse('www.baidu.com/index.html;user?id=5#comment', scheme='https')
print(result)
# 展示效果：ParseResult(scheme='https', netloc='', path='www.baidu.com/index.html', params='user', query='id=5', fragment='comment')
print(result.__getattribute__('fragment'))   #获取指定元素的值
# 展示效果：comment

print(" 接收URL参数生成URL urlunparse   --------------------------------------------------------------------------")
from urllib.parse import urlunparse
data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
print(urlunparse(data))
# 展示效果： http://www.baidu.com/index.html;user?a=6#comment


print(" 接收URL参数生成URL urlunparse   --------------------------------------------------------------------------")
from urllib.parse import urlsplit
result = urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
print(result)
# 展示效果： SplitResult(scheme='http', netloc='www.baidu.com', path='/index.html;user', query='id=5', fragment='comment')
print(result.scheme, result[0], result[1])
# 展示效果： http http www.baidu.com

print(" 接收URL参数生成URL urlunsplit   --------------------------------------------------------------------------")
from urllib.parse import urlunsplit
data = ['http', 'www.baidu.com', 'index.html', 'a=6', 'comment']
print(urlunsplit(data))
# 展示效果： http://www.baidu.com/index.html?a=6#comment


print(" 链接URL urljoin   --------------------------------------------------------------------------")
from urllib.parse import urljoin
print(urljoin('http://www.baidu.com', 'FAQ.html'))
# 展示效果：  http://www.baidu.com/FAQ.html

print(" 字典构造参数,urlencode方法   --------------------------------------------------------------------------")
from urllib.parse import urlencode
params = {
    'name': 'germey',
    'age': 22
}
base_url = 'http://www.baidu.com?'
url = base_url + urlencode(params)
print(url)
# 展示效果：  http://www.baidu.com?name=germey&age=22


print(" 参数改造成字典,parse_qs方法   --------------------------------------------------------------------------")
from urllib.parse import parse_qs
query = 'name=germey&amp;age=22'
print(parse_qs(query))
# 展示效果：  {'name': ['germey'], 'age': ['22']}

print(" 参数改造成元组组成的列表,parse_qsl方法   --------------------------------------------------------------------------")
from urllib.parse import parse_qsl
query = 'name=germey&amp;age=22'
print(parse_qsl(query))
# 展示效果： [('name', 'germey'), ('age', '22')]

print(" 将中文参数进行quote进行编码   --------------------------------------------------------------------------")
from urllib.parse import quote
keyword = '壁纸'
url = 'https://www.baidu.com/s?wd=' + quote(keyword)
print(url)
# 展示效果：https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8


print(" 将quote进行编码   --------------------------------------------------------------------------")
from urllib.parse import unquote
url = 'https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
print(unquote(url))
# 展示效果： https://www.baidu.com/s?wd=壁纸