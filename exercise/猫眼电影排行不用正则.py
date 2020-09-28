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
    print(soup.find_all('dd'))

    for link in soup.find_all('a'):


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