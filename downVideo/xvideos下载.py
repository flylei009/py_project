import requests,re,os
from pyquery import PyQuery as pq
import json

def get_page(page):
    # params = {
    #     'page': page
    # }
    url = 'https://www.xvideos.com/new/' + str(page)
    # print(url)
    # doc = pq(requests.get(url, headers=headers).text)

    allUrlList = []
    with open('xvideos1.html', 'r', encoding='UTF-8') as f:  # 打开新的文本
        text_new = f.read()  # 读取文本数据
        doc = pq(text_new)
        f.close()
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
        print(photo.attr('data-src'))
        r = requests.get(photoUrl, headers=headers, stream=True)
        if r.status_code == 200:
            tempImagename = os.path.join(fileName, id + '.jpg')
            # print(tempImagename)
            open(tempImagename, 'wb').write(r.content)  # 将内容写入图片
            # print("done")
        del r


def main(offset):
    # 经查  https://smtmm.win/article/52700/    52700 这个参数修改即可。   52700~ 52799
    for i in range(1,2,1):
        get_page(i)
        print(i,"已经下载完毕！")

headers = {
    # 'cookie': cookies,
    'Connection': 'close',
    'Host': 'www.xvideos.com',
    # 'Connection': 'keep-alive',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    'referer': 'https://www.xvideos.com/new/1'
}

domain = 'https://www.xvideos.com'

if __name__=='__main__':
    main(0)