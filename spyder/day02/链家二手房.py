#coding:utf-8
import requests
import pymongo
import pymysql
import re

class LianJiaSpider(object):

    def __init__(self):
        self.baseurl="https://sh.lianjia.com/ershoufang/pg%s/"
        self.headers={"User-Agent":"Opera/8.0 (Windows NT 5.1; U; en)"}

    def get_page(self,key):
        url=self.baseurl%(str(key))
        print(url)
        res=requests.get(url,headers=self.headers)
        res.encoding='utf-8'
        html=res.text
        self.parse_page(html)

    def parse_page(self,html):
        pattern='<div class="info clear">.*?data-el="region">(.*?)</div></div><div class="flood">.*?"totalPrice"><span>(.*?)</div><div class="unitPrice".*?data-price="\w+"><span>(.*?)</span></div></div></div>'
        p=re.compile(pattern,re.S)
        p_list=p.findall(html)
        print(p_list)
    def write_page(self):
        pass
    def main(self):
        self.get_page(2)

if __name__ == '__main__':
    spider=LianJiaSpider()
    spider.main()