# 演示Python的装饰器
def now():
	print('2015-3-25')

f=now
print(f)
print(now.__name__)
print(f.__name__)
# 装饰器就是增强一个函数的功能又不修改函数的定义
# 装饰器（Decorator）是一个返回函数的高阶函数
def log(func):
	def wrapper(*args,**kw):
		print('call %s():' % func.__name__)
		return func(*args,**kw)
	return wrapper

# 借助Python的@语法调用装饰器
@log
def now():
	print('2015-3-25')

now()
#如果装饰器本身要传入参数，就需要再写一个返回decoator的高阶函数
def log(text):
	def decorator(func):
		def wrapper(*args,**kw):
			print('%s %s():' % (text,func.__name__))
			if func.__name__== 'wrapper':
				print('wrapper(*args,**kw) has been executed!')
			return func(*args,**kw)
		return wrapper
	return decorator

def now():
	print('2018-6-4')
	return 'now() has been executed'

now()
nows=log('execute')(now)
a=nows()
'''
执行步骤：
1.执行log('execute')
2.返回decorator（未被执行）
3.执行decorator(now)
4.返回wrapper()（未被执行）
5.调用nows（nows现在是wrapper）
'''
'''
正确解答：
在函数体前面用@log
和用funcs=log(para)(func)
是一个等价的意思
用后者可以避免修改函数体定义，又能够修改函数
'''
'''
总结：
当你不需要对修饰器传入参数时，语法为：
def log(func):
    def wrapper(*args,**kw):
	    # do what you want to do
		return func(*args,**kw)
	return wrapper
	
需要传入参数时，语法为：
def log(**kwargs):
    def decorator(func):
	    def wrapper(*args,**kw):
		    # do what you want to do
			return func(*args,**kw)
		return wrapper
	return decorator
'''
# 装饰器是一个比较复杂和比较难的点 要多运用
print(nows.__name__)
# hhh为什么是wrapper？
# 因为你的函数是被wrapper修饰的啊，这个nows是一个wrapper，这个wrapper干了活之后返回的func你没有捕捉
# 也捕捉不了，除非改为return func而不是return func(*args,**kw)
# 目前能捕捉的是func的返回值，也即a->func's return value
# print(a)
# 那怎么才能正确的被修饰完之后，函数签名依然是正确的呢
# 膜法来了
import functools
# 无参数的Decorator
def log(func):
	@functools.wraps(func)
	def wrapper(*args,**kw):
		print('call %s()' % func.__name__)
		return func(*args,**kw)
	return wrapper

# 有参数的Decorator
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

nows=log('execute')(now)
print(nows.__name__)
# 现在，函数签名就被bonding啦！