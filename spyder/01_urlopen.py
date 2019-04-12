# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 15:20:20 2019

@author: Python
"""

import urllib.request
url='http://www.baidu.com/'
response=urllib.request.urlopen(url)
print(response)

html = response.read().decode('utf-8')
print(html)