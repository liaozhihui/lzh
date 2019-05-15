# coding=utf-8
import requests
import re
import pymysql
class NoteSpider(object):
    def __init__(self):
        self.url = "http://code.tarena.com.cn"
        self.headers={'User-Agent':"Mozilla/5.0"}
        self.proxies = {'http':'http://127.0.0.1:8888'}
        self.auth=("tarenacode","code_2013")
        self.db=pymysql.connect('localhost','root','123456','codedb',charset='utf8')
        self.cursor=self.db.cursor()


    def get_parse_page(self):
        res = requests.get(self.url,headers=self.headers,auth=self.auth)
        res.encoding='utf-8'
        html = res.text
        p=re.compile("<a href=.*?>(.*?)/</a>",re.S)
        r_list=p.findall(html)
        self.write_mysql(r_list)

    def write_mysql(self,r_list):
        ins="insert into note values(%s)"
        for r in r_list:
            if r!='..':
               self.cursor.execute(ins,[r])
               self.db.commit()
if __name__ == '__main__':
    spider=NoteSpider()
    spider.get_parse_page()
