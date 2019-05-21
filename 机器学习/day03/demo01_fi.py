# coding=utf-8
"""
特征重要性
"""
import sklearn.datasets as sd
import sklearn.utils as su
from sklearn.model_selection import train_test_split
import sklearn.metrics as sm
import sklearn.tree as st
import sklearn.ensemble as se
import matplotlib.pyplot as mp
import numpy as np


#加载数据
boston=sd.load_boston()
names = boston.feature_names
#打乱原始数据集，划分训练集与测试集
#当随机种子相同时得到的随机序列也相同
x,y = su.shuffle(boston.data,boston.target,random_state=7)
train_size = int(len(x)*0.8)

# train_x,test_x,train_y,test_y=x[:train_size],x[train_size:],y[:train_size],y[train_size:]
train_x,test_x,train_y,test_y=train_test_split(x,y,test_size=0.2,random_state=10)

tree = st.DecisionTreeRegressor(max_depth=4)
model = se.AdaBoostRegressor(tree,n_estimators=400,random_state=7)
model.fit(train_x,train_y)
ada_fi = model.feature_importances_
print(ada_fi)
pred_test_y=model.predict(test_x)

print(sm.r2_score(test_y,pred_test_y))

#构建DT模型　使用训练集训练，测试集测试
tree = st.DecisionTreeRegressor(max_depth=4)
tree.fit(train_x,train_y)
tree_fi = tree.feature_importances_
print(tree_fi)
pred_test_y=tree.predict(test_x)

#绘制特征重要性的柱状图
mp.figure("Feature Importance",facecolor='lightgray')
mp.subplot(211)
mp.title("AdaBoost FI",fontsize=14)
mp.ylabel("importance",fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
sorted_inds = ada_fi.argsort()[::-1]
pos = np.arange(ada_fi.size)
mp.bar(pos,ada_fi[sorted_inds],facecolor='dodgerblue',label='AdaBoost')
#设置刻度文本
mp.xticks(pos,names[sorted_inds])
mp.legend()

mp.subplot(212)
mp.title("Tree FI",fontsize=14)
mp.ylabel("importance",fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
sorted_inds = tree_fi.argsort()[::-1]
mp.bar(pos,tree_fi[sorted_inds],facecolor='orangered',label='Tree')
#设置刻度文本
mp.xticks(pos,names[sorted_inds])
mp.legend()
mp.tight_layout()
mp.show()


print(sm.r2_score(test_y,pred_test_y))