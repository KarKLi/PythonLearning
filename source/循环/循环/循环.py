# 演示Python中与C语言相差较大的循环结构
names=['Michael','Bob','Tracy']
for name in names:
    print(name)

sum=0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum=sum+x
print(sum)
# 可以用range(i)方法生成一个连续的list
sum=0
for x in range(101):
    sum=sum+x
print(sum)
# while循环与C语言类似，一样可以用break和continue关键字，此处不再赘述
