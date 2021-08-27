#list 
#Lists can be modified, while strings and tuples cannot.

#0. len()  function
#返回值：返回对象（字符、列表、元组等）长度或者项目个数
#list1 = [1,2,6,'a']
#print(len(list1))           #output: 4     

#python 中列表的方法
#1.  list.append(x)  
# : 把一个元素添加到列表的结尾，相当于 a[len(a):] = [x]。 
'''
a=b = [1,2,3]
print(a[2:3])        #output : [3]
a[len(a):] = [5,3]
print(a)             #output : [1, 2, 3, 5, 3]
print(b)             #output : [1, 2, 3, 5, 3]
b.append(6)            
print(b)             # [1, 2, 3, 5, 3, 6]
print(b.append(6))   #   None
b.append(5,6)
print(b)             #syntaxError  : .append() only add one element
'''

#2.list.extend(L)
#通过添加指定列表的所有元素来扩充列表，相当于 a[len(a):] = L。 
'''
a = [1, 2, 3]
#a.extend(4,5)       #error
a.extend([4,5])
print(a)     #  [1, 2, 3, 4, 5]
print((1))   #   1
'''

#3.list.insert(i,x)
#功能 function : 在指定位置插入一个元素。第一个参数是准备插入
# 到其前面的那个元素的索引，例如 a.insert(0, x) 
# 会插入到整个列表之前，而 a.insert(len(a), x) 相当于 a.append(x) 。 
'''
a = [1, 2, 3]
a.insert(1,4)
print(a)     #output: [1, 4, 2, 3]
'''

#4. list.remove(x)
#function: 删除列表中值为 x 的第一个元素。
# 如果没有这样的元素，就会返回一个错误
'''
a = [1, 2, 3]
a.remove(2)
print(a)       # [1, 3]
a.remove(4)    # error
'''

#5. list.pop([i])
#function : 从列表的指定位置移除元素，并将其返回。如果没有指定索引，
# a.pop()返回最后一个元素。元素随即从列表中被移除。
# （方法中 i 两边的方括号表示这个参数是可选的,而不是要求你输入一对方括号)
'''
a = [1, 2, 3]
a.pop(1)           # a = [1, 3]
print(a.pop(1))    # return : [3]
print(a)      # [1]
#a.pop([1])    # error  : 而不是要求你输入一对方括号
'''

#6. list.clear()
#function : 移除列表中的所有项，等于del a[:]。
'''
a=b= [1, 2, 3]
a.clear()
del b[:]
print(a,'\n',b)    #  []   []
'''

#7. list.index(x)
#返回列表中第一个值为 x 的元素的索引。如果没有匹配的元素就会返回一个错误
'''
a = [1, 2, 3]
print(a.index(2))    # 1
b = a.index(2)
print(a)             # [1, 2, 3]
print(b)             # 1
a.index(4)           # error
'''

# 8. list.count(x)
# 返回 x 在列表中出现的次数。 
'''
a=[1, 2, 1, 1]
print(a.count(1))  # 3
print(a)           # [1, 2, 1, 1]
'''

# 9. list.sort()
# 对列表中的元素进行排序。 
'''
a = [1, 3, 2, 9]
a.sort()
print(a)   #  [1, 2, 3, 9]
'''
'''
b = ['c','a',3, -1]
#b.sort()   #   not supported between instances of 'int' and 'str'
print(b)
'''
'''
c = ['c', 'a']
c.sort()
print(c)        # ['a', 'c']

d = ['dcb', 'bag']
e = ['acb', 'bag']
e.sort()         # ['acb', 'bag']
d.sort()         # ['bag', 'dcb']
print(d,e)       #  string : 排序按 string的首字母
'''

# 10.list.reverse()
# 倒排列表中的元素。
'''
a = [3, -1, 1, 9]
a.reverse()
print(a)          # [9, 1, -1, 3]
'''

# 11. list.copy()
# 返回列表的浅复制，等于a[:]。
'''
a = [1, 2, 3]
print(a.copy())         # [1, 2, 3]
print(a)                # [1, 2, 3]
'''

# 注意：类似 insert, remove 或 sort 等修改列表的方法没有返回值。

# 将列表当做堆栈使用
# 列表方法使得列表可以很方便的作为一个堆栈来使用，堆栈作为特定的数据结构，
# 最先进入的元素最后一个被释放（后进先出）。用 append() 方法可以把一个
# 元素添加到堆栈顶。用不指定索引的 pop() 方法可以把一个元素从堆栈顶
# 释放出来。例如： 
'''
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)           # [3, 4, 5, 6, 7]

print(stack.pop())     # 7
print(stack)           # [3, 4, 5, 6]
print(stack.pop())     # 6
print(stack)           # [3, 4, 5]
'''

# 将列表当作队列使用
# 只是在队列里第一加入的元素，第一个取出来；但是拿列表用作这样的目的效率
# 不高。在列表的最后添加或者弹出元素速度快，然而在列表里插入或者从头部
# 弹出速度却不快（因为所有其他的元素都得一个一个地移动）。
"""
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves
queue.popleft()                 # The second to arrive now leaves
#queue                           # Remaining queue in order of arrival
#deque(['Michael', 'Terry', 'Graham'])
print(queue)             #  deque(['Michael', 'Terry', 'Graham'])
print(deque)           #   <class 'collections.deque'>
"""

# 列表推导式
# 列表推导式提供了从序列创建列表的简单途径。通常应用程序将一些操作应用于
# 某个序列的每个元素，用其获得的结果作为生成新列表的元素，或者根据确定的
# 判定条件创建子序列。每个列表推导式都在 for 之后跟一个表达式，然后有零
# 到多个 for 或 if 子句。返回结果是一个根据表达从其后的 for 和 if 上下文
# 环境中生成出来的列表。如果希望表达式推导出一个元组，就必须使用括号。 

# example 1: 这里我们将列表中每个数值乘三，获得一个新的列表
'''
vec = [2, 4, 6]
vec2=[3*x for x in vec]
print(vec2)     # [6, 12, 18]
print(vec)     # [2, 4, 6]
vec3=[[x,x**2] for x in vec]
print(vec3)       # [[2, 4], [4, 16], [6, 36]]
'''
'''
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([weapon.strip() for weapon in freshfruit])
# ['banana', 'loganberry', 'passion fruit']
print([weapon.strip('abcdef') for weapon in freshfruit])
# ['  banan', '  loganberry ', 'passion fruit  ']
print([weapon.strip('abcdefy') for weapon in freshfruit])
# ['  banan', '  loganberry ', 'passion fruit  ']
# a.strip('string')  用于移除字符串a头尾指定的字符(移除头尾在string里的)
a = ['abcert','bsgrcdhsj']
print([b.strip('abcdetj') for b in a])
# ['r', 'sgrcdhs']
#从a的头和尾分别逐个检索，一旦出现在字符串'abcdetj'中便移除，
#一旦某处中断立即停止
'''
# 我们可以用 if 子句作为过滤器： 
'''
a=[1, 2, 6]
print([x**x for x in a if x >= 2])
# [4, 46656]
b = [1, 2, 3, 4, 5.1, 5.6]
print(x**2 for x in b if x%2==0)
#<generator object <genexpr> at 0x0000023F759720C0>
print([x**2 for x in b if x%2==0])
# [4, 16]
print([x**2 for x in b if type(x)==float])
# [26.009999999999998, 31.359999999999996]
print([x**2 for x in b if x ])
# [1, 4, 9, 16, 26.009999999999998, 31.359999999999996]
'''

# 列表推导式可以使用复杂表达式或嵌套函数： 
'''
print([str(round(789/7, i)) for i in range(0,5)])
# ['113.0', '112.7', '112.71', '112.714', '112.7143']
# function :  str(x)  ----  'x'
# function :  round(数值，保留的小数位数)
#print([str(round(789//7,i) for i in range(0,5)])
# error
print([str(round(3.1415926, i)) for i in range(0,5)])
# ['3.0', '3.1', '3.14', '3.142', '3.1416']
'''
'''
# 嵌套列表解析
# 以下实例展示了3X4的矩阵列表：
matrix = [
    [1, 2, 3, 4],
    [2, 5, 8, 7],
    [4, 2, 4, 9],
]
print((matrix))
# [[1, 2, 3, 4], [2, 5, 8, 7], [4, 2, 4, 9]]
# 以下实例将3X4的矩阵列表转换为4X3列表：
print([[row[i] for row in matrix] for i in range(4)])
# [[1, 2, 4], [2, 5, 2], [3, 8, 4], [4, 7, 9]]
print(range(4))     # range(0, 4)
'''
# 也可以使用以下方法来实现
'''
>>> transposed = []
>>> for i in range(4):
...     transposed.append([row[i] for row in matrix])
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
'''

# 另外一种实现方法：
'''
>>> transposed = []
>>> for i in range(4):
...     # the following 3 lines implement the nested listcomp
...     transposed_row = []
...     for row in matrix:
...         transposed_row.append(row[i])
...     transposed.append(transposed_row)
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
'''

# del 语句
# 使用 del 语句可以从一个列表中依索引而不是值来删除一个元素。这与使用 
# pop() 返回一个值不同。可以用 del 语句从列表中删除一个切割，
# 或清空整个列表（我们以前介绍的方法是给该切割赋一个空列表）
'''
>>> a = [-1, 1, 66.25, 333, 333, 1234.5]
>>> del a[0]
>>> a
[1, 66.25, 333, 333, 1234.5]
>>> del a[2:4]
>>> a
[1, 66.25, 1234.5]
>>> del a[:]
>>> a
[]
'''
# 也可以用 del 删除实体变量： del a

# 元组和序列 
#在输入时可能有或没有括号， 不过括号通常是必须的

#集合
'''
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
set = set({1,2,3})
print('apple' in basket)    #True
print(1 in basket)     # False
print (1 in set)       # True
# 集合也支持推导式
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)        # {'r', 'd'}
'''

# 字典
'''
>>> tel = {'jack': 4098, 'sape': 4139}
>>> tel['guido'] = 4127
>>> tel
{'sape': 4139, 'guido': 4127, 'jack': 4098}
>>> tel['jack']
4098
>>> del tel['sape']
>>> tel['irv'] = 4127
>>> tel
{'guido': 4127, 'irv': 4127, 'jack': 4098}
>>> list(tel.keys())
['irv', 'guido', 'jack']
>>> sorted(tel.keys())
['guido', 'irv', 'jack']
>>> 'guido' in tel
True
>>> 'jack' not in tel
False
'''

'''
构造函数 dict() 直接从键值对元组列表中构建字典。如果有固定的模式，列表推导式指定特定的键值对：
>>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'jack': 4098, 'guido': 4127}

此外，字典推导可以用来创建任意键和值的表达式词典：
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}

如果关键字只是简单的字符串，使用关键字参数指定键值对有时候更方便：
>>> dict(sape=4139, guido=4127, jack=4098)
{'sape': 4139, 'jack': 4098, 'guido': 4127}
'''
'''
# 遍历技巧
#在字典中遍历时，关键字和对应的值可以使用 items() 方法同时解读出来：
dict = {'one':1,'two':2}
for k,v in dict.items():      
    print(k,v)                # one 1    \n     two 2

#在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到：

for i,v in enumerate(['a', 'b', 'c']):
   print(i,v)
# 0 a  \n  1 b   \n     2 c

#同时遍历两个或更多的序列，可以使用 zip() 组合：
questions = ['name', 'quest', 'favorite color']
answer =['a', 'b', 'c']
for q, a in zip(questions,answer):
    print('what is your {0}? it is {1}' .format(q,a))
#what is your name? it is a
#what is your quest? it is b
#what is your favorite color? it is c

# 要反向遍历一个序列，首先指定这个序列，然后调用 reversed() 函数： 
for i in reversed(range(1, 10, 2)):
     print(i)

#要按顺序遍历一个序列，使用 sorted() 函数返回一个已排序的序列，
# 并不修改原值：
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)
'''






































