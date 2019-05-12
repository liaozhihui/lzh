# coding=utf-8
import numpy as np

a = np.arange(1,10)

print(a[:-4:-1])
print(a[::3])

#针对高维的数组的切片

a = a.reshape(3,3)

print(a,a.shape)

print(a[:2:,:2:])
print(a[:2,0])