# coding=utf-8
import numpy as np
import matplotlib.pyplot as mp
"""绘制正弦曲线"""

#x:x坐标数组
x = np.linspace(-np.pi,np.pi,1000)
#y：y坐标数组
y=np.sin(x)
#设置可视区域
# mp.xlim(0,np.pi)
# mp.ylim(0,1)
#设置坐标刻度
vals=[-np.pi,-np.pi/2,0,np.pi/2,np.pi]
texts=[r'$-\pi$',r'$-\frac{\pi}{2}$','0',r'$\frac{\pi}{2}$',r'$\pi$']
mp.xticks(vals,texts)
ytext=["-1.0","-0.5","0.5","1.0"]
mp.yticks([-1,-0.5,0.5,1],ytext)

mp.plot(x,y,linestyle='--',linewidth=2,color="orangered",alpha=0.8,label=r'$y=sin(x)$')
mp.plot(x,np.cos(x)/2,linestyle=':',linewidth=2,color="orangered",alpha=0.8,label=r"$y=\frac{1}{2}cos(x)$")
#设置坐标轴
ax = mp.gca()
ax.spines['top'].set_color("none")
ax.spines['right'].set_color("none")
ax.spines['left'].set_position(('data',0))
ax.spines['bottom'].set_position(('data',0))
mp.legend(loc=0) #0表示最优的位置

#绘制特殊点
px =[np.pi/2,np.pi/2]
py=[1,0]

mp.scatter(px,py,s=100,marker='o',edgecolors='steelblue',facecolor='deepskyblue',zorder=3)

mp.annotate(r'$[\frac{\pi}{2},1]$',)


mp.show()