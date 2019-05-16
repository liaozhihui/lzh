# coding=utf-8

import numpy as np
ary = np.arange(1,7).reshape(2,3)
print(ary,type(ary))

m = np.matrix(ary,copy=True)
ary[0,0]=999
print(ary,type(ary))
print(m,type(m))

#字符串拼块规则
ary = np.mat('1 2 3;4 5 6;7 8 9')
print(ary,ary.astype,type(ary))
print(ary * ary)
b=np.arange(1,10).reshape(3,3)
print(ary*b)
print(b.dot(b)) #和两个矩阵相乘是一样的

#测试矩阵的逆矩阵
print('-'*45)
a = np.mat('1 2 3;4 4 3;2 3 6')

print(a)
print(a.I)
print(a*a.I)
print(a.I*a)

A=np.mat('3 3.2;3.5 3.6')
B=np.mat('118.4;135.2')
# x=np.linalg.lstsq(A,B)[0]
x=np.linalg.solve(A,B)
print(x)

persons = A.I*B
print(persons)

n=32
m = np.mat('1 1;1 0')
print((m**n)[0,0])

