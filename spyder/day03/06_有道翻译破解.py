import requests
from hashlib import md5
import random
import time 
import json 

key = input('请输入要翻译的单词:')
# 获取ts
ts = int(time.time()*1000)
# 获取bv
s = md5()
s.update('5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'.encode())
bv = s.hexdigest()
# 获取salt
salt = str(ts) + str(random.randint(0,10))

# 获取sign
string = "fanyideskweb" + key + \
              str(salt) + \
              "p09@Bn{h02_BIEe]$P^nG"
s = md5()
s.update(string.encode())
sign = s.hexdigest()

url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
headers = {
        'Accept':'application/json, text/javascript, */*; q=0.01',
        #Accept-Encoding: gzip, deflate
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Connection':'keep-alive',
        'Content-Length':'255',
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie':'OUTFOX_SEARCH_USER_ID=970246104@10.169.0.83; OUTFOX_SEARCH_USER_ID_NCOO=570559528.1224236; td_cookie=18446744070977892747; JSESSIONID=aaafIcAzS1BhQ_osg6YKw; ___rl__test__cookies=1551342801940',
        'Host':'fanyi.youdao.com',
        'Origin':'http://fanyi.youdao.com',
        'Referer':'http://fanyi.youdao.com/',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest',
    }
data = {
    'i':key,
    'from':'AUTO',
    'to':'AUTO',
    'smartresult':'dict',
    'client':'fanyideskweb',
    'salt': salt,
    'sign': sign,
    'ts': str(ts),
    'bv': bv,
    'doctype':'json',
    'version':'2.1',
    'keyfrom':'fanyi.web',
    'action':'FY_BY_REALTIME',
    'typoResult':'false',
}

res = requests.post(url,data=data,
                    headers=headers)
res.encoding = 'utf-8'
html = res.text

rDict = json.loads(html)
print('翻译:',
  rDict['translateResult'][0][0]['tgt'])

try:
    rList = rDict['smartResult']['entries']
    print('解释:',''.join(rList))
except:
    pass















