from socket import * 
import os,sys
import signal

#客户端处理函数
def client_handle(c):
    print("客户端:",c.getpeername())
    while True:
        data = c.recv(1024)
        if not data:
            break 
        print(data.decode())
        c.send(b"Receive message")
    c.close()

#创建监听套接字
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)

s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(5)

#处理僵尸进程
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

print("Listen to the port 8888....")
#循环等待客户端连接
while True:
    try:
        c,addr = s.accept()
    except KeyboardInterrupt:
        sys.exit("服务器退出")
    except Exception as e:
        print("Error:",e)
        continue 
    
    #创建子进程处理客户端请求
    pid = os.fork()

    if pid == 0:
        s.close()
        client_handle(c) #处理客户端请求
        os._exit(0)
    #无论父进程或者创建进程失败都是循环接受新的连接
    else:
        c.close()





