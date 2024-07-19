def write(change):
    file=open('test.txt','w+',encoding='utf-8')
    file.write(change)
    file.close()
def read():
    file=open("test.txt",'r',encoding='utf-8')
    print(file.read())
    file.close()
if __name__ == '__main__':
    input=input('plz input string')
    write(input)
    read()