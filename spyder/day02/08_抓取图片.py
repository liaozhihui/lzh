# coding=utf-8
import requests
url="http://img3.duitang.com/uploads/item/201510/03/20151003071851_kuHXs.thumb.700_0.jpeg"
headers={"User-Agent":"Mozila/5.0"}

res = requests.get(url,headers=headers)

html=res.content
with open("颖宝.jpg","wb") as f:
    f.write(html)

    # 