"""
绘制移动平均线
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

print(dates,type(dates[0]))

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

mp.plot(list(dates), closing_prices,
	c='dodgerblue', linestyle='--',
	linewidth=3, label='closing_prices',alpha=0.8)
#计算5日均线
sma5 = np.zeros(closing_prices.size - 4)

for i in range(sma5.size):
	sma5[i] = closing_prices[i:i+5].mean()

mp.plot(dates[4:],sma5,color='orangered',label='SMA-5',linewidth=1)

#基于卷积实现5日均线

core=np.ones(5)/5

sma52=np.convolve(closing_prices,core,"valid")
mp.plot(dates[4:],sma52,color='orangered',label='SMA-5',linewidth=7,alpha=0.3)

#使用卷积绘制10日均线
core = np.ones(10)/10
sma10 = np.convolve(closing_prices,core,'valid')
mp.plot(dates[9:],sma10,color='limegreen',label='SMA-10',linewidth=3)

#实现加权5日均线
#从y=e^x,取得5个函数值作为卷积核

weights = np.exp(np.linspace(-1,0,5))
ema5 = np.convolve(closing_prices,weights[::-1]/weights.sum(),"valid")
mp.plot(dates[4:],ema5,color="violet",label='EMA%',linewidth=2)


mp.legend()
mp.gcf().autofmt_xdate()
mp.show()