# 演示切片的威力
# 切片可用于list和tuple
L=['Michael','Sarah','Tracy','Bob','Jack']
# 取前三个元素
# 原始方法
L1=[L[0],L[1],L[2]]
print(L1)
# 切片方法（薯片超棒的QWQ）
print(L[0:3])
print(L[:3])
# 语法：x1:x2，从索引为x1，切到索引为x2（如果x1=0还可以省略x1）
# 还支持倒数切片
print(L[-2:])
print(L[-2:-1])
#还可以有这种语法：L[x1:x2:x3]，意为从x1切到x2，每x3个切一个
print(L[:10:2])
print(L[::5]) #0到0切片意为全遍历
#要获得一个list的复制，可以进行全切片
# tuple和str一样可以被切片，此处仅演示各一个例子
print((0,1,2,3,4,5)[:3])
print('ABCDEFG'[:3])