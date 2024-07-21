import re

def input_sth(input):
    with open("test.txt","a+") as f:
        print("您的本次输入为:",input)
        f.write(input)
        f.write('\n')
def num_total():
    with open("test.txt",'r+') as f:
        count = 0
        lst1=[]
        for line in f:
            lst1.append(line)
            count += 1
        return count,lst1
def find(name):
    find_result=""
    with open("test.txt",'r') as f:
        for line in f:
            if re.match(f'{name},[0-9]*',line):
                find_result=line
                break
    if find_result:
        return find_result
    else:
        find_resul="匹配失败"
        return find_resul

class person():
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def set_name(self,name):
        self.__name=name
    def get_name(self):
        return self.__name
    def set_age(self,age):
        self.__age=age
    def get_age(self):
        return self.__age

lst=[]
verify_code=0
err_num=0
while verify_code==0:
    name_age=input("请输入姓名和年龄,使用逗号间隔开,输入0选择退出")
    if name_age=='0':
        verify_code=1
    else:
        if not (re.match('[\u4E00-\u9FFF]*，[0-9]{1,}',name_age)):
            print("输入格式有误请自行检查后输入！")
            err_num+=1
            if err_num==3:
                print("您已错误三次！err")
                break
            continue
        lst_temp=name_age.split('，')
        input_sth(",".join(lst_temp))
        err_num=0
count,lst=num_total()
print(f"总共有{count}人")

lst_person=[]
for index,item in enumerate(lst):
    lst_temp=item.split(',')
    # print(lst_temp)
    # print(lst_temp[0],lst_temp[1],type(lst_temp[0]),type(lst_temp[1]))
    lst_person.append(person(lst_temp[0],eval(lst_temp[1])))
lst_person.sort(key=lambda person:person.get_age(),reverse=True)

for index,item in enumerate(lst_person,start=1):
    print('NO',index,item.get_name(),'age is',item.get_age())
#lst_person 用了类来存储和查找

find_obj=input("请输入你要查找的名字：")
print(find(find_obj))




#####下面使用字典
lst_dic=[]
for index,item in enumerate(lst_person,start=1):
    dic_temp={'name':f'{item.get_name()}','age':eval(f'{item.get_age()}')}
    # print('NO',index,item.get_name(),'age is',item.get_age())
    # print(dic_temp)
    lst_dic.append(dic_temp)
# print(lst_dic)
def find_dic(name):
    find_result=""
    for index,item in enumerate(lst_dic):
        if item.get('name')==name:
            find_result=item.get('name')+','+str(item.get('age'))
    if find_result:
        return find_result
    else:
        find_result="字典查找失败"
        return find_result
print(find_dic("陈云鹏"))


