#coding:utf-8
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier,export_graphviz
SEED=222
np.random.seed(SEED)
df=pd.read_csv('input.csv')
#Training and Test set
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score

def get_train_test(val,shuxing,test_size=0.95):
    y=1*(df.shuxing ==val)
    X=df.drop([shuxing],axis=1)
    X=pd.get_dummies(X,sparse=True)
    X.drop(X.columns[X.std()==0],axis=1,inplace=True)
    return train_test_split(X,y,test_size=test_size,random_state=SEED)

def print_graph(clf,feature_names):
    graph=export_graphviz(clf,label='root',proportion=True,impurity=False,out_file=None,
                          feature_names=feature_names,class_names={0:'D',1:'R'},filled=True,rounded=True)


xtrain,xtest,ytrain,ytest=get_train_test()

t1=DecisionTreeClassifier(max_depth=1,random_state=SEED)
t1.fit(xtrain,ytrain)
p=t1.predict_proba(xtest)[:,1]
roc_auc_score(ytest,p)

from sklearn.ensemble import RandomForestClassifier

rf=RandomForestClassifier(n_estimators=10,max_depth=3,random_state=SEED)
rf.fit(xtrain,ytrain)
p=rf.predict_proba(xtest)[:,1]
score=roc_auc_score(ytest,p)