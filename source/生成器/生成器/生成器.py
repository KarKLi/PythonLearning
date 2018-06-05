# 演示Python中的generator
# 概述：generator相当于一种动态数组，遵循着“用时生成”原则，由数组规则约束，而动态生成数据
# 语法：把语法生成式的方括号换为括号
L=[x*x for x in range(10)]
print(L)
g=(x*x for x in range(10))
print(g)
#我们可以看到，print(g)得到的是其地址
#通过next(g)得到下一个返回值
for x in range(10):
	print(next(g))
print(g)
# 或者：
g=(x*x for x in range(10))
for n in g:
	print(n)

# 用函数打印斐波那契数列：
def fib(max):
	n,a,b=0,0,1
	while n<max:
		print(b)
		a,b=b,a+b
		n=n+1
	return 'done'

print(fib(6))
#下列介绍 yield关键字，一个函数里一旦有yield，那它就不是一个普通函数，是一个generator
def fib2(max):
	n,a,b=0,0,1
	while n<max:
		yield b
		a,b=b,a+b
		n=n+1
	return 'done'

f=fib2(6)
print(f)
# 每次调用next(f)的时候，都从yield语句继续进行
for n in f:
	print(n)

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

o=odd()
print(next(o))
print(next(o))
print(next(o))
# 当yield执行完再调用next就会报错
# print(next(o))
# 我们基本不用next()方法，太麻烦了
for n in fib2(6):
	print(n)
#但是捕获不到'done'
#所以必须捕获StopIteration异常
g=fib2(6)
while True:
	try:
		x=next(g)
		print('g:',x)
	except StopIteration as e:
		print('Generation return value:',e.value)
		break