# coding=utf-8
"""
多项式核函数
"""
import numpy as np
import sklearn.model_selection as ms
import sklearn.svm as svm
import sklearn.metrics as sm
import matplotlib.pyplot as mp

data = np.loadtxt("../ml_data/multiple2.txt",unpack=False,delimiter=',')

x=data[:,:-1]
y=data[:,-1]

l,r=x[:,0].min()-1,x[:,0].max()+1
b,t=x[:,1].min()-1,x[:,1].max()+1

n=500

#基于SVM实现分类
model=svm.SVC(kernel="poly",degree=2)
model.fit(x,y)

grid_x,grid_y = np.meshgrid(np.linspace(l,r,n),np.linspace(b,t,n))
test_x=np.column_stack((grid_x.ravel(),grid_y.ravel()))
pred_test_y=model.predict(test_x)
grid_z=pred_test_y.reshape(grid_x.shape)


mp.figure("SVM Poly",facecolor="lightgray")
mp.title("SVM Poly",fontsize=12)

mp.pcolormesh(grid_x,grid_y,grid_z,cmap="gray")
mp.scatter(x[:,0],x[:,1],c=y,cmap='brg',s=60)

mp.legend()
mp.show()