# coding=utf-8
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy.random
import time



path='data'+os.sep+'LogiReg_data.txt'
pdData=pd.read_csv(path,header=None,names=['Exam1','Exam2','Admitted'])
# print(pdData.head())
# print(pdData.shape)
positive=pdData[pdData['Admitted']==1]
negative=pdData[pdData['Admitted']==0]

fig,ax=plt.subplots(figsize=(10,5))

ax.scatter(positive['Exam1'],positive['Exam2'],s=30,\
           c='b',marker='o',label='Admitted')
ax.scatter(negative['Exam1'],negative['Exam2'],s=30,\
           c='r',marker='x',label='Not Admitted')
ax.legend()
ax.set_xlabel('Exam1 Score')
ax.set_ylabel("Exam2 Score")
# plt.show()

def sigmoid(x):
    return 1/(1+np.exp(-x))

# nums = np.arange(-10,10,step=1)
# fig,ax=plt.subplots(figsize=(12,4))
# ax.plot(nums,sigmoid(nums),'r')
# plt.show()

def model(X,theta):
    return sigmoid(np.dot(X,theta.T))

pdData.insert(0,"Ones",1)
orig_data=pdData.as_matrix()
cols=orig_data.shape[1]
X=orig_data[:,0:cols-1]
y=orig_data[:,cols-1:cols]
theta=np.zeros([1,3])

def cost(X,y,theta):
    left = np.multiply(-y,np.log(model(X,theta)))
    right = np.multiply(1-y, np.log(1-model(X, theta)))
    return np.sum(left-right)/len(X)

# print(cost(X,y,theta))

def gradient(X,y,theta):

    result=y-model(X,theta) #shape(m,1)
    print(result.shape)
    result=np.multiply(result,X)  #shape(m,n) m个样本,n个feature
    return -result.sum(axis=0)/len(X)


def gradient1(X, y, theta):
    grad = np.zeros(theta.shape)
    error = (model(X, theta) - y).ravel()
    for j in range(len(theta.ravel())):  # for each parmeter
        term = np.multiply(error, X[:, j])
        grad[0, j] = np.sum(term) / len(X)

    return grad

STOP_ITER = 0
STOP_COST = 1
STOP_GRAD = 2

def stopCriterion(type, value, threshold):
    #设定三种不同的停止策略
    if type == STOP_ITER:        return value > threshold
    elif type == STOP_COST:      return abs(value[-1]-value[-2]) < threshold
    elif type == STOP_GRAD:      return np.linalg.norm(value) < threshold

def shuffleData(data):
    np.random.shuffle(data)
    cols = data.shape[1]
    X = data[:, 0:cols - 1]
    y = data[:, cols - 1:]
    return X, y

def descent(data,theta,batchSize,stopType,thresh,alpha):
    init_time = time.time()
    i = 0 #迭代次数
    k = 0 #batch
    X,y = shuffleData(data)
    grad = np.zeros(theta.shape) #计算梯度
    costs = [cost(X,y,theta)]   #损失值
    while True:
        grad = gradient(X[k:k+batchSize],y[k:k+batchSize],theta)
        k += batchSize #去batch数量个数
        if k>=len(X):
            k=0
            X,y=shuffleData(data)
        theta=theta - alpha*grad
        costs.append(cost(X,y,theta))
        i+=1
        if stopType == STOP_ITER:
            value = i
        elif stopType == STOP_COST:
            value = costs
        elif stopType == STOP_GRAD:
            value = grad
        if stopCriterion(stopType, value, thresh): break
    return theta,i-1,costs,grad,time.time()-init_time

