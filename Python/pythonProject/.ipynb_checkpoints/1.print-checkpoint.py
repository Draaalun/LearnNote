# dralun818
# 自带集成开发环境 idle
#使用pycharm
#ipo 输入-处理-输出
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

#