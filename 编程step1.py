#斐波纳契数列
'''
a, b = 0, 1
while b <30 :
  print (b)
  a, b = b, a+b  # 右边表达式在赋值变动之前执行
'''
'''
# output variable value
i = 256 * 256
i = 34 ** 5
print ('i的数值为', i)
'''
# end 关键字
# end 可以将结果输出到同一行，或者在输出的末尾添加不同的字符
'''
a =0
b=1
a, b =0, 1
while b<1000 :
    print (b, end=',')
    a, b = b, a+b
'''
#if 语句
#keywords : if-elif-else
'''
var1 = 100
if var1 :
    print ("1-if 表达式条件为true")
    print (var1)

var2 = 0
if var2 :
    print ("true")    #zero : false    else : true
    print (var2)
print('good bye')
'''
# calculate dog's age
'''
age = int(input('请输入狗的年龄'))
print ('')
if age <= 0 :
    print ('逗')
elif age == 1 :
    print ('相当于14岁的人')
elif age == 2 :
    print ('相当于22岁的人')
#elif age > 2 :
else :
    a = 22 + (age - 2)*5
    print ('对应人类的年龄：', a)
### prompt(提示) exit(退出)
input('点击 enter 退出')
'''
#运算符的演示 ==等于，（=赋值），<=,>=,>,<, !=不等于
'''
num1,num2,num3,num4 = 1.2,2,2,3
print (num1 < 3)
print (num2 == num3)
print (num1 != num4)
print (num3 <= num4)
print (num1 >= num2)
print (num3 > 8)
'''
# 猜谜游戏
'''
number1 = 6
guess = 0
print ('猜谜游戏 riddles')
while guess != number1 :
    guess = int(input('请输入你猜测的数字:'))
    if guess == number1 :
      print ('恭喜你，猜对了！')
    elif guess < number1 :
      print ('亲，猜得小了一点')
    else :
      print ('猜得大了呢，宝')
input('please press enter to exit')
'''
# if 嵌套
'''
num = int(input('输入一个数字：'))
if num %2 ==0 :
    if num % 3 ==0 :
        print ('可整除2和3')
    elif num % 3 != 0 :
        print ('可整除2但不可整除3')
else :
    if num % 3 == 0 :
        print('可整除3但不能整除2')
    else :
        print ('既不能整除2也不能整除3')
input('enter')
'''
# 循环语句 for   while 
'''
a =1
a += 2  # a=3
a =+ 3  # =+ a  value不return   a=3
print (a)
'''
'''
a = 1
while a<= 11 :
    #print(a)
    a += 2
    print(a, end=',')
#print (a)
'''
#1到100和
'''
a = 0
b = 0
while a < 100 :
    a += 1
    b = a + b
print ('1到100之和为：',b)
'''
'''
# 计算等差数列 an = 3n + 1 前n 项和
n = int(input('请输入项数：'))
ai = 4
i = 1
b = 0
while i  <= n :
    b= ai + b
    i +=1
    ai= 3 + ai
print('前%d项之和为：%d' % (n,b))
input('press enter to exit')
'''
#无限循环
'''
var = -1
while var :
    num = float(input('请输入一个数字:\t'))
    print('你输入的数字是 : %f' % (num))
'''
 # while 使用 else
'''
flag = 0
#当while循环体里只有一句时，可与while写在一行
while (flag) : print('welcome')   #flag可不加（）
print ('good bye')         
'''
'''
a = float(input('请输入一个数字：\t'))
b = 5
print()
while a < b :
    print ('小于5')
else :
    if a == b :
      print ('等于5')
    else :
      print ('大于5')
input('please press enter to exit')
'''

# for 循环（loop)语句(words)
'''
languages = ['c', 'c++', 'python', 'c#']
for x in languages :
    print (x)
'''
 # break 跳出循环体
'''
sites = ['a', 'b', 'c', 'd']
for site in sites :
    if site == 'd' :
        print ('菜鸟教程')
        break
   # elif site != 'd' :
    print ('loop word:', site)
else : 
    print('没有循环数据')
print ('完成循环')
'''

# range()  function
# 生成数列
'''
for i in range(6,9): # 6 7 8
         #range(6)   # 0 1 2 3 4 5
  print (i)
'''

#for a in range(0, 9, 3) :  # 范围 0<= a <9 , stpe size : 3
#for a in range (-5, 100, 11) :   # range: -5<=a<100 ,正向index 
#for a in range(-5, -100, -6) :   #反向index
#   print (a)

#To combine the range() and len() functions 
# to traverse the index of a sequence
#结合range()和len()函数以遍历一个序列的索引
'''
list = ['A', 'B', 'C', 'D', 'E', 'F']
for x in range(len(list)) :
    print (x,list[x])
'''
# set up a list by range() function
'''
a = list( range(6))
print(a)
'''
# break and continue:else 子句 in word and loop 
#break 和 continue 语句及循环中的 else 子句 
#break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环
# 中终止，任何对应的循环 else 块将不执行。 
#continue 语句被用来告诉 Python 跳过当前循环块中的
# 剩余语句，然后继续进行下一轮循环。 
# 1.while 中使用 break
'''
i = 6
while i> 0 :
    i -= 1
    print (i)
    if i == 2 :
        break
print ('done')
'''
#while 中使用continue
'''
i = 6
while i > 0:
    i -= 1
    if i == 2 :
        continue
    print(i)
print ('done')
'''
#the first example
'''
str = 'handsome'
for x in str :
    if x == 'o' :
        #break      #  h a n d s
        continue    #  h a n d s m e
    print ('当前字母为：',x)
print('done')
'''
#循环语句可以有 else 子句，它在穷尽列表(以for循环)或条件变为 false 
# (以while循环)导致循环终止时被执行，但循环被 break 终止时不执行。 
'''
for i in range(2,13):
    for x in range(2,i):
        if i % x == 0 :
            print(i,'是合数，等于：',x,'*',i//x)
            break
    else :
        #loop 中没找到 element
        print(i,'为质数')
print('done')
'''
# pass 语句 :是空语句，是为了保持程序结构的完整性
#class MyEmptyClass:
   # pass
'''
for letter in 'Runoob': 
   if letter == 'o':
      pass
      print ('执行 pass 块')
   print ('当前字母 :', letter)
 
print ("Good bye!")
'''
'''
i = sum = 0
while i<=4:
    sum += i
    i = i+1
else :
    print(sum)
'''
































































