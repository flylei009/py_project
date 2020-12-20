
print('显示命令行的参数 ：   ---------------------------------------------------------------------------------')

import sys

print('命令行参数如下:')
for i in sys.argv:
    print(i)

print('\n\nPython 路径为：', sys.path, '\n')
"""
$ python using_sys.py 参数1 参数2
命令行参数如下:
using_sys.py
参数1
参数2
"""

print('from … import 语句  ：  要导入模块 fibo 的 fib 函数 ---------------------------------------------------------------------------------')
from  database_test.mysqltest2 import print_welcome    # from modname import *
print_welcome(500)

from  mypackage1.mypackage2.test import *    # from modname import *
print_welcome(500)
