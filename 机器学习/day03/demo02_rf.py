# coding=utf-8
"""
共享单车
"""
import numpy as np
import sklearn.utils as su
import sklearn.ensemble as se
import sklearn.metrics as sm
import matplotlib.pyplot as mp
from sklearn.model_selection import train_test_split

data=np.loadtxt('../ml_data/bike_day.csv',unpack=False,dtype="U20",delimiter=",")

day_headers=data[0,2:13]
x=np.array(data[1:,2:13],dtype='f4')
y=np.array(data[1:,-1],dtype='f4')
print(x.shape,y.shape)

#打乱数据集，划分测试集与训练集
x,y=su.shuffle(x,y,random_state=7)
train_size = int(len(x)*0.9)
print(x.shape,y.shape)
train_x,test_x,train_y,test_y=x[:train_size],x[train_size:],y[:train_size],y[train_size:]
# X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)
#基于随机森林训练模型
model = se.RandomForestRegressor(max_depth=10,n_estimators=1000,min_samples_split=2)
model.fit(train_x,train_y)
day_fi=model.feature_importances_
pred_test_y=model.predict(test_x)
print(sm.r2_score(test_y,pred_test_y))

data=np.loadtxt('../ml_data/bike_hour.csv',unpack=False,dtype="U20",delimiter=",")

hour_headers=data[0,2:14]
x=np.array(data[1:,2:14],dtype='f4')
y=np.array(data[1:,-1],dtype='f4')
print(x.shape,y.shape)

#打乱数据集，划分测试集与训练集
x,y=su.shuffle(x,y,random_state=7)
train_size = int(len(x)*0.9)
print(x.shape,y.shape)
train_x,test_x,train_y,test_y=x[:train_size],x[train_size:],y[:train_size],y[train_size:]
#基于随机森林训练模型
model = se.RandomForestRegressor(max_depth=10,n_estimators=1000,min_samples_split=2)
model.fit(train_x,train_y)
hour_fi=model.feature_importances_
pred_test_y=model.predict(test_x)
print(sm.r2_score(test_y,pred_test_y))

#绘制两组数据的特征重要性的柱状图(子图)
day_inds=day_fi.argsort()[::-1]
day_pos=np.arange(day_fi.size)
hour_inds=hour_fi.argsort()[::-1]
hour_pos=np.arange(hour_fi.size)
mp.figure("Bike",facecolor="lightgray")
mp.subplot(121)
mp.title("day Features")
mp.bar(day_pos,day_fi[day_inds],facecolor='orangered',label="day Feature")
mp.xticks(day_pos,day_headers[day_inds])
mp.tick_params(labelsize=10)
mp.legend()

mp.subplot(122)
mp.title("Hour Features")
mp.bar(hour_pos,hour_fi[hour_inds],facecolor='dodgerblue',label="hour Feature")
mp.xticks(hour_pos,hour_headers[hour_inds])
mp.tick_params(labelsize=10)
mp.legend()

mp.tight_layout()
mp.show()