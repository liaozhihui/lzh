import socket

#创建套接字

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('127.0.0.1',8888))

#收发消息

while True:
    data=input(">>")
    if not data:
        break
    s.send(data.encode())
    data=s.recv((1024))
    print("From server",data.decode())
s.close()