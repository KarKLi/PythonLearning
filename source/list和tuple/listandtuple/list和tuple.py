# 演示list和tuple
# 如下的classmates就是一个list，是一个有序的集合
classmates=['Michael','Bob','Tracy']
print(classmates)
# len()函数获其强度，“数据类型和变量”的代码有讲
# 可用索引访问list中的元素（其实就是把list想象成C语言中的数组）
for i in range(0,3):
	print(classmates[i])

# 如果越界了，即将上面的改为range(0,4)，则会抛出一个IndexError错误，它的下界是它的上界的相反数，即：
for i in range(-3,0):
	print(classmates[i])

# 追加元素到末尾用append()方法，删除末尾用pop()方法。如果插入指定位置，用insert(i,data)方法，删除指定位置用pop(i)方法
classmates.append('Adam')
print(classmates)
classmates.pop()
print(classmates)
classmates.insert(1,'Jack')
print(classmates)
classmates.pop(1)
print(classmates)
# 还可以用sort()方法进行排序
a=['b','g','c']
a.sort()
print(a)
# 还可以赋值给对应的索引位置（和C数组一样）
# list里面可以为任何数据，也可以为另一个list，访问list中的list使用n重数组的方法访问
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(s[2][1])

# tuple相当于const数组，一旦初始化就不能被修改。只能够读取，定义空tuple的方法：t=()，定义只有一个元素的tuple的方法：t=(1,)，以消除歧义
# print的时候，tuple会加上括号以体现其为tuple
classmates = ('Michael', 'Bob', 'Tracy')
print(classmates)
