# coding=utf-8
import re
import requests
class JinDonSpider(object):
    def __init__(self):
        self.baseurl="https://search.jd.com/Search?"
        self.headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'}
    def get_page(self,params):
        res=requests.get(self.baseurl,params=params,headers=self.headers)
        res.encoding="utf-8"
        html=res.text
        self.parse_page(html)
    def parse_page(self,html):
        pattern1='<div class="gl-i-wrap">.*?<div class="p-price">.*?<em>(.*?)</i>.*?<div class="p-name p-name-type-2">.*?<em>(.*?)</em>.*?</div>'
        pattern='<div class="gl-i-wrap">.*?<div class="p-price">.*?</em><i>(.*?)</i>.*?<div class="p-name p-name-type-2">.*?<em>(.*?)<font class="skcolor_ljg">.*?</font>(.*?)</em>.*?</div>'

        p=re.compile(pattern,re.S)
        p_list=p.findall(html)
        print(p_list)
        for r in p_list:
           print(r)

    def main(self):
        params={"keyword":"笔记本电脑",
                "enc":"utf-8",
                "page":6

                }
        self.get_page(params)
if __name__ == '__main__':
    spider=JinDonSpider()
    spider.main()