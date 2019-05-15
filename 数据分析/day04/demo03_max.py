"""
demo03_max 极值
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

#评估AAPL股票的波动性 最高价与最低价的波动性

max_price = np.max(highest_prices)
min_price = np.min(lowest_prices)

print(max_price,min_price)

#查看最高价与最低价到底是哪一天
max_i=np.argmax(highest_prices)
min_i=np.argmin(lowest_prices)
print(dates[max_i],dates[min_i])

a=np.arange(1,10)
b=a[::-1]
a=a.reshape(3,3)
b=b.reshape(3,3)
print(a,b)




