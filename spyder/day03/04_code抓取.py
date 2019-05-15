# coding=utf-8
import requests
import re
import pymongo
class NoteSpider(object):
    def __init__(self):
        self.url = "http://code.tarena.com.cn"
        self.headers={'User-Agent':"Mozilla/5.0"}
        self.proxies = {'http':'http://127.0.0.1:8888'}
        self.auth=("tarenacode","code_2013")
        self.conn=pymongo.MongoClient("176.47.9.172",27017)
        self.db=self.conn['codedb']
        self.myset=self.db['noteset']

    def get_parse_page(self):
        res = requests.get(self.url,headers=self.headers,auth=self.auth)
        res.encoding='utf-8'
        html = res.text
        p=re.compile("<a href=.*?>(.*?)/</a>",re.S)
        r_list=p.findall(html)
        self.write_mongo(r_list)

    def write_mongo(self,r_list):
        for r in r_list:
            if r!='..':
               self.myset.insert_one({"课程方向":r})
if __name__ == '__main__':
    spider=NoteSpider()
    spider.get_parse_page()
