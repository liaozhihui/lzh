# coding=utf-8
import scipy.interpolate as si #插值器模块
import numpy as np
import matplotlib.pyplot as mp
#搞一组散点
min_x = -50
max_x = 50
dis_x = np.linspace(min_x,max_x,15)
dis_y = np.sinc(dis_x)
mp.scatter(dis_x,dis_y,s=60,marker="o",label="Points",c='red')

#通过散点设计出符合一定规律的插值器函数
#返回的linear是一个函数 可以:linear(x)

#三次样条插值起
cubic=si.interp1d(dis_x,dis_y,'cubic')
x=np.linspace(min_x,max_x,1000)
y=cubic(x)
mp.plot(x,y,c='orangered',label="cubic")
linear=si.interp1d(dis_x,dis_y,'linear')
y=linear(x)
mp.plot(x,y,c='dodgerblue',label="linear")


mp.legend()
mp.show()