# coding=utf-8
import matplotlib.pyplot as mp

lables=['Python',"Javascript",'C++','Java','PHP']

values=[26,17,21,29,11]
spaces=[0.05,0.01,0.01,0.01,0.01]
colors=['dodgerblue','orangered','limegreen','violet','gold']
mp.figure('Pie Chart',facecolor='lightgray')
mp.title('Pie Chart',fontsize=14)
#设置等轴比例显示饼状图
mp.axis('equal')
mp.pie(values,spaces,lables,colors,'%.2f%%',shadow=True)
mp.legend(loc=0)
mp.show()