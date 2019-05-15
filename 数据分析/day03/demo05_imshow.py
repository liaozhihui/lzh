# coding=utf-8
import numpy as np
import matplotlib.pyplot as mp

n=1000
#构建网格点坐标矩阵
x,y = np.meshgrid(np.linspace(-3,3,n),np.linspace(-3,3,n))

#根据每个坐标点的x与y的值计算高度z
z=(1-x/2+x**5+y**3)*np.exp(-x**2-y**2)

#绘制热成像图
mp.figure('Countour',facecolor='lightgray')
mp.title("Countour",fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
cntr=mp.imshow(z,cmap='jet',origin='lower')
mp.legend()
mp.colorbar()
mp.show()