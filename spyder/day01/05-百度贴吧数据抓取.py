# coding=utf-8
"""百度贴吧数据抓取,不同吧不同页"""
from urllib import request,parse
import random
import time
#定义常用变量
baseurl="http://tieba.baidu.com/f?"

h_list=[
    {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0"},
    {"User-Agent":"Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50"},
    {"User-Agent":"Opera/8.0 (Windows NT 5.1; U; en)"},
    {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        ]
#拼接url
name = input("请输入贴吧名称:")
begin = int(input("请输入起始页:"))
end = int(input("请输入终止页:"))

#发请求保存数据
for page in range(begin,end+1):
    pn=(page-1)*50
    url=baseurl+parse.urlencode({"kw":name,"pn":str(pn)})
    headers=random.choice(h_list)
    print(url)
    req=request.Request(url,headers=headers)
    res=request.urlopen(req)
    html = res.read().decode("utf-8")
    with open("第{}页.txt".format(page),"w",encoding="utf-8") as f:
        f.write(html)

    time.sleep(1)
    print("第%s页爬取成功"%page)
