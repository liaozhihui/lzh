# coding=utf-8
import numpy as np
theta = np.array([[1],
                  [2],
                  [3]])#(3,1)
X=np.array([[1,1,1,1],     #(3,4)
            [2,2,2,1],
            [3,3,3,1]
                    ])
print(X.sum(axis=0),X)