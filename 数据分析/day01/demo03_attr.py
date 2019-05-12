# coding=utf-8
import numpy as np

ary = np.array([i for i in range(1,7)])

print(ary,ary.shape)

ary.shape=(2,3)
print(ary,ary.shape)

#数组元素类型

print("="*45)
print(ary,ary.dtype)

b=ary.astype('float32')
print(b,b.dtype)

#数组元素的个数

print("="*45)
print(ary,ary.size)
print(len(ary))

#数组元素的下标

print("="*45)

ary=np.arange(1,9)
ary.shape=(2,2,2)
print(ary,ary.shape)
print(ary[0][0][0]) #0页0行0列
print(ary[0,0,0]) #0页0行0列
print("="*45)
#使用for循环,ary数组中的元素遍历出来
for i in range(ary.shape[0]):
    for j in range(ary.shape[1]):

        for k in range(ary.shape[2]):
            print(ary[i][j][k])