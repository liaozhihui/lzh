# coding=utf-8
import numpy as np
import matplotlib.pyplot as mp
import sklearn.linear_model  as lm


x=np.array([
    [3,1],
    [2,5],
    [1,8],
    [6,4],
    [5,2],
    [3,5],
    [4,7],
    [4,-1],
])

y=np.array([0,1,1,0,0,1,1,0])

#把整个空间进行网格化拆分，通过拆分出来的每个点，根据分类模型预测每个点类别名，填充相应的颜色值,pcolormesh
l,r=x[:,0].min()-1,x[:,0].max()+1
b,t=x[:,1].min()-1,x[:,1].max()+1

n=500



grid_x,grid_y = np.meshgrid(np.linspace(l,r,n),np.linspace(b,t,n))

model = lm.LogisticRegression(solver="liblinear",C=100)
model.fit(x,y)
#整理结构变为２５万行２列的二维数组
test_x=np.column_stack((grid_x.ravel(),grid_y.ravel()))
pred_test_y=model.predict(test_x)
grid_z=pred_test_y.reshape(grid_x.shape)


mp.figure("Logistic Classification",facecolor='lightgray')
mp.title("Logistic classfication",fontsize=12)
mp.xlabel("x",fontsize=12)
mp.ylabel('y',fontsize=12)
mp.pcolormesh(grid_x,grid_y,grid_z,cmap="brg")
mp.scatter(x[:,0],x[:,1],c=y,cmap='gray',s=80)

mp.show()