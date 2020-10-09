from bs4 import BeautifulSoup
# html = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
# <p class="story">...</p>
# """
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# print(soup.prettify())
# print(soup.title.string)

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
print(soup.title)
print(type(soup.title))
print(soup.title.string)
print(soup.head)
print(soup.p)
print(soup.p.string)            #获取第一个p 对应对应的文本

print(soup.p.attrs)             #获取所有的属性值： {'class': ['title'], 'name': 'dromouse'}
print(soup.p.attrs['name'])     #获取name的属性值: dromouse   ;  也可以简写成: soup.p['name']
print('----------------------------------------------------------------------------------------------')
print(soup.p.contents)          #返回结果是列表形式

print('----------------------------------------------------------------------------------------------')
print(soup.p.descendants)                          #获取第一个P的所有元素
for i, child in enumerate(soup.p.descendants):     #遍历p元素下面
    print(child)

# # 获取某个元素的值
# html = """
# <html><head><title>The Dormouse's story</title></head>
# <p class="releasetime">上映时间：1994-09-10(加拿大)</p>
# """
# soup = BeautifulSoup(html, 'lxml')
# print(soup.p.attrs['class'])

# # 嵌套选择
# html = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# """
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# print(soup.head.title)
# print(type(soup.head.title))
# print(soup.head.title.string)