# dralun818
import random




#####序列和索引#####
#序列多个值的连续空间，每个值对应一个整数编号，称为编号。
#正向递增索引
s="helloworld"
for i in range(1,len("helloworld")):
    print(i,s[i],end="    ")
print()
#反向递减
for i in range(-10,0):
    print(i,s[i],end="    ")
print()
#切片操作
s1=s[0:5:2]
s2=s[:5:1]
s3=s[:5:]
s4=s[::]
print(s1,s2,s3,s4)#hlo hello hello helloworld,第三个参数为步长，可以为负数反方向看
#序列的相加操作
#x in s逻辑输出True or false---x not in s逻辑输出---len(s)长度---max(s)序列中的最大值---
# min(s)序列中的最小值---s.index(x)序列s中第一次出现x的位置---s.count(x)序列s中x的总次数---
print(s1+s2)
print(s1*5)
print('e' in s,'e' not in s,s.index('e'),s.count('e'))
print(len(s),min(s),max(s))




#####列表#####
#一些按特定顺序排列的元素，可变数据类型（之前的整数型浮点型和字符串型都是不可变数据类型）
#使用[]定义列表，元素之间使用英文逗号分隔，列表中的元素可以是任意的数据类型
lst1=['he','1',1]
lst2=list("helloworld")
lst3=list(range(1,10,2))
print(lst1,lst2,lst3,sep="  ")
#列表是序列的一种，对序列的操作、运算和函数均可以使用
print(lst3+lst2+lst1,lst2*3,len(lst2))
del lst1,lst2,lst3
#enumerate函数的使用语法结构
'''
for index,item in enumerate(lst)
    输出index和item
index序号，默认从零开始item元素
'''
lst=['w','q','1',12,45]
for item in lst:
    print(item,end=" ")
#w q 1 12 45
print()
for i in range(0,len(lst)):
    print(i,'--->',lst[i],end=" ")
#0 ---> w 1 ---> q 2 ---> 1 3 ---> 12 4 ---> 45
print()
for index,item in enumerate(lst,start=1):
    print(index,"--->",item,end=" ")
#1 ---> w 2 ---> q 3 ---> 1 4 ---> 12 5 ---> 45
print()
#列表的相关操作方法
lst=['l','s','t',1,2]
lst.append(3)#lst最后增加一个元素
lst.insert(1,1)#在index位置增加一个元素
print(lst)
#lst.clear()#清除lst
lst.pop(1)#删除index位置的元素
print(lst)
"""
lst.remove(x)#将lst第一个元素x删除
lst.reverse(x)#将lst的元素反转（序号顺序反转）
lst.copy(x)#拷贝lst所有元素生成一个新的列表
lst[1]="123456789"#也可以更改列表
"""
#列表排序
lst=[5,4,95,0,1,2]
sorted(lst,key=None,reverse=False)#排序对象，，，，
lst.sort(key=None,reverse=False)#key排序规则，rev中false升序true降序；
print(lst)
#[0, 1, 2, 4, 5, 95]
lst=list("banana")
lst.sort(key=None,reverse=True)#升序排列
print(lst)
#['n', 'n', 'b', 'a', 'a', 'a']
#列表生成式的语法结构
#lst=[exp for item in range]
#lst=[exp for item in range if condition]
#表达式结合for和if
lst=[item for item in range(1,11)]
lst1=[item*item for item in range(1,5)]
lst2=[random.randint(1,100) for _ in range(1,11)]#随机生成10个数
print(lst,lst1,lst2)
lst=[i for i in range(10) if i%2==0 ]
print(lst)
#二维列表
lst=[['q','w','e'],
     ['a','s','d'],
     ['z','x','c']]
print(lst)
#[['q', 'w', 'e'], ['a', 's', 'd'], ['z', 'x', 'c']]
for a in lst:
    for b in a:
        print(b,end=" ")
    print()
"""
for row in lst:
    for item in row:
        print(item,end=" ")
    print()
q w e 
a s d 
z x c 
"""
#列表生成式
lst=[[j for j in range(5)]for _ in range(4)]#_起到占位符的作用
print(lst)




######元组tuple#####
#元组不可变数据类型，
#使用（）定义元组，元素与元素之间使用英文都好分隔，只有一个元素也不能省略逗号
"""
元组=（，，，）
"""
t=("hello",[10,20,30],'world')
print(t)#('hello', [10, 20, 30], 'world')
t=tuple("helloworld")
print(t)#('h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd')
t=tuple([10,20,30])
print(t,type(t))#(10, 20, 30) <class 'tuple'>
print("10在元组中是否存在",10 in t)#10在元组中是否存在 True
#in 运算符用于检查一个元素是否存在于另一个序列（例如列表、元组或字符串）中
del t#删除元组
#元组遍历
t=("q",'w','e','r')
for i in range(len(t)):
    print(i,'--->',t[i],sep="",end="    ")
print()#0--->q    1--->w    2--->e    3--->r
for index,item in enumerate(t,start=1):
    print(index,'--->',item,sep="",end="    ")
print()#1--->q    2--->w    3--->e    4--->r
del t
#元组生成
t=tuple(i for i in range(5,9))
print(t)#(5, 6, 7, 8)
for item in t:
    print(item,end=" ")#5 6 7 8
print()




######区别#####
"""
my_list = [1, 2, 3, "apple", "banana"]
my_tuple = (1, 2, 3, "apple", "banana")

可变性：
列表是可变的，这意味着可以在创建后对其内容进行修改。例如，可以向列表中添加、删除或修改元素。
元组是不可变的，这意味着一旦创建，其内容就无法更改。尝试修改元组会引发 TypeError 异常。

用途：
列表通常用于存储需要在运行时进行修改的数据。例如，可以使用列表来跟踪一组待办事项或玩家的分数。
元组通常用于存储不需要更改的数据。例如，可以使用元组来存储颜色列表或常量值。

其他区别：
列表可以嵌套其他列表。元组也可以嵌套其他元组，但不能嵌套列表。
列表可以使用切片操作来提取子列表。元组也可以使用切片操作来提取子元组。
列表可以连接在一起形成新的列表。元组不能连接在一起。
"""



#####字典#####
#字典是一种可变容器数据结构，用于存储键值对。
#键通常是字符串或数字，值可以是任何类型的数据，包括其他字典、列表和元组。
#字典中的键必须唯一，但值可以重复。
"""
字典 = {键1: 值1, 键2: 值2, ...}

student = {"姓名": "小明", "年龄": 12, "年级": 6}
1.
姓名 = student["姓名"]
print(姓名)  # 输出：小明
2.
年龄 = student.get("年龄", 0)
print(年龄)  # 输出：12
3.
student["班级"] = "三班"
print(student)  # 输出：{'姓名': '小明', '年龄': 12, '年级': 6, '班级': '三班'}
4.
new_student = {"年龄": 13, "年级": 7}
student.update(new_student)
print(student)  # 输出：{'姓名': '小明', '年龄': 13, '年级': 7, '班级': '三班'}
5.
new_student = {"年龄": 13, "年级": 7}
student.update(new_student)
print(student)  # 输出：{'姓名': '小明', '年龄': 13, '年级': 7, '班级': '三班'}
6.
del student["班级"]
print(student)  # 输出：{'姓名': '小明', '年龄': 13, '年级': 7}
7.
age = student.pop("年龄")
print(age)  # 输出：13
print(student)  # 输出：{'姓名': '小明', '年级': 7}
"""
#创建字典
# 使用花括号创建字典
student = {"姓名": "小明", "年龄": 12, "年级": 6}
# 使用 dict() 函数创建字典，这里的key好像不用加引号
student = dict(姓名="小明", 年龄=12, 年级=6)
print(student)
# 添加新的键值对
student["班级"] = "三班"
print(student)  # 输出：{'姓名': '小明', '年龄': 12, '年级': 6, '班级': '三班'}
# 更新字典中的值
new_student = {"年龄": 13, "年级": 7}
student.update(new_student)
print(student)  # 输出：{'姓名': '小明', '年龄': 13, '年级': 7, '班级': '三班'}
# 删除键值对
del student["班级"]
print(student)  # 输出：{'姓名': '小明', '年龄': 13, '年级': 7}
# 使用 pop() 方法删除键值对
age = student.pop("年龄")
print(age)  # 输出：13
print(student)  # 输出：{'姓名': '小明', '年级': 7}
#zip映射
lst=[1,2,3,4]
lst1=['a','b','c','d']
zipobj=zip(lst,lst1)
# d=list(zipobj)
# print(d,type(d))#[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')] <class 'list'>
#d=tuple(zipobj)
#print(d,type(d))#((1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')) <class 'tuple'>
d=dict(zipobj)
print(d,type(d))
#{1: 'a', 2: 'b', 3: 'c', 4: 'd'} <class 'dict'>
#
#参数创建字典
d=dict(n=1,m=2)
print(d)
#{'n': 1, 'm': 2},,,注意这里使用等于号
t=(1,2,3)
print({t:1})
#{(1, 2, 3): 1},,,注意这里使用：元组可以作为键使用
# r=[1,2,3]
# print({r:1})
#列表无法作为键使用，以上不会输出
#可变数据类型不会作为字典中的键使用
# del d,t
#字典是无序的，看起来有序是因为3.5解释器版本后做了修改
d={"a":'q',"b":"w","c":'e',"d":'r'}
print(d.get('a'))#q
print(d['b'])#w
# print(d['s'])
# print(d.get("s"))#程序在此编译器下不会报错但是空输出因为没有查到
print(d.get(1,'find nothoing'))
#输出：find nothoing
#
#字典的遍历
for item in d.items():
    print(item,end="")
print()
#('a', 'q')('b', 'w')('c', 'e')('d', 'r')这其实是元组
for key,item in d.items():
    print(key,':',item, sep="",end="  ")
#a:q  b:w  c:e  d:r
#
# 获取字典的键
keys = student.keys()
print(keys)  # 输出：dict_keys(['姓名', '年龄', '年级'])
# 获取字典的值
values = student.values()
print(values)  # 输出：dict_values(['小明', 13, 7])
# 获取字典的键值对
items = student.items()
print(items)  # 输出：[('姓名', '小明'), ('年龄', 13), ('年级', 7)]
###注意：items的形式是key-values形式，以元组的形式进行展示
#复制字典
new_student = student.copy()
print(new_student)  # 输出：{'姓名': '小明', '年龄': 13, '年级': 7}
#清空字典
student.clear()
print(student)  # 输出：{}
'''
a=(1,2,3)
print(a[0],type(a))
a=list(a)
a[0]=2
print(a[0],type(a))
a=tuple(a)
print(a,type(a))
# 1 <class 'tuple'>
# 2 <class 'list'>
# (2, 2, 3) <class 'tuple'>
#很有意思，注意元组类型是无法修改的，但是转换为list后可以修改
'''
#字典生成式
"""
import random
d={item :random.randint(1,100) for item in range(10) }
print(d)
#{0: 1, 1: 3, 2: 21, 3: 49, 4: 22, 5: 77, 6: 9, 7: 9, 8: 14, 9: 57}
lst1=['chen','zhang''wang','kang']
lst2=[1,2,3,4]
# d=dict(zip(lst1,lst2))#也可以
d={key:value for key,value in zip(lst1,lst2)}
print(d,type(d))
#{'chen': 1, 'zhangwang': 2, 'kang': 3} <class 'dict'>
"""



#####集合#####
#
#在 Python 中，集合是一种无序、不重复元素的集合。
# 这意味着集合中的每个元素只出现一次，元素的顺序并不保留。
# 集合使用哈希表实现，这允许高效地插入、删除和成员关系测试。
#
# 集合是可变的，这意味着您可以在创建后添加、删除和修改元素。
# 集合是无序的，这意味着集合中元素的顺序并不保证会保留。
# 集合是可散列的，这意味着它们可以用作字典中的键和作为其他集合中的元素。
my_set = {1, 2, 3}
print(my_set,type(my_set))
#s={}创建的是字典不是集合
my_set = set()#创建了一个空集合,布尔值是false
print(my_set,type(my_set))
s={'helloworld'}
print(s,type(s))#{'helloworld'} <class 'set'>
s=set("helloworld")
print(s,type(s))#{'h', 'w', 'r', 'd', 'e', 'l', 'o'} <class 'set'>
#
# 创建集合
s1 = {1, 2, 3}
s2 = {3, 4, 5}
# 检查元素是否存在
print(1 in s1)  # 输出：True
print(4 in s2)  # 输出：False
# 添加元素
s1.add(6)
print(s1)  # 输出：{1, 2, 3, 6}
# 删除元素
s2.remove(5)
print(s2)  # 输出：{3, 4}
# 并集运算
s3 = s1 | s2
print(s3)  # 输出：{1, 2, 3, 4, 6}
# 交集运算
s4 = s1 & s2
print(s4)  # 输出：{3}
# 差集运算
s5 = s1 - s2
print(s5)  # 输出：{1, 2, 6}
# 对称差集运算 # A并B-A交B
s6 = s1 ^ s2
print(s6)  # 输出：{1, 2, 4, 5, 6}
# 比较集合
print(s1 == s2)  # 输出：False
print(s1 != s2)  # 输出：True
# 集合的遍历操作
for x in s1:
    print(x,end=" ")#1 2 3 6
print()
for index,item in enumerate(s1):
    print(index,'-->',item,end="    ")
print()
#集合的生成式
s={i for i in range (1,20) if i%2==0}
print(s,type(s))




#####列表、元组、字典和集合的区别#####
#列表list 可变序列 元素可重复 有序 []
#元组tuple 不可变序列 可重复  有序 ()
#字典dict  可变序列 key不可重复value可重复 无序 {key:value}
#集合set 可变序列 不可重复  无序  {}
