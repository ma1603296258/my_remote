#模块是一个包含所有你定义的函数和变量的文件，其后缀名是.py。模块可以被别
# 的程序引入，以使用该模块中的函数等功能。这也是使用 python 标准库的方法。
'''
import sys
 
print('命令行参数如下:')
for i in sys.argv:
   print(i)
 
print('\n\nPython 路径为：', sys.path, '\n')
'''
#1、import sys 引入 python 标准库中的 sys.py 模块；这是引入某一模块的方法。
#2、sys.argv 是一个包含命令行参数的列表。
#3、sys.path 包含了一个 Python 解释器自动查找所需模块的路径的列表。

#import 语句
# 有一个变体，可以直接把模块里的名称导入到另一个模块的符号表。例如：
'''
from fibo import fib, fib2
fib(500)
'''

print('你好')































































