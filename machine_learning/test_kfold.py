# coding=utf-8
import numpy as np
# from sklearn.model_selection import KFold
from sklearn.cross_validation import KFold
X=np.arange(24).reshape(12,2)
print(X)
y=np.random.choice([1,2],12,p=[0.4,0.6])
kf=KFold(len(y),5,shuffle = False)
# for train_index,test_index in kf.split(X):
#     print(train_index,test_index)

for iteration, indices in enumerate(kf,start=1):
    print(iteration,indices)