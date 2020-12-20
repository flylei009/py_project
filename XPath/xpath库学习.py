# # from lxml import etree
# # text = '''
# # <div>
# #     <ul>
# #          <li class="item-0"><a href="link1.html">first item</a></li>
# #          <li class="item-1"><a href="link2.html">second item</a></li>
# #          <li class="item-inactive"><a href="link3.html">third item</a></li>
# #          <li class="item-1"><a href="link4.html">fourth item</a></li>
# #          <li class="item-0"><a href="link5.html">fifth item</a>
# #      </ul>
# #  </div>
# # '''
# # html = etree.HTML(text)
# # result = etree.tostring(html)
# # print(result.decode('utf-8'))
#
#
#
# # from lxml import etree
# #
# # html = etree.parse('./test.html', etree.HTMLParser())
# # result = etree.tostring(html)
# # print(result.decode('utf-8'))
#
#
# # from lxml import  etree
# #
# # html = etree.parse('./test.html', etree.HTMLParser())
# # result = etree.tostring(html)
# # print(result.decode('utf-8'))
#
#
# # from lxml import etree
# # html = etree.parse('./test.html', etree.HTMLParser())
# # result = html.xpath('//*')
# # print(result)
#
# # text = '''
# # <div>
# #     <ul>
# #          <li class="item-0"><a href="link1.html">first item</a></li>
# #          <li class="item-1"><a href="link2.html">second item</a></li>
# #          <li class="item-inactive"><a href="link3.html">third item</a></li>
# #          <li class="item-1"><a href="link4.html">fourth item</a></li>
# #          <li class="item-0"><a href="link5.html">fifth item</a>
# #      </ul>
# #  </div>
# # '''
#
# from lxml import etree
#
# html = etree.parse('./test.html', etree.HTMLParser())
# result1 = html.xpath('//li//a')
# # 现在首先选中 href 属性为 link4.html 的 a 节点，然后再获取其父节点，然后再获取其 class 属性，相关代码如下：
# result2 = html.xpath('//a[@href="link4.html"]/../@class')
# # //a[@href ="link4.html"]/**/@class
#
# # ************** 属性匹配：这里如果要选取 class 为 item-0 的 li 节点
# result3 = html.xpath('//li[@class="item-0"]')
# # ************** 属性获取
# result31 = html.xpath('//li/a/@href')
# # ************** 属性多值匹配
# # 错误示例：result = html.xpath('//li[@class="li"]/a/text()')
# text32 = '''
# <li class="li li-first"><a href="link.html">first item</a></li>
# '''
# html32 = etree.HTML(text32)
# result32 = html32.xpath('//li[contains(@class, "li")]/a/text()')
#
#
#
#
#
# # **************文本获取
# result4 = html.xpath('//li[@class="item-0"]//text()')
# result5 = html.xpath('//li[@class="item-0"][0]//text()')
#
#
#
# print(result1)
# print(result2)
# print('-------------------------------------------------------------------------------')
# print(result3)
# print(result31)
# print(result32)
# print('-------------------------------------------------------------------------------')
#
# print(result4)
# print(result5)
#
#
# # ************** 多属性匹配
# from lxml import etree
# text = '''
# <li class="li li-first" name="item"><a href="link.html">first item</a></li>
# '''
# html = etree.HTML(text)
# result = html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')
# print(result)

# # ************** 按序选择

# from lxml import etree
#
# text = '''
# <div>
#     <ul>
#          <li class="item-0"><a href="link1.html">first item</a></li>
#          <li class="item-1"><a href="link2.html">second item</a></li>
#          <li class="item-inactive"><a href="link3.html">third item</a></li>
#          <li class="item-1"><a href="link4.html">fourth item</a></li>
#          <li class="item-0"><a href="link5.html">fifth item</a>
#      </ul>
#  </div>
# '''
# html = etree.HTML(text)
# result = html.xpath('//li[1]/a/text()')
# print(result)
# # print(html.xpath('//li[1]/a//text()'))
# result = html.xpath('//li[last()]/a/text()')
# print(result)
# result = html.xpath('//li[position()<3]/a/text()')
# print(result)
# result = html.xpath('//li[last()-2]/a/text()')
# print(result)

from lxml import etree

text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html"><span>first item</span></a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''
html = etree.HTML(text)
result = html.xpath('//li[1]/ancestor::*')
print(result)
result = html.xpath('//li[1]/ancestor::div')
print(result)
result = html.xpath('//li[1]/attribute::*')
print(result)
result = html.xpath('//li[1]/child::a[@href="link1.html"]')
print(result)
result = html.xpath('//li[1]/descendant::span')
print(result)
result = html.xpath('//li[1]/following::*[2]')
print(result)
result = html.xpath('//li[1]/following-sibling::*')