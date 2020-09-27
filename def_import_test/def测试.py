
def area(width, height):
    return width * height

def print_welcome(name):
    print("Welcome", name)

print_welcome("Runoob")
w = 4
h = 5
print("width =", w, " height =", h, " area =", area(w, h))

print('传参不可变对象实例（Number（数字）、String（字符串）、Tuple（元组）） ：  ---------------------------------------------------------------------------------')
def change(a):
    print(id(a))  # 指向的是同一个对象
    a = 10
    print(id(a))  # 修改Nmber(不可变类型)后，实际上是指向一个新对象
a = 1
print(id(a))
change(a)

print('传参可变对象实例（List（列表）、Dictionary（字典）、Set（集合）） ：  ---------------------------------------------------------------------------------')
def change(a):
    print(id(a))  # 指向的是同一个对象
    # a = [4,5,6]   # 这样指向地址就会变
    a.append([1, 2, 3, 4])
    print(id(a))  # List(可变类型)后，实际上是指向一个新对象
a = [1,2,3]
print(id(a))
change(a)


print('不定长参数 ：  ---------------------------------------------------------------------------------')
def printinfo(arg1, *vartuple):   # 如果是 **（两个星号）  代表是一个字典
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vartuple)
# 调用printinfo 函数
printinfo(70, 60, 50)

# printinfo(1, a=2,b=3)   可变参数是字典的情况

print('匿名函数 ：   ---------------------------------------------------------------------------------')
""" 
python 使用 lambda 来创建匿名函数。
所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。
lambda 只是一个表达式，函数体比 def 简单很多。
lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。

语法如下 
lambda [arg1 [,arg2,.....argn]]:expression
"""

sum = lambda arg1, arg2: arg1 + arg2
print ("相加后的值为 : ", sum( 10, 20 ))