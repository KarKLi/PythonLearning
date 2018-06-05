# 演示Python中的dict和set
# 其中dict代表字典，是一个key-value的类型数据
# 而set代表不重复集合
# 格式：d={key1:value1,key2:value2,...}
d={'Michael':95,'Bob':75,'Tracy':85}
# 上述代码建立了一个含有三个key的字典
print(d['Michael']) #此处返回key所对应的value
# key-value唯一对应，多次对一个key放不同的value会取最新的value
d['Jack']=90 #往dict里面增加新key可以直接加入key并赋值相应的value
print(d['Jack'])
d['Jack']=88
print(d['Jack'])
# 如果key不存在，抛出KeyError异常
# 避免方法：1.通过in关键字判断是否存在
if 'Thomas' in d is True:
    print('Thomas exist!')
else:
    print('no!')
# 2.通过dict提供的get()方法，分为get(key)和get(key,rtv)两种用法，
# rtv（return value）的默认值为None
print(d.get('Thomas'))
if d.get('Thomas',-1) == -1:
    print('Not exist!')
else:
    print('exist!')
# 删除key用pop方法，对应返回key对应的value
print(d.pop('Bob'))
print(d)
# 在dict中，由于key是哈希的依据，所以key要为const类型，str,int,tuple都是const类型，可以放心用作key。
# list可变，不可用于key
dc={(1,2):'Michael',(3,4):'Bob'}
print(dc)
print(dc[(1,2)])
'''
key = [1, 2, 3]
d[key] = 'a list'
'''
# set的建立示例
s=set([1,2,3])
print(s)
# 输入重复元素后，set会自动将重复元素过滤
s=set([1,1,2,2,3,3])
print(s)
# 可用add()办法添加元素
s.add(4)
print(s)
# add()的反方法是remove()
s.remove(4)
# set实际上就是数学上的集合，可以进行交并两种运算
s1=set([1,2,3])
s2=set([2,3,4])
print(s1&s2)
print(s1|s2)
# set不可以放入可变对象，下列代码会报错
'''
s3=set([[1,2],[2,3]])
print(s3)
'''