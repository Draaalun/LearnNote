"""
import 模块
import 模块 as 别名
from 模块 import 变量/函数/类/*
"""
import my_info
print(my_info.name)#chen

from my_info import name
print(name)#chen

from my_info import *
print(name,age,collage)#chen 23 HIT
"""
导入变量中存在重叠的元素，后者会覆盖前者，
可以直接使用import模块，
后续使用模块.变量名就可以了
"""




"""
包
"""
import admin.my_admin as a#导入方式为import 包.模块 as 别名
a.info()
#dralun818(init中的代码)
#hello everyone! My name is dr.alun
from admin import my_admin as b
b.info()
#hello everyone! My name is dr.alun(init中的代码只执行一次)
from admin.my_admin import info
info()
#hello everyone! My name is dr.alun
from admin.my_admin import *
info()
#hello everyone! My name is dr.alun




"""
阻值全局变量的代码被其他程序调用时执行
下例子中，main函数只有在脚本直接运行时才会被调用。
如果模块被其他程序导入，main() 函数将不会被调用。
"""
def main():
  # 仅在脚本直接运行时执行的代码
    pass
if __name__ == "__main__":
  main()




"""
Python 的 random 模块提供了多种函数，用于生成随机数和进行随机操作。以下是 random 模块中一些常用的函数：

生成随机数
random.random()：生成一个介于 0.0 和 1.0 之间的均匀分布的随机浮点数。不包含1
random.uniform(a, b)：生成一个介于 a 和 b 之间的均匀分布的随机浮点数。
random.randint(a, b)：生成一个介于 a 和 b 之间的均匀分布的随机整数。包含b
random.randrange(start, stop, step)：生成一个从 start 到 stop 的整数范围内的随机数，步长为 step。
random.choice(seq)：从序列 seq 中随机选择一个元素。
random.choices(seq, k)：从序列 seq 中随机选择 k 个元素，并返回一个列表。
打乱序列
random.shuffle(seq)：将序列 seq 中的元素随机打乱。
设置种子
random.seed(a)：设置随机数生成器的种子。相同的种子将生成相同的随机数序列。
"""
import random
# 生成一个随机浮点数
random_float = random.random()
print(random_float)  # 输出：0.723456789
# 生成一个介于 10 和 20 之间的随机整数
random_int = random.randint(10, 20)
print(random_int)  # 输出：15
# 从列表中随机选择一个元素
random_element = random.choice(["apple", "banana", "orange"])
print(random_element)  # 输出：apple
# 将列表中的元素随机打乱
fruits = ["apple", "banana", "orange"]
random.shuffle(fruits)
print(fruits)  # 输出：['orange', 'apple', 'banana']
# 设置种子并生成相同的随机数序列
random.seed(10)
random_float1 = random.random()
random.seed(10)
random_float2 = random.random()
print(random_float1, random_float2)  # 输出：0.543210987654321, 0.543210987654321
random.seed()
print(random.randrange(0, 101, 50))#随机生成0/50/100





"""
time模块
"""
import time
current_time = time.time()
print(current_time)  # 输出：1721268728.60672
#该函数返回自 Unix 纪元（1970 年 1 月 1 日 00:00:00 UTC）以来当前时间的浮点数秒数。

start_time = time.process_time()
# 执行一些耗时的操作
end_time = time.process_time()
elapsed_time = end_time - start_time
print(elapsed_time)  # 输出：0.234567
#该函数返回当前进程花费的累积 CPU 时间（以秒为单位）。
# 该值包括用户时间（执行进程代码所花费的时间）和系统时间（等待 I/O 或其他系统资源所花费的时间）
print(time.localtime())
#time.struct_time(tm_year=2024, tm_mon=7, tm_mday=18, tm_hour=10,
#tm_min=19, tm_sec=2, tm_wday=3,(星期四) tm_yday=200, (一年之中的第几天)tm_isdst=0(夏令时标志))
print(time.localtime(1658148262.200687))
#time.struct_time(tm_year=2022, tm_mon=7, tm_mday=18, tm_hour=20,
# tm_min=44, tm_sec=22, tm_wday=0, tm_yday=199, tm_isdst=0)
my_time=time.localtime()
print(my_time.tm_year,'年',my_time.tm_mon,'月',my_time.tm_mday,'日','\n',
      my_time.tm_hour,':',my_time.tm_min)
#2024 年 7 月 18 日
# 10 : 27
print(time.ctime())
#Thu Jul 18 10:59:31 2024
my_time=time.localtime()
str_time=time.strftime("%Y-%m-%d %H:%M:%S",my_time)
print(str_time)#2024-07-18 11:14:59





"""
datetime模块
"""
from datetime import date, time, datetime, timedelta

# 创建日期对象
today = date.today()
print(today)  # 输出：2024-07-18
# 创建日期和时间对象
dt = datetime.now()
print(dt)  # 输出：2024-07-18 00:00:00.000000
print(dt.year,dt.month,dt.day)#2024 7 18
# 格式化为字符串
formatted_date = dt.strftime('%Y-%m-%d')
print(formatted_date)  # 输出：2024-07-18
formatted_time = dt.strftime('%H:%M:%S')
print(formatted_time)  # 输出：11:06:58
formatted_datetime = dt.strftime('%Y-%m-%d %H:%M:%S')
print(formatted_datetime)  # 输出：2024-07-18 11:07:09
#字符串转换为datetime类型
dt1=datetime.strptime('2024-01-1 12:08:18','%Y-%m-%d %H:%M:%S')
print(type(dt1),dt1)#<class 'datetime.datetime'> 2024-01-01 12:08:18
print(type(formatted_datetime),formatted_datetime)#<class 'str'> 2024-07-18 11:10:55





# 创建表示一天的时间间隔
delta1 = timedelta(days=1)
print(delta1)  # 输出：1 day, 0:00:00
# 创建表示 2 小时 30 分钟的时间间隔
delta2 = timedelta(hours=2, minutes=30)
print(delta2)  # 输出：2 hours, 30 minutes
# 创建表示 10 秒的时间间隔
delta3 = timedelta(seconds=10)
print(delta3)  # 输出：10 seconds
# 创建表示 1000 微秒的时间间隔
delta4 = timedelta(microseconds=1000)
print(delta4)  # 输出：1000 microseconds

dt1 = datetime(2024, 7, 18)
dt2 = datetime(2024, 7, 19)
delta = dt2 - dt1
print(delta)  # 输出：1 day, 0:00:00

delta = timedelta(days=1, hours=2, minutes=30, seconds=45)
print(delta.days)  # 输出：1
print(delta.seconds)  # 输出：9045
print(delta.microseconds)  # 输出：0
print(delta.total_seconds())  # 输出：95445.0

# 加减 timedelta 对象
delta1 = timedelta(days=1)
delta2 = timedelta(hours=2, minutes=30)
delta3 = delta1 + delta2
print(delta3)  # 输出：1 day, 2:30:00
delta4 = delta1 - delta2
print(delta4)  # 输出：21:30:00
# 与 datetime 对象相加或相减
dt = datetime.now()
delta5 = dt + timedelta(days=1)
print(delta5)  # 输出：2024-07-19 11:24:00.830832
delta6 = dt - timedelta(hours=2)
print(delta6)  # 输出：2024-07-18 09:24:00.830832
# 比较大小
delta7 = timedelta(days=1)
delta8 = timedelta(days=2)
if delta7 < delta8:#delta7 小于 delta8
    print("delta7 小于 delta8")
else:
    print("delta7 大于或等于 delta8")
# 格式化为字符串
delta9 = timedelta(days=1, hours=2, minutes=30, seconds=45)
print(type(delta9))
