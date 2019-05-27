# coding=utf-8
import numpy as np
import matplotlib as plt

x=np.array([[1,0],[0,0],[0,1],[1,1],[1,1]])

y=np.array([[0],[0],[0],[1],[1]])

weights=np.random.normal(0,0.01,size=[2,1])

b=np.random.normal(0,0.01,size=[1])
output=np.dot(x,weights)+b
print(output)