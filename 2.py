str_one="123456789"    #定义变量

print(str_one)#输出字符串
print(str_one[0:-1])#输出第一个到倒数第二个的所有字符
print(str_one[0])#输出第一个字符
print(str_one[2:5])#输出3到5的字符
print(str_one[1:-2])#输出2到倒数3的字符
#-表示从右向左检索
print(str_one[2:])#输出3往后的字符
print(str_one[1:5:2])
"""
输出2到5之间的字符，步长为2
步长即相邻两个之间的间隔
"""
print(str_one*3)#输出字符串3次\ output string 3 times
print(str_one + 'hello')# connecting string
print('--------------------------')

print('hello\nrunoob')#\+ escape character(转义字符)
print(r'hello\nrunoob')#r : there is no escape
# r refer to 'raw string'


