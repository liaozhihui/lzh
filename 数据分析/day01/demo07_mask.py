# coding=utf-8
import numpy as np

a=np.arange(1,10,1)

mask=a>8
print(a[mask])

#输出100以内3或7的倍数
b=np.arange(1,100)
mask = (b%3==0) | (b%7==0)
print(mask)
print(b[mask])

#输出100以内3与7的公倍数
b=np.arange(1,100)
mask = (b%3==0) & (b%7==0)
print(mask)
print(b[mask])

#利用掩码运算对数组进行排序

p = np.array(["Mi","Apple","Huawei","Oppo"])
print(p)
r=[1,3,2,0]
print(p[r])
