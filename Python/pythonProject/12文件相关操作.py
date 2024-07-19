# dralun818
"""
创建文件

要创建一个新文件，可以使用 open() 函数。该函数接受两个参数：文件名和打开模式。打开模式指定了如何打开文件。常见的打开模式包括：

'r': 以只读模式打开文件。
'w': 以写入模式打开文件。如果文件存在，则会覆盖现有内容。
'a': 以追加模式打开文件。将新内容追加到文件末尾。
'rb': 以二进制只读模式打开文件。
'wb': 以二进制写入模式打开文件。
'ab': 以二进制追加模式打开文件。
"""
import re

# with open('test.txt', 'w') as f:
#     f.write('Hello, world!\n')
#     f.close()
"""
要读取文件的内容，可以使用 open() 函数并将其设置为只读模式。
然后，可以使用 read() 方法读取整个文件的内容，
或者使用 readline() 方法逐行读取文件的内容。
"""
with open('test.txt', 'w') as f:
    f.write('Hello, world!\n')
    f.close()
with open('test.txt', 'r') as f:
    content = f.read()
    print(content)
    f.close()
with open('test.txt', 'a+') as f:
    for i in range(10):
        f.write("this is NO."+str(i))
    f.seek(0)
    print(f.read)#f.read(),f.read(2),f.readline(),f.readline(3),f.readlines()
    #读取，读取两个字符，读取一行，读取一行中的两个字符,读取所有行且每一行为列表中一个元素
    f.close()
#使用a+可以追加和查看，f.seek使光标归零，可以查看


import os
#os.remove('test.txt')
if os.path.exists('test.txt'):
    print('File exists')
else:
    print('File does not exist')
#output:File exists
"""
要获取文件的信息，可以使用 os.stat() 函数。
该函数接受一个参数：文件名。
它返回一个包含文件信息的对象，例如文件大小、创建时间和修改时间。
os.walk(top, topdown=True, onerror=None, followlinks=False)
top: 要遍历的目录的路径。
topdown: 可选参数，默认为 True。
    如果为 True，则优先遍历 top 目录，然后遍历 top 中的每个子目录。
    如果为 False，则优先遍历 top 中的子目录，然后遍历 top 本身。
onerror: 可选参数，用于指定当遇到错误时如何处理。
    如果为 None，则会抛出异常。如果为可调用的对象，则会将错误对象传递给该对象。
followlinks: 可选参数，默认为 False。如果为 True，则会跟踪符号链接。
    如果为 False，则只会遍历实际目录。
    
os.walk() 函数返回一个生成器，该生成器会生成当前目录、子目录和文件名的元组。每个元组包含以下三个元素：
root: 当前目录的路径。
dirs: 当前目录中子目录的列表。
files: 当前目录中的文件名的列表。
"""
stat_info = os.stat('test.txt')
print(stat_info.st_size)
#15
for root, dirs, files in os.walk('.\\admin'):
    for file in files:
        print(os.path.join(root,file))

"""
join
"""
numbers = [1, 2, 3, 4, 5]
print('*'.join(str(num) for num in numbers))  # 输出：1*2*3*4*5
names = ['Alice', 'Bob', 'Charlie']
print(', '.join(names))  # 输出：Alice, Bob, Charlie
#join允许我们以指定的分隔符将序列中的元素连接成一个字符串

# 将字典中的键连接成字符串
data = {'name': 'Alice', 'age': str(30), 'city': 'New York'}
print(', '.join(data.keys()))  # 输出：name, age, city
# 将字典中的值连接成字符串
print(data.values(),data.keys())
print(';'.join(data.values()))  # 输出：Alice; 30; New York
# 将字典中的键值对连接成字符串
print(': '.join(f'{key}:{value}' for key, value in data.items()))
# 输出：name:Alice; age:30; city:New York





"""
json.loads(): This function takes a JSON string as input and returns a Python object.
json.dumps(): This function takes a Python object as input and returns a JSON string.
"""
import json
data=[
{"name":"Alice","age":30,"city":"New York"},
{"name":"Chen","age":23,"city":"New York"},
{"name":"Ding","age":24,"city":"New York"},
]
json_string = json.dumps(data)#indent增加数据缩进更美观
print(type(json_string))#<class 'str'>
print(json_string)
# result=re.findall('[a-zA-Z""]{6}:',json_string)
# print(result,type(result),result[2])
"""
[
    {
        "name": "Alice",
        "age": 30,
        "city": "New York"
    },
    {
        "name": "Chen",
        "age": 23,
        "city": "New York"
    },
    {
        "name": "Ding",
        "age": 24,
        "city": "New York"
    }
]
"""
lst2=json.loads(json_string)
print(type(lst2),lst2)
#<class 'list'> [{'name': 'Alice', 'age': 30, 'city': 'New York'}, {'name': 'Chen', 'age': 23, 'city': 'New York'}, {'name': 'Ding', 'age': 24, 'city': 'New York'}]
"""
利用json保存到文件并提取文件
"""
with open("student.txt",'w') as f:
    json.dump(data,f,indent=2)
with open("student.txt","r") as f:
    lst3=json.load(f)
    print(type(lst3))
    print(lst3)
#<class 'list'>
#[{'name': 'Alice', 'age': 30, 'city': 'New York'}, {'name': 'Chen', 'age': 23, 'city': 'New York'}, {'name': 'Ding', 'age': 24, 'city': 'New York'}]






"""

The os module in Python provides a comprehensive set of functions for interacting with the operating system. It encompasses a wide range of operations, including:

1. File and Directory Management:

Creating, renaming, deleting, and moving files and directories:

os.mkdir() - Create a directory
os.rename() - Rename a file or directory
os.remove() - Delete a file
os.rmdir() - Remove a directory
os.makedirs() - Create a directory hierarchy
os.path.join() - Join multiple path components into a single path
Checking file and directory attributes:

os.path.exists() - Check if a file or directory exists
os.path.isfile() - Check if a path points to a file
os.path.isdir() - Check if a path points to a directory
os.path.getsize() - Get the size of a file in bytes
os.path.getmtime() - Get the modification time of a file
os.path.getatime() - Get the access time of a file
os.path.getctime() - Get the creation time of a file
Getting file system information:

os.getcwd() - Get the current working directory
os.path.abspath() - Get the absolute path of a file or directory
os.path.normpath() - Normalize a path
os.path.realpath() - Get the real path of a file or directory
os.stat() - Get detailed information about a file or directory
2. Process Management:

Executing system commands and capturing their output:

os.system() - Execute a system command and wait for its completion
os.popen() - Execute a system command and return a pipe object for reading its output
os.subprocess.Popen() - Create a subprocess object for more control over execution
Running subprocesses and managing their execution:

os.subprocess.call() - Execute a subprocess and wait for its completion
os.subprocess.check_output() - Execute a subprocess and capture its output
os.subprocess.run() - Execute a subprocess with more options and control
Waiting for processes to finish or terminating them:

os.wait() - Wait for a child process to finish
os.kill() - Send a signal to a process
os.waitpid() - Wait for a specific child process to finish
3. Environment Management:

Getting and setting environment variables:

os.environ - A dictionary-like object containing environment variables
os.getenv() - Get the value of an environment variable
os.putenv() - Set the value of an environment variable
Changing the current working directory:

os.chdir() - Change the current working directory
Accessing system information, such as the hostname and platform:

os.uname() - Get system information, including hostname, platform, and release version
os.name() - Get the operating system name (e.g., 'nt' for Windows, 'posix' for Linux/macOS)
4. Error and Exception Handling:

Raising and catching exceptions related to file operations and system interactions:

FileNotFoundError - Raised when a file is not found
PermissionError - Raised when an operation requires permission that is not granted
OSError - A general error related to operating system operations
Handling errors gracefully and providing informative messages:

Use try-except blocks to handle exceptions and provide appropriate error messages
Use logging to record errors and events for debugging and monitoring
5. Platform-Specific Functionality:

Providing functions specific to the underlying operating system (Windows, Linux, macOS):

os.name() - Get the operating system name
os.path.expanduser() - Expand user-specific paths (e.g., ~/.config)
platform.system() - Get the system platform (e.g., 'Windows', 'Linux', 'Darwin')
Adapting code to different platforms using conditional execution:

Use if os.name == 'nt': or if platform.system() == 'Linux': to execute code specific to each platform
"""
