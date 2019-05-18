# coding=utf-8
import numpy as np
import sklearn.preprocessing as sp


raw_samples = np.array(['audi','ford','audi','toyota','ford','bmw','toyota','ford','audi'])
lbe=sp.LabelEncoder()
a=lbe.fit_transform(raw_samples)
print(a)
#通过数字向量获取对应的字符串向量
b=lbe.inverse_transform([0,1,1])
print(b)