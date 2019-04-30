# coding=utf-8
import requests
import time
from hashlib import md5
import random

url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
headers = {'Cookie': '_ga=GA1.2.1882710736.1551152604; OUTFOX_SEARCH_USER_ID_NCOO=1035574104.8376166; OUTFOX_SEARCH_USER_ID="-1006103452@10.169.0.84"; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; JSESSIONID=abcaWryrCYj126xjsnTPw; _ntes_nnid=372caa8bcb1c163c3fd4c435298bb08c,1556610369792; ___rl__test__cookies=1556617379829',
           "Referer":'http://fanyi.youdao.com/',
           "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}
key = input("Input word:")
salt=str(int(time.time()*1000)) + str(random.randint(0,10))
string = "fanyideskweb"+key+salt+"@6f#X3=cCuncYssPsuRUE"
s=md5()
s.update(string.encode())
sign=s.hexdigest()
ts=str(int(time.time()*1000))

data={
'i': key,
'from': 'AUTO',
'to': 'AUTO',
'smartresult': 'dict',
'client': 'fanyideskweb',
'salt': salt,
'sign': sign,
'ts': ts,
'bv': '363eb5a1de8cfbadd0cd78bd6bd43bee',
'doctype': 'json',
'version': 2.1,
'keyfrom': 'fanyi.web',
'action': 'FY_BY_CLICKBUTTI,ON',
}

res=requests.post(url,data=data)
res.encoding="utf-8"
print(res.text)