'''
counter = 22       # integer variable(整型变量)
miles   = 11.1     # float    (浮点型)
name    = "abc"    # string   (字符串)

print (counter)
print (miles)
print (name)
'''
'''
a=b=c=1
print(a)
print(b)
print(c)
'''# simultaneous assignment of multipie variables is allowed.
   #允许为多个变量同时赋值
   
'''  
a, b, c = 1, 2, "an"
print (a)
print (b)
print (c)
'''    # multiple variables can be specified for multiple objects
       # 可以为多个对象指定多个变量

# immutable datas(不可变数据) contain Number(数字)，String(字符串) and
# Tuple(元组).
# variable datas (可变数据) contain List(列表)，Dictionary(字典)，and
# Set(集合)

# Number : int(长整型)，float, bool, complex(复数)
#The built-in type() function can be used to query 
# the object type indicated by the variable
#内置的 type() 函数可以用来查询变量所指的对象类型
'''
a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))
'''    # Note that indentation will cause error.
       #注意缩进将致错(每行的开头)
#in addition, 'isinstance' can be also used to judge/verify type.
'''
a = True
print (isinstance (a,float))
'''
# type() and isinstance difference :
# Type () does not consider a subclass to be a parent type
# type()不会认为子类是一种父类类型
#Isinstance () considers a subclass to be a parent type.
# isinstance()会认为子类是一种父类类型。
'''
var1 = 1   #当你指定一个值时，Number 对象就会被创建
var2 = 2   #When you specify a value, the number object is created
del var1   # delete single object
del var1, var2  # delete multiple objects
'''
'''
a = 5 + 3  # addition(+)
a = 1.6 -0.7   #  subtraction(-)
a = 1.1 * 1.2  # multiplication(*)
a = 1.6 / 0.3  #division(/)
a = 17.1 % 3     #modular (%)取余
a = 2 / 4      # get a float(/得到一个浮点数)
a = 2 // 4     # get a integer(//get only the integer portion)
a = 3 ** 5     # power(**乘方)
a = 'e '
print (a)
'''
#1.note that Python can assign values to 
# multiple variables at the same time
# for example, a,b = 1,2
#2.A variable can be assigned to different types of objects
#3.In mixed computing, python converts 
# integers to floating-point numbers.
'''
var = 0x260   # hexadecimal(260H)
var = -0x69 
var = 32.3e+18   #(e+18 : 10 ** 18;e-7 : 10** -7)
var = complex (2,3) # define complex
var = 2 + 3j
print (type(var))
print (var)
'''
#print ('multi\
# ple')
#word = 'python'
#print (word[0],word[5],word[-1],word[-2])
#strings in python cannot be changed
# there are two ways to index trings in python, starting with 0 
# from left to right and -1 from right to left
#------------------------------------
#List(列表)
'''
t = ['a', 'b', 'string', '123.7', 'False']
m = ['1', '2']
#print (isinstance (2.1, int))
#print (t[0],t[-1])
print (t[0:-2])    # output ['a', 'b', 'string']
print (t[0:])
print (t[:4])
print (t[:])       # output complete list
print (t)          # output complete list
print (t[-1:-2])   # output []  so it cannot output from right to left
print (m * 2)      # output the list 'm' twice
print (t + m)      # splice(拼接) the list 't' and 'm'
'''
#print('a' ,'b')   #  , it plays a separate role
#unlike strings, the elements in the list can be changed
'''
list = [1, 3, '4', '7','8', 9]
list[0] = 0.1
list[1:5] = 0.2, 0.3, 0.8, 5

print(list[ : : 2])    # the third parameter(参数) is step size
print(list[5:4:-1])
print (list[-1 : -5 : -2])
# if the third parameter is negative, it means reverse reading
'''
'''
def reverseWords(input) :
    inputWords = input.split(" ")
    inputWords = inputWords[-1: :-1]
    output = ''.join(inputWords)
    
    return output

if __name__ == "__main__":
    input = 'i\n like\t you\t'
    rw    = reverseWords(input)
    print(rw)
'''
# Tuple(元组) is similar to List
# the difference is that the element of Tuple cannot be modified(修改)
'''
tuple = (6, 1.1, False, complex(-1,2),'tring')
tinytuple = (4, 8)
print (tuple)     #output complete tuple
print (tuple[0])  #output the first element
print (tuple[1:3]) # the output starts from the second element to the third
print (tuple[2:])  # Output all elements starting with the third element
print (tuple * 2)  # output the tuple twice
print (tuple + tinytuple) # connect the two tuples
print (tuple[-1 :  :-2])  # reverse  and   step size is 2
#tuple[0] = 5   tuple cannot be modified
'''
'''
tup1 = ()     #empty Tuple
tup2 = (11,)  #only an element  (note ,)
'''     # string, list and tuple belong to sequence
'''
# Set(集合)
#establish by {} or set() 
# note :  empty set : set() ;  empty dictionary : {}
M = {1, 1, 'abc','raw', complex(1,2)}
# duplicate elements are removed automatically
N = set('1''abc')   #note
print (M)
print (M|N)    # union(并集)
print (M - N)  # difference set(差集)
print (M & N)  # intersection(交集)
print (M ^ N)  # elements that do not exist at the same time
# mumbers test
if 1 in M :
    print ('在集合M中')
else :
    print ('不在集合M中')
'''
#Dictionary
# List : ordered    Dictionary : disordered
# one and only key(键) in the same dictionary
# key is immutable
'''
dict = {}
dict['one'] = '1 - 菜鸟教程'
dict[2]     = '2 - 菜鸟工具'

tinydict = {'name' : 'ru', 'code' : 1, 'site' : 'www.runoob.com'}

print (dict['one'])  #output value of the key 'one'
print (dict[2])      #output value of the key 2
print (tinydict)     #output complete dictionary
print (tinydict.keys())   #output all keys
print (tinydict.values()) #           values
'''
'''
a = dict([('one', 1), ('two', 2)])
b = dict(one=1,two=2)
c = {x: x**2 for x in (2,4,6)}
print (a, b, c)
print ()
print (a.keys())
print (a.values())
'''






































































































