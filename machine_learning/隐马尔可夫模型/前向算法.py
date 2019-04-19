# coding=utf-8
import numpy as np
Pi=np.array([[0.2,0.4,0.4]])

A=np.array([[0.5,0.2,0.3],
            [0.3,0.5,0.2],
            [0.2,0.3,0.5]])
B=np.array([[0.5,0.5],
            [0.4,0.6],
            [0.7,0.3]])
O=['红','白','红']
O=[0,1,0]
S=['盒子1','盒子2',"盒子3"]
V=["红","白"]

# a1=np.multiply(Pi,B[:,0].reshape(1,3)) #[[0.1,0.16,0.28]]  (1,3).dot()
# a2=np.multiply(np.dot(a1,A),B[:,1].reshape(1,3))
# print(a2)


def forward_(pi,A,B,O):
    a=np.multiply(pi,B[:,0].reshape(1,3))
    for i in O[1:]:
        a=np.multiply(np.dot(a,A),B[:,i].reshape(1,3))
        print(a)
    return np.sum(a)

print(forward_(Pi,A,B,O))
