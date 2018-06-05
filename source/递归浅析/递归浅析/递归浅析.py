# 演示Python中的递归和尾递归
def fact(n):
	if n==1:
		return 1
	return n*fact(n-1)

print(fact(1))
print(fact(5))
print(fact(100))

# 如果过大 会溢出 我们采用尾递归的方式优化
def fact(n):
	return fact_iter(n,1)

def fact_iter(num,product):
	if num==1:
		return product
	return fact_iter(num-1,num*product)

print(fact(5))
# Python并没有对尾递归做优化，尾递归，一样会爆栈
