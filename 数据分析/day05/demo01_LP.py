"""
线性预测
"""
import numpy as np
import matplotlib.pyplot as mp
import datetime as dt
import matplotlib.dates as md

def dmy2ymd(dmy):
	# 把二进制字符串转为普通字符串
	dmy = str(dmy, encoding='utf-8')
	t = dt.datetime.strptime(dmy, '%d-%m-%Y')
	s = t.date().strftime('%Y-%m-%d')
	return s

dates, opening_prices, highest_prices, \
	lowest_prices, closing_prices = \
	np.loadtxt('../da_data/aapl.csv',
		usecols=(1,3,4,5,6),
		unpack=True,
		dtype='M8[D], f8, f8, f8, f8',
		delimiter=',',
		converters={1:dmy2ymd})


#绘制收盘价的折线图

mp.figure('AAPL', facecolor='lightgray')
mp.title('AAPL', fontsize=14)
mp.xlabel('Date', fontsize=12)
mp.ylabel('Price', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
# 设置刻度定位器
ax = mp.gca()
#设置主刻度定位器-每周一一个主刻度
major_loc=md.WeekdayLocator(byweekday=md.MO)
ax.xaxis.set_major_locator(major_loc)
ax.xaxis.set_major_formatter(
	md.DateFormatter('%Y-%m-%d'))
# 设置次刻度定位器为日定位器
minor_loc=md.DayLocator()
ax.xaxis.set_minor_locator(minor_loc)
dates = dates.astype(md.datetime.datetime)
mp.plot(dates, closing_prices,
	c='dodgerblue', linestyle='--',
	linewidth=3, label='AAPL')


#线性预测
N=3
#通过前6个元素，组成3元一次方程组，解之
#整理出矩阵A,列向量B,调用API求出xyz

pred_prices = np.zeros(closing_prices.size-2*N+1)

for i in range(pred_prices.size):

	A = np.zeros((N,N))
	for j in range(N):
		A[j,]=closing_prices[j+i:j+N+i]

	B=closing_prices[N+i:N*2+i]
	x=np.linalg.lstsq(A,B)[0]

	pred_price = B.dot(x) #点乘
	pred_prices[i]=pred_price
#绘制图像
mp.plot(dates[2*N:],pred_prices[:-1],"o-",color='orangered',label="pred_price")
mp.legend(loc=0)
mp.gcf().autofmt_xdate()
mp.show()