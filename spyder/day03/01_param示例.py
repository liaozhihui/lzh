# coding=utf-8
import requests
url="http://www.baidu.com/s?"
headers = {"User-Agent":"Opera/8.0 (Windows NT 5.1; U; en)"}
params={
    "kw":"美女",
    'pn':'30'
}
res=requests.get(url,params=params,headers=headers)
res.encoding='utf-8'
print(res.text)