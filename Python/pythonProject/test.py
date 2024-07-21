# dralun818
import re
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

print(find('陈云鹏'))