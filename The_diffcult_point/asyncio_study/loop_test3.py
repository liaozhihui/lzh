# coding=utf-8
#事件循环+回调（驱动生成器）+epoll(IO多路复用)
#asyncio是python用于解决异步IO编程的一整套解决方案
#tornado、gevent、twisted(scrapy,django channels)
#torando(实现web服务器),django+flask(uwsgi,gunicorn+nginx)
#tornado可以直接部署,nginx+tornado

#使用asyncio
#wait和gather的区别
import asyncio
import time

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

    tasks = [get_html("http://www.imooc.com") for i in range(10)]
    # loop.run_until_complete(get_html("http://www.imooc.com"))#一个事件
    # loop.run_until_complete(asyncio.wait(tasks))  # wait中的tasks是一个可迭代对象
    # loop.run_until_complete(asyncio.gather(*tasks))
    # print("协程耗时:", time.time() - start_time)
    #gather和wait的区别：
    #gather更加high-level
    group1 = [get_html("http://www.imooc.com") for i in range(2)]
    group2 = [get_html("http://www.baidu.com") for i in range(2)]
    # loop.run_until_complete(asyncio.gather(*group1,*group2))
    group1 = asyncio.gather(*group1)
    group2 = asyncio.gather(*group2)
    group2.cancel()
    loop.run_until_complete(asyncio.gather(group1, group2))
    print("协程耗时:", time.time() - start_time)