# coding=utf-8
import numpy as np
import matplotlib.pyplot as mp

import matplotlib.animation as ma
import random
#随机生成100个泡泡


mp.figure("Animation",facecolor='lightgray')
mp.title('Animation',fontsize=14)

mp.xticks([])
mp.yticks([])
mp.ylim(-3,3)
mp.xlim(0,10)
pl=mp.plot([],[])[0]

#每30毫秒 更新泡泡大小
def update(data):
    t,v=data
    #把新坐标加入曲线
    x,y=pl.get_data()
    x=np.append(x,t)
    y=np.append(y,v)
    pl.set_data(x,y)
    if x[-1]>10:
        mp.xlim(x[-1]-10,x[-1])


x=0
def generator():
    global x
    y=np.sin(2*np.pi*x)*np.exp(np.sin(0.2*np.pi*x))
    yield(x,y)
    x+=0.05

anim=ma.FuncAnimation(mp.gcf(),update,generator,interval=30)

mp.show()