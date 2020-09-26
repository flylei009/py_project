from sys import argv,path  #  导入 sys 模块的 argv,path 成员

print('字符串操作   ---------------------------------------------------------------------------------')
str = 'Runoob'
print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第五个的字符
print(str[2:])  # 输出从第三个开始后的所有字符
print(str * 2)  # 输出字符串两次
print(str + '你好')  # 连接字符串
print(str[-3:])  # 区最后三个
print('------------------------------')
print (str + "TEST") # 连接字符串
print('hello\nrunoob')  # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义


print('isinstance、type测试   ---------------------------------------------------------------------------------')

print(type(1.0))
print(type(1))
print(type(4+3j))     # complex（复数） 类型
print(type(False))    # bool  两种类型首字母大写  False  True

# 判断类型
isinstance(1, int)

class A:
    pass
print(isinstance(A(), A))

# 实例一个对象 判断 对应的类型
print(type(A()) == A)


print('当你指定一个值时，Number 对象就会被创建：  ---------------------------------------------------------------------------------')
var1 = 1
var2 = 10
var3 = 10
print(type(var1))

print('删除对象  ：  ---------------------------------------------------------------------------------')
del var1
del var2,var3
# print(type(var1))    #  报错 NameError: name 'var1' is not defined

print('运算符  ：  ---------------------------------------------------------------------------------')
print(5 + 4)  # 加法  9
print(4.3 - 2) # 减法  2.3
print(3 * 7)  # 乘法  21
print(2 / 4)  # 除法，得到一个浮点数 0.5
print(2 // 4) # 除法，得到一个整数 0
print(17 % 3) # 取余  2
print(2 ** 5) # 乘方  32

print('常用转义字符 ：  ---------------------------------------------------------------------------------')
print('\b')
"""
\(在行尾时)	续行符
\\	反斜杠符号
\'	单引号
\"	双引号
\a	响铃
\b	退格(Backspace)
\e	转义
\000	空
\n	换行
\v	纵向制表符
\t	横向制表符
\r	回车
\f	换页
\oyy	八进制数，yy代表的字符，例如：\o12代表换行
# \ xyy	十六进制数，yy代表的字符，例如：\x0a代表换行
\other	其它的字符以普通格式输出
"""

print('py6个标准的数据类型 ：  ---------------------------------------------------------------------------------')
# 不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
# 可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。
# Python3 Number支持 int、float、bool、complex（复数）。


print('列表和元组 ：基本操作方法一致  ---------------------------------------------------------------------------------')
# 列表（List）用中括号[];元组(Tuple)用小括号（）
list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
tinylist = [123, 'runoob']
print (list)            # 输出完整列表
print (list[0])         # 输出列表第一个元素
print (list[1:3])       # 从第二个开始输出到第三个元素
print (list[2:])        # 输出从第三个元素开始的所有元素
print (tinylist * 2)    # 输出两次列表
print (list + tinylist) # 连接列表


print('集合  无序不重复；以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。---------------------------------------------------------------------------------')
sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}
print(sites)   # 输出集合，重复的元素被自动去掉
# 成员测试
if 'Runoob' in sites :
    print('Runoob 在集合中')
else :
    print('Runoob 不在集合中')

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

a.add('x')       # 添加元素
a.remove('x')       # 删除元素
a.clear()        # 清空集合
c =b.copy()      # 拷贝一个集合
print('c:',c)

print(a)
print(a - b)     # a 和 b 的差集
print(a | b)     # a 和 b 的并集
print(a & b)     # a 和 b 的交集
print(a ^ b)     # a 和 b 中不同时存在的元素


print('字典：键(key)唯一且必须使用不可变类型；列表是有序，字典是无序 。---------------------------------------------------------------------------------')

dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2]     = "2 - 菜鸟工具"

tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}
print (dict['one'])       # 输出键为 'one' 的值
print (dict[2])           # 输出键为 2 的值
print (tinydict)          # 输出完整的字典
print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有值
print(type(tinydict.keys()))


# 构造函数 dict() 可以直接从键值对序列中构建字典如下：
dict1 =[('Runoob', 1), ('Google', 2), ('Taobao', 3)]
print(dict1)


print('Python位运算符---------------------------------------------------------------------------------')
a = 60  #二进制为0011 1100
b = 13  #二进制为0000 1101
c = 0

print('a的十进制为：',a,'  二进制为：',bin(a)) # 十进制为60， 二进制为 0011 1100
print('b的十进制为：',b,'  二进制为：',bin(b)) # 十进制为13， 二进制为 0000 1101

print('十进制为：',a&b,'  二进制为：',bin(a&b)) # 十进制为12， 二进制为 0000 1100
print('十进制为：',a|b,'  二进制为：',bin(a|b)) # 十进制为12， 二进制为 0011 1101
print('十进制为：',a^b,'  二进制为：',bin(a^b)) # 十进制为12， 二进制为 0011 0001
print('十进制为：',~a,'   二进制为：',bin(~a))   # 十进制为12， 二进制为 1100 0011

# a|b = 0011 1101
#
# a^b = 0011 0001
#
# ~a  = 1100 0011


var1 = 'Hello World!'
print(var1)
print(id(var1))    #查看内存地址
var1+='Runoob!'
print(var1)
print(id(var1))

print(var1*2)       #字符串重复输出
print(var1.upper())       #字符串转化为大写
print(var1.lower())       #字符串转化为小写
print(var1[0:5])          #字符串转化为小写

para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
print (para_str)
"""
'''
这是多行注释，用三个单引号
这是多行注释，用三个单引号 
这是多行注释，用三个单引号
'''

"""
这是多行注释，用三个双引号
这是多行注释，用三个双引号 
这是多行注释，用三个双引号
"""

print('列表---------------------------------------------------------------------------------')
list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5]    #元组的创建可以直接用逗号隔开，不加逗号类型为整整
# 所谓列表的可变指的是所指向的内存中的内容可变的。
print(id(list1))
print(id(list2))
print(list1 == list2)

print('元组(tuple)---------------------------------------------------------------------------------')
tup1 = (1, 2, 3, 4, 5)
tup2 = 1, 2, 3, 4, 5    #元组的创建可以直接用逗号隔开，不加逗号类型为整整
tup3 = (1)
tup4 = (1,)
tup5 = 1,

print (type(tup2))
print (type(tup3))
print (type(tup4))
print (type(tup5))

# 元组中的元素值是不允许修改的，但我们可以对元组进行连接组合，如下实例:
# tup1[0] = 100     要报错

# 删除元组
del tup3
print ("删除后的元组 tup3 : ")
# print (tup3)         要报错

print (len(tup4))

print('变量的内存地址---------------------------------------------------------------------------------')
# 所谓元组的不可变指的是元组所指向的内存中的内容不可变。
print(id(tup4))
print(id(tup5))
print(tup4 == tup5)

# 元组最大值
max(tup2)

# 元组最小值
min(tup2)

# 列表转元组
list1= ['Google', 'Taobao', 'Runoob', 'Baidu']
tuple1=tuple(list1)


print('字典 ---------------------------------------------------------------------------------')
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])


dict['Age'] = 8                # 修改  Age
dict['SEX'] = '女'             # 增加字典  SEX
# del dict['Name']             # 删除键 'Name'
print(dict)
print(type(dict))
print(dict.keys())               #输出所有的键
print(dict.values())               #输出所有的值