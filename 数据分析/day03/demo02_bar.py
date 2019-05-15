# coding=utf-8
import numpy as np
import matplotlib.pyplot as mp

#整理苹果12个月的销量
apples=[45,46,55,68,79,85,66,74,63,52,54,65]
oranges=[34,24,15,67,87,85,74,35,24,25,75,75]
x=np.arange(len(apples))


mp.figure('Bar Chart',facecolor='lightgray')
mp.title("Bar Chart",fontsize=14)
mp.xlabel("Date",fontsize=12)
mp.ylabel("Volumn",fontsize=12)
mp.grid(linestyle=':')
mp.tick_params(labelsize=10)
mp.bar(x-0.2,apples,0.4,color='limegreen',label="Apples")
mp.bar(x+0.2,oranges,0.4,color='orangered',label='Oranges')

#修改x刻度版本
mp.xticks(x,['Jan','Feb','Mar','Apr',"May","Jun",'Jul','Aug','Sep','Oct','Nov',"Dec"])

mp.legend(loc=0)
mp.show()