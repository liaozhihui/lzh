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

async def get_html(url):
    print("start get url")
    await asyncio.sleep(2)
    # time.sleep(2)
    print("end get url")

def get_html1(url):
    # print("start get url")
    # await asyncio.sleep(2)
    time.sleep(2)
    # print("end get url")


if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()
    tasks = [get_html("http://www.imooc.com") for i in range(10000)]
    # loop.run_until_complete(get_html("http://www.imooc.com"))#一个事件
    loop.run_until_complete(asyncio.wait(tasks)) #wait中的tasks是一个可迭代对象
    print("协程耗时:",time.time()-start_time)
    #使用多线程
    start_time = time.time()
    threads=[]
    for i in range(10000):
        t=Thread(target=get_html1,args=("http://www.imooc.com",))
        threads.append(t)
        t.start()
    for i in threads:
        i.join()
    print("线程耗时：",time.time() - start_time)

    #使用多进程

    start_time = time.time()
    process = []
    for i in range(10000):
        p = Process(target=get_html1, args=("http://www.imooc.com",))
        process.append(p)
        p.start()
    for i in process:
        i.join()
    print("进程耗时",time.time() - start_time)
