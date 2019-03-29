# coding=utf-8
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import KFold,cross_val_score
from sklearn.metrics import confusion_matrix,recall_score,classification_report

data=pd.read_csv("./data/creditcard.csv")
print(data.head())
count_classes = pd.value_counts(data['Class'],sort = True).sort_index()
# print(count_classes)
# count_classes.plot(kind='bar')
# plt.title("Fraud class hitogram")
# plt.xlabel("Class")
# plt.ylabel("Frequency")
# plt.show()

data['normAmount']=StandardScaler().fit_transform(data['Amount'].reshape(-1,1))
data = data.drop(['Time','Amount'],axis=1)
X=data.ix[:,data.columns != 'Class']
y=data.ix[:,data.columns == "Class"]

number_records_fraud = len(data[data.Class == 1])
fraud_indices = np.array(data[data.Class==1].index)

normal_indices = data[data.Class==0].index
random_normal_indices = np.random.choice(normal_indices, \
                                         number_records_fraud,\
                                         replace=False)
random_normal_indices=np.array(random_normal_indices)

under_sample_indices=np.concatenate([fraud_indices,random_normal_indices])

under_sample_data=data.iloc[under_sample_indices,:]

X_undersample = under_sample_data.ix[:,under_sample_data.columns !=\
                'Class']
y_undersample = under_sample_data.ix[:,under_sample_data.columns ==\
                'Class']


X_train,x_test,y_train,y_test=train_test_split(X,y,\
                                               test_size=0.3,random_state=0)

X_train_undersample, X_test_undersample, \
                y_train_undersample, y_test_undersample = train_test_split(X_undersample,y_undersample,test_size = 0.3,random_state = 0)



def printing_Kfold_scores(x_train_data,y_train_data):
    fold = KFold(len(y_train_data),5,shuffle=False)
    c_param_range=[0.01,0.1,1,10,100]

