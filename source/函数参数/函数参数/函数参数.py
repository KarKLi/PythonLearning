# 这是一个最基本的函数
def power(x):
	return x*x

print(power(10))
# 如果要计算n次幂（默认为2次）呢
def power(x,n=2):
	s=1
	while n>0:
		n=n-1
		s=s*x
	return s

print(power(5,2))
# 当写参数的时候要注意，必选参数在前，默认参数在后，否则传入参数的时候，解释器不知道你传入的是必选参数还是想要修改默认参数。当函数有多个参数时，把变化大的参数放前面，小的放后面，小的可以作为默认参数
def enroll(name,gender,age=6,city='Beijing'):
	print('name=',name)
	print('gender=',gender)
	print('age=',age)
	print('city=',city)
	return ''

print(enroll('Sarah','F'))
# 如果不按顺序提供默认参数，必须把默认参数的参数名写上
print(enroll('Bob','M',7))
print(enroll('Adam','M',city='Tianjin'))
# 默认参数的易错点（默认参数要指向不变对象）
def add_end(L=[]):
	L.append('END')
	return L
# 当调用两次add_end的时候，得出来的L会有两个'END'
print(add_end())
print(add_end())
# 原因：Python定义函数的时候，默认参数L的值已经被计算，也就是内存中已经存在了L，每次调用这个函数，如果改变了L（假设第一次调用后），就等价于：
'''
def add_end(L=['END']):
    L.append('END')
	return L

'''
# 因此要指向不变对象的方法
def add_end(L=None):
	if L is None:
		L=[]
	L.append('END')
	return L

# 这样就解决了重复添加的问题
# 接下来演示可变参数
def calc(*numbers):
	sum=0
	for n in numbers:
		sum = sum+n*n
	return sum

print(calc(1,2))
# 如果要传入list或者tuple到接受可变参数的函数里怎么办呢
# 有两种方法
nums=[1,2,3]
print(calc(nums[0],nums[1],nums[2]))
# 好麻烦！
print(calc(*nums))
# 关键字参数就是允许你传入0个或者任意个含参数名的的参数，它们会自动组装成为一个dict
def person(name,age,**kw):
	print('name:',name,'age:',age,'other:',kw)

# 用法演示
person('Michael',30)
person('bob',35,city='Beijing')
person('Adam',45,gender='M',job='Engineer')
# 还可以先组装出一个dict，再传进去
extra={'city':'Beijing','job':'Engineer'}
person('Jack',24,city=extra['city'],job=extra['job'])
# 可以简化成为
person('Jack',24,**extra)
# 可以通过kw检查关键字参数的传入情况
def person(name,age,**kw):
	if 'city' in kw:
		pass
	if 'job' in kw:
		pass
	print('name:',name,'age:',age,'other:',kw)

person('Jack',24,city='Beijing',addr='Chaoyang',zipcode=123456)
# 如果要限制关键字参数的名字，就用命名关键字参数
# *号后面的所有参数均为命名关键字参数
def person(name,age,*,city,job):
	print(name,age,city,job)

person('Jack',24,city='Beijing',job='Engineer')
#命名关键字参数可以有缺省值，传入的时候可以不传入city参数
def person(name,age,*,city='Beijing',job):
	print(name,age,city,job)

person('Jack',24,job='Engineer')
# 参数的顺序：必选参数，默认参数，可变参数，命名关键字参数和关键字参数
def f1(a,b,c=0,*args,**kw):
	print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)

def f2(a,b,c=0,*,d,**kw):
	print('a=',a,'b=',b,'c=',c,'d=',d,'kw=',kw)

# 调用的时候自动按照参数位置和参数名把对应的参数传进去
f1(1,2,3,'a','b',x=99)
args=(1,2,3,4)
kw={'d':99,'x':'#'}
f1(*args,**kw)
args=(1,2,3)
kw={'d':88,'x':'#'}
f2(*args,**kw)
