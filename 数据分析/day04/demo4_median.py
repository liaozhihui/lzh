
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
	lowest_prices, closing_prices,volumns = \
	np.loadtxt('../da_data/aapl.csv',
		usecols=(1,3,4,5,6,7),
		unpack=True,
		dtype='M8[D], f8, f8, f8, f8,f8',
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
	linewidth=3, label='closing_price',alpha=0.3)
#计算均值
mean = np.mean(closing_prices)
mp.hlines(mean,dates[0],dates[-1],color='orangered',label='Mean(Closing)')
#成交量加权平均线
vwap = np.average(closing_prices,weights=volumns)
mp.hlines(vwap,dates[0],dates[-1],colors='limegreen',label='VWAP')
#时间加权平均线
times = np.arange(1,closing_prices.size+1)
twap = np.average(closing_prices,weights=times)
mp.hlines(twap,dates[0],dates[-1],color='violet',label='TWAP')
#绘制中位数水平线
sorted_prices = np.msort(closing_prices)
media = np.median(sorted_prices)
mp.hlines(media,dates[0],dates[-1],colors='gold',label="Median")

mp.legend(loc=0)
mp.gcf().autofmt_xdate()
mp.show()