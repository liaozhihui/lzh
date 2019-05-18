# coding=utf-8
import sklearn.preprocessing as sp
import numpy as np

raw_samples = np.array([[17,100,4000],
                       [20,80,500],
                       [23,75,3500]])

A=sp.normalize(raw_samples,norm='l1')

print(A)

print(A.mean(axis=0)) #每列的均值
print(A.std(axis=0)) #每列的标准差