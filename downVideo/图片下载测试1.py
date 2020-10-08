import urllib.request
import http.cookiejar
import re


cj = http.cookiejar.MozillaCookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)

HEADER = {
    "Host": "img-hw.xvideos-cdn.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Connection": "keep-alive",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0"
}

req = urllib.request.Request('https://img-hw.xvideos-cdn.com/videos/thumbs169ll/26/29/59/262959a81ca11a36a871dcf911f3825d/262959a81ca11a36a871dcf911f3825d.4.jpg', None, HEADER)
rt = urllib.request.urlopen(req)
fw = open( '1.png', 'wb')
fw.write(rt.read())
fw.close()


# rt = urllib.request.urlopen('http://www.variflight.com/flight/PEK-SYX.html?AE71649A58c77&fdate=20160518')
# html = rt.read().decode()
# imglist = re.findall('<img src="/flight/detail/([^"]+)"', html)
# ut = 'http://www.variflight.com/flight/detail/'
# i = 0
# for img in imglist:
#     i += 1
#     url = ut + img
#     req = urllib.request.Request(url, None, HEADER)
#     rt = urllib.request.urlopen(req)
#     fw = open(str(i) + '.png', 'wb')
#     fw.write(rt.read())
#     fw.close()
#     print('save img', i)