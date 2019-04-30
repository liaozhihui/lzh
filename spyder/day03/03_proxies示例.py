# coding=utf-8
import requests
url = 'http://httpbin.org/get'

headers = {"User-Agent":"Mozila/5.0"}

proxies={'http':"http://79.138.99.254:8080"}
#定义私密代理ip


res = requests.get(url=url,proxies=proxies,headers=headers)
res.encoding = "utf-8"

print(res.text)