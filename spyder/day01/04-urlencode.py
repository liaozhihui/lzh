# coding=utf-8
from urllib import request,parse


#定义常用的变量
baseurl = "http://www.baidu.com/s?wd="
headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"}
#对url编码
key=input('请输入要搜索的内容')
key=parse.quote(key)
url=baseurl+key
req=request.Request(url,headers=headers)
res=request.urlopen(req)

html=res.read().decode('utf-8')
print(html)
#保存到本地
with open("百度.html",'w',encoding='utf-8') as f:
    f.write(html)

print("成功")