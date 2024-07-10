# dralun818
##############if##################
num=eval(input("plz input passwd:"))
if num==123456:
    print("right")
else:
    print("false")
if not num==123456:
    print("1")

x=input("plz input str")
if x:
    print("x is not null")
else:
    print("x is null")
###
score=eval(input("plz input u score"))
if score<0 or score>100:
    print("score is error")
elif score>=90:
    print("u get A!")
elif score>=80:
    print("u get B!")
elif score>=70:
    print("u get C!")
elif score>=60:
    print("u get D!")
else:
    print("go put!")



##############模式匹配################
score=input("plz input grade")
match score:
    case 'A':
        print("good")
    case _:
        print("others")



#############循环###################
#for循环和while循环
"""
for 循环变量 in 遍历对象：
    语句1
else：
    语句2
"""
#range()函数，产生一个[n,m)的整数序列
s=0
for i in range(1,11):
    s+=i
print(s)
###寻找水仙花树
for i in range(100, 1000):
    if i == ((i % 10) ** 3 + (i // 10 % 10) ** 3 + (i // 100) ** 3):
        print(i)
"""
for...in...
    语句1
else:
    语句2
###正常结束后才会执行else，中途遇到break退出不会执行。    
"""



#############while####################
'''
while 表达式：
    语句1
else：
    语句2
1.初始化变量
2.条件判断
3.语句块
4.改变变量
'''
ans=input("y/n")
while ans=='y':
    print("y")
    ans = input("y/n")#只要输入y就一直问，n退出
###
s=0
i=1
while i<=100:
    s+=i
    i+=1
else:
    print(s)
###while循环实现模拟用户登录
i=0
while i<3:
    name=input("name")
    pwd=input("pwd")
    if name=='1' and pwd=='1':
        print("OK")
        i=4
    else:
        if i<2:
          print(2-i,"次机会")
        i+=1
if i==3:
    print("err")
###while 嵌套循环
i=1
j=4
for i in range(1,6):
    print(" "*j+'*'*(2*i-1))
    j=j-1
j=1
for i in range(1,5):
    print(" "*j+'*'*(9-2*i))
    j=j+1

"""
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
"""


############break#############
sum=0
i=0
while i<100:
    sum+=i
    if sum>=100:
        break
    i += 1
print(sum,i)###105 14
##########cotinue#########
#跳过本次循环直接执行下一次while
#########pass#############
#起到占位符的作用，没有的话可能执行会受到影响
