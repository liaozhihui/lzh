# coding=utf-8
import sklearn.preprocessing as sp
import numpy as np

raw_samples = np.array([[17,100,4000],
                       [20,80,500],
                       [23,75,3500]])

bin=sp.Binarizer(threshold=80)

A=bin.transform(raw_samples)

print(A)