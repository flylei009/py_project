import json
import requests
from requests.exceptions import RequestException
import time
from bs4 import BeautifulSoup


# def get_one_page(url):
#     try:
#         headers = {
#             'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
#         }
#         response = requests.get(url, headers=headers)
#         if response.status_code == 200:
#             return response.text
#         return None
#     except RequestException:
#         return None

def main(offset):
    # url = 'http://maoyan.com/board/4?offset=' + str(offset)
    # print(url)
    # html = get_one_page(url)
    # print(html)

    file1 = open('movie.txt', 'r', encoding='UTF-8')
    html = file1.read()
    soup = BeautifulSoup(html, 'lxml')
    # print(soup.text)

    ddList = soup.find_all('dd')
    print(ddList)
    newList = [];
    for dd in ddList:
        newDic = {}
        # 获取title属性
        newDic['id'] = dd.i.string
        # 获取title属性
        # newDic['title'] = dd.a.attrs['title']
        newDic['title'] = dd.a['title']   #一个节点多个属性的，获取某个属性的值
        # 获取图片
        imgList = dd.find_all('img')
        for imgLabel in imgList:
            if 'data-src' not in imgLabel.attrs:
                continue
            else:
                newDic['img'] = imgLabel['data-src']
        # 获取P标签
        pList = dd.find_all('p')
        for pLabel in pList:
            print(pLabel)
            if pLabel.attrs['class'] == ['star']:
                newDic['actor'] = pLabel.string.replace('\n                ','').replace('\n        ','')
            elif pLabel.attrs['class'] == ['releasetime']:
                newDic['time'] = pLabel.string.replace('上映时间：', '')
            elif pLabel.attrs['class'] == ['score']:
                score = ''
                scoreList = pLabel.find_all('i')
                for zpLabel in scoreList:
                    score= score+zpLabel.string
                newDic['score'] = score
            else:
                continue

        # newDic['actor'] = imgLabel['data-src']

        # newDic['img'] = dd.img.attrs['src']
        # newDic['actors'] = dd.img('data-src')
        newList.append(newDic)

    print("newList",newList)

#     print(link.get('href'))



# def parse_one_page(html):
#     soup = BeautifulSoup(html, 'lxml')
#     print(soup.text)
    # for link in soup.find_all('dd'):
    #     print(link)
    #     print(link.get('href'))

    # for item in items:
    #     # print("item", item)
    #     yield {
    #         'index': item[0],
    #         'image': item[1],
    #         'title': item[2],
    #         'actor': item[3].strip()[3:],
    #         'time': item[4].strip()[5:],
    #         'score': item[5] + item[6]
    #     }

if __name__ == '__main__':
    # for i in range(10):
    #     time.sleep(5)
    #     print("------------------------------------------------------------------------------")
    #     main(offset=i * 10)
    main(0)