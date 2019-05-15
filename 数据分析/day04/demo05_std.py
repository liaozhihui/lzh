"""
demo05_std 标准差
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

#获取收盘价的标准差

print(np.std(closing_prices))
print(np.std(closing_prices,ddof=1))
print(closing_prices.std())

mean=np.mean(closing_prices)
d=closing_prices-mean
d2=d**2
var=np.mean(d2)
std=np.sqrt(var)

print(std)