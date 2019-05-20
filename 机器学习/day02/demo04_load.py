# coding=utf-8
import numpy as np
import sklearn.linear_model as lm
import pickle
import sklearn.metrics as sm
#读取文件采集数据
x,y = np.loadtxt('../ml_data/single.txt',delimiter=',',usecols=(0,1),unpack=True)


with open('../ml_data/linear.pkl','rb') as f:

    model=pickle.load(f)

x=x.reshape(-1,1)

pred_v=model.predict(x)
#评估训练结果误差
result4=sm.r2_score(y,pred_v)
print("R2",result4)
