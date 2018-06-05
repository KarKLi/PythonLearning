# 演示Python中的函数式编程的一种方式：高阶函数
# 高阶函数称为higher-order function，指函数可以作为变量进行传递
f=abs
print(f)
print(f(10))
#一个最简单的高阶函数：
def add(x,y,f):
	return f(x)+f(y)

print(add(-3,4,f))
# 下列介绍三种内置的高阶函数
'''
map/reduce
map()函数接受两个参数，一个是函数，一个是Iterable。
map将传入的函数作用于Iterable的每个元素上，将结果作为新的Iterator返回
'''
def f(x):
	return x*x

r=map(f,[1,2,3,4,5,6,7,8,9,10])
# r是一个惰性序列，可以用list让它返回一个list
print(list(r))
print(list(map(str,[1,2,3,4,5,6,7,8,9])))
# reduce()就是……有点像秦九韶序列，又有点像递归
# 可以这么想：
'''
def f(x1):
    if x1<100:
	    return f(f(x1))
'''
#差不多就这意思吧
from functools import reduce
def add(x,y):
	return x+y
#哦对了！Python不能重载函数！
print(reduce(add,[1,3,5,7,9]))
#比如说我们要把一个序列变成整数
def fn(x,y):
	return x*10+y

print(reduce(fn,[1,3,5,7,9]))
#我们可以利用map来设计一个str转换为int的函数
def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]

print(reduce(fn,map(char2num,'13579')))
#还可以使用奇怪的lambda表达式
def str2int(s):
	return reduce(lambda x,y:x*10+y,map(char2num,s))
print(str2int('12345'))

# filter()，顾名思义就是拿来进行序列过滤的高阶函数
def is_odd(n):
	return n%2==1

print(list(filter(is_odd,[1,2,4,5,6,9,10,15])))
'''
语法：filter(function,Iterable)
返回一个function作用下的Iterable为true的对象的惰性序列，也即筛出符合function下的Object
'''
def not_empty(s):
	return s and s.strip()

print(list(filter(not_empty,['A','','B',None,'C',' '])))
#用filter实现埃氏筛
#构建奇数数列
def _odd_iter():
	n=1
	while True:
		n=n+2
		yield n

def _not_divisible(n):
	return lambda x:x%n>0

def primes():
	yield 2
	it=_odd_iter()
	while True:
		n=next(it) #返回第二个素数（第一个素数是2）
		yield n
		it=filter(_not_divisible(n),it)

'''
for n in primes():
	if n<1000:
		print(n)
	else:
		break
'''

'''
sorted()高阶函数——
语法：sorted(Iterable object,function)
作用：根据function规则下的Iterable object排序
返回值：一个惰性序列(generator)
'''
print(sorted([36,5,-12,9,-21]))
#默认规则为升序
#参见C++中的STL中的sort重载，可接受lambda匿名函数那个和可接受函数指针那个
print(sorted([36,5,-12,9,-21],key=abs))
#字符串排序（根据ASCII升序），大写字母的ASCII码在前
print(sorted(['bob','about','Zoo','Credit']))
#忽略大小写
print(sorted(['bob','about','Zoo','Credit'],key=str.lower))
#原理就是全小写嘛
#反向排序用参数reverse的真假位判断
print(sorted(['bob','about','Zoo','Credit'],key=str.lower,reverse=True))