# coding=utf-8
import numpy as np
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import axes3d

n=1000
#构建网格点坐标矩阵
x,y = np.meshgrid(np.linspace(-3,3,n),np.linspace(-3,3,n))

#根据每个坐标点的x与y的值计算高度z
z=(1-x/2+x**5+y**3)*np.exp(-x**2-y**2)

#绘制等高线
mp.figure('3D Surface',facecolor='lightgray')
mp.tick_params(labelsize=10)

ax3d=mp.gca(projection='3d')
ax3d.plot_wireframe(x,y,z,color='dodgerblue',rstride=30,cstride=30)


mp.show()