#迭代器与生成器
#迭代器对象从集合的第一个元素开始访问，直到所有的元素被
#访问完结束。迭代器只能往前不会后退。
#迭代器有两个基本的方法：iter() 和 next()。
#字符串，列表或元组对象都可用于创建迭代器
'''
list = [1, 2, 3, 4]
it = iter(list)    #establish iterator object
print(next(it))    #output next element     1
print(it)          #output address
print(next(it))    #     2
#print(next(it))    #    3
#print(next(it))    #   4
for x in it :       #迭代器只能往前访问不能后退
    if x == 3:      #Iterators can only be accessed forward, 
                     #not backward
        #break
        continue
    print(x)
'''
'''
list = [1, 2, 3, 4]
it = iter(list)
for x in it :
    print (x,end=' ')
'''
'''
import sys         # 引入 sys 模块
 
list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
 
while True:
    try:
        print (next(it))
    except StopIteration:
        sys.exit()
'''

#function
'''
    函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()。
    任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
    函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
    函数内容以冒号 : 起始，并且缩进。
    return [表达式] 结束函数，选择性地返回一个值给调用方，
    不带表达式的 return 相当于返回 None。
'''
# set up the first function  (取最大值)
'''
def max (a,b) :
    if a > b :
        return a
    else :
        return b
# call function (调用)
t = max(1, 3)
print (t)
'''
'''
def hello() :
    print('hello world')

hello()
'''
# calculate area function
'''
def area(L,W) :
    s = L * W
    return s

def print_welcome(name):
    print ('welcome',name)

print_welcome('runoob')
L = 4.5
W = 2
print('length=',L,'\nwidth=', W, '\narea=',area(L,W))
'''
# call function
#定义一个函数：给了函数一个名称，指定了函数里包含的参数，和代码块结构。
#这个函数的基本结构完成以后，你可以通过另一个
# 函数调用执行，也可以直接从 Python 命令提示符执行。
'''
# 定义函数
def printme( str ):
   # 打印任何传入的字符串
   print (str)
   return
 
# 调用函数
printme("我要调用用户自定义函数!")
printme("再次调用同一函数")
'''
#类型属于对象，变量是没有类型的
# 不可变类型：类似 C++ 的值传递，如整数、字符串、元组。如 fun(a)，
# 传递的只是 a 的值，没有影响 a 对象本身。如果在 fun(a) 内部修改 
# a 的值，则是新生成一个 a 的对象。
# 可变类型：类似 C++ 的引用传递，如 列表，字典。如 fun(la)，
# 则是将 la 真正的传过去，修改后 fun 外部的 la 也会受影响

#python 传immutable object example:
#通过 id() 函数来查看内存地址变化
'''
def change(a) :
    print(id(a))
    a = 10  
    print(id(a))   # a new object
    return 
a = 2
print(id(a))
change(a)
print(id(a))
print(a)
'''

# convey mutable object
'''
def change(list):
    list.append([1, 2, 3, 4])        # append 添加
    print('函数内部取值：', list)
    return 

list = [1,2,3,4]
change(list)
print('函数外取值：', list)
'''

# 参数 ：required arguments ; 关键字参数；默认参数；不定长参数
#1.必需参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样
#2.使用关键字参数允许函数调用时参数的顺序与声明时不一致，
# 因为 Python 解释器能够用参数名匹配参数值。
#3.调用函数时，如果没有传递参数，则会使用默认参数。
#4.能处理比当初声明时更多的参数。这些参数叫做不定长参数
# 和上述 2 种参数不同，声明时不会命名
'''
def printinfo( name, age ):
   "打印任何传入的字符串"
   print ("名字: ", name)
   print ("年龄: ", age)
   return
 
#调用printinfo函数
printinfo( age=50, name="runoob" )
'''
'''
def func(name, age = 35):
    print('name:', name)
    print('age:', age)
    return

print(func(name = 'mjq'))
print('------------')
print(func(age =21, name = 'mjq'))
'''
'''
spam = print('Hello')
print(None == spam)
'''
'''
a = None is ''
b = None is []
print(a,'\n', b)      # False    False
'''

# 加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数
'''
def printinfo(arg1, *vartuple):
    print('输出：')
    print(arg1)
    print(vartuple)

printinfo(1, 2, 3,4)
'''
#如果在函数调用时没有指定参数，它就是一个空元组
'''
def printinfo(arg1, *vartuple):
    print('OUTPUT:')
    print(arg1)
    for var in vartuple:
        print (var)
    return

printinfo(1)
printinfo(1,2,3)
'''
#加了两个星号 ** 的参数会以字典的形式导入
'''
def printinfo( arg1, **vardict ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   print (vardict)
 
# 调用printinfo 函数
printinfo(1, a=2,b=3)
'''

#如果单独出现星号 * 后的参数必须用关键字传入
'''
def f(a,b,*,c):
    print(a+b+c)
    return 0
#f(1,2,3)        error
f(1,2,c=3)
'''

#匿名函数  lambda
'''
sum = lambda arg1, arg2: arg1+arg2

print('sum:', sum(1, 2))
print('sum:', sum(5,6))
'''
#return
'用于退出函数，选择性地向\
    调用方返回一个表达式。不带参数值的return语句返回None'
'''
def sum(arg1, arg2):
    total = arg1 + arg2
    print('函数内:', total)
    return total

total = sum(1, 2)
print('函数外:', total)
'''
'''
#python 3.8
def f(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)

#以下使用方法是正确的:

f(10, 20, 30, d=40, e=50, f=60)
'''














