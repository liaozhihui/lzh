# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 15:20:20 2019

@author: Python
"""

import urllib.request
url='http://www.baidu.com/'
response=urllib.request.urlopen(url)
#获取响应对象
#read得到的是一个bytes数据类型
html = response.read().decode('utf-8')
print(html)