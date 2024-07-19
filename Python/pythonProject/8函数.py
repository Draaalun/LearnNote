# dralun818
def get_sum(num):
    s=0
    for i in range(1,num+1):
        s+=i
    print(s)
sum=get_sum(3)





'''
def fun1(a=10,b):
    pass
fun1(10)
#这个会报错，因为你默认会把10传给a导致b没有值
'''
def fun(a,b=10):
    pass
fun(10)
fun(10,20)
fun(b=100,a=20)
#以上都不会报错





#####可变参数#####
#个数可变的位置参数
def para(*para):
    print(para,type(para))
    for i in para:
        print(i,end=" ")
para(10,20,30,40)
print()
para([1,2,3])
print()
para(*[1,2,3])#解包操作
print()
para((4,5,3))#解包操作
print()
para(*(4,5,3))#解包操作
print()
"""
(10, 20, 30, 40) <class 'tuple'>
10 20 30 40 
([1, 2, 3],) <class 'tuple'>
[1, 2, 3] 
(1, 2, 3) <class 'tuple'>
1 2 3 
((4, 5, 3),) <class 'tuple'>
(4, 5, 3) 
(4, 5, 3) <class 'tuple'>
4 5 3 
"""
#个数可变的关键字参数
def para2(**kwpara):
    print(kwpara,type(kwpara))
    for key,value in kwpara.items():
        print(key,"----",value)
para2(name=1,age=2,height=12)
"""
{'name': 1, 'age': 2, 'height': 12} <class 'dict'>
name ---- 1
age ---- 2
height ---- 12
"""
dic=dict(name=1,age=2,grade=3)
#print(*dic)#name age grade
para2(x=5,**dic)#**字典解包
"""
{'x': 5, 'name': 1, 'age': 2, 'grade': 3} <class 'dict'>
x ---- 5
name ---- 1
age ---- 2
grade ---- 3
"""





#####  #####
def calu(a,b):
    return a+b
print(calu(1,2))#3
print(calu(calu(1,2),3))#6
"""
如果为多返回值的话是元组数据类型
针对元组可以进行如下操作
"""
tu=(1,2,3)
a,b,c=tu
print(tu,a,b,c)#(1, 2, 3) 1 2 3
print(*tu)#1 2 3



#####局部or全部#####
#global定义全局变量，可以在函数中定义




#####lambda#####
"""
lambda 表达式用于创建匿名函数，也被称为 lambda 函数。
它们是一种简写形式的函数，通常用于简化需要传递给其他函数或作为参数使用的简单函数的定义。
lambda arguments: expression

# 计算平方
square = lambda x: x * x
# 计算平方根
square_root = lambda x: x ** 0.5
# 计算两个数字的和
add = lambda x, y: x + y
# 调用匿名函数
result = square(5)  # result = 25
print(result)
result = square_root(9)  # result = 3.0
print(result)
result = add(3, 4)  # result = 7
print(result)

s=lambda a,b:a+b#s表示的就是一个匿名函数
print(type(s))#<class 'function'>
print(s(10,20))#30
"""
# 对年龄使用降序排列,,,按字典中某一项进行排序为常用操作
students = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 22},
]
students.sort(key=lambda x:x.get("age"),reverse=False)
print(students)
#[{'name': 'Charlie', 'age': 22}, {'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]
sorted_students = sorted(students, key=lambda x: x.get("age"), reverse=True)
print(sorted_students)
#[{'name': 'Bob', 'age': 30}, {'name': 'Alice', 'age': 25}, {'name': 'Charlie', 'age': 22}]
sorted_students = sorted(students, key=lambda student: student["age"], reverse=True)
print(sorted_students)
#[{'name': 'Bob', 'age': 30}, {'name': 'Alice', 'age': 25}, {'name': 'Charlie', 'age': 22}]




#####递归操作#####
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(5)
print(result)  # Output: 120

def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
result = fibonacci(9)
print(result)  # Output: 34





#####常用的内置函数#####
"""
1. 通用函数

print(): 用于输出信息到控制台。
len(): 返回对象（如字符串、列表、元组等）的长度。
type(): 返回任意对象的类型。
range(): 生成一个数字序列，常用于循环。
input(): 获取用户的文本输入。
sorted(): 对序列进行排序，并返回新的排序列表。
sum(): 计算输入的可迭代对象中所有元素的总和。
2. 数字操作

abs(): 返回一个数的绝对值。
pow(): 计算幂运算。
round(): 四舍五入一个数字。
floor(): 向下取整一个数字。
ceil(): 向上取整一个数字。
int(): 将对象转换为整数。
float(): 将对象转换为浮点数。
str(): 将对象转换为字符串。
bool(): 将对象转换为布尔值。
3. 字符串操作

upper(): 将字符串转换为大写。
lower(): 将字符串转换为小写。
strip(): 删除字符串两端的空格。
split(): 将字符串按分隔符拆分成列表。
join(): 将列表中的元素连接成字符串。
find(): 在字符串中查找子字符串的第一个位置。
replace(): 将字符串中的部分内容替换为其他内容。
4. 列表操作

append(): 向列表末尾追加元素。
insert(): 在指定位置插入元素。
remove(): 删除指定元素。
pop(): 删除并返回指定位置的元素。
count(): 统计列表中元素出现的次数。
sort(): 对列表进行排序。
reverse(): 反转列表的元素顺序。
5. 元组操作

len(): 返回元组的长度。
type(): 返回元组的类型。
in： 检查元素是否在元组中。
tuple(): 将可迭代对象转换为元组。
6. 字典操作

keys(): 返回字典的键列表。
values(): 返回字典的值列表。
items(): 返回字典的键值对元组列表。
get(): 获取指定键的值，如果键不存在则返回默认值。
in： 检查键或值是否在字典中。
update(): 更新字典中的键值对。
7. 文件操作

open(): 打开文件。
read(): 读取文件内容。
write(): 写入文件内容。
close(): 关闭文件。
8. 日期和时间操作

datetime(): 创建日期和时间对象。
date(): 创建日期对象。
time(): 创建时间对象。
strftime(): 格式化日期和时间。
strptime(): 解析格式化的日期和时间字符串。
9. 数学函数

math.sin(): 计算正弦值。
math.cos(): 计算余弦值。
math.tan(): 计算正切值。
math.atan()： 计算反正切值。
math.log()： 计算对数。
math.exp()： 计算指数。
math.sqrt()： 计算平方根。
math.pi: 圆周率常数 π。
10. 其他函数

random.randint(): 生成指定范围内的随机整数。
random.random(): 生成 0 到 1 之间的随机浮点数。
sys.exit(): 退出程序。
time.sleep(): 暂停程序执行指定时间。
"""

"""
map() 函数将一个函数应用于序列中的每个元素，并返回一个包含转换后元素的新序列。
它接受两个参数：
函数: 要应用于每个元素的函数。
序列: 要处理的序列。

filter() 函数根据条件过滤序列中的元素，并返回一个只包含满足条件的元素的新序列。
它接受两个参数：
函数: 定义过滤条件的函数。
序列: 要过滤的序列。
"""
def square(x):
    return x * x
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)  # map(...) 返回一个迭代器
print(list(squared_numbers))  # 输出： [1, 4, 9, 16, 25]

def is_even(x):
    return x % 2 == 0
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(is_even, numbers)  # filter(...) 返回一个迭代器
print(list(even_numbers))  # 输出： [2, 4, 6]

def square_and_filter_even(x):
    if x % 2 == 0:
        return x * x
    else:
        return None
numbers = [1, 2, 3, 4, 5, 6]
result = filter(lambda x: x is not None, map(square_and_filter_even, numbers))
print(list(result))  # 输出： [4, 16, 36]
