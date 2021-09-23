'''
Author: your name
Date: 2021-08-03 19:01:31
LastEditTime: 2021-09-14 01:08:14
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \py\py\1.py
'''
#!/usr/bin/python3
# 注释1
# 注释2（单行）
'''
(多行)
1
2
'''
"""（多行）
1
2
"""
""""
print("Hello, World!")
print("hello,world\n")#\n换行转义
print(r"hello,world\n")#r使不发生转义
print('''多行
      字符串''')#3单引号或双引号可指定多行字符串
print("this\t" "is\t" "string\n")#级联字符串
print('a'+'b'+'c')
print('a*')
"""
# a = 10000000000000000000000000.0
# b = 1.0
# c = a+b
# for i in range(100000000000):
#     b = b + 1.0
# print(b)

# a = 10000000000000000.0
# b = 1.0
# c = a+b
# print(c)

x = 3
y = 1.1
#print('%.2f' % (x/y))
print(x/y)
