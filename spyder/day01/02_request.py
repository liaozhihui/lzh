# coding=utf-8
from urllib import request

url="http://www.baidu.com"

headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"}

req = request.Request(url,headers=headers)
res=request.urlopen(req)

html=res.read().decode("utf-8")
print(dir(res))