# 对于不可变对象来说，将其进行变换会产生一个新的副本
a='abc'
b=a.replace('a','A')
print(b)
print(a)
# 可以看到,a虽然被replace，但是a的值依然不变，因为str是一个const对象