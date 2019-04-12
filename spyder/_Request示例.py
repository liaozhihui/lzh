# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 18:48:05 2019

@author: Python
"""

import urllib.request
url='http://www.baidu.com/'
headers={'User-Agent':'Mozilla/5.0'}
#1、创建请求对象
request = urllib.request.Request(url,headers=headers)
#2、获取响应对象
response=urllib.request.urlopen(request)
#3、获取内容

html=response.read().decode('utf-8')