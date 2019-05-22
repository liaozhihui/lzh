# coding=utf-8
"""

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
model=svm.SVC(kernel="rbf",C=600,gamma=0.01,probability=True)
model.fit(x,y)

#新增测试样本
prob_x=np.array([
    [2,1.5],
    [8,9],
    [4.8,5.2],
    [4,4],
    [2.5,7]]
                )
#预测新增的测试样本的类别，输出测试样本的输出概率

pred_prob_y =model.predict(prob_x)

probs=model.predict_proba(prob_x)
print(probs)


grid_x,grid_y = np.meshgrid(np.linspace(l,r,n),np.linspace(b,t,n))
test_x=np.column_stack((grid_x.ravel(),grid_y.ravel()))
pred_test_y=model.predict(test_x)
grid_z=pred_test_y.reshape(grid_x.shape)


mp.figure("SVM Poly",facecolor="lightgray")
mp.title("SVM Poly",fontsize=12)

mp.pcolormesh(grid_x,grid_y,grid_z,cmap="gray")
mp.scatter(x[:,0],x[:,1],c=y,cmap='brg',s=60)

mp.scatter(prob_x[:,0],prob_x[:,1],s=88,marker="D",color="red",label="Prob Point")

mp.legend()
mp.show()