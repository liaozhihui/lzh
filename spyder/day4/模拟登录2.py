# coding=utf-8
import requests

#把用户名和密码信息post到一个URL
post_url="http://www.renren.com/PLogin.do"

post_data={
    'email':"1581627402@qq.com",
    'password':'lzh849641'
}

headers={
    "User-Agent":'',
    "Referer":"",
}

session = requests.session()
session.post(post_url,data=post_data,headers=headers)

#访问个人主页URL地址
url = ''

res=session.get(url,headers=headers)

print(res.text)