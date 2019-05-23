# coding=utf-8
"""
网格搜索
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
model=svm.SVC(probability=True)
#基于网格搜索获取最优模型
params=[{'kernel':['linear'],'C':[1,10,100,1000]},
        {'kernel':["poly"],'C':[1],'degree':[2,3]},
        {'kernel':['rbf'],'C':[1,10,100,1000],
         'gamma':[1,0.1,0.01,0.001]}
        ]
model=ms.GridSearchCV(model,params,cv=5)
model.fit(x,y)

#网格搜索训练后的副产品
print(model.best_params_)
print(model.best_score_)
print(model.best_estimator_)
#输出网格搜索每组超参数的cv的数据
for p,s in zip(model.cv_results_['params'],model.cv_results_['mean_test_score']):
    print(p,s)

pred_y=model.predict(x)
print(sm.classification_report(y,pred_y))

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