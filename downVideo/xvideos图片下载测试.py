import requests,re,os
from pyquery import PyQuery as pq
from pathlib import Path

def save_image(fileName,id, imageUrl):
    r = requests.get(imageUrl, headers=headers, stream=True)
    if r.status_code == 200:
        tempImagename= os.path.join(fileName,str(id)+'.jpg')
        # print(tempImagename)
        open(tempImagename, 'wb').write(r.content)  # 将内容写入图片
        # print("done")
    del r

def main(offset):
    fileName = 'temp'
    if not os.path.exists(fileName):
        os.makedirs(fileName)
    imageUrl ='https://img-hw.xvideos-cdn.com/videos/thumbs169ll/26/29/59/262959a81ca11a36a871dcf911f3825d/262959a81ca11a36a871dcf911f3825d.4.jpg'
    save_image(fileName, 1, imageUrl)


headers = {
    # 'cookie': cookies,
    'Connection': 'Keep-Alive',
    'Host': 'img-hw.xvideos-cdn.com',
    # 'Connection': 'keep-alive',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    'referer': 'https://img-hw.xvideos-cdn.com/'
}


if __name__=='__main__':
    main(0)