# dralun818
#####常用字符串#####
import re

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
print(bytes.decode(s_code,"gbk",errors="strict"))
#伟大的中国万岁






#####数据的验证#####
"""
type() 函数：用于获取变量的数据类型。
isinstance() 函数：用于判断一个变量是否属于某个类或其子类。
len() 函数：用于获取字符串或序列的长度。
str.isdigit() 方法：用于判断字符串是否只包含数字。
str.isnumeric() 方法：用于判断字符串是否包含数字（包括中文数字、罗马数字和其他禁止的数字）。
str.isalpha() 方法：用于判断字符串是否只包含字母(包括中文)。
str.islower() 方法：用于判断字母都是小写。
str.isupper() 方法：用于判断字母都是大写。
str.istitle() 方法：用于判断字母都是首字母大写。
str.isalnum() 方法：用于判断字符串是否只包含字母或数字。
str.isspace() 方法：用于判断字符串是否只包含空格。
re.match() 函数：用于判断字符串是否匹配正则表达式。
"""





#####数据的处理######
#拼接操作
s1="hello"
s2="world"
#1.
print(s1+s2)
#2.
print("".join([s1,s2]))
print("*-*".join([s1,s2]))#hello*-*world
print(("-*-".join(["q","w","e","r"])))#q-*-w-*-e-*-r
#3.
print("%s%s"%(s1,s2))#helloworld
print(f"{s1}{s2}")#helloworld
print("{0}{1}".format(s1,s2))#helloworld
#去重
s="hello"*5
print(s)
new_s=""
for item in s:
    if item not in new_s:
        new_s=new_s+item
print(new_s)#helo





#####正则表达式#####
"""
.匹配任意字符\w匹配字母数字下划线\W匹配非字母数字下划线\s匹配任意空白字符\S匹配任意非空白字符\d匹配十进制数
re.match(pattern, string, flags=0)
    pattern：要匹配的正则表达式模式。
    string：要匹配的字符串。
    flags：可选的标志位，用于控制匹配行为。
如果匹配成功，则返回一个 Match 对象，包含有关匹配结果的信息。
如果匹配失败，则返回 None。

Match 对象包含有关匹配结果的信息，可以通过以下属性和方法访问：
group()：返回整个匹配的字符串。
# group(n)：返回第 n 个分组的字符串。
# groups()：返回所有分组的字符串的元组。
start()：返回匹配的开始位置。
end()：返回匹配的结束位置。
string():待匹配的字符串
span()：返回匹配的开始位置和结束位置的元组。  

Flags参数可以用于控制匹配行为。以下是一些常用的标志位：
re.I（IGNORECASE）：忽略大小写。
re.MULTILINE：将字符串视为多行文本。
re.DOTALL：将 . 视为匹配任何字符，包括换行符

.：匹配任何单个字符。
*：匹配零个或多个字符。同+，但是可以是还可以是零次即为color
+：匹配一个或多个字符。colou+r可以匹配colour或colou...r
^：匹配字符串的开头。
$：匹配字符串的结尾。
?:匹配前面的字符0或者1次，colou?r可以匹配colour或者color
[]：匹配指定字符集中的任意一个字符。例如，[a-z] 匹配小写字母，[0-9] 匹配数字。
[^]：匹配不在指定字符集中的任意一个字符。例如，[^a-z] 匹配非小写字母，[^0-9] 匹配非数字。
()：用于分组，可以将多个子表达式组合在一起。例如，(ab)* 匹配 ab 重复零个或多次。
|:匹配|左右的任意字符
{n}：匹配前面的子n次。例如，d{18} 匹配 18位的数字。
{n,}：匹配前面的字符至少n个
{n,m}：匹配前面的字符n-m个
"""
pattern="\d\.\d+"#
s="i study python 3.14 everyday"
match=re.match(pattern,s,re.IGNORECASE)
print(match)#None
s1="3.14python i study everyday"
match2=re.match(pattern,s1)
print(match2)#<re.Match object; span=(0, 4), match='3.14'>
print(match2.group())#3.14
"""
re.search(pattern, string, flags=0)
只是第一个匹配的值
"""
pattern="\d\.\d+"#
s="i study python 3.14 everyday7.16"
s1="i will become beautiful"
match3=re.search(pattern,s)
match4=re.search(pattern,s1)
print(match3,match3.group())#<re.Match object; span=(15, 19), match='3.14'> 3.14
print(match4)#None
"""
re.findall(pattern, string, flags=0)
会找到所有查找值并放到列表里
"""
pattern="\d\.\d+"
s="i study python 3.14 everyday7.16"
s1="i will study hard"
match=re.findall(pattern,s)
print(match)#['3.14', '7.16']
match2=re.findall(pattern,s1)
print(match2)#[]
"""
re.sub
实现对字符串中指定字符串的替换
re.split
分割字符串
"""
pattern="黑客|破解|反爬"
s="我想学习python，破解一些VIP视频，可以实现反爬嘛？"
new_S=re.sub(pattern,"**",s)
print(new_S)#我想学习python，**一些VIP视频，可以实现**嘛？
pattern="[s|&]"
s1="https://mp.weixin.qq.com/s/GVVsHCtFsmd6vG6BCQqvYA"
new_s=re.split(pattern,s1)
print(new_s)#['http', '://mp.weixin.qq.com/', '/GVV', 'HCtF', 'md6vG6BCQqvYA']


import re

pattern = "[a-zA-Z0-9+_-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}"
email_address = "johndoe@example.com"
match = re.match(pattern, email_address)
print(match)
if match:
    print("Valid email address:", match.group())
else:
    print("Invalid email address")

import re

pattern = "\d{3}-\d{3}-\d{4}"
text = "My phone number is 123-456-7890. Please call me if you have any questions."
match = re.findall(pattern, text)
if match:
    print("Phone number found:", str(match))
else:
    print("No phone number found")


import re

pattern = r"\d{4}-\d{1,2}-\d{1,2}"
date_string = "2024-07-20"

match = re.match(pattern, date_string)
if match:
    print("Valid date:", match.group())
else:
    print("Invalid date format")
