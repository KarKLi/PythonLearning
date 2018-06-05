# 演示Python中的偏函数
# 和数学中的偏函数不同哈
print(int('12345'))
# int函数本身还可以提供进制转换参数，作用：把该X进制数转为10进制
print(int('12345',base=8))
print(int('12345',16))
print(int('0XFFFFFFFF',16))
# 偏函数就是一个可以改变默认值并绑定的新函数
# 和C语言中的函数替换有点类似
import functools
int2=functools.partial(int,base=2)
# 这样int2就变为了一个默认计算二进制的函数
print(int2('1000000'))
# 它一样可以改变默认参数，但是要标明默认参数的名称
print(int2('100000',base=10))
# 偏函数可以接受函数对象，args,kwargs
kw={'base':10}
print(int('100000',**kw))
max2 = functools.partial(max, 10)
print(max2(5, 6, 7))
#相当于
args=(10,5,6,7)
print(max2(*args))
#默认参数会被包含在*args的开头