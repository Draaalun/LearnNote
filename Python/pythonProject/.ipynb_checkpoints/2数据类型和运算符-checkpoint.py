# dralun818

#保留字 35个
#import keyword
#print(keyword.kwlist)
#['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break',
# 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally',
# 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal',
# 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
#print(len(keyword.kwlist))
#35

#标识符可以是字符、下划线_和数字，并且第一个字符不能是数字
#严格区分大小写
#下划线开头的标识符有特殊意义，避免使用相似的标识符
#允许中文做标识符不建议使用
"""
模块：尽量短小，全部小写，可以下划线分割单词字母grame_main
包名：短小，全部小写，不推荐下划线，使用点可以com.ysjpython
类名：单词首字母大写形式MyClass
模块内部类名：_InnerMyClass
函数、类的属性和方法的命名：小写，多下划线分割

常量：大写字母，下划线
_开头的模块变量或者函数受保护
__实例变量或者方法是类私有的
__init__()双下划线开头和结尾的是python专用标识

变量：栈内存——>堆内存
luck_num=8,栈内存luck_num，堆内存8.
动态语言，变量类型由后面的变量类型决定。
允许多个变量指向同一个值，地址值相同。

type(),查看变量类型
id(),查看变量地址值

"""


num="zhang"
print(type(num))
num=num1=2
print(type(num),type(num),sep="------")
print(id(num))
print(id(num1))

#整数类型int，不可变数据类型
#987 0b1001 0o754 0x54AF,print输出都是十进制
#浮点型float，带有小数点的数值，由整数和小数部分组成
#18.9  1.99E1413
#浮点数运算会出出现确定的尾数问题,使用round(0.1+0.2,1),对运算结果保留一位小数
#复数类型使用：x=123+456j，实属x.real，x.imag

#字符串类型:换行符\n水平制表位，横向跳到下一个制表位\t双引号\"单引号\'一个反斜杠\\
print("he says:\"learn!\"")#he says:"learn!"
print(r"he says:\"learn!\"")#直接输出he says:\"learn!\"
#切片和索引
#注意：切片中不包含后面数值对应的字符
s="helloworld"#0 ————> 9 // -10 <————— -1
print(s[0],s[-10])
print(s[2:7])
print(s[:5])
print(s[2:])
#+连接符   x*n或者n*x复制n次字符串x    x in s，如果x是s的子串，结果为true，否则为false
x='gun'
y='dan'
print(x+y)
print(x*3)
#True False bool类型,非零整数的布尔值都为true，浮点数为false，非空字符串也是true。

#数据类型的转换
#int(x) float(x) str(x)  hex(x) oct(x) bin(x) //整数和字符互换chr(x) ord(x)
#必须本身是整数的变量才能转换为整数类型
q='3+3.14'
q=eval(q)
print(round(q,2))
age=eval(input("plz input u age:"))#将字符串去掉引号
print(age,type(age))

#算数运算符
#+-*/ //整除 %取余 **幂运算
print(2**4, 10//3, 10%3)

#赋值运算符
# = +=  -=  *=  /=  %=  **= //=
a,b=10,20
print(a,b)
a,b=b,a#交换ab的值
print(a,b)

#比较运算符
#>  <   ==  ！=  >=  <=

#逻辑运算符
#and or not
print('-'*40)

#位运算
#&  |   ^异或    ~取反    <<左移位>>右移位

###
num=input("plz input a 3 num：")#字符串
print(num[0],num[1],num[2])
num=eval(input("plz input a 3 num："))#整数型
print(num//100,num//10%10,num%10)
