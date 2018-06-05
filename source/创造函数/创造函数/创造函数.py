# 演示Python程序如何构造函数
# 定义空函数
def nop():
	pass

# pass还可用于循环中，相当于continue
# 如果参数个数不对，会自动抛出TypeError异常
def my_abs(x):
	if x>=0:
		return x
	else:
		return -x

# print(my_abs(1,2))
# 我们可以改进一下这个函数
def my_abs(x):
	if not isinstance(x,(int,float)):# isinstance函数用于判断x参数是否为一个int或者float类型的参数，如果不是的话抛出一个TypeEroor异常并有用户自己的报错信息
		raise TypeError('bad operand type')
	if x>=0:
		return x
	else:
		return -x

# print(my_abs('A'))
# 返回多值的函数
import math

def move(x,y,step,angle=0):
	nx=x+step*math.cos(angle)
	ny=y-step*math.sin(angle)
	return nx,ny

# 获得返回值

x,y=move(100,100,60,math.pi/6)
print(x,y)
# 但返回的其实是一个tuple，只是可以按位置分别给单变量赋值罢了
print(move(100,100,60,math.pi/6))
# 如果不返回任何值，可以不写，自动return None