# dralun818
"""
try:
    # 可能引发异常的代码
except Exception as e:
    # 在此处处理异常

try 块： try 块包含您怀疑可能引发异常的代码。它是您执行可能存在风险的代码的地方。
except 块： except 块紧跟在 try 块之后，用于处理 try 块中发生的异常。它包含一个或多个异常处理程序，每个处理程序由一个 except 子句指定。
Exception as e： Exception 是一个通用的异常类，可以捕获所有类型的异常。as e 部分将异常对象分配给变量 e，允许您访问有关异常的信息。

try:
    # 以读模式打开文件
    file = open("myfile.txt", "r")
    # 读取文件内容
    content = file.read()
    # 将内容转换为整数
    number = int(content)
    # 打印数字
    print(number)
except FileNotFoundError as e:
    # 处理FileNotFoundError异常
    print("文件未找到：", e.filename)
except ValueError as e:
    # 处理ValueError异常
    print("无效输入：", e.args[0])
finally:
    # 关闭文件（可选）
    if file:
        file.close()
"""






"""
raise [Exception]([reason])
raise 语句用于在程序中手动引发异常。它允许您在特定条件下或遇到错误时显式地停止程序执行并抛出异常。

Exception：可选参数，用于指定要引发的异常类型。如果省略，则会引发当前上下文中捕获的异常（例如在 except 块中）。
reason：可选参数，用于提供有关异常的描述信息。

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    else:
        return x / y
try:
    result = divide(10, 0)
except ValueError as e:
    print("Error:", e.args[0])

"""
try:
    gender=input("plz input u gender")
    if gender!="man" or "women":
        raise Exception ("gender only is man or women")
    else:
        print("u gender is :",gender)
except Exception as e:
    print(e)
#plz input u gender7
#gender only is man or women
"""
常见的异常类型：
BaseException： 所有异常的基类。它没有提供任何其他信息或功能。

Exception： 常规错误的基类。它代表由程序逻辑错误或意外条件引起的异常。

StandardError： 所有内建标准异常的基类。它包含以下子类：

        IOError： 输入/输出操作失败，如文件打开失败。
        ImportError： 无法导入模块或对象，主要是路径有误或名称错误。
        OSError： 操作系统相关错误。
        ArithmeticError： 所有数值计算错误的基类。
        ZeroDivisionError： 除以零。
        OverflowError： 结果超出最大值。
        FloatingPointError： 浮点数运算错误。
        SyntaxError： Python 语法错误。
        SystemExit： 使用 sys.exit() 函数退出程序。
        KeyboardInterrupt： 当在键盘上按住Ctrl+C 时会触发该异常。
        TypeError： 操作的对象类型不正确。

NameError： 访问一个未声明的变量。

KeyError： 访问字典里不存在的键。

IndexError： 索引超出列表或字符串的范围。

ValueError： 传递给函数或方法的参数无效。

AssertionError： 断言语句失败。

MemoryError： 内存不足。

EOFError： 到了文件的尾部了。

UnicodeError： 处理 Unicode 字符时出现错误。

ContextMenuManagerError： 上下文管理器错误。
"""





"""
设置断点
debug
"""