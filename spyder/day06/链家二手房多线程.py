# coding=utf-8
from threading import Thread
from bs4 import BeautifulSoup
from queue import Queue
import requests
import time

class LianjiaSpider(object):

    def __init__(self):
        self.url_queue=Queue()
        self.headers={"User-Agent":'Mozilla/5.0'}

        pass

    #入队列
    def url_in(self):
        for i in range(1,50):
            url="https://sh.lianjia.com/ershoufang/pg%s/"%str(i)
            self.url_queue.put(url)


    def get_page(self):
        while True:
            if not self.url_queue.empty():
                url = self.url_queue.get()
                res=requests.get(url,headers=self.headers)
                res.encoding="utf-8"
                html=res.text
                self.parse_page(html)



    def parse_page(self,html):
        soup = BeautifulSoup(html,'lxml')
        li_list= soup.find_all('li',arrts={"class":'clear LOGCLICKDATA'})


        for li in li_list:
            li_h = li.find('div',{'class':'houseInfo'})
            for h in li_h:
                h.find()

    def main(self):
        self.url_in()
        t_list=[]
        for i in range(5):
            t=Thread(target=self.get_page)
            t.start()
            t_list.append(t)
        for p in t_list:
            p.join
        pass
if __name__ == '__main__':
    spider= LianjiaSpider()
    spider.main()