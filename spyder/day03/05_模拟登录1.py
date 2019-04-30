# coding=utf-8
import requests

url = 'http://www.renren.com/967469305/profile'
headers = {
    'Cookie':'',
    'Referer':'',
    'User-Agent':''
}

res = requests.get(url,headers=headers)
res.encoding="utf-8"
print(res.text)