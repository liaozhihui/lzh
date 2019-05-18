# coding=utf-8
import numpy as np
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import axes3d

n=1000
#构建网格点坐标矩阵
x,y = np.meshgrid(np.linspace(-3,3,n),np.linspace(-3,3,n))
x1,y1=np.linspace(-3,3,n),np.linspace(-3,3,n)


#根据每个坐标点的x与y的值计算高度z
z=(1-x/2+x**5+y**3)*np.exp(-x**2-y**2)

z1=(1-x1/2+x1**5+y1**3)*np.exp(-x1**2-y1**2)
#绘制等高线
mp.figure('3D Surface',facecolor='lightgray')
mp.tick_params(labelsize=10)

ax3d=mp.gca(projection='3d')
ax3d.plot_surface(x,y,z,cmap='jet',rstride=10,cstride=10)
ax3d.plot(x1,y1,z1,c="red")


mp.show()