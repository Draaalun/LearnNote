# dralun818
#####常用字符串#####
s='HelloWorld'
print(s.lower())#helloworld
print(s.upper())#HELLOWORLD

s="dralun818@163.com"
lst=s.split("@")
print(lst[0],lst[1],type(lst),sep="     ")#dralun818     163.com     <class 'list'>

print(s.count("8"))#2

print(s.find('a'),s.index('a'))#2 2两个a，位置在s[2]
print(s.find("p"))#-1没有找到的意思,index找不到的时候会报错

print("end.py".endswith('.py'))#True确定是以.py结尾的
print("end.txt".endswith('txt'))#True
print(s.startswith("dralun"))#True

new_s=s.replace("dralun","chen")
print(s,new_s)#dralun818@163.com chen818@163.com

print(s.center(30))#      dralun818@163.com       在三十个字符串中居中
print(s.center(30,'-'))#------dralun818@163.com-------

s1='    h    w    e    '
print(s1.strip())#h    w    e
print(s1.rstrip())#    h    w    e
print(s1.lstrip())#h    w    e
print(s1.strip('h w'))#e只要是引号中的出现的字符都被去除了

#格式化字符串
#1.占位符
name="chen"
age=18
score=99.9
print("name:%s,age:%d,score:%.1f"%(name,age,score))#name:chen,age:18,grade:99.9实现了不同类型的连接而且不用进行转换
#2.f-string
print(f"name:{name},age:{age},score:{score}")#name:chen,age:18,score:99.9
#3.format
print("name:{0},age:{1},score:{2}".format(name,age,score))#name:chen,age:18,score:99.9注意012对应format中参数顺序
"""
s="helloworld"
#:引导符   用于填充   对齐方式<>^左右中   宽度字符串输出的宽度   ,数字的千位分隔符   .精度表示小数点或字符串的长度   整数类型bdoxX浮点数类型eEf%
print("{0:-<20}".format(s))#helloworld----------0-20空格用-填充<左对齐
print("{0:->20}".format(s))#----------helloworld>右对齐
print("{0:-^20}".format(s))#-----helloworld-----居中对齐
print("{0:,}".format(9876543210))#9,876,543,210
print("{0:,}".format(9876543210.12354))#9,876,543,210.12354
print('{0:.2f}'.format(3.1415926))#3.14
print("{0:.5}".format("helloworld"))#hello只保留五位
a=123
print("{0:b},{0:o},{0:d},{0:x},{0:X}".format(a))#1111011,173,123,7b,7B
b=3.1415926535
print("{0:.2f},{0:.2%},{0:.2e},{0:.2E}".format(b))#3.14,314.16%,3.14e+00,3.14E+00
"""





#####字符串的编解码#####
'''
utf-8中文占三个字节 gbk中文占两个字节
str.encode(encoding='utf-8',
           errors='')
bytes.decode(encoding='utf-8',
             errors='')
errors中replace无法编码时会出现问号 ignore出现无法编码会忽略 strict严格编码，无法编码会报错
'''
s="伟大的中国万岁"
s_code=s.encode("utf-8",errors="replace")
print(s_code)
#b'\xe4\xbc\x9f\xe5\xa4\xa7\xe7\x9a\x84\xe4\xb8\xad\xe5\x9b\xbd\xe4\xb8\x87\xe5\xb2\x81'21个字符
s_code=s.encode("gbk",errors="replace")
print(s_code)
#b'\xce\xb0\xb4\xf3\xb5\xc4\xd6\xd0\xb9\xfa\xcd\xf2\xcb\xea'
