# coding=utf-8
import numpy as np
from sklearn.model_selection import KFold
X=np.arange(24).reshape(12,2)
print(X)
y=np.random.choice([1,2],12,p=[0.4,0.6])
kf=KFold(n_splits=5,shuffle = False)
for train_index,test_index in kf.split(X):
    print(train_index,test_index)

print(list(range(5,2)))