# import json
import requests
from requests.exceptions import RequestException
# import re
# import time
from pyquery import PyQuery as pq

def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


# def parse_one_page(html):
    # pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
    #                      + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
    #                      + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    # items = re.findall(pattern, html)



# def write_to_file(content):
#     with open('result.txt', 'a', encoding='utf-8') as f:
#         f.write(json.dumps(content, ensure_ascii=False) + '\n')


def main(offset):
    url = 'https://maoyan.com/board/4?offset=10'


    html = """
          <dd>
                        <i class="board-index board-index-9">9</i>
    <a href="/films/784" title="甜蜜蜜" class="image-link" data-act="boarditem-click" data-val="{movieId:784}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p1.meituan.net/movie/0b0d45b58946078dd24d4945dd6be3b51329411.jpg@160w_220h_1e_1c" alt="甜蜜蜜" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/784" title="甜蜜蜜" data-act="boarditem-click" data-val="{movieId:784}">甜蜜蜜</a></p>
        <p class="star">
                主演：黎明,张曼玉,杜可风
        </p>
<p class="releasetime">上映时间：2015-02-13</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">2</i></p>
    </div>

      </div>
    </div>

                </dd>
    
    """
    html = get_one_page(url)
    # html = pq(filename='movie.html')
    print(html)
    doc = pq(html)
    # items = doc('dd').items()
    # print(type(items))
    # print(items)
    movieList =[]
    #
    #
    # for item in items:
    #     print(item)
    movieOne = {}
    movieOne['id'] = doc('i' ".board-index").text()
    movieOne['name'] = doc('a').attr('title')

    for item in doc('img').items():     #如果是多个节点，就需要遍历了，否则只返回第一个节点的内容
        print(item)
        if item.attr('data-src') != None:
            movieOne['image'] = item.attr('data-src')

    # movieOne['image'] = doc('img').attr('data-src')

    movieOne['actors'] = doc('p' '.star').text()
    movieOne['time'] = doc('p' '.releasetime').text()
    movieOne['score'] = doc('p i' '.integer').text() + doc('.fraction').text()
    # movieOne['score'] =



    print(movieOne)
    #     movieOne.items()

        # movieList
        # yield {
        #     'index': item[0],
        #     'image': item[1],
        #     'title': item[2],
        #     'actor': item[3].strip()[3:],
        #     'time': item[4].strip()[5:],
        #     'score': item[5] + item[6]
        # }

    # parse_one_page(html)
    # print(html)


    # for item in parse_one_page(html):
    #     print(item)
    #     write_to_file(item)


if __name__ == '__main__':

    main(0)