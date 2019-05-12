# coding=utf-8
import numpy as np
import matplotlib.pyplot as mp

x=np.array([i for i in range(1,7)])
y=np.array([34,12,34,12,3,34])
#x:x坐标数组
#y：y坐标数组

mp.plot(x,y)
mp.hlines(15,1,6)
mp.vlines(4,5,35)
mp.show()