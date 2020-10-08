import requests,re,os
from pyquery import PyQuery as pq
import json
# from urlparse import urlparse
import tldextract


def get_page(page):
    url = 'https://www.xvideos.com/new/' + str(page)
    headers = {
        'Connection': 'Keep-Alive',
        'Host': 'www.xvideos.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
        'referer': url
    }
    print(headers)


    print(url)
    s = requests.session()
    s.keep_alive = False

    requests.adapters.DEFAULT_RETRIES = 5  # 增加重连次数
    s = requests.session()
    s.keep_alive = False  # 关闭多余连接
    getcontent = s.get(url, headers=headers)

    doc = pq(getcontent.text)
    allUrlList = []
    # with open('xvideos1.html', 'r', encoding='UTF-8') as f:  # 打开新的文本
    #     text_new = f.read()  # 读取文本数据
    #     doc = pq(text_new)
    #     f.close()
    linkList = doc('a').items()
    photoList = doc('.thumb-block .thumb-inside .thumb a img ')   #视频中的图片宣传

# 1.1收集需要视频的url
    for link in linkList:
        tempUrl = link.attr('href')
        # print(type(tempUrl))
        if isinstance(tempUrl, str) and tempUrl.startswith('/video')  and (not tempUrl=='/videos-i-like'):
            # print(tempUrl)
            tureUrl = domain+tempUrl
            allUrlList.append(tureUrl)

# 1.2收集需要视频的url存放到文件
#     print(allUrlList)
    with open('all_url.txt', 'ab') as wf:
        wf.write(json.dumps(allUrlList).encode())
        wf.close()
    id = 0


# 2.1保存对应视频简介图片
    fileName = "xvideos_photo"
    if not os.path.exists(fileName):
        os.makedirs(fileName)

    for photo in photoList.items():
        id +=1
        photoUrl = photo.attr('data-src')
        print(photoUrl)
        # parts = urlparse(url)
        # host = parts.netloc
        val = tldextract.extract(photoUrl)
        print(val.subdomain, val.domain, val.suffix, val.registered_domain)

        if val.subdomain == 'img-hw':
            r = requests.get(photoUrl, headers=headers_hwcdn, stream=True)
        elif  val.subdomain == 'img-l3':
            r = requests.get(photoUrl, headers=headers_l3cdn, stream=True)
        if r.status_code == 200:
            tempImagename = os.path.join(fileName, str(id) + '.jpg')
            # print(tempImagename)
            open(tempImagename, 'wb').write(r.content)  # 将内容写入图片
            # print("done")
        # del r

def main(offset):
    # 经查  https://smtmm.win/article/52700/    52700 这个参数修改即可。   52700~ 52799
    for i in range(1,2,1):
        get_page(i)
        print(i,"已经下载完毕！")




headers_hwcdn = {
    'Connection': 'Keep-Alive',
    'Host': 'img-hw.xvideos-cdn.com',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    'referer': 'https://img-hw.xvideos-cdn.com/'
}

headers_l3cdn = {
    'Connection': 'Keep-Alive',
    'Host': 'img-l3.xvideos-cdn.com',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    'referer': 'https://img-l3.xvideos-cdn.com/'
}

domain = 'https://www.xvideos.com'

if __name__=='__main__':
    main(0)