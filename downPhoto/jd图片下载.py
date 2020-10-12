import requests,re,os
from pyquery import PyQuery as pq
from pathlib import Path

print()

def get_page(page):
    # params = {
    #     'page': page
    # }
    url = 'https://smtmm.win/article/52771/'
    url = 'https://search.jd.com/Search?keyword=%E6%80%A7%E6%84%9F%E5%86%85%E8%A1%A3'
    print(url)
    rs= requests.get(url, headers=headers).text
    print(rs)
    doc = pq(rs)

    # imageList = doc('.alignnone.size-medium.wp-image-42')
    # id = 0
    # for image in imageList.items() :
    #     id += 1
    #     if id % 10 ==0:
    #         print(page,": 下载了 ", id, "张图片了！")
    #     imagUrl = image.attr('data-original')
    #     fullImageUrl = domain+imagUrl
    #     # print(fullImageUrl)
    #     save_image(str(page)+'_'+str(id), fullImageUrl)

def save_image(id, imageUrl):
    # 创建文件的目录和文件名一致
    img_path = Path(__file__).name
    fileName = img_path.replace('.py', '')
    if not os.path.exists(fileName):
        os.makedirs(fileName)

    r = requests.get(imageUrl, headers=headers, stream=True)
    if r.status_code == 200:
        tempImagename= os.path.join(fileName,id+'.jpg')
        # print(tempImagename)
        open(tempImagename, 'wb').write(r.content)  # 将内容写入图片
        # print("done")
    del r

def main(offset):
    # 经查  https://smtmm.win/article/52700/    52700 这个参数修改即可。   52700~ 52799
    for i in range(52701,52799,1):
        get_page(i)
        print(i,"已经下载完毕！")

headers = {
    # 'cookie': cookies,
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'referer': 'https://search.jd.com/Search?keyword=%E6%80%A7%E6%84%9F%E5%86%85%E8%A1%A3'
}

domain = 'https://smtmm.win'

if __name__=='__main__':
    main(0)