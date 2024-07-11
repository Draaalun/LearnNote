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
lst2=[random.randint(1,100) for _ in range(1,11)]#range(10)也是十个数的意思
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



######元组#####
#元组不可变数据类型，
