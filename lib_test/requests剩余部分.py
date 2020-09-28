print("通过用户名和密码登录---------------------------------------------------------------")

import requests
from requests.auth import HTTPBasicAuth
r = requests.get('http://192.168.0.77:8888/5.x/', auth=HTTPBasicAuth('yanjp', '6hd58'))
print(r.status_code)
# print(r.text)



print("request的预处理方式---------------------------------------------------------------")

from requests import Request, Session
url = 'http://httpbin.org/post'
data = {'name': 'germey'}
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}
s = Session()
req = Request('POST', url, data=data, headers=headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)