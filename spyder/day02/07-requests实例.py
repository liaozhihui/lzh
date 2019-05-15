# coding=utf-8
import requests

headers={"User-Agent":"Mozila/5.0"}
url = "http://www.baidu.com/"
#发请求并获取响应对象
res = requests.get(url,headers=headers)
#获取响应内容text
res.encoding='utf8'
#获取响应内容字符串(text)
print(res.text)
#获取响应bytes
print(res.content)
#http响应码
print(res.status_code)
#返回实际数据的url地址
print(res.url)