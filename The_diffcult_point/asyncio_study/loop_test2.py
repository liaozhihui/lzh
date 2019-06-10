# coding=utf-8
#事件循环+回调（驱动生成器）+epoll(IO多路复用)
#asyncio是python用于解决异步IO编程的一整套解决方案
#tornado、gevent、twisted(scrapy,django channels)
#torando(实现web服务器),django+flask(uwsgi,gunicorn+nginx)
#tornado可以直接部署,nginx+tornado

#使用asyncio
import asyncio
import time
from threading import Thread
from multiprocessing import Process
from functools import partial #可以将函数变成另一个函数

async def get_html(url):
    print("start get url")
    await asyncio.sleep(2)
    # time.sleep(2)
    print("end get url")
    #获取线程的返回值
    return "bobby"
def callback(url,future):
    print(url)
    print("send email to bobby")


if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()
    # get_future=asyncio.ensure_future(get_html("http://www.imooc.com")) #和loop.create_task()等价
    #
    # # tasks = [get_html("http://www.imooc.com") for i in range(10000)]
    # loop.run_until_complete(get_future)
    # print(get_future.result())
    task=loop.create_task(get_html("http://www.imooc.com"))
    task.add_done_callback(partial(callback,"http://www.imooc.com"))
    loop.run_until_complete(task)
    print(task.result())
