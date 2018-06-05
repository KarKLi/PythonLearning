# 演示Python中的迭代
# dict迭代
d={'a':1,'b':2,'c':3}
for key in d:
	print(key)
# 默认迭代的是key
for value in d.values():
	print(value)

#同时迭代 key,value
for k,v in d.items():
	print(k,' ',v)

#迭代str
for ch in 'ABC':
	print(ch)

from collections import Iterable
print(isinstance('abc',Iterable)) #使用isinstance来判断是否可迭代
print(isinstance([1,2,3],Iterable))
print(isinstance(123,Iterable))
# enumerate函数可以将一个list编程索引-元素对
for i,value in enumerate(['A','B','C']):
	print(i,value)