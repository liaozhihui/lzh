# coding=utf-8
import requests
from threading import Thread
from multiprocessing import Queue,Process,Lock
import json
import time

class XiaomiSpider(object):
    def __init__(self):
        self.url_queue = Queue()
        self.headers={"User-Agent":"Mozilla/5.0"}
        self.lock=Lock()

        pass

    # URL入队列
    def url_in(self):
        # 拼接多个URL地址,然后put()到队列中
        for i in range(67):
            url="http://app.mi.com/categotyAllListApi?page=%s&categoryId=2&pageSize=30" % str(i)
            self.url_queue.put(url)
        pass

    # 线程事件函数(请求,解析提取数据)
    def get_page(self):
        # 先get()URL地址,发请求
        # json模块做解析
        while True:
            #当队列不为空时
            if not self.url_queue.empty():
                url = self.url_queue.get()
                res = requests.get(url,headers = self.headers)
                res.encoding="utf-8"
                html = res.text
                self.parse_page(html)
            else:
                break
        pass
    def parse_page(self,html):
        html = json.loads(html)
        for h in html['data']:
            #应用名称
            name =h['displayName']
            #应用连接
            link="http://app.mi.com/details?id={}".format(h['packageName'])
            d={
                '名称':name,
                "链接":link
            }
            self.lock.acquire()
            with open('小米.json','a') as f:
                f.write(str(d)+"\n")
            self.lock.release()
    # 主函数
    def main(self):
        self.url_in()
        t_list = [] #存放所有进程的列表

        for i in range(3):
            t = Process(target=self.get_page)
            t.start()
            t_list.append(t)

        # 统一回收线程
        for p in t_list:
            p.join()

if __name__ == '__main__':
    start=time.time()
    spider = XiaomiSpider()
    spider.main()
    end = time.time()
    print("执行时间:%.2f"%(end-start))