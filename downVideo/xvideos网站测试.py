# import requests
# import time
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
#     'Connection': 'close'
# }
# url =  "https://www.xvideos.com/new/1"
#
# requests.adapters.DEFAULT_RETRIES = 5
# s = requests.session()
# s.keep_alive = False
#
#
# proxies = { "http": "https://www.xvideos.com/new/1", "https": "http://199.19.104.83:443", }
#
# try:
#     r = requests.get(url, headers=headers, proxies=proxies)
#     print(r.text)
# except requests.exceptions.ConnectionError as ex:
#     print(ex)
#     time.sleep(5)
#     # r.status_code = "Connection refused"
# # r = requests.get()


import urllib2

url = "http://www.ip181.com/"
proxy_support = urllib2.ProxyHandler({'http':'121.40.108.76'})
#参数是一个字典{'类型':'代理ip:端口号'}
opener = urllib2.build_opener(proxy_support)
#定制opener
opener.add_handler=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36')]
#add_handler给加上伪装
urllib2.install_opener(opener)
response = urllib2.urlopen(url)

print response.read().decode('gbk')
