# 本脚本演示Python的函数特性
print(abs(12.34)) #单一参数函数
print(max(1,2,3,4,5)) #多参数函数
# print(abs('a')) 这句话会报出TypeError的错误
# 内置的类型转换函数
# int()可以将其他数据类型转换为整数，其它的同理
print(int('123'))
print(int(12.34))
print(float('12,34'))
print(str(1.23))
print(str(100))
print(bool(1))
print(bool(''))
# 函数的别名用法
a=abs
print(a(-1))
# 有点函数指针的味道