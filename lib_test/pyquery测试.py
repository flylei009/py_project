# from pyquery import PyQuery as pq
# import requests
# doc = pq(requests.get('http://cuiqingcai.com').text)
# print(doc('title'))

# from pyquery import  PyQuery as pq
# import  requests
# doc = pq(requests.get('http://cuiqingcai.com').text)
# print(type(doc))
# print(doc('title'))

# # print("通过文件名获取           ------------")

from pyquery import PyQuery as pq
doc = pq(filename='movie.html')
print(doc('li'))
print(type(doc('li')))

# # print("基本 CSS 选择器           ------------")

# html = '''
# <div id="container">
#     <ul class="list">
#          <li class="item-0">first item</li>
#          <li class="item-1"><a href="link2.html">second item</a></li>
#          <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#          <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#          <li class="item-0"><a href="link5.html">fifth item</a></li>
#      </ul>
#  </div>
# '''
# # # from pyquery import PyQuery as pq
# # # doc = pq(html)
# # # print(doc('#container .list li'))
# # # print(type(doc('#container .list li')))
# #
# #
# # from pyquery import PyQuery as pq
# # doc = pq(html)
# # # print(doc('li'))
# # # print(doc('#container .list' ))
# # # print(doc('#container .list li' ))
# # # print(doc('#container .list .item-1' ))
# #
# #
# # # print("查找子节点           ------------")
#
# from pyquery import PyQuery as pq
# doc = pq(html)
# items = doc('.list')
# print(type(items))
# print(items)
# lis = items.find('li')
# print(type(lis))
# print(lis)
#
# print("items.children()           ------------")
#
# lis = items.children()
# print(type(lis))
# print(lis)
#
# print("查找某个具体的子节点 items.children(‘.active’) 包含都算          ------------")
#
# lis = items.children('.active')  # 查找某个具体的子节点
# print(type(lis))
# print(lis)
#
# print(doc.find('.list'))
# print(doc.find('li'))

# 测试验证一下没有子节点的现实效果
# html1 = """
# <p>
# <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>
# <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>
# </p>
# """
#
# from pyquery import PyQuery as pq
# doc1 = pq(html1)
# items1 = doc1('p')
# lis1 = items1.children()
# print(type(lis1))
# print(lis1)

# # print("查找父节点           ------------")
# html = '''
# <div class="wrap">
#     <div id="container">
#         <ul class="list">
#              <li class="item-0">first item</li>
#              <li class="item-1"><a href="link2.html">second item</a></li>
#              <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#              <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#              <li class="item-0"><a href="link5.html">fifth item</a></li>
#          </ul>
#      </div>
#  </div>
# '''
# from pyquery import PyQuery as pq
# doc = pq(html)
# items = doc('.list')
# container = items.parent()   # 返回上级节点的所有信息
# print(type(container))
# print(container)
#
#
# from pyquery import PyQuery as pq
# doc = pq(html)
# items = doc('.list')
# parents = items.parents()   # 返回所有上级节点的信息
# print(type(parents))
# print(parents)
#
#
# parent = items.parents('.wrap')   # 返回指定上级节点的信息
# print(parent)



# # print("查找兄弟节点           ------------")

# html = '''
# <div class="wrap">
#     <div id="container">
#         <ul class="list">
#              <li class="item-0">first item</li>
#              <li class="item-1"><a href="link2.html">second item</a></li>
#              <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#              <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#              <li class="item-0"><a href="link5.html">fifth item</a></li>
#          </ul>
#      </div>
#  </div>
# '''
# from pyquery import PyQuery as pq
# doc = pq(html)
# li = doc('.list .item-0.active')
# # print(li)
# # print(li.siblings())  # 选择所有的兄弟节点
# print(li.siblings('.item-0'))  # 选择某个具体的兄弟节点


# # print("遍历所有节点           ------------")
# html = '''
# <div class="wrap">
#     <div id="container">
#         <ul class="list">
#              <li class="item-0">first item</li>
#              <li class="item-1"><a href="link2.html">second item</a></li>
#              <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#              <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#              <li class="item-0"><a href="link5.html">fifth item</a></li>
#          </ul>
#      </div>
#  </div>
# '''
# from pyquery import PyQuery as pq
# doc = pq(html)
# lis = doc('li').items()
# print(type(lis))
# for li in lis:
#     print(li, type(li))


# # print("6获取信息           ------------")

# html = '''
# <div class="wrap">
#     <div id="container">
#         <ul class="list">
#              <li class="item-0">first item</li>
#              <li class="item-1"><a href="link2.html">second item</a></li>
#              <li class="item-0 active"><a href="link3.html">斯蒂芬斯蒂芬<span class="bold">third item</span></a></li>
#              <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#              <li class="item-0"><a href="link5.html">fifth item</a></li>
#          </ul>
#      </div>
#  </div>
# '''
# from pyquery import PyQuery as pq
# doc = pq(html)
# a = doc('.item-0.active a')
# print(a, type(a))
# print(a.attr('href'))    #  获取某个属性的值
#
# print('-------------------------')
# print(a.attr.href)
# print('-------------------------')
#
# from pyquery import PyQuery as pq
# doc = pq(html)
# a = doc('a')
# for item in a.items():
#     print(item.attr('href'))
#
# print("获取节点后文本信息           ------------")
#
# from pyquery import PyQuery as pq
# doc = pq(html)
# a = doc('.item-0.active a')
# print(a)
# print(a.text())
#
# print("节点内部的 HTML 文本           ------------")
# from pyquery import PyQuery as pq
# doc = pq(html)
# li = doc('.item-0.active')
# print(li)
# print(li.html())html = '''
# <div class="wrap">
#     <div id="container">
#         <ul class="list">
#              <li class="item-0">first item</li>
#              <li class="item-1"><a href="link2.html">second item</a></li>
#              <li class="item-0 active"><a href="link3.html">斯蒂芬斯蒂芬<span class="bold">third item</span></a></li>
#              <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#              <li class="item-0"><a href="link5.html">fifth item</a></li>
#          </ul>
#      </div>
#  </div>
# '''
# from pyquery import PyQuery as pq
# doc = pq(html)
# a = doc('.item-0.active a')
# print(a, type(a))
# print(a.attr('href'))    #  获取某个属性的值
#
# print('-------------------------')
# print(a.attr.href)
# print('-------------------------')
#
# from pyquery import PyQuery as pq
# doc = pq(html)
# a = doc('a')
# for item in a.items():
#     print(item.attr('href'))
#
# print("获取节点后文本信息           ------------")
#
# from pyquery import PyQuery as pq
# doc = pq(html)
# a = doc('.item-0.active a')
# print(a)
# print(a.text())
#
# print("节点内部的 HTML 文本           ------------")
# from pyquery import PyQuery as pq
# doc = pq(html)
# li = doc('.item-0.active')
# print(li)
# print(li.html())

# html 方法返回的是第一个 li 节点的内部 HTML 文本，而 text 则返回了所有的 li 节点内部的纯文本，中间用一个空格分割开，即返回结果是一个字符串。

# # print("7 节点操作          ------------")
# html = '''
# <div class="wrap">
#     <div id="container">
#         <ul class="list">
#              <li class="item-0">first item</li>
#              <li class="item-1"><a href="link2.html">second item</a></li>
#              <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#              <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#              <li class="item-0"><a href="link5.html">fifth item</a></li>
#          </ul>
#      </div>
#  </div>
# '''
# from pyquery import PyQuery as pq
# doc = pq(html)
# li = doc('.item-0.active')
# print(li)
# li.removeClass('active')
# print(li)
# li.addClass('active')
# print(li)

# # print(" text html attr操作 改变节点内部的内容         ------------")
html = '''
<ul class="list">
     <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
</ul>
'''
from pyquery import PyQuery as pq
doc = pq(html)
li = doc('.item-0.active')
print(li)
li.attr('name', 'link')
print(li)
li.text('changed item')
print(li)
li.html('<span>changed item</span>')
print(li)