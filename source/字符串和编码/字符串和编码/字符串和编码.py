# 演示字符串和编码中的一些常用函数

# 获取一个字符的ASCII码，使用ord()函数
print(ord('你'))
# 它的反作用方法是chr()
print(chr(65))
# 可以用十六进制编码来输出字符，这里的字符代表“中文”
print('\u4e2d\u6587')
# Python对字节型数据用前缀b表示
x=b'ABC'
# str类型的数据可以通过内置的encode()方法编码为指定的字节，其默认值为UTF-8，注意：汉字不能用ascii参数转换，因为超出了ascii的范围
print('ABC'.encode('ascii'))
print('中文'.encode())
# encode()方法的反作用方法是byte类型的decode()方法
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
# 还可以采用ignore参数忽略错误字节，如果采用strict参数，就会报错
print(b'\xe4\xb8\xad\xff'.decode('utf-8',errors='ignore'))
'''
print(b'\xe4\xb8\xad\xff'.decode('utf-8',errors='strict'))
'''
# 使用len()函数来计算str长度，如果传入参数是byte类型，则计算字节数。可以通过实验得出，中文字符通过UTF-8编码后会占用三个字节（因为‘中文’字符的byte长度为6）
print(len('HelloWorld!'))
print(len('你好！'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')))
print(len('中文'.encode('utf-8')))
# 格式化字符串的方法（与C语言类似），后面用%()接你要表示的格式化变量
print( 'Hello, %s' % 'world')
print('Hi, %s, you have $%d.' % ('Michael', 1000000))
'''
常见的占位符
%x 十六进制整数
'''