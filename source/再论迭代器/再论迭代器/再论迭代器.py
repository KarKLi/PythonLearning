# 我们之前已经接触过迭代，也使用过了isinstance()方法来判断一个对象是否能迭代
# 那么现在我们来深究迭代器
# 先介绍isinstance()方法的用法
from collections import Iterable
print(isinstance([],Iterable))
print(isinstance({},Iterable))
print(isinstance('abc',Iterable))
print(isinstance((x for x in range(10)),Iterable))
print(isinstance(100,Iterable))
#请牢记一件事 可Iterable的对象未必为Iterator
#下面会讲Iterator的定义
#可以被next()方法调用并返回下一个值的对象称为 Iterator
# 可以使用isinstance()判断一个对象是否是Iterator对象：
from collections import Iterator
print(isinstance((x for x in range(10)),Iterator))
print(isinstance([],Iterator))
print(isinstance({},Iterator))
print(isinstance('abc',Iterator))
#生成器都是Iterator对象，list、dict、str Iterable，但不是Iterator
#要变成Iterator要用iter()函数
print(isinstance(iter([]),Iterator))
print(isinstance(iter('abc'),Iterator))
#Iterator指惰性序列，遵循“需要才计算”原理