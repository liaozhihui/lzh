# coding=utf-8
import gevent
from gevent import monkey
monkey.patch_all()#执行脚本插件，修改原有阻塞行为

from socket import *

#创建他戒子

def server():
    s=socket()
    s.bind(("0.0.0.0",8888))
    s.listen(10)
    while True:
        c,addr=s.accept()
        print("Connect from ",addr)
        # handle(c) #处理客户端清球
        gevent.spawn(handle,c)

def handle(c):
    while True:
        data=c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b"OK")
    c.close()

server()