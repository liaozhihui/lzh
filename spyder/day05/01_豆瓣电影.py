# coding=utf-8
import requests
import json

class DoubanSpider(object):
    def __init__(self):
        self.url = "https://movie.douban.com/j/chart/top_list?"
        self.headers={'User-Agent':"Mozilla/5.0"}

    def get_page(self,params):
        res = requests.get(self.url,headers=self.headers,params=params)
        res.encoding="utf-8"
        html=json.loads(res.text)
        self.parse_page(html)

    def parse_page(self,html):
        for h in html:
            name = h['title'].strip()
            score=float(h['score'].strip())

            print(name, score)
    def main(self):
        limit=input("请输入电影数量:")
        params={
            'type':'24',
            'interval_id':'100:90',
            'action':'',
            'start':'0',
            'limit':limit
        }
        self.get_page(params=params)


if __name__ == '__main__':
    douban=DoubanSpider()
    douban.main()