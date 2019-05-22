# coding=utf-8
import numpy as np
import sklearn.preprocessing as sp
import sklearn.ensemble as se
import sklearn.model_selection as ms
import matplotlib.pyplot as mp
data=np.loadtxt("../ml_data/car.txt",unpack=False,delimiter=",",dtype="U10")
print(data.shape)

encoders=[]
train_x=[]
train_y=[]
data=data.T

for row in range(len(data)):
    encoder = sp.LabelEncoder()
    if row <(len(data)-1):
        train_x.append(encoder.fit_transform(data[row]))
    else:
        train_y=encoder.fit_transform((data[row]))

    encoders.append(encoder)

train_x=np.array(train_x).T
train_y=np.array(train_y)
model=se.RandomForestClassifier(max_depth=6,n_estimators=150,random_state=7)

#使用验证曲线,得到模型最优超参数
train_scores,test_scores=ms.validation_curve(model,train_x,train_y,'n_estimators',np.arange(50,550,50),cv=5)

vc_array=np.mean(test_scores,axis=1)
mp.figure("Validation Curve",facecolor="lightgray")
mp.title("Validation Curve",fontsize=16)
mp.xlabel('n_estimators')
mp.ylabel('f1_scores')
mp.grid(linestyle=':')
mp.plot(np.arange(50,550,50),vc_array)
mp.show()


m=ms.cross_val_score(model,train_x,train_y,scoring="f1_weighted").mean()



model.fit(train_x,train_y)

#自定义测试集,进行模型预测
data=[
    ['high','med','5more','4','big','low','unacc'],
    ['high','high','4','4','med','med','acc'],
    ['low','low','2','4','small','high','good'],
    ['low','med','3','4','med','high','vgood'],
]

#使用相同的标签编码１器进行编码
data=np.array(data).T
test_x=[]
for row in range(len(data)):
    encoder=encoders[row]
    if row <len(data)-1:
        test_x.append(encoder.transform(data[row]))

test_x=np.array(test_x).T
pred_test_y=model.predict(test_x)
print(pred_test_y)

print(encoders[-1].inverse_transform(pred_test_y))