import _thread
import time

# 线程的第一个实现方法通过 _thread 模块中的start_new_thread()函数来产生新线程。语法如下
# _thread.start_new_thread ( function, args[, kwargs] )
# function - 线程函数。
# args - 传递给线程函数的参数,他必须是个tuple（元组）类型。
# kwargs - 可选参数。

# 为线程定义一个函数
def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

# 创建两个线程
try:
   _thread.start_new_thread( print_time, ("Thread-1", 2, ) )
   _thread.start_new_thread( print_time, ("Thread-2", 4, ) )
except:
   print ("Error: 无法启动线程")

while 1:
   pass