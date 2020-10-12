from selenium import webdriver
from pyquery import PyQuery as pq
import time


browser = webdriver.Chrome()
browser.get('https://search.jd.com/Search?keyword=ipad')
html = browser.page_source
doc = pq(html)
# print(html)
# items  = doc('.gl-warp clearfix')    #不能行
# items  = doc('#J_main')              #可以
items  = doc('#J_goodsList  .gl-warp li .gl-i-wrap .p-img a')
print(items)
skuList = []

for item in items.items():
    # print(item)
    sku = {}

    href = item.attr('href')
    # lazyImg = item('img').attr('src')
    if  (href== None):
        continue
    # print(href, lazyImg)
    # sku['href'] = href
    # sku['data-lazy-img'] =lazyImg
    skuList.append(href)
#
print(skuList)

# 页面布局
"""
body
div#J_searchWrap
div#J_container
div#J_main
div#m-list
div#ml-wrap
div#J_goodsList
ul .gl-warp .clearfix]
li data-sku=''
div .gl-i-wrap
div .p-img
a  href="//item.jd.com/70861907953.html"  #详细的商品信息
img  src
"""