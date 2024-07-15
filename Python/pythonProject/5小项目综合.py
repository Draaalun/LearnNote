#####千年虫#####
'''
lst=[88,89,90,98,00,99]
print(lst)
# for index in range(len(lst)):
#     if str(lst[index])!='0':
#         lst[index]='19'+str(lst[index])
#     else:
#         lst[index]='200'+str(lst[index])
# print(lst)
for index,item in enumerate(lst):
    if str(item)!='0':
            lst[index]='19'+str(item)
    else:
            lst[index]='200'+str(item)
print(lst)
'''




#####模拟京东购物流程#####
'''
lst=[]
for i in range(5):
    goods=input("plz input goods' index and name enter repo(u can't input two or more info once inout):")
    lst.append(goods)
for index,item in enumerate(lst):
    print(item)
cart=[]
while True:
    flag=False
    num=input("plz input goods' num")
    for item in lst:
        if num==item[0]:
            flag=True
            cart.append(item)
            print("success add cart")
            break
    if not flag and num!="q":
        print("nothing")
    if num=="q":
        break
print('-'*50)
print("u cart",cart)
'''





#####模拟12306火车票订票#####
'''
dict_ticket=dict(G1=['bj-tj','18:06','00:33'],
                 G2=['bj-tj','19:00','00:50'],
                 G3=['bj-tj','19:19','00:59'],
                 G4=['bj-tj','19:50','00:43'],
                 G5=['bj-tj','19:55','00:23'])
print('车次   出发站-终点站   出发时间   历经时长')
for key in dict_ticket.keys():
    print(key,end="        ")
    for item in dict_ticket.get(key):
        print(item,end="     ")
    print()
print()
train_no=input("plz input index u want to buy")
info=dict_ticket.get(train_no,'nothing')
if info!="nothing":
    person=input("plz input u name:")
    s=info[0]+' '+info[1]
    print("info:"+train_no+' '+s+"\npassage:"+person)
else:
    print(info)
'''





#####模拟手机通信录#####
'''
s=set()
for i in range(5):
    print(f"plz input no.{i+1}:")
    info=input()
    s.add(info)
for item in s:
    print(item,end=" ")
'''
