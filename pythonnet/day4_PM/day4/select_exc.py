from select import select
from socket import *
import sys 
from time import ctime 

s = socket()
s.bind(('0.0.0.0',8800))
s.listen(3)

#日志文件
f = open('log.txt','a')

rlist = [s,sys.stdin]
wlist = []
xlist = []

while True:
    rs,ws,xs = select(rlist,wlist,xlist)
    for r in rs:
        if r is s:
            c,addr = r.accept()
            rlist.append(c)
        elif r is sys.stdin:
            f.write("%s  %s"%(ctime(),r.readline()))
            f.flush() #刷新文件缓冲
        else:
            data = c.recv(1024)
            if not data:
                rlist.remove(r)
                r.close()
                continue
            f.write("%s  %s\n"%(ctime(),data.decode()))
            f.flush()



