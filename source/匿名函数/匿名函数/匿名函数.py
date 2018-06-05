# 演示Python中的匿名函数
'''
匿名函数的语法：
lambda x: something about x
作用：接受一个x参数，执行一条关于x的语句并返回该语句执行完的值
'''
print(list(map(lambda x:x*x,[1,2,3,4,5,6,7,8,9])))
# 匿名函数可以防止函数名的冲突
# 它一样可以用作返回函数的值
f=lambda x:x*x
print(f)
print(f(5))
def build(x,y):
	return lambda: x*x+y*y

f1=build(3,4)
print(f1())
