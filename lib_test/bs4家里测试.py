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
# # print(soup.prettify())
# print(soup.title)
# print(type(soup.title))
# print(soup.title.string)
# print(soup.head)
# print(soup.p)            # 当有多个节点时，这种选择方式只会选择到第一个匹配的节点，其他的后面节点都会忽略。
# print("------------")
# print(soup.p.string)
# print(soup.p.b)
#
# print("------------")
# print(soup.p.attrs)              # 获取所有的属性值
# print(soup.p.attrs['name'])      # 获取某属性对应的值
# print(soup.p['name'])            # 获取某属性对应的值（简写）
# print("获取直接子节点：contents------------")
# print(soup.p.contents)           # 获取直接子节点
#
# print("嵌套选择  --------------------------------------------------------------------------------")
#
# html = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# """
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# print(soup.head.title)
# print(type(soup.head.title))
# print(soup.head.title.string)

# print("获取直接子节点：contents， 用于组装html------------")
# html = """
# <html>
#     <head>
#         <title>The Dormouse's story</title>
#     </head>
#     <body>
#         <p class="story">
#             Once upon a time there were three little sisters; and their names were
#             <a href="http://example.com/elsie" class="sister" id="link1">
#                 <span>Elsie</span>
#             </a>
#             <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
#             and
#             <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
#             and they lived at the bottom of a well.
#         </p>
#         <p class="story">...</p>
# """
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# # print(soup.p)
# # print(soup.p.contents)    #一行，并且保留了文本的格式，必须换行等
#
#
# print("children 属性得到相应的结果------------")
# print(soup.p.children)
# for i, child in enumerate(soup.p.children):
#     print(i, child)
#
# print("父节点和祖先节点           ------------")
# print(soup.a.parent)
#
# print("获取所有的祖先节点           ------------")
# html = """
# <html>
#     <body>
#         <p class="story">
#             <a href="http://example.com/elsie" class="sister" id="link1">
#                 <span>Elsie</span>
#             </a>
#         </p>
# """
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# print(type(soup.a.parents))
# print(list(enumerate(soup.a.parents)))

# print("获取同级的节点           ------------")
#
# html = """
# <html>
#     <body>
#         <p class="story">
#             Once upon a time there were three little sisters; and their names were
#             <a href="http://example.com/elsie" class="sister" id="link1">
#                 <span>Elsie</span>
#             </a>
#             Hello
#             <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
#             and
#             <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
#             and they lived at the bottom of a well.
#         </p>
# """
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# print('Next Sibling', soup.a.next_sibling)
# print('Prev Sibling', soup.a.previous_sibling)
# print('Next Siblings', list(enumerate(soup.a.next_siblings)))
# print('Prev Siblings', list(enumerate(soup.a.previous_siblings)))


# print("关联元素节的文本和属性           ------------")
#
# html = """
# <html>
#     <body>
#         <p class="story">
#             Once upon a time there were three little sisters; and their names were
#             <a href="http://example.com/elsie" class="sister" id="link1">Bob</a>
#             <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
#         </p>
# """
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# print('Next Sibling:')
# print(type(soup.a.next_sibling))
# print(soup.a.next_sibling)
#
# print(soup.a.next_sibling.string)
# print('Parent:')
# print(type(soup.a.parents))
# print(list(soup.a.parents)[0])     #当前层级往上一层，  序号是几就是往上几层
# print(list(soup.a.parents)[0].attrs['class'])



# html='''
# <div class="panel">
#     <div class="panel-heading">
#         <h4>Hello</h4>
#     </div>
#     <div class="panel-body">
#         <ul class="list" id="list-1">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#             <li class="element">Jay</li>
#         </ul>
#         <ul class="list list-small" id="list-2">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#         </ul>
#     </div>
# </div>
# '''
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# print(soup.find_all(name='ul'))
# print("___________________________________")
# print(soup.find_all('ul'))
# print(type(soup.find_all(name='ul')[0]))


# # print("通过属性值查找           ------------")
# html='''
# <div class="panel">
#     <div class="panel-heading">
#         <h4>Hello</h4>
#     </div>
#     <div class="panel-body">
#         <ul class="list" id="list-1" name="elements">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#             <li class="element">Jay</li>
#         </ul>
#         <ul class="list list-small" id="list-2">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#         </ul>
#     </div>
# </div>
# '''
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# print(soup.find_all(attrs={'id': 'list-1'}))
# # print(soup.find_all(attrs={'name': 'elements'}))
# # print(soup.find_all(attrs={'class': 'element'}))
#
# # print(soup.find_all("div"))
# print(soup.find_all(id='list-1'))
# # print(soup.find_all(class_='element'))


# # print("通过文本text查找           ------------")
#
# import re
# html='''
# <div class="panel">
#     <div class="panel-body">
#         <a>Hello, this is a link</a>
#         <a>Hello, this is a link, too</a>
#     </div>
# </div>
# '''
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# print(soup.find_all(text=re.compile('link')))


# # print("通过文本find查找(只找第一个能匹配到的)           ------------")

# html='''
# <div class="panel">
#     <div class="panel-heading">
#         <h4>Hello</h4>
#     </div>
#     <div class="panel-body">
#         <ul class="list" id="list-1">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#             <li class="element">Jay</li>
#         </ul>
#         <ul class="list list-small" id="list-2">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#         </ul>
#     </div>
# </div>
# '''
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# # print(soup.find(name='ul'))
# print(type(soup.find(name='ul')))
# print(soup.find(class_='list'))
# print(soup.findAll(class_='list'))     # class_ 包含的都算



html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
print(soup.select('.panel .panel-heading'))
print(soup.select('ul li'))
print(soup.select('#list-2 .element'))
print(type(soup.select('ul')[0]))