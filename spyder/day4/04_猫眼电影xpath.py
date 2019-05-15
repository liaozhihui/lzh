# coding=utf-8
from lxml import etree
from urllib import request,parse
import re
import pymongo
class CatEyeSpider(object):

    def __init__(self,baseurl,user_agent):
        self.baseurl=baseurl
        self.user_agent=user_agent


    def get_page(self,key):
        key=parse.urlencode(key)
        url=self.baseurl+key
        req=request.Request(url,headers=self.user_agent)
        res=request.urlopen(req)
        html=res.read().decode("utf-8")
        return html

    def parse_page(self,html):
        parse_html = etree.HTML(html)
        dd_list= parse_html.xpath('//dl[@class="board-wrapper"]/dd')
        print(dd_list)
        for dd in dd_list:
            name=dd.xpath('./a/@title')[0].strip()
            star=dd.xpath('.//p[@class="star"]/text()')[0].strip()
            time =dd.xpath('.//p[@class="releasetime"]/text()')[0].strip()
            print(name,star,time)

    def write_page(self,p_list):

           pass







    def main(self):
        p_list=[]
        for i in range(5):
            key={"offset":i*10}
            html=self.get_page(key)
            result=self.parse_page(html)
        self.write_page(p_list)



if __name__=="__main__":
    baseurl="https://maoyan.com/board/4?"
    user_agent={"User-Agent":"Opera/8.0 (Windows NT 5.1; U; en)"}
    spider=CatEyeSpider(baseurl,user_agent)
    spider.main()