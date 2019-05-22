# coding=utf-8
"""
交叉验证
"""
import numpy as np
import matplotlib.pyplot as mp
import sklearn.naive_bayes as nb
from sklearn.model_selection import train_test_split
import sklearn.model_selection as ms

#加载文件，读取数据

data=np.loadtxt("../ml_data/multiple1.txt",unpack=False,delimiter=',')


x=np.array(data[:,:-1])
y=np.array(data[:,-1])
print(x.shape)
print(y.shape)

#把整个空间进行网格化拆分，通过拆分出来的每个点，根据分类模型预测每个点类别名，填充相应的颜色值,pcolormesh
l,r=x[:,0].min()-1,x[:,0].max()+1
b,t=x[:,1].min()-1,x[:,1].max()+1

n=500



grid_x,grid_y = np.meshgrid(np.linspace(l,r,n),np.linspace(b,t,n))

#拆分训练集与测试集
train_x,test_x,train_y,test_y=train_test_split(x,y,test_size=0.25,random_state=7)
model = nb.GaussianNB()
#进行交叉验证，看一下模型精度，若不错在训练
ac=ms.cross_val_score(model,train_x,train_y,cv=5,scoring="accuracy")
print(ac)

pw=ms.cross_val_score(model,train_x,train_y,cv=5,scoring="precision_weighted")
print(pw)

rw=ms.cross_val_score(model,train_x,train_y,cv=5,scoring="recall_weighted")
print(rw)

model.fit(train_x,train_y)

grid_z=np.column_stack((grid_x.ravel(),grid_y.ravel()))
grid_z=model.predict(grid_z)

grid_z=grid_z.reshape(grid_x.shape)


mp.figure("NB Classification",facecolor='lightgray')
mp.title("NB classfication",fontsize=12)
mp.xlabel("x",fontsize=12)
mp.ylabel('y',fontsize=12)

mp.pcolormesh(grid_x,grid_y,grid_z,cmap="gray")
mp.scatter(test_x[:,0],test_x[:,1],c=test_y,cmap='brg',s=80)
mp.show()