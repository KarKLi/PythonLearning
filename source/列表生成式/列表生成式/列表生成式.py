# 演示Python中的List Comprenhensions
# 生成一个从1迭代到10的list
a=list(range(1,11))
print(a)
#生成1-10的阶乘list
L=[]
for x in range(1,11):
	L.append(x*x)

print(L)
L=[x*x for x in range(1,11)]
print(L)
# 还可以在后面跟上判断
L=[x*x for x in range(1,11) if x%2==0]
print(L)
# 还可以用两层循环生成全排列
print([m+n for m in 'ABC' for n in 'XYZ'])
# 运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：
import os
print([d for d in os.listdir('.')])
# 还可以用两个变量生成一个list
d={'x':'A','y':'B','z':'C'}
print([k + '=' + v for k,v in d.items()])
#把字符串变成小写
L=['Hello','world','IBM','Apple']
print([s.lower() for s in L])
#小结：
'''
语法：[ expection for a in b if condition]
返回expection修饰过的在b里面的符合condition的a
'''
# 最后扩充一下isinstance函数的用法
L = ['Hello', 'World', 18, 'Apple', None]
# print([s.lower() for s in L])
print([s.lower() for s in L if isinstance(s,str)])
# s.lower()把字符串s变为小写
