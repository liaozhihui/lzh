# coding=utf-8
"""
决策树
"""
import sklearn.datasets as sd
import sklearn.utils as su
from sklearn.model_selection import train_test_split
import sklearn.metrics as sm
import sklearn.tree as st


#加载数据
boston=sd.load_boston()

#打乱原始数据集，划分训练集与测试集
#当随机种子相同时得到的随机序列也相同
x,y = su.shuffle(boston.data,boston.target,random_state=7)
train_size = int(len(x)*0.8)

train_x,test_x,train_y,test_y=x[:train_size],x[train_size:],y[:train_size],y[train_size:]
train_x,test_x,train_y,test_y=train_test_split(x,y,test_size=0.2)

model = st.DecisionTreeRegressor(max_depth=4)
model.fit(train_x,train_y)
pred_test_y=model.predict(test_x)
print(sm.r2_score(test_y,pred_test_y))

