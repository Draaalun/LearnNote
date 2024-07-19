# dralun818
"""
面向过程：功能上的封装 面向对象编程以对象为基本单元，
    将问题分解成一个个相互协作的对象，每个对象都具有自己的属性和方法，并封装了数据和行为。
面向对象：属性和行为上的封装 面向过程编程以过程为基本单元，
    将问题分解成一个个步骤，通过顺序执行这些步骤来完成任务。

类定义了对象的属性和方法。
对象是类的实例，它拥有类定义的属性和方法。
通过定义类，我们可以创建多个具有相同属性和方法的对象。

class 类名:
  属性定义
  方法定义
"""
#类属性，属性用于描述对象的特征或状态。
# 属性可以用变量来表示。在类中定义属性时，需要使用 = 语句来赋值。
class Person:
  name = "小明"  # 定义属性 name，并赋值为 "小明"
  age = 18  # 定义属性 age，并赋值为 18
print(Person.age,Person.name)#18 小明
Person.age=20
print(Person.age)#20

#类方法，方法用于定义对象的的行为。方法可以用函数来表示。
# 在类中定义方法时，需要使用 def 语句。
# 方法的第一个参数通常是 self，它表示当前实例对象。
class Person:
  school="NO.1 middle school"#类属性
  def __init__(self, name, age):  # 初始化方法
    self.name = name#self.name和self.age都是实例属性，name和age都是局部变量
    self.age = age
  def say_hello(self):  # 实例方法
    print(f"我的名字是{self.name}，今年{self.age}岁。")
  @staticmethod#静态方法
  def sm():
    print("这是一个静态方法，不能调用实例属性和实例方法")
  @classmethod#类方法
  def cm(cls):
    print("这是一个类方法，不能调用实例属性和实例方法")

#创建对象
p1 = Person("小明", 18)  # 创建 Person 类的实例 p1
p2 = Person("小红", 19)  # 创建 Person 类的实例 p2

#访问属性和方法，
print(p1.name)  # 输出：小明
print(p2.age)  # 输出：19
p1.say_hello()  # 输出：我的名字是小明，今年18岁。
p2.say_hello()  # 输出：我的名字是小红，今年19岁。

#类变量，类变量是属于整个类的变量，而不是属于单个实例的变量。类变量可以使用 类名.变量名 语句来访问。
class Person:
  count = 0  # 定义类变量 count
  def __init__(self, name, age):
    self.name = name
    self.age = age
    Person.count += 1  # 在初始化方法中，将 count 的值加 1
p1 = Person("小明", 18)
p2 = Person("小红", 19)
print(Person.count)  # 输出：2





#####创建一个类有四个对象并放在列表中可以遍历#####
class student:
  school="Qi lu middle school"
  def __init__(self,name,age,grade):
    self.name=name
    self.age=age
    self.grade=grade
  def introduction(self):
    print(f"my name is {self.name},my grade is {self.grade}")
stu1=student('chen',18,12)
stu2=student('zhang',17,11)
stu3=student('li',16,10)
stu4=student('liu',17,12)

lst=[stu4,stu2,stu3,stu1]
for i in lst:
  i.introduction()





#####动态绑定属性和方法#####
"""
每个对象的属性名相同但是属性值又不同
可以单独的为某个对象绑定独有的属性和方法
"""
stu5=student('ding',18,11)
stu6=student('liu',17,12)
stu6.gender="man"#动态绑定属性
print(stu6.name,stu6.gender)#gender为stu6独有的一个属性
def addmethod():#动态绑定方法
  print("add a method")
stu6.addmethod=addmethod#函数的赋值
stu6.addmethod()#output:add a method





#####封装、继承和多态#####
"""
封装将对象的属性和方法隐藏起来，只提供对外访问的接口。封装的目的是提高代码的可维护性和安全性。
self.__name=name#私有，只能本类访问
self._name=name#受保护，只能本类和子类访问
self.name=name#普通实例属性，类内部外部以及子类都可以访问
（方法也同上）
"""
class Person:
  def __init__(self, name, age,gender):
    self.__name = name  # 将 name 属性变为私有成员
    self.__age = age
    self.gender=gender
  def name(self):  # 提供获取 name 属性的接口
    return self.__name
  def set_name__(self, name):
    self.__name=name
  @property
  def age(self):
    return self.__age
  @age.setter
  def age(self,age):
    self.__age=age
per=Person("chen",18,'man')
print(per.age,per.name(),per.gender)#18 chen man
#加上@property可以想普通实例属性一样直接访问呢，否则采用类内函数进行调用
per.set_name__("zhang")
per.age=15
per.gender='women'
print(per.name(),per.age,per.gender)#zhang 15 women





#####property使用方法#####
#隐藏了部分属性，限制了属性的修改
import math
class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height
  @property
  def area(self):
    return self.width * self.height
  @area.setter
  def area(self, new_area):
    if new_area <= 0:
      raise ValueError("Area must be a positive number")
    # Calculate the new width and height
    self.width = math.sqrt(new_area )
    self.height =self.width
rectangle = Rectangle(5, 3)
print(rectangle.area)  # Output: 15.0
rectangle.area = 25
print(rectangle.width)  # Output: 5.0
print(rectangle.height)  # Output: 5.0





"""
继承，一个类可以继承自另一个类，从而获得被继承类的属性和方法。
子类可以覆盖基类的方法，也可以添加新的方法。
"""
class Animal:
  def __init__(self,name):
      self.name=name
  def speak(self):
    print("@#$")
class Cat(Animal):
  def __init__(self,name):
    super().__init__(name)
  def cat_speak(self):
    print("喵喵喵")
class Dog(Animal):
  def __init__(self,name,stuno):
    super().__init__(name)#继承之前的实例属性
    self.stuno =stuno#自己独有的实例属性
  def dog_speak(self):
    print("汪汪汪")
dog=Dog('1','2')
an=Animal('3')
print(dog.name,dog.stuno,an.name)#1 2 3
dog.dog_speak()#汪汪汪
dog.speak()#@#$#父类的共有的方法可以使用
#注意：可以继承多个父类
class father1:
  def __init__(self,name):
    self.name=name
  def show1(self):
    print("this is no.1")
class father2:
  def __init__(self,age,age1):
    self.age=age
    self.age1=age1
  def show2(self):
    print("this is no.2")

class son(father1,father2):
  def __init__(self,name,age,age1,gender):
    father1.__init__(self,name)
    father2.__init__(self,age,age1)
    self.gender=gender
  def show1(self):
    super().show1()
    print("come from father1")
  def show2(self):
    super().show2()
    print("come from father2")
s=son('chen',18,15,'man')
s.show1(),s.show2()
"""
this is no.1
come from father1
this is no.2
come from father2
"""





#####多态#####
class person:
  def eat(self):
    print("eat !!!")
class cat:
  def eat(self):
    print("eat fish")
class dog:
  def eat(self):
    print("eat bonus")
def fun(obj):#obj是函数的形式参数
  obj.eat()#通过变量obj（对象）调用eat方法
per=person()
dog1=dog()
cat1=cat()
#不关心对象的数据类型，只关心对象是否具有同名的方法
fun(cat1)
fun(dog1)
fun(per)
"""
eat fish
eat bonus
eat !!!
"""





#####object类#####
"""
object 类是所有其他类的基类。
这意味着 Python 中的所有类，包括内置类和用户定义类，都继承自 object 类。
主要方法：
__str__()：此方法返回对象的字符串表示形式。当您打印对象时，会调用 __str__() 方法来生成要打印的字符串。
__repr__()：此方法返回对象的更详细的字符串表示形式。__repr__() 方法通常用于调试目的。（用法同str）
__eq__()：此方法比较两个对象的相等性。如果两个对象被认为相等，则 __eq__() 方法应返回 True，否则返回 False。
__ne__()：此方法比较两个对象的非相等性。如果两个对象被认为不相等，则 __ne__() 方法应返回 True，否则返回 False。
__hash__()：此方法返回对象的哈希值。哈希值用于标识集合中的对象，例如字典和集合。
__del__()：此方法在销毁对象时调用。__del__() 方法可用于清理与对象关联的资源。
"""
class person_obj:
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def show(self):
    print(f"hello my name is {self.name},my age is {self.age}")
  def __str__(self):
    return "return "
per_obj=person_obj("chen",20)
print(per_obj)#return，如果不加__str返回是<__main__.person_obj object at 0x000001E754931E50>
print(per_obj.__dict__)#{'name': 'chen', 'age': 20}
print(per_obj.__class__)#<class '__main__.person_obj'>
print(son.__bases__)#(<class '__main__.father1'>, <class '__main__.father2'>)





#####类的深拷贝和浅拷贝#####
'''
深拷贝会创建一个新的对象，该对象包含原始对象的副本，以及该对象的所有子对象的副本。
这意味着新对象与原始对象完全独立，对新对象的任何更改都不会影响原始对象。
深拷贝通常使用递归算法来实现。对于可变类型（例如列表、字典、集合），
深拷贝会创建新的内存空间来存储子对象的副本。对于不可变类型（例如字符串、整数、浮点数），
深拷贝会直接创建原始对象的副本。

浅拷贝会创建一个新的对象，该对象指向原始对象的内存空间。
这意味着新对象与原始对象共享部分或全部内存空间。对新对象的任何更改都会影响原始对象。
浅拷贝通常通过简单的赋值操作来实现。
对于可变类型，浅拷贝会创建一个新的引用，指向原始对象的内存空间。
对于不可变类型，浅拷贝会直接创建原始对象的引用。
'''
class CPU:
  pass
class Disk:
  pass
class Computer:
  def __init__(self,cpu,dick):
    self.cpu=cpu
    self.dick=dick

cpu=CPU()
dick=Disk()
com=Computer(cpu,dick)
com1=com
print(com,com.cpu,com.dick)
#<__main__.Computer object at 0x0000024286DC2C00>
# <__main__.CPU object at 0x0000024286DC2BA0>
# <__main__.Disk object at 0x0000024286DC2BD0>
print(com1,com1.cpu,com1.dick)
#<__main__.Computer object at 0x0000024286DC2C00>
# <__main__.CPU object at 0x0000024286DC2BA0>
# <__main__.Disk object at 0x0000024286DC2BD0>
"""
以上操作为对象的赋值，相当于com和com1指向同一个值
"""

import copy
com2=copy.copy(com)
print(com,com.cpu,com.dick)
#<__main__.Computer object at 0x0000021619422F60>
# <__main__.CPU object at 0x0000021619422F00>
# <__main__.Disk object at 0x0000021619422F30>
print(com2,com2.cpu,com2.dick)
#<__main__.Computer object at 0x00000216194231D0>
# <__main__.CPU object at 0x0000021619422F00>
# <__main__.Disk object at 0x0000021619422F30>
"""
以上为浅拷贝
以上子对象地址完全相同，只是产生了一个com2对象，但子对象指向不变
"""

com3=copy.deepcopy(com)
print(com,com.cpu,com.dick)
#<__main__.Computer object at 0x0000017E910A32C0>
# <__main__.CPU object at 0x0000017E910A3260>
# <__main__.Disk object at 0x0000017E910A3290>
print(com3,com3.cpu,com3.dick)
#<__main__.Computer object at 0x0000017E910A8FE0>
# <__main__.CPU object at 0x0000017E910A90A0>
# <__main__.Disk object at 0x0000017E910A9100>
"""
以上为深拷贝
所有的地址都会发生变换
"""
