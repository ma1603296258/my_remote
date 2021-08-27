'''
input("\n\n按下 enter 键后退出。")#等待用户输入
#press enter to exit(退出) ；exist(存在)
#waiting for user input

import sys; x='runoob'; sys.stdout.write(x+'\n')
'''
#同一行多条语句，分号隔开
'''
if expression :   #复合语句首行关键字开始，冒号结束
    Suite
elif expression :
    suite
else expression :
    suite
'''

'''
x="a"
y="b"
#换行输出,print默认换行(default wrap)
print(x)
print(y)

print('------------------')
#不换行输出
print(x,end=" ")
print(y,end=" ")
'''
#导入sys模块
import sys
print('==========python import mode========')
print('命令行参数为：')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)
#导入sys模块的argv,path成员
from sys import argv,path  # 导入特定成员

print('==============python from import============')
print('path:',path)