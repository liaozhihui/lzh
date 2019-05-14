"""
demo05_std 标准差
"""
import numpy as np
import matplotlib.pyplot as mp
import datetime as dt
import matplotlib.dates as md


#转成需要的int类型(0 1 2 3 4 5 6)
def dmy2weekday(dmy):
	# 把二进制字符串转为普通字符串
	d = str(dmy, encoding='utf-8')
	d=dt.datetime.strptime(d,"%d-%m-%Y")
	t=d.date()
	wday=t.weekday()
	return wday

dates, closing_prices = \
	np.loadtxt('../da_data/aapl.csv',
		usecols=(1,6),
		unpack=True,
		dtype='f8, f8',
		delimiter=',',
		converters={1:dmy2weekday})

print(dates)
#存储最终结果[周一均价,周二均价]
avg_closing_prices = np.zeros(5)
for wday in range(avg_closing_prices.size):
	avg_closing_prices[wday] = closing_prices[dates==wday].mean()
print(np.round(avg_closing_prices,2))