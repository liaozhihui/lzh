# coding=utf-8
import numpy as np
import sklearn.preprocessing as sp

raw_sample=np.array([[1,3,2],
[7,5,4],
[1,8,6],
[7,3,9]])

ohe=sp.OneHotEncoder(sparse=True,dtype=int)
#fit方法意味这：训练后得到编码码表
one_dict=ohe.fit(raw_sample)
r=one_dict.transform(raw_sample)
print(r)