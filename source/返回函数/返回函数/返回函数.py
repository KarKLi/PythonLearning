# 探究Python的返回函数

#先展示一个求和函数
def calc_sum(*args):
	ax=0
	for n in args:
		ax=ax+n
	return ax

#如果不需要直接求和，随调随用呢？
def lazy_sum(*args):
	def sum():
		ax=0
		for n in args:
			ax=ax+n
		return ax
	return sum

f=lazy_sum(1,3,5,7,9)
print(f)
print(f())
'''
闭包：在上述过程中，我们在lazy_sum里面定义了内部函数sum，返回该内部函数的时候，能将相关参数和变量均在返回函数里保存，就像一个封好的包裹一样。That's why we call it closure
'''
# 每次调用返回函数时，都是新的地址
f1=lazy_sum(1,3,5,7,9)
f2=lazy_sum(1,3,5,7,9)
print('the address of f1 is:',f1,'\n','the address of f2 is:',f2)
#返回的函数并不会立刻执行，直到调用返回函数
def count():
	fs=[]
	for i in range(1,4):
		def f():
			return i*i
		fs.append(f)
	return fs

f1,f2,f3=count()
print(f1(),f2(),f3())
#会发现全是9，是因为循环变量i一直在执行，直到被调用
#如果一定要使用循环变脸，要再创建一个函数，用参数绑定循环变量当前的值
def count():
	def f(j):
		return lambda:j*j
	fs=[]
	for i in range(1,4):
		fs.append(f(i))#立即执行，绑定该循环变量

	return fs

f1,f2,f3=count()
print(f1(),f2(),f3())
# 谨记！返回函数中不要引用任何的变化变量
