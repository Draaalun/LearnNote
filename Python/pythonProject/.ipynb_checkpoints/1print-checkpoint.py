# dralun818

#自带集成开发环境 idle
#使用pycharm
#ipo 输入-处理-输出input process output
print("hello")
a=100
b=50
print(90)
print(a+b)
print(a,b,'death')
print(chr(98),'b')

#ascii 对应数值
print(ord('被'))
print(chr(34987))

#写入文件
fp=open('test.txt','w')
print("welcome to shandong",file=fp)
fp.close()

#print(value,...,sep=' ',end='\n',file=none)
#sep分隔符end换行符
#多条print输出一行
print("bj",end='-->')
print('sd')

#输入语句
name=input('提醒文字\n')
print('my name is:'+name)
#print('my name is:',name)
#别忘记print的格式，用，间隔的自动添加空格，+是相连接的但只能是字符串。

#输入整数类型，但这是字符串类型，要变换成整形需要转换
a=input("just a number is ok:")
print('number is:'+a)
num=int(a)
print('num',num)

#多行注释三引号
'''
这是一个多行注释
1
2
3
三个引号
'''

"""
这个也
可以
"""

#coding=gbk //coding=utf-8
#python编码格式由第一行决定的
#中文生命注释，一定写在第一行

#代码缩进，一般代码不需要缩进
'''
class student
    pass

#函数定义
def fun()
    pass
'''