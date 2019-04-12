# coding=utf-8
from urllib import request,parse


#定义常用的变量
baseurl = "http://www.baidu.com/s?"
headers={'User-Agent':''}
#对url编码
key=input('请输入要搜索的内容')
key=parse.urlencode({'wd':key})
url=baseurl+key
req=request.Request(url,headers=headers)
res=request.urlopen(req)

html=res.read().decode('utf-8')

#保存到本地
with open("百度.html",'w',encoding='gb18030') as f:
    f.write(html)

print("成功")