# coding=utf-8
import numpy as np
import matplotlib.pyplot as mp
#随机生成身高与体重
n=100
x=np.random.normal(173,10,n)
y=np.random.normal(65,20,n)

mp.figure("Persons",facecolor='lightgray')
mp.title("Person Points",fontsize=16)
mp.xlabel("Height",fontsize=12)
mp.ylabel("Weight",fontsize=12)
d=(x-173)**2+(y-65)**2
mp.scatter(x,y,s=60,c=d,cmap='jet_r')
mp.show()